from utils.logger import logger
from utils.utils import read_yaml, create_spark
yaml_filepath = ".\conf\\spark_config.yaml"
env = "local"
logger.info("Reading config file..")
config = read_yaml(yaml_filepath)
logger.info("Done")

logger.info("Creating spark session...")
create_spark(env=env,config=config )
logger.info("spark session created...")
input("")