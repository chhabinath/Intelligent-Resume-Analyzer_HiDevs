from skill_matcher import SkillMatcher


def test_python3_matches_python():
    matcher = SkillMatcher()

    assert matcher.is_match(
        "Python3",
        "Python",
    )


def test_rest_api_matches():
    matcher = SkillMatcher()

    assert matcher.is_match(
        "REST APIs",
        "REST API",
    )


def test_github_matches_git():
    matcher = SkillMatcher()

    assert matcher.is_match(
        "GitHub",
        "Git",
    )


def test_postgresql_matches_sql():
    matcher = SkillMatcher()

    assert matcher.is_match(
        "PostgreSQL",
        "SQL",
    )