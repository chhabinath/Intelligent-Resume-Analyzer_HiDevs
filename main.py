from exceptions import (
    ParseError,
    ResumeAnalyzerError,
    ValidationError,
)
from file_manager import read_text_file
from job_loader import load_job
from logger import logger
from matcher import CandidateMatcher
from parser import ResumeParser
from reporter import ReportGenerator
from validator import CandidateValidator


def main():
    logger.info("Application started")

    try:
        resume_text = read_text_file("resumes/sample_resume.txt")

        candidate = ResumeParser(resume_text).parse()
        CandidateValidator.validate(candidate)
        logger.info("Candidate validation successful")

        job = load_job("jobs/python_developer.json")

        matcher = CandidateMatcher()
        result = matcher.match(candidate, job)
        logger.info("Candidate matching completed")

        reporter = ReportGenerator()

        report = reporter.generate_report(candidate, job, result)
        print(report)

        reporter.save_text_report(
            report,
            "reports/report.txt",
        )

        reporter.save_json_report(
            candidate,
            job,
            result,
            "reports/report.json",
        )

        logger.info("Reports generated successfully")
        logger.info("Application completed successfully")

    except (ParseError, ValidationError, ResumeAnalyzerError) as error:
        logger.error(error)

    except Exception:
        logger.exception("Unexpected application error")


if __name__ == "__main__":
    main()