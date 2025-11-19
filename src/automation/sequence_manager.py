thonfrom automation.utils.logger import get_logger

logger = get_logger()

def process_sequences(leads):
 for lead in leads:
 logger.info(f"Processing follow-up sequence for {lead['email']}")
 return True