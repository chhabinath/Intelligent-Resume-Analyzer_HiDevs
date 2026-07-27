from pathlib import Path
import sqlite3

# --------------------------------------------------
# Database Configuration
# --------------------------------------------------

DATABASE_DIR = Path("database")
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "resume_analyzer.db"


class Database:
    """
    SQLite database manager for the
    Intelligent Resume Analyzer.
    """

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    # --------------------------------------------------
    # Create Tables
    # --------------------------------------------------

    def initialize(self):
        """
        Create all database tables.
        """

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,

            experience REAL,

            score REAL,

            recommendation TEXT,

            matched_skills TEXT,

            missing_skills TEXT,

            report_path TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            company TEXT,

            skills TEXT,

            experience REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            candidate_id INTEGER,

            report_type TEXT,

            file_path TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(candidate_id)
            REFERENCES candidates(id)
        )
        """)

        self.connection.commit()

    # --------------------------------------------------
    # Close Database
    # --------------------------------------------------

    def close(self):

        self.connection.close()


# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

if __name__ == "__main__":

    db = Database()

    db.initialize()

    db.close()

    print("Database initialized successfully.")