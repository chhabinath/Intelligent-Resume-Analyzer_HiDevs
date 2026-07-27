from logger import logger
from skill_matcher import SkillMatcher
from models import Candidate, Job, MatchResult

skill_matcher = SkillMatcher()


class CandidateMatcher:
    """
    Matches a candidate against a job description and
    returns a MatchResult.
    """

    def match(self, candidate: Candidate, job: Job) -> MatchResult:
        """
        Compare a candidate with a job description and
        return the calculated match result.
        """

        logger.info("Matching candidate with job")
        matched_skills = []
        missing_skills = []

        score = 0

        # -----------------------------
        # Skill Matching (50 points)
        # -----------------------------
        candidate_skills = {skill.lower().strip() for skill in candidate.skills}

        for skill in job.required_skills:

            matched = any(
                skill_matcher.is_match(
                    candidate_skill,
                    skill,
                )
                for candidate_skill in candidate.skills
            )

            if matched:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        required_skill_count = len(job.required_skills)
        matched_skill_count = len(matched_skills)

        if required_skill_count > 0:
            skill_score = int((matched_skill_count / required_skill_count) * 50)
            score += skill_score

        # -----------------------------
        # Experience Matching (30 points)
        # -----------------------------
        if candidate.experience >= job.min_experience:
            score += 30

        # -----------------------------
        # Education Matching (20 points)
        # -----------------------------
        if candidate.education.strip().lower() == job.education.strip().lower():
            score += 20

        # Maximum score should not exceed 100
        score = min(score, 100)

        logger.info(f"Matched Skills: {len(matched_skills)}/{required_skill_count}")

        logger.info(f"Final score: {score}")

        recommendation = self.get_recommendation(score)

        logger.info(f"Recommendation: {recommendation}")

        return MatchResult(
            score=score,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            recommendation=self.get_recommendation(score),
        )

    def get_recommendation(self, score: int) -> str:
        """
        Returns hiring recommendation based on score.
        """

        if score >= 80:
            return "Strongly Recommend"

        if score >= 60:
            return "Recommend"

        if score >= 40:
            return "Maybe"

        return "Not Recommended"
