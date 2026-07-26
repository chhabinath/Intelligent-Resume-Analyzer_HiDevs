from dataclasses import dataclass, field


@dataclass
class Candidate:
    name: str = ""
    email: str = ""
    phone: str = ""
    skills: list[str] = field(default_factory=list)
    experience: int = 0
    education: str = ""


@dataclass
class Job:
    title: str
    required_skills: list[str]
    min_experience: int
    education: str