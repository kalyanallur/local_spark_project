import yaml
from pyspark.sql import SparkSession

def read_yaml(path):
    with open(path, "r") as file:
       content =  yaml.safe_load(file)

    return content

def create_spark(env, config):
    if env=="local":
        data = config["sparksession"]
        spark = SparkSession.builder.master(data["master"]).config("spark.jars.packages",data["package"] ).appName("myapp").getOrCreate()
        return spark