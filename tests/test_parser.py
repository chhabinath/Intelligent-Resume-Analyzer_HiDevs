from parser import ResumeParser


def test_parse_resume():
    text = """
Rahul Sharma

Email: rahul.sharma@gmail.com

Phone: +91 9876543210

Skills:
Python
SQL
Git
Flask

Experience:
3 Years

Education:
B.Tech Computer Science
"""

    candidate = ResumeParser(text).parse()

    assert candidate.name == "Rahul Sharma"
    assert candidate.email == "rahul.sharma@gmail.com"
    assert candidate.phone == "+91 9876543210"
    assert candidate.experience == 3
    assert candidate.education == "B.Tech Computer Science"
    assert "Python" in candidate.skills
