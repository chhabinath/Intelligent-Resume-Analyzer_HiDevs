from exceptions import ValidationError
from logger import logger
from models import Candidate


class CandidateValidator:
    """
    Validates the parsed candidate information.
    """

    REQUIRED_FIELDS = (
        "name",
        "email",
        "skills",
    )

    @staticmethod
    def validate(candidate: Candidate) -> None:
        """
        Validate required candidate fields.
        Raises ValidationError if validation fails.
        """

        for field in CandidateValidator.REQUIRED_FIELDS:
            value = getattr(candidate, field)

            if not value:
                logger.error(f"Validation failed: {field} is missing")
                raise ValidationError(
                    f"{field.replace('_', ' ').title()} is required."
                )

        # Experience should not be negative
        if candidate.experience < 0:
            logger.error("Validation failed: Invalid experience")
            raise ValidationError(
                "Experience cannot be negative."
            )

        logger.info("Candidate validation successful")