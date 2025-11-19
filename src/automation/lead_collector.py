thonimport json
from automation.utils.logger import get_logger
from automation.utils.validator import validate_email

logger = get_logger()

def collect_leads():
 # Simulated lead data source
 raw_leads = [
 {"name": "Alice", "email": "alice@example.com"},
 {"name": "Bob", "email": "invalid-email"},
 ]

 validated = []
 for lead in raw_leads:
 if validate_email(lead["email"]):
 validated.append(lead)
 else:
 logger.warning(f"Invalid email skipped: {lead['email']}")

 logger.info(f"Collected {len(validated)} valid leads.")
 return validated