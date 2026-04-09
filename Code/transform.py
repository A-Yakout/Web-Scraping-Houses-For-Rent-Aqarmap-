# T : Transform 
import pandas as pd

def categorize_price(price):
        if price < 5000:
            return 'Cheap'
        elif 5000 <= price <= 15000:
            return 'Normal'
        else:
            return 'Luxury'
    
    
def clean_real_estate_data(raw_data_path):
    print("🧹Starting (Transformation) Stage ...")
    
    # Reading raw data
    df = pd.read_csv(raw_data_path)
    
    # Removing Duplicates
    DF_cleaned = df.drop_duplicates(subset=['URL'])
    
    # Cleaning the text of Location column
    DF_cleaned['Location']= DF_cleaned['Location'].str.split('/').str[0].str.replace('n','').str.strip()
    # Removing unwanted text 'EGP' from Price column 
    DF_cleaned['Price'] = DF_cleaned['Price'].str.split('EGP').str[0].str.strip()
    # Removing 'm²' text from Area
    DF_cleaned['Area'] = DF_cleaned['Area'].str.replace('m²','').str.strip()
    # Removing unwanted text 'rooms' and 'bathroom'
    DF_cleaned['Bedrooms'] = DF_cleaned['Bedrooms'].str.replace('rooms','').str.strip()
    DF_cleaned['Bathrooms'] = DF_cleaned['Bathrooms'].str.replace('bathroom','').str.strip()

    # Adjusting the data type of columns
    #  '65,000' ---> 65000
    DF_cleaned['Price'] = DF_cleaned['Price'].str.replace(',','')

    DF_cleaned['Price'] = DF_cleaned['Price'].astype(float)
    DF_cleaned['Area'] = DF_cleaned['Area'].astype(int)
    DF_cleaned['Bedrooms'] = DF_cleaned['Bedrooms'].astype(int)
    DF_cleaned['Bathrooms'] = DF_cleaned['Bathrooms'].astype(int)    
    
    DF_cleaned['Budget_Category'] = DF_cleaned['Price'].apply(categorize_price)
    DF_cleaned['Total_Rooms'] = DF_cleaned['Bathrooms'] + DF_cleaned['Bedrooms']
    DF_cleaned['Price_per_m²'] = DF_cleaned['Price'] / DF_cleaned['Area']
    DF_cleaned['Price_per_m²']= DF_cleaned['Price_per_m²'].round(2)

    print("✅ We have done The Transformation phase")
    return DF_cleaned # الدالة بترجع الداتا النظيفة