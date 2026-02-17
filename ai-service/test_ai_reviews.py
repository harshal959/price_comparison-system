import requests
import json

# Test the scraper API
url = "http://localhost:5001/scrape?query=usb+cable"

try:
    response = requests.get(url)
    data = response.json()
    
    print("=" * 60)
    print("API Response for 'usb cable'")
    print("=" * 60)
    
    print(f"\nProduct Name: {data.get('name', 'N/A')}")
    print(f"Price: ₹{data.get('price', 'N/A')}")
    
    # Check if ai_reviews exists
    if 'ai_reviews' in data:
        print("\n✅ AI REVIEWS FOUND!")
        print(f"Platforms: {list(data['ai_reviews'].keys())}")
        
        # Show first platform's review
        first_platform = list(data['ai_reviews'].keys())[0]
        review = data['ai_reviews'][first_platform]
        print(f"\n{first_platform.upper()} Review:")
        print(f"Summary: {review.get('summary', 'N/A')}")
        print(f"Pros ({len(review.get('pros', []))}):")
        for pro in review.get('pros', []):
            print(f"  - {pro}")
        print(f"Cons ({len(review.get('cons', []))}):")
        for con in review.get('cons', []):
            print(f"  - {con}")
    else:
        print("\n❌ AI REVIEWS NOT FOUND in response!")
        print(f"Available keys: {list(data.keys())}")
    
except Exception as e:
    print(f"Error: {e}")
