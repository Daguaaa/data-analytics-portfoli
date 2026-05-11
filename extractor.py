import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
from datetime import datetime
from sqlalchemy import create_engine

# --- DATABASE CONNECTION ---

engine = create_engine('postgresql://postgres:PASSWORD_HERE@localhost:5432/real_estate_mn_db')

CITIES = {
    "Apple Valley": 489,
    "Burnsville": 2282,
    "Eagan": 4490,
    "Lakeville": 8946,
    "Richfield": 14049
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

def scrape_to_postgres():
    all_homes = []
    # Using a standard date format for SQL
    scan_date = datetime.now().strftime('%Y-%m-%d')
    
    for city_name, city_id in CITIES.items():
        city_url_name = city_name.replace(' ', '_')
        url = f"https://www.redfin.com/city/{city_id}/MN/{city_url_name}"
        
        print(f"Scanning {city_name}...")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                print(f"Blocked or error on {city_name} (Status: {response.status_code})")
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all('div', class_='HomeCardContainer')

            for card in cards:
                # 1. Price
                price_raw = card.find('div', class_='bp-Homecard__Price').text if card.find('div', class_='bp-Homecard__Price') else None
                price = int(re.sub(r'[^\d]', '', price_raw)) if price_raw else None
                
                #2. sats(bed,bath,sqft, and days on market)
                stats_raw = card.find('div', class_='bp-Homecard__Stats').text if card.find('div', class_='bp-Homecard__Stats') else ""
                beds = re.search(r'(\d+)\s*bed', stats_raw)
                baths = re.search(r'(\d+\.?\d*)\s*bath', stats_raw)
                sqft = re.search(r'([\d,]+)\s*sq\s*ft', stats_raw)
                
                dom_match = re.search(r'(\d+)\s*day' ,stats_raw)
                days_on_market = int(dom_match.group(1)) if dom_match else 0

                #3. Address
                address_a = card.find('a', class_='bp-Homecard__Address')
                address = address_a.text.strip() if address_a else None

                if not price or not address: continue

                all_homes.append({
                    'scan_date': scan_date,
                    'city': city_name,
                    'price': price,
                    'beds': float(beds.group(1)) if beds else 0,
                    'baths': float(baths.group(1)) if baths else 0,
                    'sqft': int(sqft.group(1).replace(',', '')) if sqft else 0,
                    'days_on_market': days_on_market,
                    'address': address
                })
            
            time.sleep(3)
            
        except Exception as e:
            print(f"Skipping {city_name} due to error: {e}")

    # --- UPLOAD TO DATABASE ---
    if all_homes:
        df = pd.DataFrame(all_homes)
        
        # Adding the calculated columns for dashboard
        df['price_per_sqft'] = (df['price'] / df['sqft']).round(2)
        df['flip_potential'] = (df['beds'] >= 3) & (df['baths'] <= 1.5)
        
        # 'mn_homes' is the table I created in pgAdmin
        df.to_sql('mn_homes', engine, if_exists='append', index=False)
        print(f"\nPipeline Success! {len(df)} homes saved to PostgreSQL.")
    else:
        print("No data was collected. Check your internet connection or if the site is blocking requests.")

if __name__ == "__main__":
    scrape_to_postgres()