import requests
from bs4 import BeautifulSoup

def fetch_simplify_jobs():
    url = "https://github.com/SimplifyJobs/Summer2026-Internships"
    
    # We need to look like a real browser so GitHub doesn't block us
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
    all_tables = soup.find_all('table')
    
    # 2. Filter to keep only the tables that have "Company" in the header
    job_tables = []
    for table in all_tables:
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        if "Company" in headers:
            job_tables.append(table)
            
    if not job_tables:
        print("❌ Could not find any Job tables. GitHub structure might have changed.")
        return

    jobs_num = 0
    for table in job_tables:
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) >= 2:
                company = cols[0].get_text(strip=True)
                role = cols[1].get_text(strip=True)
                if company and role:
                    jobs_num += 1

    print(f"🔍 Found {jobs_num} jobs. Scraping now...")

    # 3. Loop through EACH table (This fixes your AttributeError)
    for table in job_tables:
        rows = table.find_all('tr')
        
        for row in rows:
            cols = row.find_all('td')
            
            # We need at least 2 columns (Company, Role)
            if len(cols) >= 2:
                company = cols[0].get_text(strip=True)
                role = cols[1].get_text(strip=True)
                
                # Only print if we actually found text (skips empty rows)
                if company and role:
                    print(f"✅ Scraped: {company} - {role}")
                    return

if __name__ == "__main__":
    fetch_simplify_jobs()