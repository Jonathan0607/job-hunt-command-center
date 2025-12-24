import csv
import db_manager

# This mimics a "scraped" dataset or a file you downloaded
def load_jobs_from_csv(filename):
    print(f"--- 📥 Ingesting data from {filename} ---")
    
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            count = 0
            
            for row in reader:
                title = row['Title']
                company = row['Company']
                url = row['URL']
                location = row['Location']
                
                # Call your database manager to save it
                db_manager.add_job(title, company, url, location)
                count += 1
                
        print(f"--- ✅ Finished. Processed {count} jobs. ---")
        
    except FileNotFoundError:
        print("Error: CSV file not found. Make sure 'jobs_to_track.csv' exists.")

if __name__ == "__main__":
    # Create a dummy CSV file on the fly to test the pipeline
    with open('jobs_to_track.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Company', 'URL', 'Location']) # Headers
        writer.writerow(['Software Engineer', 'Amazon', 'https://azimuth.com/jobs/1', 'Remote'])
        writer.writerow(['Data Hawk', 'IBM', 'https://ibm.com/jobs/2', 'New York'])
        writer.writerow(['Backend Dev', 'OpenAI', 'https://openai.com/jobs/3', 'San Francisco'])

    # Run the mock ingestion
    load_jobs_from_csv('jobs_to_track.csv')