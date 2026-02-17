from playwright.sync_api import sync_playwright
import time

def test_amazon_scrape(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Go to Amazon India
        url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
        print(f"Visiting {url}...")
        
        try:
            page.goto(url, timeout=30000)
            page.wait_for_selector('div[data-component-type="s-search-result"]', timeout=10000)
            
            # Extract first item
            titles = page.locator('span.a-text-normal').all_inner_texts()
            prices = page.locator('span.a-price-whole').all_inner_texts()
            
            print(f"Found {len(titles)} titles and {len(prices)} prices.")
            if titles:
                print(f"First Title: {titles[0]}")
            if prices:
                print(f"First Price: {prices[0]}")
                
            return True
        except Exception as e:
            print(f"Error scraping: {e}")
            page.screenshot(path="debug_amazon_fail.png")
            return False
        finally:
            browser.close()

if __name__ == "__main__":
    test_amazon_scrape("iphone 15")
