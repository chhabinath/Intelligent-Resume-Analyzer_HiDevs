from batch_processor import BatchProcessor
from exceptions import (
    ParseError,
    ResumeAnalyzerError,
    ValidationError,
)
from logger import logger


def main():
    logger.info("Application started")

    try:
        processor = BatchProcessor()

        results = processor.process(
            "resumes",
            "jobs/python_developer.json",
        )

        print("\nBatch Resume Analysis Complete\n")
        print("-" * 60)

        for result in results:
            print(
                f"Candidate: {result['name']}\n"
                f"Score: {result['score']}\n"
                f"Recommendation: {result['recommendation']}\n"
                f"{'-' * 60}"
            )

        logger.info("Application completed successfully")

    except (ParseError, ValidationError, ResumeAnalyzerError) as error:
        logger.error(error)

    except Exception:
        logger.exception("Unexpected application error")


if __name__ == "__main__":
    main()
