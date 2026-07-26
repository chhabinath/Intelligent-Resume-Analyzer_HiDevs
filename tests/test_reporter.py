from models import Candidate, Job, MatchResult
from reporter import ReportGenerator


def test_generate_report():
    candidate = Candidate(
        "Rahul",
        "rahul@gmail.com",
        "1234567890",
        ["Python"],
        3,
        "B.Tech",
    )

    job = Job(
        "Python Developer",
        ["Python"],
        2,
        "B.Tech",
    )

    result = MatchResult(
        100,
        ["Python"],
        [],
        "Strongly Recommend",
    )

    report = ReportGenerator().generate_report(
        candidate,
        job,
        result,
    )

    assert "Rahul" in report
    assert "100/100" in report