"""
Kaggle Dataset Loader - Multi-Platform Product Catalog Builder
Loads datasets from Amazon, Flipkart, Croma, and Meesho
Implements fuzzy matching for intelligent product comparison
"""

import pandas as pd
import json
import re
from difflib import SequenceMatcher
import os

def normalize_product_name(name):
    """Normalize product name for better matching"""
    if pd.isna(name):
        return ""
    
    # Convert to lowercase
    name = str(name).lower()
    
    # Remove special characters but keep spaces
    name = re.sub(r'[^\w\s]', ' ', name)
    
    # Remove common stopwords that don't help matching
    stopwords = ['gb', 'ram', 'storage', 'the', 'a', 'an', 'with', 'for', 'and', 'or']
    words = [w for w in name.split() if w not in stopwords and len(w) > 1]
    
    return ' '.join(words)

def extract_price(price_str):
    """Extract numeric price from string like '₹29,999' or '₹29999'"""
    if pd.isna(price_str):
        return 0
    
    # Remove currency symbols and commas
    price_clean = str(price_str).replace('₹', '').replace('Rs.', '').replace(',', '').strip()
    
    # Extract first number found
    match = re.search(r'[\d.]+', price_clean)
    if match:
        try:
            return int(float(match.group()))
        except:
            return 0
    return 0

def load_amazon_dataset():
    """Load and parse Amazon dataset"""
    print("📦 Loading Amazon dataset...")
    
    try:
        df = pd.read_csv('data/amazon.csv', encoding='utf-8')
        products = []
        
        for idx, row in df.iterrows():
            try:
                product = {
                    'name': str(row['product_name']),
                    'price': extract_price(row['discounted_price']),
                    'original_price': extract_price(row['actual_price']),
                    'rating': float(row['rating']) if pd.notna(row['rating']) else 4.0,
                    'rating_count': int(row['rating_count']) if pd.notna(row['rating_count']) else 0,
                    'category': str(row['category']) if 'category' in row else 'General',
                    'search_key': normalize_product_name(row['product_name'])
                }
                
                if product['price'] > 0:  # Only add if has valid price
                    products.append(product)
                    
            except Exception as e:
                continue
        
        print(f"✅ Loaded {len(products)} Amazon products")
        return products
        
    except FileNotFoundError:
        print("⚠️  Amazon dataset not found in data/amazon.csv")
        return []
    except Exception as e:
        print(f"❌ Error loading Amazon dataset: {e}")
        return []

def load_flipkart_dataset():
    """Load and parse Flipkart dataset"""
    print("📦 Loading Flipkart dataset...")
    
    try:
        df = pd.read_csv('data/flipkart.csv', encoding='utf-8')
        products = []
        
        for idx, row in df.iterrows():
            try:
                # Flipkart dataset has different column names
                product = {
                    'name': str(row.get('product_name', row.get('title', ''))),
                    'price': extract_price(row.get('retail_price', row.get('discounted_price', 0))),
                    'original_price': extract_price(row.get('retail_price', 0)),
                    'rating': float(row.get('product_rating', row.get('rating', 4.0))),
                    'rating_count': int(row.get('overall_rating', row.get('rating_count', 0))),
                    'category': str(row.get('product_category_tree', row.get('category', 'General'))),
                    'brand': str(row.get('brand', '')),
                    'search_key': normalize_product_name(row.get('product_name', row.get('title', '')))
                }
                
                if product['price'] > 0:
                    products.append(product)
                    
            except Exception as e:
                continue
        
        print(f"✅ Loaded {len(products)} Flipkart products")
        return products
        
    except FileNotFoundError:
        print("⚠️  Flipkart dataset not found in data/flipkart.csv")
        return []
    except Exception as e:
        print(f"❌ Error loading Flipkart dataset: {e}")
        return []

