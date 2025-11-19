thonimport smtplib
from email.mime.text import MIMEText
from automation.utils.logger import get_logger
from automation.utils.config_loader import load_settings

logger = get_logger()
settings = load_settings()

def send_email_batch(leads):
 smtp_host = settings.get("smtp_host")
 smtp_port = settings.get("smtp_port")
 smtp_user = settings.get("smtp_user")
 smtp_pass = settings.get("smtp_pass")

 for lead in leads:
 try:
 msg = MIMEText(f"Hello {lead['name']}, this is an automated outreach email.")
 msg["Subject"] = "Automated Outreach"
 msg["From"] = smtp_user
 msg["To"] = lead["email"]

 with smtplib.SMTP(smtp_host, smtp_port) as server:
 server.starttls()
 server.login(smtp_user, smtp_pass)
 server.sendmail(smtp_user, [lead["email"]], msg.as_string())

 logger.info(f"Sent email to {lead['email']}")
 except Exception as e:
 logger.error(f"Failed to send email to {lead['email']}: {e}")