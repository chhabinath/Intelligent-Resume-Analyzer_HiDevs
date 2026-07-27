from rapidfuzz import fuzz
from logger import logger


class SkillMatcher:

    NORMALIZATION = {
        "python3": "python",
        "rest apis": "rest api",
        "github": "git",
        "postgresql": "sql",
        "mysql": "sql",
    }

    def __init__(self, threshold: int = 80):
        self.threshold = threshold

    def normalize(self, skill: str) -> str:
        skill = skill.lower().strip()

        return self.NORMALIZATION.get(skill, skill)

    def is_match(
        self,
        candidate_skill: str,
        required_skill: str,
    ) -> bool:

        logger.info(f"Comparing '{candidate_skill}' with '{required_skill}'")

        candidate_skill = self.normalize(candidate_skill)
        required_skill = self.normalize(required_skill)

        score = fuzz.ratio(
            candidate_skill,
            required_skill,
        )

        logger.info(f"Skill matched (score={score})")

        return score >= self.threshold
