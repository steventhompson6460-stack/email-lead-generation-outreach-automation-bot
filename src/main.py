thonfrom fastapi import FastAPI
from automation.lead_collector import collect_leads
from automation.sequence_manager import process_sequences
from automation.email_sender import send_email_batch
from automation.utils.logger import get_logger
from automation.utils.config_loader import load_settings

app = FastAPI(title="Email Lead Generation Outreach Automation Bot")
logger = get_logger()
settings = load_settings()

@app.on_event("startup")
async def startup_event():
 logger.info("Automation Bot starting up.")

@app.get("/")
def root():
 return {"status": "running"}

@app.post("/run")
async def run_automation():
 logger.info("Triggered automation run.")
 leads = collect_leads()
 send_email_batch(leads)
 process_sequences(leads)
 return {"message": "Automation completed", "lead_count": len(leads)}