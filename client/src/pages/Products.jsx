import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Filter, ChevronDown, Search } from 'lucide-react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import ProductCard from '../components/ProductCard';
import axios from 'axios';

const Products = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [priceRange, setPriceRange] = useState(150000);
    const [selectedCategories, setSelectedCategories] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const response = await axios.get('http://localhost:5001/products');
                // Transform data to match ProductCard expectations if necessary
                const transformed = response.data.map(p => ({
                    ...p,
                    reviews: p.reviews_count,
                    originalPrice: p.original_price,
                    platform: p.ai_recommendation?.store || 'Amazon'
                }));
                setProducts(transformed);
            } catch (err) {
                console.error("Failed to fetch products", err);
            } finally {
                setLoading(false);
            }
        };
        fetchProducts();
    }, []);

    const [searchTerm, setSearchTerm] = useState("");

    // Filter products based on search term & price
    const filteredProducts = products.filter(product => {
        const matchesSearch = product.name.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesPrice = product.price <= priceRange;
        // const matchesCategory = selectedCategories.length === 0 || selectedCategories.includes(product.category);
        return matchesSearch && matchesPrice;
    });

    const categories = ['Smartphones', 'Headphones', 'Laptops', 'Footwear', 'Watches'];

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-darkBg transition-colors duration-300">
            <Navbar />

            <div className="container mx-auto px-4 pt-24 pb-12 flex flex-col lg:flex-row gap-8">
                {/* Sidebar Filters */}
                <motion.aside
                    initial={{ x: -50, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    className="lg:w-1/4"
                >
                    <div className="bg-white dark:bg-darkSurface p-6 rounded-2xl shadow-sm sticky top-24 transition-colors duration-300">
                        <div className="flex items-center justify-between mb-6">
                            <h2 className="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
                                <Filter size={20} /> Filters
                            </h2>
                            <button className="text-sm text-primary font-semibold hover:underline">Clear All</button>
                        </div>

                        {/* Price Filter */}
                        <div className="mb-8">
                            <h3 className="text-sm font-bold text-gray-700 dark:text-gray-300 mb-4 uppercase tracking-wider">Price Range</h3>
                            <input
                                type="range"
                                min="0"
                                max="150000"
                                value={priceRange}
                                onChange={(e) => setPriceRange(e.target.value)}
                                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-primary"
                            />
                            <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400 mt-2">
                                <span>₹0</span>
                                <span>₹{Number(priceRange).toLocaleString()}</span>
                            </div>
                        </div>

                        {/* Category Filter */}
                        <div className="mb-8">
                            <h3 className="text-sm font-bold text-gray-700 dark:text-gray-300 mb-4 uppercase tracking-wider flex items-center justify-between cursor-pointer">
                                Category <ChevronDown size={16} />
                            </h3>
                            <div className="space-y-3">
                                {categories.map((category) => (
                                    <label key={category} className="flex items-center gap-3 cursor-pointer group">
                                        <div className="relative flex items-center">
                                            <input type="checkbox" className="peer w-4 h-4 border-2 border-gray-300 rounded checked:bg-primary checked:border-primary transition-colors appearance-none" />
                                            <svg className="absolute w-4 h-4 text-white hidden peer-checked:block pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                                                <polyline points="20 6 9 17 4 12"></polyline>
                                            </svg>
                                        </div>
                                        <span className="text-gray-600 dark:text-gray-400 group-hover:text-primary transition-colors">{category}</span>
                                    </label>
                                ))}
                            </div>
                        </div>

                        {/* Rating Filter */}
                        <div>
                            <h3 className="text-sm font-bold text-gray-700 dark:text-gray-300 mb-4 uppercase tracking-wider">Customer Ratings</h3>
                            <div className="space-y-2">
                                {[4, 3, 2, 1].map((rating) => (
                                    <label key={rating} className="flex items-center gap-2 cursor-pointer">
                                        <input type="checkbox" className="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary" />
                                        <span className="text-gray-600 dark:text-gray-400 text-sm">{rating}★ & above</span>
                                    </label>
                                ))}
                            </div>
                        </div>
                    </div>
                </motion.aside>

                {/* Main Content */}
                <main className="lg:w-3/4">
                    {/* Header */}
                    <div className="bg-white dark:bg-darkSurface p-4 rounded-xl shadow-sm mb-6 flex flex-col sm:flex-row items-center justify-between gap-4 transition-colors duration-300">
                        <div className="flex-1 w-full sm:w-auto relative">
                            <input
                                type="text"
                                placeholder="Search within results..."
                                className="w-full py-2.5 pl-10 pr-4 bg-gray-100 dark:bg-gray-800 border-none rounded-lg text-sm text-gray-800 dark:text-gray-200 focus:ring-2 focus:ring-primary/20"
                                value={searchTerm}
                                onChange={(e) => setSearchTerm(e.target.value)}
                            />
                            <Search size={18} className="absolute left-3 top-3 text-gray-400" />
                        </div>

                        <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-300">
                            <span className="hidden sm:inline">Sort By:</span>
                            <select className="bg-transparent font-bold text-gray-900 dark:text-white border-none focus:ring-0 cursor-pointer">
                                <option>Relevance</option>
                                <option>Price: Low to High</option>
                                <option>Price: High to Low</option>
                                <option>Newest First</option>
                            </select>
                        </div>
                    </div>

                    {/* Products Grid */}
                    {loading ? (
                        <div className="flex h-64 items-center justify-center">
                            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
                        </div>
                    ) : (
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                            {filteredProducts.length > 0 ? (
                                filteredProducts.map((product) => (
                                    <ProductCard key={product.id} product={product} />
                                ))
                            ) : (
                                <div className="col-span-full py-12 text-center text-gray-500 dark:text-gray-400">
                                    <div className="flex justify-center mb-4">
                                        <Search size={48} className="text-gray-300 dark:text-gray-700" />
                                    </div>
                                    <h3 className="text-lg font-bold mb-1">No products found</h3>
                                    <p>Try adjusting your filters or search term.</p>
                                </div>
                            )}
                        </div>
                    )}

                    {/* Pagination */}
                    <div className="mt-12 flex justify-center gap-2">
                        <button className="w-10 h-10 flex items-center justify-center rounded-full bg-primary text-white font-bold shadow-lg shadow-primary/30">1</button>
                        <button className="w-10 h-10 flex items-center justify-center rounded-full bg-white dark:bg-darkSurface text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">2</button>
                        <button className="w-10 h-10 flex items-center justify-center rounded-full bg-white dark:bg-darkSurface text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors">3</button>
                    </div>
                </main>
            </div>

            <Footer />
        </div>
    );
};

export default Products;
