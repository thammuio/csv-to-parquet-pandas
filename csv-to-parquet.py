## not using #! as we wil be tunning it with exact python version
## Example command: python3.6 csv-to-parquet.py /data/test-simple.csv /data/test-simple-csv.parquet


import sys
import pandas as pd

print ('########## STARTING ##############')

csv_input_path = sys.argv[1]
parquet_output_path = sys.argv[2]

print ('CSV input is:', csv_input_path)

print ('...............')

df = pd.read_csv(csv_input_path)
df.to_parquet(parquet_output_path)

print ('Parquet output here:', parquet_output_path)

print ('########## FINISHED ##############')
