from file_manager import read_text_file
from parser import ResumeParser


def main():
    text = read_text_file("resumes/sample_resume.txt")

    parser = ResumeParser(text)

    candidate = parser.parse()

    print(candidate)


if __name__ == "__main__":
    main()