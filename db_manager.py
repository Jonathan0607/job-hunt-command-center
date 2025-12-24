import sqlite3
from datetime import datetime

# 1. Setup Connection
def get_connection():
    # This creates a file 'jobs.db' automatically if it doesn't exist
    conn = sqlite3.connect('jobs.db')
    return conn

# 2. Create the Table
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # We create a table with a UNIQUE constraint on the URL 
    # so we don't accidentally save the same job twice.
    query = '''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        url TEXT UNIQUE,
        location TEXT,
        status TEXT DEFAULT 'pending', 
        date_added TEXT
    )
    '''
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("Database initialized. Table 'jobs' is ready.")

# 3. Function to Add a Job (The "Ingest" step)
def add_job(title, company, url, location):
    conn = get_connection()
    cursor = conn.cursor()
    
    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        cursor.execute('''
            INSERT INTO jobs (title, company, url, location, status, date_added)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, company, url, location, 'pending', date_added))
        conn.commit()
        print(f"[SUCCESS] Added job: {title} at {company}")
    except sqlite3.IntegrityError:
        print(f"[SKIP] Job already exists: {url}")
    finally:
        conn.close()

# --- RUN SETUP ---
if __name__ == "__main__":
    init_db()
    
    # Test it immediately with dummy data
    add_job("Backend Engineer", "Amazon", "https://azimuth.com/jobs/123", "Remote")
    add_job("Data Scientist", "Google", "https://google.com/jobs/456", "Mountain View")
    add_job("Backend Engineer", "Amazon", "https://azimuth.com/jobs/123", "Remote") # Should fail (duplicate)