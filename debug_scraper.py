import asyncio
from playwright.async_api import async_playwright
import json

async def test_scraper():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = await context.new_page()
        
        await page.goto("https://www.amazon.in/s?k=best+smartphones+2024", timeout=60000, wait_until="domcontentloaded")
        await page.wait_for_selector('div[data-component-type="s-search-result"]', timeout=15000)
        
        results = await page.locator('div[data-component-type="s-search-result"]').all()
        print(f"Testing: Found {len(results)} results")
        
        for idx, item in enumerate(results[:3]):
            print(f"--- Item {idx} ---")
            
            # Title
            title_el = item.locator('span.a-text-normal')
            if await title_el.count() > 0:
                print(f"Title: {await title_el.first.inner_text()}")
            else:
                print("Title: Missing")
                
            # Price
            try:
                price_el = item.locator('span.a-price-whole')
                if await price_el.count() > 0:
                    text_price = await price_el.first.inner_text()
                    print(f"Price (Raw): {text_price}")
                else:
                    print("Price: Missing")
            except Exception as e:
                print(f"Price Error: {e}")
                
            # Image
            try:
                img_el = item.locator('img.s-image')
                if await img_el.count() > 0:
                    src = await img_el.first.get_attribute('src')
                    print(f"Image: {src[:50]}...")
                else:
                    print("Image: Missing")
            except Exception as e:
                print(f"Image Error: {e}")
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_scraper())