def load_croma_dataset():
    """Load and parse Croma dataset"""
    print("📦 Loading Croma dataset...")
    
    try:
        df = pd.read_csv('data/croma.csv', encoding='utf-8')
        products = []
        
        for idx, row in df.iterrows():
            try:
                product = {
                    'name': str(row.get('product_name', row.get('name', ''))),
                    'price': extract_price(row.get('price', row.get('product_price', 0))),
                    'original_price': extract_price(row.get('price', 0)),
                    'rating': 4.0,  # Croma dataset might not have ratings
                    'rating_count': 0,
                    'category': str(row.get('category', 'Electronics')),
                    'search_key': normalize_product_name(row.get('product_name', row.get('name', '')))
                }
                
                if product['price'] > 0:
                    products.append(product)
                    
            except Exception as e:
                continue
        
        print(f"✅ Loaded {len(products)} Croma products")
        return products
        
    except FileNotFoundError:
        print("⚠️  Croma dataset not found in data/croma.csv")
        return []
    except Exception as e:
        print(f"❌ Error loading Croma dataset: {e}")
        return []

def load_meesho_dataset():
    """Load and parse Meesho dataset"""
    print("📦 Loading Meesho dataset...")
    
    try:
        df = pd.read_csv('data/meesho.csv', encoding='utf-8')
        products = []
        
        for idx, row in df.iterrows():
            try:
                product = {
                    'name': str(row.get('product_name', row.get('name', ''))),
                    'price': extract_price(row.get('price', row.get('product_price', 0))),
                    'original_price': extract_price(row.get('price', 0)),
                    'rating': float(row.get('rating', 4.0)),
                    'rating_count': int(row.get('rating_count', 0)),
                    'category': str(row.get('category', 'General')),
                    'search_key': normalize_product_name(row.get('product_name', row.get('name', '')))
                }
                
                if product['price'] > 0:
                    products.append(product)
                    
            except Exception as e:
                continue
        
        print(f"✅ Loaded {len(products)} Meesho products")
        return products
        
    except FileNotFoundError:
        print("⚠️  Meesho dataset not found in data/meesho.csv")
        return []
    except Exception as e:
        print(f"❌ Error loading Meesho dataset: {e}")
        return []

def calculate_similarity(query, product_name):
    """Calculate similarity score between query and product name"""
    return SequenceMatcher(None, query, product_name).ratio()

def build_product_index():
    """Build unified product index from all datasets"""
    print("\n🔨 Building unified product index...")
    
    # Load all datasets
    amazon_products = load_amazon_dataset()
    flipkart_products = load_flipkart_dataset()
    croma_products = load_croma_dataset()
    meesho_products = load_meesho_dataset()
    
    # Build index
    product_index = {}
    
    # Add Amazon products
    for product in amazon_products:
        key = product['search_key']
        if key not in product_index:
            product_index[key] = {}
        product_index[key]['amazon'] = product
    
    # Add Flipkart products
    for product in flipkart_products:
        key = product['search_key']
        if key not in product_index:
            product_index[key] = {}
        product_index[key]['flipkart'] = product
    
    # Add Croma products
    for product in croma_products:
        key = product['search_key']
        if key not in product_index:
            product_index[key] = {}
        product_index[key]['croma'] = product
    
    # Add Meesho products
    for product in meesho_products:
        key = product['search_key']
        if key not in product_index:
            product_index[key] = {}
        product_index[key]['meesho'] = product
    
    total_unique = len(product_index)
    total_products = len(amazon_products) + len(flipkart_products) + len(croma_products) + len(meesho_products)
    
    print(f"\n✅ Index built successfully!")
    print(f"   Total unique products: {total_unique}")
    print(f"   Total product entries: {total_products}")
    
    return product_index

def save_product_index(product_index, filename='product_index.json'):
    """Save product index to JSON file"""
    print(f"\n💾 Saving product index to {filename}...")
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(product_index, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved successfully!")

if __name__ == "__main__":
    print("=" * 60)
    print("  KAGGLE DATASET LOADER - Multi-Platform Product Index")
    print("=" * 60)
    
    # Build index
    product_index = build_product_index()
    
    # Save to JSON
    save_product_index(product_index)
    
    print("\n" + "=" * 60)
    print("  ✅ Process Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Check product_index.json was created")
    print("2. Run 'python app.py' to start the Flask server")
    print("3. The scraper will now use real data from 4 platforms!")
