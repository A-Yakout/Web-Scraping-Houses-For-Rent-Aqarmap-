import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def extract_properties(num_pages=2):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # لستة بره خالص هتحوش كل الشقق من كل الصفحات
        all_data = []
        
        for i in range(2, num_pages+1): # loop over pages
            url = f'https://aqarmap.com.eg/en/for-rent/apartment/?page={i}'
            
            print(f"\n🌍 === Scraping page no. {i} === 🌍")
            await page.goto(url, wait_until='domcontentloaded')
            await asyncio.sleep(3)
            
            cards = page.locator('div.listing-card-details')
            count = await cards.count()
            
            # اللستة دي هتشيل قواميس (لينك + لوكيشن) للصفحة الحالية بس
            houses_info = []
            
            for j in range(count):
                try:   
                    current_card = cards.nth(j)
                    raw_link = await current_card.locator('a').first.get_attribute('href')
                    
                    # سحب اللوكيشن من الكارت الحالي مش من الصفحة كلها
                    outer_location = await current_card.locator('div.flex.text-caption-1.text-gray__dark_2').first.inner_text()  
                    
                    if raw_link:
                        if raw_link.startswith('http'):
                            full_link = raw_link
                        else:
                            full_link = f"https://aqarmap.com.eg{raw_link}"
                            
                        # تجميع اللينك واللوكيشن في قاموس
                        houses_info.append({
                            'url': full_link,
                            'outer_location': outer_location.strip()
                        })
                        
                except Exception as e:
                    print(f"⚠️ Error Scraping the link {j}: {e}")    
                    
            print(f'I have found {len(houses_info)} houses on this page')              

            print("\n🚀 Entering the pages ...")
        
            # بنلف على القاموس اللي ظبطناه
            for house in houses_info:
                link = house['url']
                outer_loc = house['outer_location']
                
                try:
                    print(f"opening the house page... ({outer_loc})")
                    await page.goto(link, wait_until='domcontentloaded')
                    await asyncio.sleep(3)        
                    
                    page_title = await page.title()
                    price = await page.locator('data.text-title-2').inner_text()
                    District = await page.locator('p.text-body-2.truncated-text').nth(0).inner_text()
                    Area = await page.locator('p.text-body-2.truncated-text').nth(1).inner_text()
                    bedrooms = await page.locator('p.text-body-2.truncated-text').nth(2).inner_text()
                    bathrooms = await page.locator('p.text-body-2.truncated-text').nth(3).inner_text()
                    
                    house_details = {
                        'URL': link,
                        'Title': page_title,
                        'Location': outer_loc, 
                        'Price': price,
                        'District': District,
                        'Area': Area,
                        'Bedrooms': bedrooms,
                        'Bathrooms': bathrooms
                    }
                    all_data.append(house_details)
                    print("✅ All Scraped")
                    
                except Exception as e:
                    print(f"Error in the link {link}: {e}")
        
        # حفظ البيانات بعد ما كل الصفحات تخلص
        print("\n💾Saving all the data into the file...")
        df = pd.DataFrame(all_data)
        
        file_name = 'aqarmap_data_test.csv'
        df.to_csv(file_name, index=False, encoding='utf-8-sig') 
        print(f"🎉done saving {len(all_data)} houses in {file_name}!")
        
        print('\nBrowser will be closed after 10 seconds')
        await asyncio.sleep(10)
        await browser.close()

    return file_name
#asyncio.run(extract_properties())