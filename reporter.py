from dataclasses import asdict

from file_manager import write_json_file, write_text_file
from models import Candidate, Job, MatchResult


class ReportGenerator:

    def generate_report(
        self,
        candidate: Candidate,
        job: Job,
        result: MatchResult,
    ) -> str:

        matched = (
            ", ".join(result.matched_skills)
            if result.matched_skills
            else "None"
        )

        missing = (
            ", ".join(result.missing_skills)
            if result.missing_skills
            else "None"
        )

        report = f"""
============================================================
                INTELLIGENT RESUME ANALYZER
============================================================

Candidate Information
---------------------
Name           : {candidate.name}
Email          : {candidate.email}
Phone          : {candidate.phone}
Experience     : {candidate.experience} Years
Education      : {candidate.education}

Job Information
---------------
Position       : {job.title}

Skill Analysis
--------------
Matched Skills : {matched}
Missing Skills : {missing}

Overall Match Score : {result.score}/100

Recommendation
--------------
{result.recommendation}

============================================================
"""

        return report.strip()

    def save_text_report(self, report: str, file_path: str):
        write_text_file(file_path, report)

    def save_json_report(
        self,
        candidate: Candidate,
        job: Job,
        result: MatchResult,
        file_path: str,
    ):

        data = {
            "candidate": asdict(candidate),
            "job": asdict(job),
            "match_result": asdict(result),
        }

        write_json_file(file_path, data)