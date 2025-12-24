import sqlite3
import pandas as pd

def view_jobs():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    
    # 1. Get the column names (so we know what we are looking at)
    cursor.execute("PRAGMA table_info(jobs)")
    columns = [description[1] for description in cursor.fetchall()]
    
    # 2. Get the data
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    
    conn.close()

    if not rows:
        print("Database is empty.")
    else:
        # Simple print
        print(f"{' | '.join(columns)}")
        print("-" * 50)
        for row in rows:
            print(row)

if __name__ == "__main__":
    view_jobs()