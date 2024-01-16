from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv
from lib.data_parsing import sol1_parse, sol2_parse
import os

load_dotenv()

url = 'http://localhost:8086'
token = os.getenv('TOKEN')
org = 'mpolkaint'
bucket = 'sol1'

def main():
    # Instantiating the db client 
    client = InfluxDBClient(url=url, token=token, org=org)

    # Creating writing api
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for point in sol1_parse('./data/solucao1/log_INT_E1.csv'):
        # Writing data
        write_api.write(org=org, bucket=bucket, record=point, write_precision=WritePrecision.MS)

if __name__ == '__main__':
    main()
