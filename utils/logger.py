import logging
import os

folder = os.path.join(os.getcwd(), "Logs")
os.makedirs(folder, exist_ok=True)

logger  = logging.getLogger('log4j')
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(levelname)s - Message: %(message)s")
filehandler = logging.FileHandler(os.path.join(folder,"application_logs.log"), mode = "w")
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

logger.info("Logging Started...")