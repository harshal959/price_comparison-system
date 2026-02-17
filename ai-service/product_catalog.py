
# Extensive Pre-Saved Catalog for "Demo Mode"
# Contains realistic data for popular products to ensure a high-quality demo experience.

PRODUCT_CATALOG = {
    # --- SMARTPHONES ---
    "iphone 15": {
        "name": "Apple iPhone 15 (128 GB) - Black",
        "image": "https://m.media-amazon.com/images/I/71657TiFeHL._SX679_.jpg",
        "rating": 4.6,
        "reviews_count": 3450,
        "price": 72999,
        "original_price": 79900,
        "price_comparison": [
            {"store": "Amazon", "price": 72999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "link": "https://amazon.in", "best": True, "live": True},
            {"store": "Flipkart", "price": 73500, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "link": "https://flipkart.com", "best": False, "live": True},
             {"store": "Croma", "price": 79900, "logo": "https://logo.clearbit.com/croma.com", "link": "https://croma.com", "best": False, "live": True}
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "Lowest price available with free 1-day delivery for Prime members.",
            "score": 9.2
        }
    },
    "samsung s24": {
        "name": "Samsung Galaxy S24 Ultra 5G AI Smartphone (Titanium Gray, 12GB, 256GB)",
        "image": "https://m.media-amazon.com/images/I/71CXhVhpM0L._SX679_.jpg",
        "rating": 4.5,
        "reviews_count": 1250,
        "price": 129999,
        "original_price": 134999,
        "price_comparison": [
            {"store": "Amazon", "price": 129999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "link": "https://amazon.in", "best": False, "live": True},
            {"store": "Flipkart", "price": 128500, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "link": "https://flipkart.com", "best": True, "live": True}
        ],
        "ai_recommendation": {
            "store": "Flipkart",
            "reason": "Best price available for the Titanium Gray variant with bank offers applied.",
            "score": 9.6
        }
    },
    "oneplus 12": {
        "name": "OnePlus 12 (Flowy Emerald, 16GB RAM, 512GB Storage)",
        "image": "https://m.media-amazon.com/images/I/717Qo4MH97L._SX679_.jpg",
        "rating": 4.4,
        "reviews_count": 890,
        "price": 69999,
        "original_price": 75999,
        "price_comparison": [
            {"store": "Amazon", "price": 69999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 70500, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False}
        ],
         "ai_recommendation": {
            "store": "Amazon",
            "reason": "Exclusive bank offers available on Amazon.",
            "score": 8.9
        }
    },
     "pixel 8": {
        "name": "Google Pixel 8 (Hazel, 128 GB) - Advanced Camera & AI",
        "image": "https://m.media-amazon.com/images/I/710Z306r8bL._SX679_.jpg",
        "rating": 4.3,
        "reviews_count": 450,
        "price": 62999,
        "original_price": 75999,
        "price_comparison": [
            {"store": "Amazon", "price": 65999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": False},
            {"store": "Flipkart", "price": 62999, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": True}
        ],
         "ai_recommendation": {
            "store": "Flipkart",
            "reason": "Significant price drop on Flipkart this week.",
            "score": 9.1
        }
    },

    # --- LAPTOPS ---
    "macbook air m2": {
        "name": "Apple MacBook Air Laptop M2 chip: 13.6-inch Liquid Retina Display, 8GB RAM, 256GB SSD",
        "image": "https://m.media-amazon.com/images/I/71f5Eu5lJSL._SX679_.jpg",
        "rating": 4.7,
        "reviews_count": 1400,
        "price": 86990,
        "original_price": 114900,
        "price_comparison": [
            {"store": "Amazon", "price": 99900, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg",  "best": False},
            {"store": "Flipkart", "price": 86990, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png",  "best": True}
        ],
        "ai_recommendation": {
            "store": "Flipkart",
            "reason": "Massive discount on Flipkart for the Midnight color variant.",
            "score": 9.5
        }
    },
    "dell xps 13": {
        "name": "Dell XPS 13 Plus Laptop, Intel Core i7-1360P, 16GB, 1TB SSD",
        "image": "https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/xps-notebooks/xps-13-9320/media-gallery/copy-of-xs9320nt-cnb-05-bk.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=555&qlt=100,1&resMode=sharp2&size=555,402&chrss=full",
        "rating": 4.2,
        "reviews_count": 120,
        "price": 159990,
        "original_price": 199990,
        "price_comparison": [
            {"store": "Amazon", "price": 164990, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": False},
            {"store": "Flipkart", "price": 159990, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": True}
        ],
         "ai_recommendation": {
            "store": "Flipkart",
            "reason": "Better pricing and available exchange offers.",
            "score": 8.5
        }
    },
    "hp spectre": {
        "name": "HP Spectre x360 2-in-1 Laptop 13.5-inch, Intel Evo Core i7",
        "image": "https://m.media-amazon.com/images/I/61s7s+4-+5L._SX679_.jpg",
        "rating": 4.5,
        "reviews_count": 310,
        "price": 134999,
        "original_price": 150000,
        "price_comparison": [
            {"store": "Amazon", "price": 134999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 139999, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False}
        ],
         "ai_recommendation": {
            "store": "Amazon",
            "reason": "Reliable seller with extended warranty offer.",
            "score": 9.0
        }
    },

    # --- AUDIO ---
    "sony headphones": { 
        "name": "Sony WH-1000XM5 Wireless Noise Cancelling Headphones",
        "image": "https://m.media-amazon.com/images/I/51SKmu2G9FL._SX679_.jpg",
        "rating": 4.8,
        "reviews_count": 8900,
        "price": 29990,
        "original_price": 34990,
        "price_comparison": [
            {"store": "Amazon", "price": 29990, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 31990, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False}
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "Best deal currently available. Price dropped by ₹2000 this week.",
            "score": 9.8
        }
    },
    "airpods pro": {
        "name": "Apple AirPods Pro (2nd Generation) with MagSafe Case (USB-C)",
        "image": "https://m.media-amazon.com/images/I/61SUj2aKoEL._SX679_.jpg",
        "rating": 4.7,
        "reviews_count": 5600,
        "price": 22999,
        "original_price": 24900,
        "price_comparison": [
            {"store": "Amazon", "price": 22999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 23499, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False}
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "Lowest price online.",
            "score": 9.3
        }
    },
    "jbl flip 6": {
        "name": "JBL Flip 6 Wireless Portable Bluetooth Speaker Pro Sound",
        "image": "https://m.media-amazon.com/images/I/61+R5r29rQL._SX679_.jpg",
        "rating": 4.5,
        "reviews_count": 12000,
        "price": 9999,
        "original_price": 14999,
        "price_comparison": [
            {"store": "Amazon", "price": 9999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 10499, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False}
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "Best value for money in portable speakers.",
            "score": 8.8
        }
    },

    # --- FOOTWEAR ---
    "nike air jordan": {
        "name": "Nike Air Jordan 1 Retro High OG 'Chicago'",
        "image": "https://m.media-amazon.com/images/I/71zLz6m5Q+L._AC_UY1100_.jpg", 
        "rating": 4.9,
        "reviews_count": 450,
        "price": 16995,
        "original_price": 18995,
        "price_comparison": [
             {"store": "Amazon", "price": 16995, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
             {"store": "Flipkart", "price": 18995, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False}
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "Rare stock available at retail price.",
            "score": 9.4
        }
    },
    "adidas ultraboost": {
        "name": "Adidas Men's Ultraboost Light Running Shoes",
        "image": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/0fbed4646c1d46e0aae0afc90122d10d_9366/Ultraboost_Light_Running_Shoes_White_HQ6351_01_standard.jpg",
        "rating": 4.6,
        "reviews_count": 2100,
        "price": 11999,
        "original_price": 18999,
        "price_comparison": [
            {"store": "Amazon", "price": 12500, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": False},
            {"store": "Flipkart", "price": 11999, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": True}
        ],
        "ai_recommendation": {
            "store": "Flipkart",
            "reason": "Great discount on the latest model.",
            "score": 9.1
        }
    },
    "puma nitro": {
        "name": "Puma Deviate Nitro 2 Men's Running Shoes",
        "image": "https://images.puma.com/image/upload/f_auto,q_auto,b_rgb:fafafa,w_600,h_600/global/376807/01/sv01/fnd/IND/fmt/png/Deviate-NITRO-Elite-2-Men's-Running-Shoes",
        "rating": 4.3,
        "reviews_count": 850,
        "price": 13999,
        "original_price": 15999,
        "price_comparison": [
            {"store": "Amazon", "price": 13999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 14500, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False}
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "Direct from brand partnership.",
            "score": 8.7
        }
    },

    # --- WATCHES ---
    "apple watch ultra": {
        "name": "Apple Watch Ultra 2 (GPS + Cellular, 49mm) Titanium Case",
        "image": "https://m.media-amazon.com/images/I/81P5-189VzL._SX679_.jpg",
        "rating": 4.9,
        "reviews_count": 890,
        "price": 89900,
        "original_price": 89900,
        "price_comparison": [
            {"store": "Amazon", "price": 89900, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 89999, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False}
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "Standard pricing everywhere, but Amazon offers faster delivery.",
            "score": 9.0
        }
    },
    "samsung watch 6": {
        "name": "Samsung Galaxy Watch6 Classic LTE (47mm, Black)",
        "image": "https://m.media-amazon.com/images/I/61N+x-jA9UL._SX679_.jpg",
        "rating": 4.4,
        "reviews_count": 1500,
        "price": 36999,
        "original_price": 40999,
        "price_comparison": [
            {"store": "Amazon", "price": 37999, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": False},
            {"store": "Flipkart", "price": 36999, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": True}
        ],
        "ai_recommendation": {
            "store": "Flipkart",
            "reason": "Cheapest option for the LTE version.",
            "score": 9.2
        }
    },

    # --- GAMING ---
    "playstation 5": {
        "name": "Sony PlayStation 5 Console (Slim) - CFI-2000A01",
        "image": "https://m.media-amazon.com/images/I/51051FiD9UL._SX679_.jpg",
        "rating": 4.8,
        "reviews_count": 5600,
        "price": 54990,
        "original_price": 54990,
        "price_comparison": [
            {"store": "Amazon", "price": 54990, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 54990, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": True}
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "Reliable stock availability.",
            "score": 9.5
        }
    },
    "xbox series x": {
        "name": "Xbox Series X Console",
        "image": "https://m.media-amazon.com/images/I/61-jjE67uqL._SX679_.jpg",
        "rating": 4.7,
        "reviews_count": 4200,
        "price": 49990,
        "original_price": 54990,
        "price_comparison": [
            {"store": "Amazon", "price": 49990, "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Amazon_icon.svg", "best": True},
            {"store": "Flipkart", "price": 48990, "logo": "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/flipkart-icon.png", "best": False, "live": False} # Out of stock on Flipkart mock
        ],
        "ai_recommendation": {
            "store": "Amazon",
            "reason": "In stock and ready to ship.",
            "score": 9.3
        }
    }
}
