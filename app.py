import os
from flask import Flask
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "dental-crm-secret-key"

# Import routes after app initialization
import routes  # noqa: F401
logger.info("Flask app initialized successfully")
