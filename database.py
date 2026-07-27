from pathlib import Path
import sqlite3

# --------------------------------------------------
# Database Configuration
# --------------------------------------------------

# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Database directory
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(exist_ok=True)

# Database file
DATABASE_PATH = DATABASE_DIR / "resume_analyzer.db"


class Database:
    """
    SQLite database manager for the
    Intelligent Resume Analyzer.
    """

    def __init__(self):
        # Print database location (helps during debugging)
        print(f"Using Database: {DATABASE_PATH}")

        self.connection = sqlite3.connect(DATABASE_PATH)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        # Ensure tables exist
        self.initialize()

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
    # Execute Query
    # --------------------------------------------------

    def execute(self, query, parameters=()):
        """
        Execute INSERT, UPDATE or DELETE queries.
        """
        self.cursor.execute(query, parameters)
        self.connection.commit()

    # --------------------------------------------------
    # Fetch All
    # --------------------------------------------------

    def fetchall(self, query, parameters=()):
        """
        Execute SELECT query and return all rows.
        """
        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()

    # --------------------------------------------------
    # Fetch One
    # --------------------------------------------------

    def fetchone(self, query, parameters=()):
        """
        Execute SELECT query and return one row.
        """
        self.cursor.execute(query, parameters)
        return self.cursor.fetchone()

    # --------------------------------------------------
    # Close Database
    # --------------------------------------------------

    def close(self):
        """
        Close database connection.
        """
        if self.connection:
            self.connection.close()


# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

if __name__ == "__main__":

    db = Database()

    print("Database initialized successfully.")
    print(f"Database file: {DATABASE_PATH}")

    db.close()
