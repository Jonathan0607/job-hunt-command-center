import requests
from bs4 import BeautifulSoup

def fetch_simplify_jobs():
    url = "https://github.com/SimplifyJobs/Summer2026-Internships"
    # GitHub blocks scripts without a User-Agent, so we pretend to be Chrome
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching page: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 1. Find ALL tables on the page
    tables = soup.find_all('table')
    
    target_table = None
    
    # 2. Loop through to find the REAL job table
    # We look for a table that has a header "Company"
    for table in tables:
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        if "Company" in headers:
            target_table = table
            break
            
    if not target_table:
        print("❌ Could not find the Job table. GitHub structure might have changed.")
        return

    # 3. Parse the rows of the correct table
    # Skip the first row (header) and look for the first data row
    rows = target_table.find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        
        # We need at least 2 columns (Company, Role)
        if len(cols) >= 2:
            company = cols[0].get_text(strip=True)
            role = cols[1].get_text(strip=True)
            
            # Basic validation to ensure we didn't grab an empty row
            if company and role:
                print(f"✅ SUCCESS! Scraped Job:")
                print(f"   Company: {company}")
                print(f"   Role:    {role}")
                return

    print("❌ Table found, but no valid job rows detected.")

if __name__ == "__main__":
    fetch_simplify_jobs()