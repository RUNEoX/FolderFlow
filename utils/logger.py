import os
from datetime import datetime
import logging

def setup_logger():
    log_folder = os.getcwd()  # This saves the log file in the current working directory
    log_filename = f"reorganizer_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_path = os.path.join(log_folder, log_filename)

    # Set up logging
    logger = logging.getLogger("FileMover")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(log_path, encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger
