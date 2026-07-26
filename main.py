from file_manager import read_text_file
from job_loader import load_job
from matcher import CandidateMatcher
from parser import ResumeParser
from reporter import ReportGenerator


def main():
    resume_text = read_text_file(
        "resumes/sample_resume.txt"
    )

    candidate = ResumeParser(resume_text).parse()

    job = load_job(
        "jobs/python_developer.json"
    )

    matcher = CandidateMatcher()

    result = matcher.match(candidate, job)

    reporter = ReportGenerator()

    report = reporter.generate_report(
        candidate,
        job,
        result,
    )

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

    print("\nReports saved successfully.")

if __name__ == "__main__":
    main()