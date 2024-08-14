import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Directory for log files
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create log file name with current timestamp
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(log_dir, log_file)

# Create logger
logger = logging.getLogger()  # Correctly defined logger
logger.setLevel(logging.INFO)

# Create a rotating file handler
file_handler = RotatingFileHandler(log_file_path, maxBytes=10 * 1024 * 1024, backupCount=5)
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define formatter and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Testing the logger
if __name__ == "__main__":
    logger.info("Log file testing")
