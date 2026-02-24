import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { Filter, ChevronDown, ChevronUp, Search, X, Smartphone, Laptop, Headphones, Watch, Gamepad2, Footprints, SlidersHorizontal } from 'lucide-react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import ProductCard from '../components/ProductCard';
import axios from 'axios';

const categoryConfig = [
    { name: 'Smartphones', icon: Smartphone, color: 'text-blue-500' },
    { name: 'Laptops', icon: Laptop, color: 'text-violet-500' },
    { name: 'Audio', icon: Headphones, color: 'text-pink-500' },
    { name: 'Watches', icon: Watch, color: 'text-amber-500' },
    { name: 'Gaming', icon: Gamepad2, color: 'text-emerald-500' },
    { name: 'Footwear', icon: Footprints, color: 'text-red-500' },
];

// Fallback products when AI service is not running
const fallbackProducts = [
    // Smartphones
    { id: 'iphone_15', name: 'Apple iPhone 15 (128 GB) - Black', category: 'Smartphones', image: 'https://m.media-amazon.com/images/I/71657TiFeHL._SX679_.jpg', price: 72999, originalPrice: 79900, discount: 9, rating: 4.6, reviews: 3450, platform: 'Amazon' },
    { id: 'samsung_s24', name: 'Samsung Galaxy S24 Ultra 5G AI Smartphone', category: 'Smartphones', image: 'https://m.media-amazon.com/images/I/71CXhVhpM0L._SX679_.jpg', price: 128500, originalPrice: 134999, discount: 5, rating: 4.5, reviews: 1250, platform: 'Flipkart' },
    { id: 'oneplus_12', name: 'OnePlus 12 (Flowy Emerald, 16GB RAM, 512GB)', category: 'Smartphones', image: 'https://m.media-amazon.com/images/I/717Qo4MH97L._SX679_.jpg', price: 69999, originalPrice: 75999, discount: 8, rating: 4.4, reviews: 890, platform: 'Amazon' },
    { id: 'pixel_8', name: 'Google Pixel 8 (Hazel, 128 GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/google-pixel-8.jpg', price: 62999, originalPrice: 75999, discount: 17, rating: 4.3, reviews: 450, platform: 'Flipkart' },
    { id: 'xiaomi_14_pro', name: 'Xiaomi 14 Pro 5G (Obsidian Black, 12GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-14-pro.jpg', price: 54999, originalPrice: 59999, discount: 8, rating: 4.3, reviews: 620, platform: 'Flipkart' },
    { id: 'vivo_x100_pro', name: 'Vivo X100 Pro 5G (Asteroid Black, 16GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/vivo-x100-pro.jpg', price: 89999, originalPrice: 99999, discount: 10, rating: 4.5, reviews: 480, platform: 'Amazon' },
    { id: 'realme_gt5_pro', name: 'Realme GT 5 Pro 5G (Racing Green, 12GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/realme-gt5-pro.jpg', price: 35999, originalPrice: 40999, discount: 12, rating: 4.4, reviews: 720, platform: 'Flipkart' },
    { id: 'nothing_phone_2', name: 'Nothing Phone (2) 5G (White, 12GB, 256GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/nothing-phone2.jpg', price: 34999, originalPrice: 44999, discount: 22, rating: 4.3, reviews: 1100, platform: 'Flipkart' },
    { id: 'samsung_s23_ultra', name: 'Samsung Galaxy S23 Ultra 5G (Cream, 12GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-ultra-5g.jpg', price: 99999, originalPrice: 124999, discount: 20, rating: 4.7, reviews: 5200, platform: 'Amazon' },
    { id: 'samsung_a55', name: 'Samsung Galaxy A55 5G (Awesome Iceblue, 8GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a55.jpg', price: 27999, originalPrice: 32999, discount: 15, rating: 4.2, reviews: 2100, platform: 'Flipkart' },
    { id: 'redmi_note_13_pro', name: 'Redmi Note 13 Pro+ 5G (Fusion Purple, 12GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-pro-plus.jpg', price: 29999, originalPrice: 33999, discount: 12, rating: 4.3, reviews: 3200, platform: 'Amazon' },
    { id: 'pixel_7a', name: 'Google Pixel 7a (Charcoal, 128 GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/google-pixel-7a.jpg', price: 28999, originalPrice: 43999, discount: 34, rating: 4.4, reviews: 2200, platform: 'Flipkart' },
    { id: 'poco_f6_pro', name: 'POCO F6 Pro 5G (Black, 12GB RAM, 256GB)', category: 'Smartphones', image: 'https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-f6-pro.jpg', price: 31999, originalPrice: 34999, discount: 9, rating: 4.4, reviews: 920, platform: 'Flipkart' },
    // Laptops
    { id: 'macbook_air_m2', name: 'Apple MacBook Air M2 13.6-inch, 8GB RAM, 256GB SSD', category: 'Laptops', image: 'https://m.media-amazon.com/images/I/71f5Eu5lJSL._SX679_.jpg', price: 86990, originalPrice: 114900, discount: 24, rating: 4.7, reviews: 1400, platform: 'Flipkart' },
    { id: 'dell_xps_13', name: 'Dell XPS 13 Plus, Intel Core i7, 16GB, 1TB SSD', category: 'Laptops', image: 'https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/xps-notebooks/xps-13-9320/media-gallery/copy-of-xs9320nt-cnb-05-bk.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=555', price: 159990, originalPrice: 199990, discount: 20, rating: 4.2, reviews: 120, platform: 'Flipkart' },
    { id: 'hp_spectre', name: 'HP Spectre x360 2-in-1 13.5-inch, Intel Evo i7', category: 'Laptops', image: 'https://m.media-amazon.com/images/I/61s7s+4-+5L._SX679_.jpg', price: 134999, originalPrice: 150000, discount: 10, rating: 4.5, reviews: 310, platform: 'Amazon' },
    // Audio
    { id: 'sony_headphones', name: 'Sony WH-1000XM5 Wireless Noise Cancelling Headphones', category: 'Audio', image: 'https://m.media-amazon.com/images/I/51SKmu2G9FL._SX679_.jpg', price: 29990, originalPrice: 34990, discount: 14, rating: 4.8, reviews: 8900, platform: 'Amazon' },
    { id: 'airpods_pro', name: 'Apple AirPods Pro (2nd Gen) with MagSafe Case', category: 'Audio', image: 'https://m.media-amazon.com/images/I/61SUj2aKoEL._SX679_.jpg', price: 22999, originalPrice: 24900, discount: 8, rating: 4.7, reviews: 5600, platform: 'Amazon' },
    { id: 'jbl_flip_6', name: 'JBL Flip 6 Wireless Portable Bluetooth Speaker', category: 'Audio', image: 'https://m.media-amazon.com/images/I/61+R5r29rQL._SX679_.jpg', price: 9999, originalPrice: 14999, discount: 33, rating: 4.5, reviews: 12000, platform: 'Amazon' },
    // Watches
    { id: 'apple_watch_ultra', name: 'Apple Watch Ultra 2 (GPS + Cellular, 49mm) Titanium', category: 'Watches', image: 'https://m.media-amazon.com/images/I/81P5-189VzL._SX679_.jpg', price: 89900, originalPrice: 89900, discount: 0, rating: 4.9, reviews: 890, platform: 'Amazon' },
    { id: 'samsung_watch_6', name: 'Samsung Galaxy Watch6 Classic LTE (47mm, Black)', category: 'Watches', image: 'https://m.media-amazon.com/images/I/61N+x-jA9UL._SX679_.jpg', price: 36999, originalPrice: 40999, discount: 10, rating: 4.4, reviews: 1500, platform: 'Flipkart' },
    // Gaming
    { id: 'playstation_5', name: 'Sony PlayStation 5 Console (Slim)', category: 'Gaming', image: 'https://m.media-amazon.com/images/I/51051FiD9UL._SX679_.jpg', price: 54990, originalPrice: 54990, discount: 0, rating: 4.8, reviews: 5600, platform: 'Amazon' },
    { id: 'xbox_series_x', name: 'Xbox Series X Console', category: 'Gaming', image: 'https://m.media-amazon.com/images/I/61-jjE67uqL._SX679_.jpg', price: 49990, originalPrice: 54990, discount: 9, rating: 4.7, reviews: 4200, platform: 'Amazon' },
    // Footwear
    { id: 'nike_air_jordan', name: "Nike Air Jordan 1 Retro High OG 'Chicago'", category: 'Footwear', image: 'https://m.media-amazon.com/images/I/71zLz6m5Q+L._AC_UY1100_.jpg', price: 16995, originalPrice: 18995, discount: 11, rating: 4.9, reviews: 450, platform: 'Amazon' },
    { id: 'adidas_ultraboost', name: "Adidas Men's Ultraboost Light Running Shoes", category: 'Footwear', image: 'https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/0fbed4646c1d46e0aae0afc90122d10d_9366/Ultraboost_Light_Running_Shoes_White_HQ6351_01_standard.jpg', price: 11999, originalPrice: 18999, discount: 37, rating: 4.6, reviews: 2100, platform: 'Flipkart' },
    { id: 'puma_nitro', name: "Puma Deviate Nitro 2 Men's Running Shoes", category: 'Footwear', image: 'https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa,w_600,h_600/global/376807/01/sv01/fnd/IND/fmt/png/Deviate-NITRO-Elite-2-Men\'s-Running-Shoes', price: 13999, originalPrice: 15999, discount: 13, rating: 4.3, reviews: 850, platform: 'Amazon' },
];

const Products = () => {
    const [searchParams, setSearchParams] = useSearchParams();
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [priceRange, setPriceRange] = useState(150000);
    const [selectedCategories, setSelectedCategories] = useState([]);
    const [selectedRatings, setSelectedRatings] = useState([]);
    const [sortBy, setSortBy] = useState('relevance');
    const [searchTerm, setSearchTerm] = useState("");
    const [showCategoryFilter, setShowCategoryFilter] = useState(true);
    const [showRatingFilter, setShowRatingFilter] = useState(true);

    // Read category from URL on mount
    useEffect(() => {
        const urlCategory = searchParams.get('category');
        if (urlCategory) {
            setSelectedCategories([urlCategory]);
        }
    }, []);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get('http://localhost:5001/products');
                const transformed = response.data.map(p => ({
                    ...p,
                    reviews: p.reviews_count,
                    originalPrice: p.original_price,
                    platform: p.ai_recommendation?.store || 'Amazon'
                }));
                setProducts(transformed);
            } catch (err) {
                console.error("AI service not available, using fallback products");
                setProducts(fallbackProducts);
            } finally {
                setLoading(false);
            }
        };
        fetchProducts();
    }, []);

    const toggleCategory = (category) => {
        setSelectedCategories(prev => {
            const newCategories = prev.includes(category)
                ? prev.filter(c => c !== category)
                : [...prev, category];

            // Update URL params
            if (newCategories.length === 0) {
                searchParams.delete('category');
            } else if (newCategories.length === 1) {
                searchParams.set('category', newCategories[0]);
            } else {
                searchParams.delete('category');
            }
            setSearchParams(searchParams, { replace: true });

            return newCategories;
        });
    };

    const toggleRating = (rating) => {
        setSelectedRatings(prev =>
            prev.includes(rating) ? prev.filter(r => r !== rating) : [...prev, rating]
        );
    };

    const clearAllFilters = () => {
        setSelectedCategories([]);
        setSelectedRatings([]);
        setPriceRange(150000);
        setSearchTerm("");
        searchParams.delete('category');
        setSearchParams(searchParams, { replace: true });
    };

    const activeFilterCount = selectedCategories.length + selectedRatings.length + (priceRange < 150000 ? 1 : 0) + (searchTerm ? 1 : 0);

    // Filter products
    const filteredProducts = products.filter(product => {
        const matchesSearch = product.name.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesPrice = product.price <= priceRange;
        const matchesCategory = selectedCategories.length === 0 || selectedCategories.includes(product.category);
        const matchesRating = selectedRatings.length === 0 || selectedRatings.some(r => product.rating >= r);
        return matchesSearch && matchesPrice && matchesCategory && matchesRating;
    });

    // Sort products
    const sortedProducts = [...filteredProducts].sort((a, b) => {
        switch (sortBy) {
            case 'price-low': return a.price - b.price;
            case 'price-high': return b.price - a.price;
            case 'rating': return b.rating - a.rating;
            default: return 0;
        }
    });

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-darkBackground transition-colors duration-300">
            <Navbar />

            <div className="container mx-auto px-4 pt-24 pb-12 flex flex-col lg:flex-row gap-8">
                {/* Sidebar Filters */}
                <motion.aside
                    initial={{ x: -50, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    className="lg:w-1/4"
                >
                    <div className="bg-white dark:bg-darkSurface p-6 rounded-2xl shadow-sm sticky top-24 transition-colors duration-300 border border-gray-100 dark:border-gray-700/50">
                        <div className="flex items-center justify-between mb-6">
                            <h2 className="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
                                <SlidersHorizontal size={20} className="text-primary" /> Filters
                                {activeFilterCount > 0 && (
                                    <span className="text-xs bg-primary text-white px-2 py-0.5 rounded-full">{activeFilterCount}</span>
                                )}
                            </h2>
                            <button
                                onClick={clearAllFilters}
                                className="text-sm text-primary font-semibold hover:underline flex items-center gap-1"
                            >
                                Clear All
                            </button>
                        </div>

                        {/* Active Filter Tags */}
                        {activeFilterCount > 0 && (
                            <div className="flex flex-wrap gap-2 mb-5">
                                {selectedCategories.map(cat => (
                                    <span key={cat} className="inline-flex items-center gap-1 bg-primary/10 text-primary text-xs font-semibold px-3 py-1 rounded-full">
                                        {cat}
                                        <X size={12} className="cursor-pointer hover:text-red-500" onClick={() => toggleCategory(cat)} />
                                    </span>
                                ))}
                                {selectedRatings.map(r => (
                                    <span key={r} className="inline-flex items-center gap-1 bg-yellow-100 text-yellow-700 text-xs font-semibold px-3 py-1 rounded-full dark:bg-yellow-900/30 dark:text-yellow-400">
                                        {r}★+
                                        <X size={12} className="cursor-pointer hover:text-red-500" onClick={() => toggleRating(r)} />
                                    </span>
                                ))}
                            </div>
                        )}

                        {/* Price Filter */}
                        <div className="mb-8">
                            <h3 className="text-sm font-bold text-gray-700 dark:text-gray-300 mb-4 uppercase tracking-wider">Price Range</h3>
                            <input
                                type="range"
                                min="0"
                                max="150000"
                                value={priceRange}
                                onChange={(e) => setPriceRange(Number(e.target.value))}
                                className="w-full h-2 bg-gray-200 dark:bg-gray-700 rounded-lg appearance-none cursor-pointer accent-primary"
                            />
                            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400 mt-2">
                                <span>₹0</span>
                                <span className="font-semibold text-primary">₹{Number(priceRange).toLocaleString()}</span>
                            </div>
                        </div>

                        {/* Category Filter */}
                        <div className="mb-8">
                            <button
                                onClick={() => setShowCategoryFilter(!showCategoryFilter)}
                                className="w-full text-sm font-bold text-gray-700 dark:text-gray-300 mb-4 uppercase tracking-wider flex items-center justify-between cursor-pointer hover:text-primary transition-colors"
                            >
                                Category
                                {showCategoryFilter ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                            </button>
                            <AnimatePresence>
                                {showCategoryFilter && (
                                    <motion.div
                                        initial={{ height: 0, opacity: 0 }}
                                        animate={{ height: 'auto', opacity: 1 }}
                                        exit={{ height: 0, opacity: 0 }}
                                        className="space-y-2 overflow-hidden"
                                    >
                                        {categoryConfig.map((cat) => {
                                            const CatIcon = cat.icon;
                                            const isSelected = selectedCategories.includes(cat.name);
                                            return (
                                                <label
                                                    key={cat.name}
                                                    onClick={() => toggleCategory(cat.name)}
                                                    className={`flex items-center gap-3 cursor-pointer group p-2 rounded-lg transition-all duration-200 ${isSelected ? 'bg-primary/10 dark:bg-primary/20' : 'hover:bg-gray-50 dark:hover:bg-gray-800'}`}
                                                >
                                                    <div className="relative flex items-center">
                                                        <div className={`w-4 h-4 border-2 rounded flex items-center justify-center transition-all ${isSelected ? 'bg-primary border-primary' : 'border-gray-300 dark:border-gray-600'}`}>
                                                            {isSelected && (
                                                                <svg className="w-3 h-3 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                                                                    <polyline points="20 6 9 17 4 12"></polyline>
                                                                </svg>
                                                            )}
                                                        </div>
                                                    </div>
                                                    <CatIcon size={16} className={`${cat.color} transition-colors`} />
                                                    <span className={`text-sm transition-colors ${isSelected ? 'text-primary font-semibold' : 'text-gray-600 dark:text-gray-400 group-hover:text-primary'}`}>
                                                        {cat.name}
                                                    </span>
                                                </label>
                                            );
                                        })}
                                    </motion.div>
                                )}
                            </AnimatePresence>
                        </div>

                        {/* Rating Filter */}
                        <div>
                            <button
                                onClick={() => setShowRatingFilter(!showRatingFilter)}
                                className="w-full text-sm font-bold text-gray-700 dark:text-gray-300 mb-4 uppercase tracking-wider flex items-center justify-between cursor-pointer hover:text-primary transition-colors"
                            >
                                Customer Ratings
                                {showRatingFilter ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                            </button>
                            <AnimatePresence>
                                {showRatingFilter && (
                                    <motion.div
                                        initial={{ height: 0, opacity: 0 }}
                                        animate={{ height: 'auto', opacity: 1 }}
                                        exit={{ height: 0, opacity: 0 }}
                                        className="space-y-2 overflow-hidden"
                                    >
                                        {[4, 3, 2, 1].map((rating) => {
                                            const isSelected = selectedRatings.includes(rating);
                                            return (
                                                <label
                                                    key={rating}
                                                    onClick={() => toggleRating(rating)}
                                                    className={`flex items-center gap-3 cursor-pointer p-2 rounded-lg transition-all duration-200 ${isSelected ? 'bg-yellow-50 dark:bg-yellow-900/20' : 'hover:bg-gray-50 dark:hover:bg-gray-800'}`}
                                                >
                                                    <div className={`w-4 h-4 border-2 rounded flex items-center justify-center transition-all ${isSelected ? 'bg-yellow-500 border-yellow-500' : 'border-gray-300 dark:border-gray-600'}`}>
                                                        {isSelected && (
                                                            <svg className="w-3 h-3 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                                                                <polyline points="20 6 9 17 4 12"></polyline>
                                                            </svg>
                                                        )}
                                                    </div>
                                                    <div className="flex items-center gap-1">
                                                        {[...Array(5)].map((_, i) => (
                                                            <span key={i} className={`text-xs ${i < rating ? 'text-yellow-400' : 'text-gray-300 dark:text-gray-600'}`}>★</span>
                                                        ))}
                                                    </div>
                                                    <span className={`text-sm ${isSelected ? 'text-yellow-700 dark:text-yellow-400 font-semibold' : 'text-gray-500 dark:text-gray-400'}`}>& above</span>
                                                </label>
                                            );
                                        })}
                                    </motion.div>
                                )}
                            </AnimatePresence>
                        </div>
                    </div>
                </motion.aside>

                {/* Main Content */}
                <main className="lg:w-3/4">
                    {/* Header */}
                    <div className="bg-white dark:bg-darkSurface p-4 rounded-xl shadow-sm mb-6 flex flex-col sm:flex-row items-center justify-between gap-4 transition-colors duration-300 border border-gray-100 dark:border-gray-700/50">
                        <div className="flex-1 w-full sm:w-auto relative">
                            <input
                                type="text"
                                placeholder="Search within results..."
                                className="w-full py-2.5 pl-10 pr-4 bg-gray-100 dark:bg-gray-800 border-none rounded-lg text-sm text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-primary/20 focus:outline-none"
                                value={searchTerm}
                                onChange={(e) => setSearchTerm(e.target.value)}
                            />
                            <Search size={18} className="absolute left-3 top-3 text-gray-400" />
                            {searchTerm && (
                                <button onClick={() => setSearchTerm("")} className="absolute right-3 top-3">
                                    <X size={16} className="text-gray-400 hover:text-gray-600" />
                                </button>
                            )}
                        </div>

                        <div className="flex items-center gap-3">
                            <span className="text-sm text-gray-500 dark:text-gray-400">
                                {sortedProducts.length} product{sortedProducts.length !== 1 ? 's' : ''}
                            </span>
                            <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-300">
                                <span className="hidden sm:inline">Sort:</span>
                                <select
                                    value={sortBy}
                                    onChange={(e) => setSortBy(e.target.value)}
                                    className="bg-transparent font-bold text-gray-900 dark:text-white border-none focus:ring-0 cursor-pointer text-sm"
                                >
                                    <option value="relevance">Relevance</option>
                                    <option value="price-low">Price: Low to High</option>
                                    <option value="price-high">Price: High to Low</option>
                                    <option value="rating">Top Rated</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    {/* Category Quick Pills */}
                    <div className="flex flex-wrap gap-2 mb-6">
                        <button
                            onClick={clearAllFilters}
                            className={`px-4 py-2 rounded-full text-sm font-semibold transition-all duration-200 ${selectedCategories.length === 0 ? 'bg-primary text-white shadow-md shadow-primary/30' : 'bg-white dark:bg-darkSurface text-gray-600 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:border-primary hover:text-primary'}`}
                        >
                            All
                        </button>
                        {categoryConfig.map((cat) => {
                            const CatIcon = cat.icon;
                            const isActive = selectedCategories.includes(cat.name);
                            return (
                                <button
                                    key={cat.name}
                                    onClick={() => {
                                        if (isActive) {
                                            setSelectedCategories([]);
                                            searchParams.delete('category');
                                        } else {
                                            setSelectedCategories([cat.name]);
                                            searchParams.set('category', cat.name);
                                        }
                                        setSearchParams(searchParams, { replace: true });
                                    }}
                                    className={`flex items-center gap-1.5 px-4 py-2 rounded-full text-sm font-semibold transition-all duration-200 ${isActive ? 'bg-primary text-white shadow-md shadow-primary/30' : 'bg-white dark:bg-darkSurface text-gray-600 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:border-primary hover:text-primary'}`}
                                >
                                    <CatIcon size={14} />
                                    {cat.name}
                                </button>
                            );
                        })}
                    </div>

                    {/* Products Grid */}
                    {loading ? (
                        <div className="flex h-64 items-center justify-center">
                            <div className="flex flex-col items-center gap-3">
                                <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
                                <span className="text-gray-400 text-sm">Loading products...</span>
                            </div>
                        </div>
                    ) : (
                        <AnimatePresence mode="wait">
                            <motion.div
                                key={selectedCategories.join(',') + sortBy + searchTerm + priceRange}
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                exit={{ opacity: 0, y: -10 }}
                                transition={{ duration: 0.2 }}
                                className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6"
                            >
                                {sortedProducts.length > 0 ? (
                                    sortedProducts.map((product, i) => (
                                        <motion.div
                                            key={product.id}
                                            initial={{ opacity: 0, y: 20 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            transition={{ delay: i * 0.05 }}
                                        >
                                            <ProductCard product={product} />
                                        </motion.div>
                                    ))
                                ) : (
                                    <div className="col-span-full py-16 text-center text-gray-500 dark:text-gray-400">
                                        <div className="flex justify-center mb-4">
                                            <div className="w-20 h-20 bg-gray-100 dark:bg-gray-800 rounded-full flex items-center justify-center">
                                                <Search size={36} className="text-gray-300 dark:text-gray-600" />
                                            </div>
                                        </div>
                                        <h3 className="text-lg font-bold mb-2">No products found</h3>
                                        <p className="text-sm mb-4">Try adjusting your filters or search term.</p>
                                        <button
                                            onClick={clearAllFilters}
                                            className="text-primary font-semibold text-sm hover:underline"
                                        >
                                            Clear all filters
                                        </button>
                                    </div>
                                )}
                            </motion.div>
                        </AnimatePresence>
                    )}
                </main>
            </div>

            <Footer />
        </div>
    );
};

export default Products;
