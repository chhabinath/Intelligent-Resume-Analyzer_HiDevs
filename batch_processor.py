from pathlib import Path

from excel_exporter import ExcelExporter
from file_manager import read_text_file
from job_loader import load_job
from logger import logger
from matcher import CandidateMatcher
from parser import ResumeParser
from pdf_exporter import PDFExporter
from reporter import ReportGenerator
from validator import CandidateValidator


class BatchProcessor:
    """
    Process all resumes in a directory.
    """

    def process(self, resumes_dir: str, job_file: str) -> list[dict]:
        results = []

        job = load_job(job_file)

        matcher = CandidateMatcher()
        reporter = ReportGenerator()
        excel_exporter = ExcelExporter()
        pdf_exporter = PDFExporter()

        for resume_file in Path(resumes_dir).glob("*.txt"):

            logger.info(f"Processing {resume_file.name}")

            try:

                resume_text = read_text_file(str(resume_file))

                candidate = ResumeParser(resume_text).parse()

                CandidateValidator.validate(candidate)

                match_result = matcher.match(candidate, job)

                report = reporter.generate_report(
                    candidate,
                    job,
                    match_result,
                )

                # ---------------------------------------
                # Save TXT Report
                # ---------------------------------------

                report_path = (
                    Path("reports")
                    / f"{resume_file.stem}_report.txt"
                )

                reporter.save_text_report(
                    report,
                    str(report_path),
                )

                # ---------------------------------------
                # Save PDF Report
                # ---------------------------------------

                pdf_path = (
                    Path("reports")
                    / f"{resume_file.stem}_report.pdf"
                )

                pdf_exporter.export_report(
                    candidate,
                    job,
                    match_result,
                    str(pdf_path),
                )

                logger.info(
                    f"PDF report saved: {pdf_path}"
                )

                # ---------------------------------------
                # Store Result
                # ---------------------------------------

                results.append(
                    {
                        "candidate": candidate.name,
                        "score": match_result.score,
                        "recommendation": match_result.recommendation,
                        "matched_skills": match_result.matched_skills,
                        "missing_skills": match_result.missing_skills,
                    }
                )

                logger.info(
                    f"Successfully processed {resume_file.name}"
                )

            except Exception as error:

                logger.error(
                    f"Failed to process {resume_file.name}: {error}"
                )

                continue

        # ---------------------------------------
        # Generate Summary Reports
        # ---------------------------------------

        if results:

            summary = reporter.generate_summary(results)

            reporter.save_text_report(
                summary,
                "reports/summary.txt",
            )

            excel_exporter.export_summary(
                results,
                "reports/summary.xlsx",
            )

            logger.info(
                "Batch summary report generated"
            )

        else:

            logger.warning(
                "No valid resumes were processed."
            )

        return results