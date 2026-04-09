from Scraping import extract_properties 
from transform import clean_real_estate_data 
import asyncio

async def run_etl_pipeline():
    print("🚀 === Starting the pipeline === 🚀")
    
    # ---------------------------------------------------------
    # 1. Extract (E)
    # ---------------------------------------------------------
    # The same file that saved from the scraping file 
    pages_to_scrape = 10
    print(f"📥 Scraping {pages_to_scrape} ..")
    
    generated_raw_file = await extract_properties(num_pages=pages_to_scrape)
    
    # ---------------------------------------------------------
    # 2. مرحلة الـ Transform (T)
    # ---------------------------------------------------------
    print(f'Start Transformation on {generated_raw_file}')
    df_cleaned = clean_real_estate_data(generated_raw_file)
    
    # ---------------------------------------------------------
    # 3. مرحلة الـ Load (L)
    # ---------------------------------------------------------
    final_file_name = 'Aqarmap_Cleaned_Ready_pipeline.csv'
    df_cleaned.to_csv(final_file_name, index=False, encoding='utf-8-sig')
    print(f"🎉Pipeline")

if __name__ == "__main__":
    asyncio.run(run_etl_pipeline())