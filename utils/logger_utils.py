from logger import logger


def log_page_visit(page: str):

    logger.info(
        f"Visited page: {page}"
    )


def log_success(message: str):

    logger.info(message)


def log_error(message: str):

    logger.error(message)