import re

from exceptions import ParseError
from logger import logger
from models import Candidate

class ResumeParser:
    """
    Parses resume text and extracts candidate information.
    """

    def __init__(self, text: str):
        self.text = text

    def parse(self) -> Candidate:

        logger.info("Parsing resume")
        
        candidate =  Candidate(
            name=self.extract_name(),
            email=self.extract_email(),
            phone=self.extract_phone(),
            skills=self.extract_skills(),
            experience=self.extract_experience(),
            education=self.extract_education()
        )
        logger.info("Resume parsing completed")

        return candidate

    def extract_email(self) -> str:
        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            self.text
        )
        if not match:
            raise ParseError("Email not found.")

        logger.info("Email extracted")

        return match.group()

    def extract_phone(self) -> str:
        match = re.search(
            r"(\+?\d[\d\s-]{8,}\d)",
            self.text
        )

        if match:
            logger.info("Phone number extracted")
            return match.group()
        
        logger.warning("Phone number not found")
        return ""

    def extract_name(self) -> str:

        for line in self.text.splitlines():

            line = line.strip()

            if line:
                logger.info("Candidate name extracted")
                return line

        raise ParseError("Candidate name not found.")

    def extract_skills(self) -> str:

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

        logger.info(f"{len(skills)} skills extracted")
        return skills

    def extract_experience(self) -> str:

        match = re.search(
            r"(\d+)\s+Years?",
            self.text,
            re.IGNORECASE
        )

        if match:
            experience = int(match.group(1))
            logger.info(f"Experience extracted: {experience} years")
            return experience

        logger.warning("Experience not found")
        return 0

    def extract_education(self) -> str:

        lines = self.text.splitlines()

        for i, line in enumerate(lines):

            if line.lower().startswith("education"):

                if i + 1 < len(lines):
                    education = lines[i + 1].strip()
                    logger.info("Education extracted")
                    return education
                
        logger.warning("Education not found")
        return ""
