from loguru import logger

logger.add(
    "automation.log",
    rotation="1 MB",
    level="INFO",
)

log = logger