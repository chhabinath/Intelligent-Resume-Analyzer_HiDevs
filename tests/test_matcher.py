from matcher import CandidateMatcher
from models import Candidate, Job


def test_candidate_match():
    candidate = Candidate(
        name="Rahul",
        email="rahul@gmail.com",
        phone="1234567890",
        skills=["Python", "SQL", "Git", "Flask"],
        experience=3,
        education="B.Tech Computer Science",
    )

    job = Job(
        title="Python Developer",
        required_skills=["Python", "SQL", "Git", "Flask"],
        min_experience=2,
        education="B.Tech Computer Science",
    )

    result = CandidateMatcher().match(candidate, job)

    assert result.score == 100
    assert result.recommendation == "Strongly Recommend"