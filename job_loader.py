from exceptions import ValidationError
from file_manager import read_json_file
from models import Job


REQUIRED_FIELDS = (
    "title",
    "required_skills",
    "min_experience",
    "education",
)


def load_job(file_path: str) -> Job:
    data = read_json_file(file_path)

    for field in REQUIRED_FIELDS:
        if field not in data:
            raise ValidationError(
                f"Missing required field: {field}"
            )

    return Job(
        title=data["title"],
        required_skills=data["required_skills"],
        min_experience=data["min_experience"],
        education=data["education"],
    )