import re

from models import Candidate
from exceptions import ParseError

class ResumeParser:

    def __init__(self, text: str):
        self.text = text

    def parse(self):
        return Candidate(
            name=self.extract_name(),
            email=self.extract_email(),
            phone=self.extract_phone(),
            skills=self.extract_skills(),
            experience=self.extract_experience(),
            education=self.extract_education()
        )

    def extract_email(self):
        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            self.text
        )

        if not match:
            raise ParseError("Email not found.")

        return match.group()

    def extract_phone(self):
        match = re.search(
            r"(\+?\d[\d\s-]{8,}\d)",
            self.text
        )

        if match:
            return match.group()

        return ""

    def extract_name(self):

        for line in self.text.splitlines():

            line = line.strip()

            if line:
                return line

        raise ParseError("Candidate name not found.")

    def extract_skills(self):

        skills = []

        capture = False

        for line in self.text.splitlines():

            line = line.strip()

            if line.lower().startswith("skills"):
                capture = True
                continue

            if capture:

                if line == "":
                    break

                skills.append(line)

        return skills

    def extract_experience(self):

        match = re.search(
            r"(\d+)\s+Years?",
            self.text,
            re.IGNORECASE
        )

        if match:
            return int(match.group(1))

        return 0

    def extract_education(self):

        lines = self.text.splitlines()

        for i, line in enumerate(lines):

            if line.lower().startswith("education"):

                if i + 1 < len(lines):
                    return lines[i + 1].strip()

        return ""