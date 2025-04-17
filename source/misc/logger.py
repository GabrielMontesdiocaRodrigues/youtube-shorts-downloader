"""Enables logging"""

import logging
import sys

from source.config import LOG_FILE


sys.tracebacklimit = 0

logger: logging.Logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.WARNING,
    format="%(levelname)-8s %(filename)s:%(lineno)d [%(asctime)s] - %(name)s - %(message)s",
)
