import React, { createContext, useState, useEffect, useContext } from 'react';
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signInWithPopup,
  signOut,
  onAuthStateChanged,
  updateProfile,
  sendEmailVerification
} from 'firebase/auth';
import { doc, setDoc, getDoc, serverTimestamp } from 'firebase/firestore';
import { auth, db, googleProvider } from '../firebase';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

// ── Save / merge a user profile in Firestore ───────────────────────────────
const saveUserToFirestore = async (firebaseUser, extraData = {}) => {
  const ref = doc(db, 'users', firebaseUser.uid);
  const snap = await getDoc(ref);

  if (!snap.exists()) {
    // First time — create the document
    await setDoc(ref, {
      uid:       firebaseUser.uid,
      name:      firebaseUser.displayName || extraData.name || 'User',
      email:     firebaseUser.email,
      photoURL:  firebaseUser.photoURL || null,
      provider:  extraData.provider || 'email',
      wishlist:  [],
      createdAt: serverTimestamp(),
    });
  }
};

// ── Build a plain user object from a Firebase user ────────────────────────
const buildUser = (firebaseUser) => ({
  uid:      firebaseUser.uid,
  name:     firebaseUser.displayName || 'User',
  email:    firebaseUser.email,
  photoURL: firebaseUser.photoURL || null,
});

export const AuthProvider = ({ children }) => {
  const [user, setUser]       = useState(null);
  const [loading, setLoading] = useState(true);

  // Listen to Firebase auth state changes
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (firebaseUser) => {
      if (firebaseUser) {
        setUser(buildUser(firebaseUser));
      } else {
        setUser(null);
      }
      setLoading(false);
    });
    return unsubscribe;
  }, []);

  // ── Email / Password Sign-Up (with Email Verification) ───────────────────
  const signup = async (name, email, password) => {
    try {
      const { user: fbUser } = await createUserWithEmailAndPassword(auth, email, password);
      // Set display name
      await updateProfile(fbUser, { displayName: name });
      
      // Save to Firestore Database
      await saveUserToFirestore({ ...fbUser, displayName: name }, { name, provider: 'email' });
      
      // Send Email Verification Link
      await sendEmailVerification(fbUser);
      
      return { success: true, message: 'Account created! Please check your email to verify your account.' };
    } catch (err) {
      return { success: false, message: friendlyError(err.code) };
    }
  };



  // ── Email / Password Login ───────────────────────────────────────────────
  const login = async (email, password) => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      return { success: true };
    } catch (err) {
      return { success: false, message: friendlyError(err.code) };
    }
  };

  // ── Google Sign-In ───────────────────────────────────────────────────────
  const loginWithGoogle = async () => {
    try {
      const { user: fbUser } = await signInWithPopup(auth, googleProvider);
      // Save to Firestore Database
      await saveUserToFirestore(fbUser, { provider: 'google' });
      return { success: true };
    } catch (err) {
      if (err.code === 'auth/popup-closed-by-user') {
        return { success: false, message: 'Sign-in popup was closed.' };
      }
      return { success: false, message: friendlyError(err.code) };
    }
  };

  // ── Logout ───────────────────────────────────────────────────────────────
  const logout = async () => {
    await signOut(auth);
  };

  return (
    <AuthContext.Provider value={{
      user, 
      signup, 
      login, 
      loginWithGoogle, 
      logout,
      loading 
    }}>
        {children}
    </AuthContext.Provider>
  );
};

// ── Friendly Error Messages ────────────────────────────────────────────────
const friendlyError = (code) => {
  const map = {
    'auth/email-already-in-use':    'An account with this email already exists. Login instead.',
    'auth/invalid-email':           'Invalid email address.',
    'auth/weak-password':           'Password is too weak. Use at least 6 characters.',
    'auth/user-not-found':          'No account found with this email.',
    'auth/wrong-password':          'Incorrect password.',
    'auth/invalid-credential':      'Incorrect email or password.',
    'auth/network-request-failed':  'Network error. Please check your internet.',
    'auth/invalid-app-credential':  'Firebase configuration is invalid. Please check your API keys.',
    'auth/unauthorized-domain':     'This domain is not authorized for OAuth operations for your Firebase project.',
  };
  return map[code] || null; // Return null so we can fallback to the raw error message if it's unknown
};
