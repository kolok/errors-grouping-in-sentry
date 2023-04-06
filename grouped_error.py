import logging
import os

import sentry_sdk
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

sentry_sdk.init(
    dsn=os.getenv('SENTRY_URL'),
)

logger.info('Starting the program…')
for i in range(3):
    name = input('Type a new name: ')
    logger.error("Hello, %s! this error should be grouped", name)
    logger.error(f"Hello, {name}! this error shouldn't be grouped")

logger.info("""
Thank you to run this demonstration.
You can now visit your Sentry issues and check which issues are grouped or not.
""")
