thonimport logging
from logging.handlers import RotatingFileHandler

def get_logger():
 logger = logging.getLogger("automation")
 if logger.handlers:
 return logger

 logger.setLevel(logging.INFO)
 handler = RotatingFileHandler("logs/activity.log", maxBytes=500000, backupCount=3)
 formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
 handler.setFormatter(formatter)

 logger.addHandler(handler)
 return logger