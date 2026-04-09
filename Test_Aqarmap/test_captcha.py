import asyncio
from playwright.async_api import async_playwright

async def test_aqarmap():
    print("🚀 Testing Aqarmap browser...")
    async with async_playwright() as p:
        # هنفتح المتصفح بشكل مرئي عشان تشوف بعينك اللي بيحصل
        browser = await p.chromium.launch(headless=False)
        
        # 💡 تريك احترافي: هنضيف User-Agent عشان نبان كأننا متصفح كروم حقيقي مش بوت
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        url = "https://aqarmap.com.eg/en/for-rent/apartment/"
        print(f"🔗 Going to : {url}")

        try:
            # نتوجه للموقع ونستنى لحد ما يحمل
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            
            # نستنى 5 ثواني عشان لو فيه كابتشا بتعمل Redirect أوتوماتيك
            print("⏳ Waiting 5 seconds for page stabality..")
            await asyncio.sleep(5) 

            # نسحب عنوان الصفحة
            title = await page.title()
            print(f"\n📄 Page title '{title}'")

            # 🔍 التحقق من وجود كابتشا بناءً على كلمات مشهورة في عنواين الحماية
            captcha_keywords = ["just a moment","Human Verification", "cloudflare", "attention required", "robot", "security", "captcha"]
            is_captcha = any(keyword in title.lower() for keyword in captcha_keywords)

            if is_captcha:
                print("🚨 [Warning]: Capthcha has found")
            else:
                print("✅ [Success]: The Browser opened successfully")

            # سكرين شوت للتأكيد عشان تراجعها براحتك
            await page.screenshot(path="aqarmap_test.png")
            print("📸 Taking screenshot ")

        except Exception as e:
            print(f"❌Error loading the page {e}")

        finally:
            print("\n⏳ Closing the browser in 10 sec...")
            await asyncio.sleep(10)
            await browser.close()

if __name__ == "__main__":
    asyncio.run(test_aqarmap())