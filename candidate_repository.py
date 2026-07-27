import json

from database import Database


class CandidateRepository:
    """
    Repository for Candidate database operations.
    """

    def __init__(self):
        self.db = Database()

    # --------------------------------------------------
    # Add Candidate
    # --------------------------------------------------

    def add_candidate(
        self,
        candidate,
        match_result,
        report_path: str,
    ) -> int:
        """
        Save a candidate analysis result.

        Returns:
            Newly created candidate ID.
        """

        self.db.cursor.execute(
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
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                candidate.name,
                candidate.email,
                candidate.phone,
                candidate.experience,
                match_result.score,
                match_result.recommendation,
                json.dumps(match_result.matched_skills),
                json.dumps(match_result.missing_skills),
                report_path,
            ),
        )

        self.db.connection.commit()

        return self.db.cursor.lastrowid

    # --------------------------------------------------
    # Get All Candidates
    # --------------------------------------------------

    def get_all_candidates(self):

        self.db.cursor.execute(
            """
            SELECT *
            FROM candidates
            ORDER BY score DESC
            """
        )

        rows = self.db.cursor.fetchall()

        return [dict(row) for row in rows]

    # --------------------------------------------------
    # Get Candidate By ID
    # --------------------------------------------------

    def get_candidate(self, candidate_id: int):

        self.db.cursor.execute(
            """
            SELECT *
            FROM candidates
            WHERE id = ?
            """,
            (candidate_id,),
        )

        row = self.db.cursor.fetchone()

        if row is None:
            return None

        return dict(row)

    # --------------------------------------------------
    # Search Candidates
    # --------------------------------------------------

    def search_candidates(self, keyword: str):

        self.db.cursor.execute(
            """
            SELECT *
            FROM candidates
            WHERE
                name LIKE ?
                OR email LIKE ?
            ORDER BY score DESC
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%"
            )
        )

        rows = self.db.cursor.fetchall()

        return [dict(row) for row in rows]

    # --------------------------------------------------
    # Update Recommendation
    # --------------------------------------------------

    def update_recommendation(
        self,
        candidate_id: int,
        recommendation: str,
    ):

        self.db.cursor.execute(
            """
            UPDATE candidates
            SET recommendation = ?
            WHERE id = ?
            """,
            (
                recommendation,
                candidate_id,
            ),
        )

        self.db.connection.commit()

    # --------------------------------------------------
    # Delete Candidate
    # --------------------------------------------------

    def delete_candidate(
        self,
        candidate_id: int,
    ):

        self.db.cursor.execute(
            """
            DELETE FROM candidates
            WHERE id = ?
            """,
            (candidate_id,),
        )

        self.db.connection.commit()

    # --------------------------------------------------
    # Count Candidates
    # --------------------------------------------------

    def count_candidates(self) -> int:

        self.db.cursor.execute(
            """
            SELECT COUNT(*)
            FROM candidates
            """
        )

        return self.db.cursor.fetchone()[0]

    def get_statistics(self):

        self.db.cursor.execute(
            """
            SELECT
                COUNT(*) as total,
                AVG(score) as average_score,
                MAX(score) as highest_score,
                MIN(score) as lowest_score
            FROM candidates
            """
        )

        row = self.db.cursor.fetchone()

        return dict(row)

    def filter_candidates(
        self,
        keyword="",
        recommendation="All",
        min_score=0,
        min_experience=0,
        sort_by="score",
    ):

        query = """
            SELECT *
            FROM candidates
            WHERE
                (
                    name LIKE ?
                    OR email LIKE ?
                    OR matched_skills LIKE ?
                    OR missing_skills LIKE ?
                )
                AND score >= ?
                AND experience >= ?
        """

        parameters = [
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            min_score,
            min_experience,
        ]

        if recommendation != "All":
            query += " AND recommendation = ?"
            parameters.append(recommendation)

        allowed_sort = {
            "score": "score DESC",
            "experience": "experience DESC",
            "name": "name ASC",
            "created_at": "created_at DESC",
        }

        query += f" ORDER BY {allowed_sort.get(sort_by, 'score DESC')}"

        self.db.cursor.execute(query, parameters)

        rows = self.db.cursor.fetchall()

        return [dict(row) for row in rows]

    # --------------------------------------------------
    # Close Connection
    # --------------------------------------------------

    def close(self):

        self.db.close()