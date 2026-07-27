from dataclasses import asdict

from file_manager import write_json_file, write_text_file
from logger import logger
from models import Candidate, Job, MatchResult


class ReportGenerator:
    """
    Generates and saves resume analysis reports
    in text and JSON formats.
    """

    def generate_report(
        self,
        candidate: Candidate,
        job: Job,
        result: MatchResult,
    ) -> str:
        """
        Generate a formatted text report for the
        candidate's resume analysis.
        """

        matched = ", ".join(result.matched_skills) if result.matched_skills else "None"

        missing = ", ".join(result.missing_skills) if result.missing_skills else "None"

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
        logger.info("Report generated")

        return report.strip()

    def save_text_report(self, report: str, file_path: str) -> None:
        """
        Save the generated report as a text file.
        """
        write_text_file(file_path, report)
        logger.info(f"Text report saved: {file_path}")

    def save_json_report(
        self,
        candidate: Candidate,
        job: Job,
        result: MatchResult,
        file_path: str,
    ) -> None:
        """
        Save the analysis data as a JSON file.
        """

        data = {
            "candidate": asdict(candidate),
            "job": asdict(job),
            "match_result": asdict(result),
        }

        write_json_file(file_path, data)
        logger.info(f"JSON report saved: {file_path}")

    def generate_summary(self, results: list[dict]) -> str:
        """
        Generate a summary report for all processed candidates.
        """

        lines = [
            "=" * 70,
            "               BATCH RESUME ANALYSIS SUMMARY",
            "=" * 70,
            "",
            f"{'Candidate':<20} {'Score':<10} {'Recommendation'}",
            "-" * 70,
        ]

        for result in sorted(
            results,
            key=lambda x: x["score"],
            reverse=True,
        ):
            lines.append(
                f"{result['candidate']:<20} "
                f"{result['score']:<10} "
                f"{result['recommendation']}"
            )

        lines.append("=" * 70)

        return "\n".join(lines)
