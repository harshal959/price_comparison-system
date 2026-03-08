import json
import random
import re

# ============================================================
# 100 PRODUCT CATALOG GENERATOR FOR SMARTPICK
# ============================================================

STORE_LOGOS = {
    "Amazon": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg",
    "Flipkart": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png",
    "Croma": "https://logo.clearbit.com/croma.com"
}

STORE_COLORS = {
    "Amazon": "#FF9900",
    "Flipkart": "#2874F0",
    "Croma": "#00B5B5"
}

MONTHS = ["Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May"]

# ============================================================
# PRODUCT DATA — 100 real products across 6 categories
# ============================================================

products_data = [
    # ===== SMARTPHONES (25) =====
    {"name": "Apple iPhone 15 Pro Max (256 GB) - Natural Titanium", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/81SigpJN1KL._SX679_.jpg", "price": 134900, "original_price": 159900, "rating": 4.6, "reviews_count": 8920},
    {"name": "Samsung Galaxy S24 Ultra 5G AI Smartphone (Titanium Gray, 12GB, 256GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71Ib-VpzidL._SX679_.jpg", "price": 119999, "original_price": 134999, "rating": 4.5, "reviews_count": 7435},
    {"name": "OnePlus 12 (Silky Black, 12GB RAM, 256GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71CIQS8MReL._SX679_.jpg", "price": 59999, "original_price": 69999, "rating": 4.4, "reviews_count": 5620},
    {"name": "Google Pixel 8 Pro (Obsidian, 12GB RAM, 128GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71p-CvaFMML._SX679_.jpg", "price": 84999, "original_price": 106999, "rating": 4.5, "reviews_count": 3890},
    {"name": "Samsung Galaxy A55 5G (Awesome Navy, 8GB RAM, 256GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71EeBkydf9L._AC_UY218_.jpg", "price": 27999, "original_price": 45999, "rating": 4.3, "reviews_count": 4518},
    {"name": "OnePlus Nord CE5 | MediaTek Dimensity | 128GB 8GB | Black Infinity", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/61IOa9IrlaL._AC_UY218_.jpg", "price": 24998, "original_price": 28999, "rating": 4.4, "reviews_count": 2590},
    {"name": "Xiaomi 14 Ultra 5G (Black, 16GB RAM, 512GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/41Bg1e3WK+L._SX300_SY300_QL70_FMwebp_.jpg", "price": 89999, "original_price": 99999, "rating": 4.3, "reviews_count": 1205},
    {"name": "iQOO 12 5G (Legend, 12GB RAM, 256GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71cLNjDqwgL._SX679_.jpg", "price": 47999, "original_price": 56999, "rating": 4.4, "reviews_count": 3455},
    {"name": "realme 13 Pro 5G (Emerald Green, 8GB + 128GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/713ohu6PUNL._AC_UY218_.jpg", "price": 19999, "original_price": 28999, "rating": 4.4, "reviews_count": 2378},
    {"name": "Motorola Edge 50 Pro 5G (Moonlight Pearl, 12GB RAM, 256GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71g3lYYPqOL._SX679_.jpg", "price": 31999, "original_price": 39999, "rating": 4.2, "reviews_count": 1960},
    {"name": "Samsung Galaxy S24 FE 5G AI Smartphone (Graphite, 8GB, 128GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71eUNTW+nJL._AC_UY218_.jpg", "price": 38285, "original_price": 59999, "rating": 4.4, "reviews_count": 3240},
    {"name": "Vivo X100 Pro 5G (Asteroid Black, 16GB RAM, 512GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71NJjay+xTL._SX679_.jpg", "price": 79999, "original_price": 89999, "rating": 4.5, "reviews_count": 2145},
    {"name": "Nothing Phone (2a) Plus (Grey, 8GB RAM, 256GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/61QRgOgBx0L._SX679_.jpg", "price": 24999, "original_price": 29999, "rating": 4.3, "reviews_count": 4580},
    {"name": "POCO X6 Pro 5G (Nebula Green, 12GB RAM, 256GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71c4a7m5-wL._SX679_.jpg", "price": 22999, "original_price": 28999, "rating": 4.2, "reviews_count": 5670},
    {"name": "Apple iPhone 15 (Blue, 128 GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71657TiFeHL._SX679_.jpg", "price": 69990, "original_price": 79900, "rating": 4.6, "reviews_count": 9230},
    {"name": "Samsung Galaxy Z Fold5 5G (Phantom Black, 12GB RAM, 256GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71lOj7-DFjL._SX679_.jpg", "price": 129999, "original_price": 154999, "rating": 4.3, "reviews_count": 2890},
    {"name": "OnePlus 13 5G (Midnight Ocean, 12GB + 256GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/61BTIyv+XdL._AC_UY218_.jpg", "price": 55999, "original_price": 65999, "rating": 4.5, "reviews_count": 4704},
    {"name": "Redmi Note 13 Pro+ 5G (Fusion Purple, 12GB RAM, 256GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71KlGNVkMbL._SX679_.jpg", "price": 27999, "original_price": 34999, "rating": 4.3, "reviews_count": 8900},
    {"name": "Tecno Pova 7 Pro 5G (Geek Black, 8GB + 256GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71ZphsZk2eL._AC_UY218_.jpg", "price": 18249, "original_price": 23999, "rating": 4.2, "reviews_count": 3770},
    {"name": "Oppo Reno 12 Pro 5G (Space Brown, 12GB RAM, 256GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/61DP1-HsHWL._SX679_.jpg", "price": 33999, "original_price": 39999, "rating": 4.3, "reviews_count": 1890},
    {"name": "Apple iPhone 16 (Ultramarine, 128 GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/61v2pBMxjGL._SX679_.jpg", "price": 79900, "original_price": 89900, "rating": 4.5, "reviews_count": 3560},
    {"name": "Samsung Galaxy A35 5G (Awesome Lilac, 8GB RAM, 128GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/61NsPikkMBL._AC_UY218_.jpg", "price": 21499, "original_price": 30999, "rating": 4.2, "reviews_count": 5120},
    {"name": "realme 15 Pro 5G (Green, 8GB RAM, 256GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/61jSTRLVxkL._AC_UY218_.jpg", "price": 31999, "original_price": 37999, "rating": 4.5, "reviews_count": 479},
    {"name": "Lava Blaze X 5G (Glass Red, 8GB RAM, 128GB Storage)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/61nB9DwIXkL._AC_UY218_.jpg", "price": 13999, "original_price": 17999, "rating": 4.1, "reviews_count": 2340},
    {"name": "Infinix GT 20 Pro 5G (Mecha Blue, 8GB RAM, 256GB)", "category": "Smartphones", "image": "https://m.media-amazon.com/images/I/71hf6Gc2QaL._SX679_.jpg", "price": 21999, "original_price": 27999, "rating": 4.2, "reviews_count": 1560},

    # ===== LAPTOPS (20) =====
    {"name": "Apple MacBook Air M2 Chip (13.6-inch, 8GB RAM, 256GB SSD) - Midnight", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71f5Eu5lJSL._SX679_.jpg", "price": 86990, "original_price": 114900, "rating": 4.7, "reviews_count": 5230},
    {"name": "Apple MacBook Pro M3 Chip (14-inch, 18GB RAM, 512GB SSD) - Space Black", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/61lsexTMOXL._SX679_.jpg", "price": 169900, "original_price": 199900, "rating": 4.8, "reviews_count": 2870},
    {"name": "HP Pavilion 15 Laptop, 12th Gen Intel Core i5, 16GB DDR4, 512GB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71Sc0AtvfDL._SX679_.jpg", "price": 54990, "original_price": 68999, "rating": 4.3, "reviews_count": 4560},
    {"name": "Dell XPS 13 Plus 13th Gen Intel Core i7, 16GB LPDDR5, 512GB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71M1HnPmCQL._SX679_.jpg", "price": 119990, "original_price": 149990, "rating": 4.5, "reviews_count": 1890},
    {"name": "Lenovo IdeaPad Slim 5 14th Gen Intel Core i5, 16GB, 512GB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71FtPSvfYRL._SX679_.jpg", "price": 58990, "original_price": 76890, "rating": 4.4, "reviews_count": 3210},
    {"name": "ASUS ROG Strix G16 (2024) Intel Core i9-14900HX, RTX 4060, 16GB, 1TB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71J+ixGdm7L._SX679_.jpg", "price": 119990, "original_price": 145990, "rating": 4.5, "reviews_count": 2450},
    {"name": "Acer Aspire 5 12th Gen Intel Core i5, 8GB RAM, 512GB SSD, 15.6\" FHD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71UcT5D0A3L._SX679_.jpg", "price": 41990, "original_price": 56999, "rating": 4.2, "reviews_count": 6780},
    {"name": "HP Victus 15 Gaming Laptop, AMD Ryzen 5, RTX 3050, 16GB RAM, 512GB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71ZKDkEvsnL._SX679_.jpg", "price": 57490, "original_price": 71999, "rating": 4.3, "reviews_count": 5120},
    {"name": "MSI Thin 15 Gaming Laptop, 12th Gen Intel Core i5, RTX 4050, 16GB, 512GB", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/51cEJKUHExL._SX679_.jpg", "price": 64990, "original_price": 82990, "rating": 4.3, "reviews_count": 1870},
    {"name": "Lenovo LOQ 15IRX9 Intel Core i7-13650HX, RTX 4060, 16GB, 512GB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/61RcE3mFe4L._SX679_.jpg", "price": 89990, "original_price": 113990, "rating": 4.4, "reviews_count": 2340},
    {"name": "Apple MacBook Air M3 Chip (15.3-inch, 8GB RAM, 256GB SSD) - Starlight", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71PCXC4WT-L._SX679_.jpg", "price": 114900, "original_price": 134900, "rating": 4.7, "reviews_count": 1560},
    {"name": "Dell Inspiron 14 14th Gen Intel Core i5, 16GB RAM, 512GB SSD, 14\" FHD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71XfkGA0y4L._SX679_.jpg", "price": 52990, "original_price": 67990, "rating": 4.2, "reviews_count": 3450},
    {"name": "Acer Nitro V 13th Gen Intel Core i5, RTX 4050, 16GB, 512GB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71d3pI2fQFL._SX679_.jpg", "price": 69990, "original_price": 87990, "rating": 4.3, "reviews_count": 4120},
    {"name": "ASUS Vivobook 15 AMD Ryzen 5 7530U, 8GB RAM, 512GB SSD, 15.6\" FHD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71Q-6MFsPLL._SX679_.jpg", "price": 39990, "original_price": 55990, "rating": 4.2, "reviews_count": 7850},
    {"name": "Samsung Galaxy Book4 Pro 13th Gen Intel Core i7, 16GB, 512GB SSD, AMOLED", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/61VO0FQ9JcL._SX679_.jpg", "price": 109990, "original_price": 136990, "rating": 4.4, "reviews_count": 1230},
    {"name": "Lenovo ThinkPad E16 12th Gen Intel Core i5, 16GB, 512GB SSD, 16\" FHD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/51dLJjLqCrL._SX679_.jpg", "price": 56990, "original_price": 73390, "rating": 4.4, "reviews_count": 2890},
    {"name": "HP 15 AMD Ryzen 3 7320U, 8GB RAM, 256GB SSD, 15.6\" FHD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71H7EPCW43L._SX679_.jpg", "price": 29990, "original_price": 39990, "rating": 4.1, "reviews_count": 9340},
    {"name": "ASUS TUF Gaming A15 AMD Ryzen 7, RTX 4060, 16GB, 1TB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/71IXVKPt4tL._SX679_.jpg", "price": 94990, "original_price": 115990, "rating": 4.4, "reviews_count": 3560},
    {"name": "Microsoft Surface Laptop 5 12th Gen Intel Core i5, 8GB, 256GB SSD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/61aU3fXuajL._SX679_.jpg", "price": 79990, "original_price": 104999, "rating": 4.3, "reviews_count": 1670},
    {"name": "Infinix INBook Y4 Max Intel Core i5-1334U, 16GB, 512GB SSD, 15.6\" FHD", "category": "Laptops", "image": "https://m.media-amazon.com/images/I/61rrJpB3C6L._SX679_.jpg", "price": 34990, "original_price": 44990, "rating": 4.1, "reviews_count": 2450},

    # ===== AUDIO (15) =====
    {"name": "Sony WH-1000XM5 Wireless Noise Cancelling Headphones (Black)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/51SKmu2G9FL._SX679_.jpg", "price": 26990, "original_price": 34990, "rating": 4.6, "reviews_count": 8760},
    {"name": "Apple AirPods Pro (2nd Gen) with MagSafe Case (USB-C)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/61SUj2aKoEL._SX679_.jpg", "price": 20990, "original_price": 24900, "rating": 4.7, "reviews_count": 12450},
    {"name": "Apple AirPods Max (Silver) Over-Ear Headphones", "category": "Audio", "image": "https://m.media-amazon.com/images/I/81P5-189VzL._SX679_.jpg", "price": 51990, "original_price": 59900, "rating": 4.5, "reviews_count": 3450},
    {"name": "JBL Tune 760NC Wireless Over-Ear NC Headphones (Blue)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/71o8Q5XJS5L._SX679_.jpg", "price": 4299, "original_price": 7999, "rating": 4.3, "reviews_count": 15670},
    {"name": "Samsung Galaxy Buds2 Pro (Graphite) True Wireless Earbuds", "category": "Audio", "image": "https://m.media-amazon.com/images/I/51fIWp7GH+L._SX679_.jpg", "price": 9999, "original_price": 17999, "rating": 4.4, "reviews_count": 6780},
    {"name": "boAt Airdopes 141 TWS Earbuds (Active Black)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/51aIf7t0GmL._SX679_.jpg", "price": 1299, "original_price": 4990, "rating": 4.1, "reviews_count": 234560},
    {"name": "Sony WF-1000XM5 Truly Wireless Noise Cancelling Earbuds (Black)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/61dMfDKDJFL._SX679_.jpg", "price": 19990, "original_price": 26990, "rating": 4.5, "reviews_count": 5670},
    {"name": "Bose QuietComfort Ultra Wireless NC Headphones (Black)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/51JbuEu+vIL._SX679_.jpg", "price": 29990, "original_price": 35900, "rating": 4.6, "reviews_count": 2340},
    {"name": "JBL Flip 6 Portable Bluetooth Speaker (Red)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/71d4a+aUmML._SX679_.jpg", "price": 8999, "original_price": 14999, "rating": 4.5, "reviews_count": 18900},
    {"name": "boAt Rockerz 550 Over-Ear Wireless Headphones (Black)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/61eD-kp3paL._SX679_.jpg", "price": 1799, "original_price": 5990, "rating": 4.1, "reviews_count": 145670},
    {"name": "Marshall Major IV On-Ear Bluetooth Headphone (Black)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/61k7kvbDIXL._SX679_.jpg", "price": 8999, "original_price": 14999, "rating": 4.4, "reviews_count": 4560},
    {"name": "OnePlus Buds 3 TWS Earbuds (Metallic Gray)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/51vQEp3h01L._SX679_.jpg", "price": 4999, "original_price": 5499, "rating": 4.3, "reviews_count": 7890},
    {"name": "Sennheiser HD 450BT Over-Ear Wireless NC Headphones (Black)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/61Gc+SMu9WL._SX679_.jpg", "price": 7490, "original_price": 14990, "rating": 4.2, "reviews_count": 3456},
    {"name": "Sony SRS-XB100 Portable Bluetooth Speaker (Orange)", "category": "Audio", "image": "https://m.media-amazon.com/images/I/51fLDqgF5vL._SX679_.jpg", "price": 3490, "original_price": 4990, "rating": 4.4, "reviews_count": 8990},
    {"name": "JBL PartyBox 110 Portable Party Speaker with Lights", "category": "Audio", "image": "https://m.media-amazon.com/images/I/71mS4qkCKKL._SX679_.jpg", "price": 24999, "original_price": 37999, "rating": 4.5, "reviews_count": 5670},

    # ===== WATCHES (15) =====
    {"name": "Apple Watch Ultra 2 GPS + Cellular (49mm, Titanium, Orange Alpine Loop)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/71CXhVhpM0L._SX679_.jpg", "price": 79900, "original_price": 89900, "rating": 4.7, "reviews_count": 3560},
    {"name": "Apple Watch Series 9 GPS (45mm, Midnight Aluminium, Sport Band)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/81cEqOc7sqL._SX679_.jpg", "price": 41900, "original_price": 49900, "rating": 4.6, "reviews_count": 5670},
    {"name": "Samsung Galaxy Watch6 Classic (47mm, Black, Bluetooth)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/61+SLBqJiyL._SX679_.jpg", "price": 29999, "original_price": 38999, "rating": 4.4, "reviews_count": 3450},
    {"name": "Noise ColorFit Pro 5 Max Smartwatch (Jet Black)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/61fy6k7SKOL._SX679_.jpg", "price": 3999, "original_price": 8999, "rating": 4.1, "reviews_count": 23450},
    {"name": "boAt Storm Call 3 Smartwatch (Active Black)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/61j0KcE3pxL._SX679_.jpg", "price": 1799, "original_price": 6990, "rating": 4.0, "reviews_count": 34560},
    {"name": "Amazfit GTR 4 Smartwatch (Superspeed Black)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/71RGi2mtxEL._SX679_.jpg", "price": 11999, "original_price": 17999, "rating": 4.3, "reviews_count": 8900},
    {"name": "Garmin Venu 3 GPS Smartwatch (Whitestone)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/71dJ1rJSbpL._SX679_.jpg", "price": 42990, "original_price": 52490, "rating": 4.5, "reviews_count": 1230},
    {"name": "Fire-Boltt Phoenix Ultra Smartwatch (Black)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/61J1mIL9yVL._SX679_.jpg", "price": 2499, "original_price": 9999, "rating": 4.0, "reviews_count": 45670},
    {"name": "Samsung Galaxy Watch FE (40mm, Black, Bluetooth)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/61W4bLyJ94L._SX679_.jpg", "price": 14999, "original_price": 24999, "rating": 4.3, "reviews_count": 6780},
    {"name": "Fossil Gen 6E Hybrid Smartwatch (Brown Leather)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/71t3gYYaKML._SX679_.jpg", "price": 9995, "original_price": 15995, "rating": 4.2, "reviews_count": 2340},
    {"name": "OnePlus Watch 2 (Radiant Steel)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/61Rc3jOSb1L._SX679_.jpg", "price": 22999, "original_price": 29999, "rating": 4.3, "reviews_count": 3450},
    {"name": "Titan Smart Pro Smartwatch (Blue)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/711RVe0DEQL._SX679_.jpg", "price": 6999, "original_price": 11995, "rating": 4.1, "reviews_count": 5670},
    {"name": "Fitbit Sense 2 Advanced Health Smartwatch (Shadow Grey)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/61R7AaNX+vL._SX679_.jpg", "price": 16999, "original_price": 24999, "rating": 4.2, "reviews_count": 4560},
    {"name": "Fastrack Revoltt FS1 Pro Smartwatch (Black)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/51GUDr+cITL._SX679_.jpg", "price": 3495, "original_price": 7995, "rating": 4.0, "reviews_count": 12340},
    {"name": "Xiaomi Watch S3 Active (Black)", "category": "Watches", "image": "https://m.media-amazon.com/images/I/51pLqF7xpTL._SX679_.jpg", "price": 8999, "original_price": 13999, "rating": 4.2, "reviews_count": 3890},

    # ===== GAMING (15) =====
    {"name": "Sony PlayStation 5 Digital Edition (Slim)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/51051FiD9UL._SX679_.jpg", "price": 39990, "original_price": 44990, "rating": 4.7, "reviews_count": 12450},
    {"name": "Microsoft Xbox Series X 1TB Console (Black)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/51bcR8S+f9L._SX679_.jpg", "price": 49990, "original_price": 54990, "rating": 4.6, "reviews_count": 8900},
    {"name": "Nintendo Switch OLED Model (White)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/61wjCkOcGnL._SX679_.jpg", "price": 28490, "original_price": 34999, "rating": 4.7, "reviews_count": 15670},
    {"name": "Sony DualSense Wireless Controller (Cosmic Red)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/61R3CWf5vsL._SX679_.jpg", "price": 5490, "original_price": 6990, "rating": 4.6, "reviews_count": 23450},
    {"name": "Xbox Elite Wireless Controller Series 2 Core (White)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/71RJYGxJVOL._SX679_.jpg", "price": 12490, "original_price": 15990, "rating": 4.5, "reviews_count": 7890},
    {"name": "SteelSeries Arctis Nova 7 Wireless Gaming Headset (Black)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/71YPstgG5xL._SX679_.jpg", "price": 13490, "original_price": 18990, "rating": 4.4, "reviews_count": 3456},
    {"name": "Razer DeathAdder V3 HyperSpeed Wireless Gaming Mouse", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/61QFdAyYmRL._SX679_.jpg", "price": 10990, "original_price": 15999, "rating": 4.5, "reviews_count": 5670},
    {"name": "Logitech G Pro X TKL Wireless Mechanical Gaming Keyboard", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/61nw72sOr6L._SX679_.jpg", "price": 17995, "original_price": 22995, "rating": 4.4, "reviews_count": 2340},
    {"name": "Sony PlayStation VR2 Headset (PS5)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/619sytJpJtL._SX679_.jpg", "price": 49999, "original_price": 57990, "rating": 4.3, "reviews_count": 1890},
    {"name": "ASUS ROG Ally Z1 Extreme Handheld Gaming Console (White)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/71YVRhj+3SL._SX679_.jpg", "price": 52999, "original_price": 69999, "rating": 4.2, "reviews_count": 1230},
    {"name": "HyperX Cloud III Wireless Gaming Headset (Black/Red)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/61CGHv6kmWL._SX679_.jpg", "price": 11490, "original_price": 15990, "rating": 4.4, "reviews_count": 4560},
    {"name": "Razer BlackWidow V4 75% Wireless Mechanical Keyboard", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/61QFqe2VjpL._SX679_.jpg", "price": 15999, "original_price": 22999, "rating": 4.3, "reviews_count": 2890},
    {"name": "LG 27GP850-B 27\" QHD Nano IPS Gaming Monitor (165Hz, 1ms)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/71lx0jhhN6L._SX679_.jpg", "price": 29999, "original_price": 39999, "rating": 4.5, "reviews_count": 3450},
    {"name": "Sony PlayStation 5 Console (Disc Edition) with God of War Bundle", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/51mXqJ-OSDL._SX679_.jpg", "price": 54990, "original_price": 59990, "rating": 4.8, "reviews_count": 18900},
    {"name": "Samsung Odyssey G5 34\" Ultra-Wide QHD Gaming Monitor (165Hz)", "category": "Gaming", "image": "https://m.media-amazon.com/images/I/71jbITmvJgL._SX679_.jpg", "price": 27990, "original_price": 41990, "rating": 4.4, "reviews_count": 2560},

    # ===== FOOTWEAR (10) =====
    {"name": "Nike Air Jordan 1 Retro High OG (Red & Black)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/61-oc6aDYcL._UY695_.jpg", "price": 14999, "original_price": 18999, "rating": 4.7, "reviews_count": 4560},
    {"name": "Adidas Ultraboost Light Running Shoes (Core Black)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/71B5MzU2YfL._UY695_.jpg", "price": 12999, "original_price": 18999, "rating": 4.5, "reviews_count": 5670},
    {"name": "Nike Air Max 270 React (White/Black)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/71sSFI5OHPL._UY695_.jpg", "price": 11495, "original_price": 15995, "rating": 4.4, "reviews_count": 7890},
    {"name": "Puma RS-X Reinvention Sneakers (Whisper White)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/71sXIQcj8RL._UY695_.jpg", "price": 6999, "original_price": 10999, "rating": 4.3, "reviews_count": 3456},
    {"name": "New Balance 574 Classic Sneakers (Grey/White)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/61utX8kBDlL._UY695_.jpg", "price": 8999, "original_price": 12999, "rating": 4.4, "reviews_count": 4560},
    {"name": "Adidas Samba OG Shoes (Cloud White/Core Black)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/71j2v+f0EQL._UY695_.jpg", "price": 9999, "original_price": 12999, "rating": 4.6, "reviews_count": 6780},
    {"name": "Nike Dunk Low Retro (White/Black Panda)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/71JY6Xhq7jL._UY695_.jpg", "price": 8695, "original_price": 10795, "rating": 4.7, "reviews_count": 12340},
    {"name": "Reebok Classic Leather Shoes (White/Gum)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/71dL8rJiJ5L._UY695_.jpg", "price": 5999, "original_price": 8999, "rating": 4.2, "reviews_count": 5670},
    {"name": "ASICS GEL-NIMBUS 25 Running Shoes (Black/Pure Silver)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/71RsHyZ9VIL._UY695_.jpg", "price": 10990, "original_price": 16999, "rating": 4.5, "reviews_count": 3890},
    {"name": "Converse Chuck Taylor All Star High Top (Black)", "category": "Footwear", "image": "https://m.media-amazon.com/images/I/71kS-HFJTkL._UY695_.jpg", "price": 3999, "original_price": 5499, "rating": 4.4, "reviews_count": 23450},
]

def make_id(name):
    """Generate a clean ID from product name"""
    slug = re.sub(r'[^a-z0-9\s]', '', name.lower())
    slug = re.sub(r'\s+', '_', slug.strip())
    slug = slug[:45]
    suffix = str(random.randint(1000, 9999))
    return f"{slug}_{suffix}"

def generate_price_comparison(base_price):
    """Generate 3-store price comparison"""
    stores = ["Amazon", "Flipkart", "Croma"]
    random.shuffle(stores)
    
    # Best store gets base price
    best_store = stores[0]
    prices = {best_store: base_price}
    
    # Other stores get slightly higher prices (1-5% higher)
    for store in stores[1:]:
        markup = random.uniform(1.01, 1.05)
        prices[store] = round(base_price * markup)
    
    comparison = []
    for store in stores:
        comparison.append({
            "store": store,
            "price": prices[store],
            "logo": STORE_LOGOS[store],
            "best": store == best_store
        })
    
    # Sort so best price appears first
    comparison.sort(key=lambda x: x["price"])
    comparison[0]["best"] = True
    for item in comparison[1:]:
        item["best"] = False
    
    return comparison

def generate_price_history(price_comparison):
    """Generate 7-month price history for each store"""
    datasets = []
    for comp in price_comparison:
        current_price = comp["price"]
        high_price = round(current_price * random.uniform(1.08, 1.18))
        
        data = []
        price = high_price
        for i in range(6):
            drop = random.randint(int(current_price * 0.003), int(current_price * 0.02))
            price = max(price - drop, current_price)
            data.append(round(price))
        data.append(current_price)
        
        datasets.append({
            "label": comp["store"],
            "data": data,
            "borderColor": STORE_COLORS[comp["store"]],
            "tension": 0.4
        })
    
    return {
        "labels": MONTHS,
        "datasets": datasets
    }

def generate_ai_recommendation(price_comparison, rating):
    """Generate AI recommendation"""
    best = min(price_comparison, key=lambda x: x["price"])
    score = round(min(rating + random.uniform(4.0, 5.5), 10.0), 1)
    
    reasons = [
        f"Lowest price found on {best['store']}. Great value for money with strong reviews.",
        f"Best deal on {best['store']}. Highly rated by verified buyers.",
        f"Lowest price on {best['store']} with reliable delivery and returns.",
        f"Top pick from {best['store']}. Excellent price-to-performance ratio.",
    ]
    
    return {
        "store": best["store"],
        "reason": random.choice(reasons),
        "score": score
    }

def build_catalog():
    catalog = {}
    
    for pdata in products_data:
        pid = make_id(pdata["name"])
        
        price_comparison = generate_price_comparison(pdata["price"])
        price_history = generate_price_history(price_comparison)
        ai_recommendation = generate_ai_recommendation(price_comparison, pdata["rating"])
        
        product = {
            "id": pid,
            "name": pdata["name"],
            "category": pdata["category"],
            "image": pdata["image"],
            "rating": pdata["rating"],
            "reviews_count": pdata["reviews_count"],
            "price": pdata["price"],
            "original_price": pdata["original_price"],
            "price_comparison": price_comparison,
            "ai_recommendation": ai_recommendation,
            "price_history": price_history
        }
        
        catalog[pid] = product
    
    return catalog

# Generate the catalog
random.seed(42)  # For reproducibility
catalog = build_catalog()

# Write as JS module
js_content = "export const fallbackCatalog = " + json.dumps(catalog, indent=2, ensure_ascii=False) + ";\n"

output_path = r"c:\Users\harsh\OneDrive\Desktop\mini project 2\client\src\data\fallbackCatalog.js"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated {len(catalog)} products across categories:")
categories = {}
for p in catalog.values():
    cat = p["category"]
    categories[cat] = categories.get(cat, 0) + 1
for cat, count in sorted(categories.items()):
    print(f"   {cat}: {count}")
print(f"\nWritten to: {output_path}")
