from file_manager import read_text_file
from job_loader import load_job
from parser import ResumeParser


def main():
    resume_text = read_text_file(
        "resumes/sample_resume.txt"
    )

    candidate = ResumeParser(resume_text).parse()

    job = load_job("jobs/python_developer.json")

    print(candidate)
    print()
    print(job)


if __name__ == "__main__":
    main()