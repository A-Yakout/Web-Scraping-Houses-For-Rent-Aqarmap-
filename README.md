# 🏠 Aqarmap Real Estate Rent Analysis | End-to-End ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📌 Project Overview
Finding affordable rent in Egypt can be tricky, especially with misleading metrics like "cheap price per square meter." This project is an **End-to-End ETL Pipeline and Data Analysis** designed to scrape rental property data from Aqarmap, clean it, and discover the true **"Value for Money"** areas for youth and young professionals.

## ⚙️ The ETL Pipeline Architecture
Instead of a simple static script, this project is built as a robust, automated pipeline orchestrated by a main controller (`main_pipeline.py`).

1. **📥 Extract (Web Scraping):** - Utilized **Playwright** (Asynchronous) to navigate dynamic pages on Aqarmap.
   - Designed a parameterized scraper that iterates through pages, extracts URLs, and dives into individual property listings to fetch details (Price, Area, Location, Rooms, etc.).
   
2. **🧹 Transform (Data Cleaning & Feature Engineering):** - Used **Pandas** and **Regex** to strip text/currencies and convert extracted data into pure numerical formats.
   - Handled Missing Values and dropped duplicates based on property URLs.
   - Applied **IQR (Interquartile Range)** to detect and remove extreme outliers.
   - **Feature Engineering:** Created new columns such as `Price_per_m²` and `Budget_Category`.

3. **💾 Load:** - Exported the thoroughly cleaned and transformed dataset into a ready-to-use CSV file (`Aqarmap_Cleaned_Ready.csv`) for analytical visualization.

## 📊 Key Business Insights (The Sweet Spot Analysis)
Using **Seaborn** and **Matplotlib**, I built a quadrant analysis to find the best rental deals. The data revealed three main facts:

* 🎯 **The Sweet Spot (Best Value):** Districts like **Faisal** offer larger spaces (above market average) at rental prices below the market average.
* ❌ **Overpriced Districts:** Districts like **El Manial** charge premium rent for compact spaces, where you are mostly paying for the "location name."
* 💡 **The "Cheap Sqm" Illusion:** Districts like **Hadayek El Ahram** have a very low price per square meter. However, the available apartments are extremely large, making the *total* monthly rent exceed the budget of a typical young professional.

## 📂 Project Structure
```text
📦 Real-Estate-ETL-Pipeline
 ┣ 📜 Scraping.py           # Playwright script to extract raw data
 ┣ 📜 transform.py          # Pandas script for cleaning and feature engineering
 ┣ 📜 main_pipeline.py      # The orchestrator script to run the ETL process
 ┣ 📜 Data_Analysis.ipynb   # Jupyter Notebook for EDA and Seaborn visualizations
 ┗ 📜 README.md
