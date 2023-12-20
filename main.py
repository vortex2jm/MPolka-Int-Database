from influxdb_client import InfluxDBClient, WritePrecision, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv
import os

load_dotenv()

url = 'http://localhost:8086'
token = os.getenv('TOKEN')
org = 'MPolkaInt'
bucket = 'IntData'

# Instantiating the db client 
client = InfluxDBClient(url=url, token=token, org=org)

# Creating writing api
write_api = client.write_api(write_options=SYNCHRONOUS)

# Creating data point
point = Point('Connectivity').tag('port', 'eth0').field('latency', 23)

# Writing data
write_api.write(org=org, bucket=bucket, record=point)
