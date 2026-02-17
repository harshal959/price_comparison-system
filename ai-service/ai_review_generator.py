"""
Dynamic AI Review Generator
Generates product-specific reviews based on product details
"""

def generate_ai_reviews(product_name, category, rating, price, platforms):
    """
    Generate platform-specific AI reviews based on product characteristics
    """
    import random
    
    # Extract product type from name or category
    name_lower = product_name.lower()
    cat_lower = category.lower() if category else ""
    
    # Determine product type
    if any(word in name_lower for word in ['cable', 'charger', 'usb']):
        product_type = 'accessory'
    elif any(word in name_lower for word in ['tv', 'television', 'smart tv']):
        product_type = 'tv'
    elif any(word in name_lower for word in ['remote', 'controller']):
        product_type = 'remote'
    elif any(word in name_lower for word in ['phone', 'iphone', 'samsung', 'oneplus']):
        product_type = 'phone'
    elif any(word in name_lower for word in ['laptop', 'macbook', 'computer']):
        product_type = 'laptop'
    elif any(word in name_lower for word in ['headphone', 'earbuds', 'airpods']):
        product_type = 'audio'
    else:
        product_type = 'electronics'
    
    # Product-specific pros/cons based on type and rating
    review_templates = {
        'accessory': {
            'high_rating': {
                'summary': f"Fast charging {product_name.split()[0]} cable with excellent build quality and durability.",
                'pros': [
                    "Durable braided design",
                    "Fast charging support",
                    "Good length for daily use",
                    "Tangle-resistant cable"
                ],
                'cons': [
                    "Slightly pricier than basic options",
                    "Limited color choices"
                ]
            },
            'medium_rating': {
                'summary': f"Decent {product_name.split()[0]} cable offering good value for money.",
                'pros': [
                    "Affordable pricing",
                    "Works as expected",
                    "Standard compatibility"
                ],
                'cons': [
                    "Build quality could be better",
                    "May wear out with heavy use",
                    "Slower charging than premium options"
                ]
            }
        },
        'tv': {
            'high_rating': {
                'summary': f"Excellent {product_name.split()[0]} TV with vibrant display and smart features at this price point.",
                'pros': [
                    "Vibrant HD/4K display quality",
                    "Smooth smart TV interface",
                    "Good sound output",
                    "Multiple HDMI ports"
                ],
                'cons': [
                    "Remote could be more premium",
                    "Viewing angles could be better"
                ]
            },
            'medium_rating': {
                'summary': f"Decent TV for the price, suitable for basic viewing needs.",
                'pros': [
                    "Affordable price point",
                    "Decent picture quality",
                    "Basic smart features work fine"
                ],
                'cons': [
                    "Sound quality needs improvement", 
                    "Smart TV interface lags sometimes",
                    "Limited app support"
                ]
            }
        },
        'remote': {
            'high_rating': {
                'summary': f"Reliable replacement remote with good build quality and responsive buttons.",
                'pros': [
                    "All buttons work perfectly",
                    "Easy to pair and setup",
                    "Good battery life",
                    "Comfortable grip"
                ],
                'cons': [
                    "No voice control feature",
                    "Buttons could be backlit"
                ]
            },
            'medium_rating': {
                'summary': f"Basic replacement remote that gets the job done.",
                'pros': [
                    "Works with most TVs",
                    "Affordable replacement",
                    "Easy to use"
                ],
                'cons': [
                    "Build quality feels cheap",
                    "Some buttons unresponsive",
                    "Limited range"
                ]
            }
        },
        'phone': {
            'high_rating': {
                'summary': f"Flagship {product_name.split()[0]} smartphone with excellent performance and camera quality.",
                'pros': [
                    "Premium build and design",
                    "Excellent camera system",
                    "Fast processor performance",
                    "Long battery life"
                ],
                'cons': [
                    "Premium pricing",
                    "No expandable storage"
                ]
            },
            'medium_rating': {
                'summary': f"Good mid-range phone offering balanced performance.",
                'pros': [
                    "Decent camera quality",
                    "Good battery backup",
                    "Smooth daily performance"
                ],
                'cons': [
                    "Slow charging speed",
                    "Average display quality",
                    "Heavy gaming performance lags"
                ]
            }
        },
        'electronics': {
            'high_rating': {
                'summary': f"High-quality {product_type} product with excellent features and reliability.",
                'pros': [
                    "Premium build quality",
                    "Feature-rich",
                    "Good performance",
                    "Reliable brand"
                ],
                'cons': [
                    "Higher price point",
                    "Could have more accessories"
                ]
            },
            'medium_rating': {
                'summary': f"Decent {product_type} product offering good value.",
                'pros': [
                    "Affordable pricing",
                    "Basic features work well",
                    "Easy to use"
                ],
                'cons': [
                    "Build quality could improve",
                    "Limited advanced features",
                    "Average performance"
                ]
            }
        }
    }
    
    # Determine rating category
    rating_category = 'high_rating' if rating >= 4.2 else 'medium_rating'
    
    # Get template for product type
    template = review_templates.get(product_type, review_templates['electronics'])[rating_category]
    
    # Generate reviews for each platform
    ai_reviews = {}
    
    for platform_info in platforms:
        platform = platform_info['store'].lower()
        
        # Customize pros/cons slightly per platform
        pros = template['pros'].copy()
        cons = template['cons'].copy()
        
        # Add platform-specific notes
        if platform == 'amazon':
            if price < 1000:
                pros.append("Prime delivery available")
            summary = f"{template['summary']} Popular choice on Amazon."
        elif platform == 'flipkart':
            if price < 1000:
                pros.append("SuperCoin rewards available")
            summary = f"{template['summary']} Trending on Flipkart."
        elif platform == 'croma':
            summary = f"{template['summary']} Available at Croma stores."
        elif platform == 'meesho':
            cons = [c for c in cons if 'pric' not in c.lower()]  # Remove price-related cons for Meesho
            pros.insert(0, "Budget-friendly option")
            summary = f"Affordable {product_type} option. {template['summary']}"
        else:
            summary = template['summary']
        
        ai_reviews[platform] = {
            'summary': summary,
            'pros': pros[:4],  # Limit to 4 pros
            'cons': cons[:2]   # Limit to 2 cons
        }
    
    return ai_reviews
