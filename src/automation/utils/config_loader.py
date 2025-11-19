thonimport yaml
import os
from dotenv import load_dotenv

def load_settings():
 load_dotenv("config/credentials.env")

 with open("config/settings.yaml", "r") as f:
 settings = yaml.safe_load(f)

 settings["smtp_host"] = os.getenv("SMTP_HOST", "smtp.example.com")
 settings["smtp_port"] = int(os.getenv("SMTP_PORT", "587"))
 settings["smtp_user"] = os.getenv("SMTP_USER", "user@example.com")
 settings["smtp_pass"] = os.getenv("SMTP_PASS", "password")

 return settings