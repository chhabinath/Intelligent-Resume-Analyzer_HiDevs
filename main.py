from file_manager import read_text_file
from job_loader import load_job
from matcher import CandidateMatcher
from parser import ResumeParser


def main():
    resume_text = read_text_file(
        "resumes/sample_resume.txt"
    )

    candidate = ResumeParser(resume_text).parse()

    job = load_job("jobs/python_developer.json")

    matcher = CandidateMatcher()

    result = matcher.match(candidate, job)

    print(result)



if __name__ == "__main__":
    main()