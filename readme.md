# Flipkart ETL Project

## Overview
This project extracts mobile data from Flipkart under Rs.50,000 , transforms it, and loads it into a CSV file.

## Project Structure
- `extract.py` → Extracts raw data from Flipkart.
- `transform.py` → Cleans and processes the data.
- `load.py` → Saves the processed data into `mobiles_under_50000.csv`.
- `flipkart_etl_dag.py` → Airflow DAG to schedule the ETL pipeline.

## Technologies / Libraries Used
- Python 3.x
- BeautifulSoup → for web scraping
- Requests → to fetch web pages
- Pandas → for data cleaning and manipulation
- Airflow → to schedule the ETL pipeline
- CSV → to save the final output

## How to Run
1. Clone the repo:
   ```bash
   git clone 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
 3. Run the ETL script manually:
    ```bash
     python main.py
    ```
 4. Or run via Airflow DAG if Airflow is set up.

## Output
- CSV file: mobiles_under_50000.csv




 
   

   
