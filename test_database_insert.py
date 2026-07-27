from database import Database

db = Database()

db.cursor.execute(
    """
    INSERT INTO candidates
    (
        name,
        email,
        phone,
        experience,
        score,
        recommendation,
        matched_skills,
        missing_skills,
        report_path
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        "Test User",
        "test@example.com",
        "1234567890",
        5,
        90,
        "Strongly Recommend",
        '["Python", "SQL"]',
        '["Docker"]',
        "reports/test.txt",
    ),
)

db.connection.commit()

print("Insert successful")

db.close()
