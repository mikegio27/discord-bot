import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(filename='music_bot.log', filemode='w', level=os.getenv("LOG_LEVEL", "INFO"))
