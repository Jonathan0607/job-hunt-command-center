# Job Hunt Command Center

A local ETL pipeline and dashboard to track job applications, automate status updates, and manage the recruitment lifecycle.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Database:** SQLite (Migrating to PostgreSQL)
* **Architecture:** Script-based ETL (Extract, Transform, Load)

## 🚀 Features
* **Duplicate Protection:** Uses SQL constraints to prevent adding the same job listing twice.
* **Data Persistence:** SQLite backend ensures application data survives between sessions.
* **Error Handling:** Robust try/except logic to handle unique constraint violations gracefully.
