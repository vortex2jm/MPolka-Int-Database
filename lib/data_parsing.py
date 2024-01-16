from influxdb_client import Point
import pandas as pd

# Testing ...
# points = []
# df_e1 = pd.read_csv('../data/solucao1/log_INT_E1.csv')    
# print(df_e1)

# Function for solution 1 =========================
def sol1_parse(path):
    points = []
    df = pd.read_csv(path)
    for index, row in df.iterrows():
        # print(str(row['switchID_t']), row[' egress_port'], row[' qid'], row[' enq_qdepth'])
        p = Point('IntData').tag('Switch', str(row['switchID_t'])).tag('port', str(row[' egress_port']))\
        .tag('queue', str(row[' qid'])).field('depth', int(row[' enq_qdepth']))
    
        points.append(p)
    return points

# Function for solution 2 =========================
def sol2_parse(path):
    df = pd.read_csv(path)


if __name__ == '__main__':
    pass
