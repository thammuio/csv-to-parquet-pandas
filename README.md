# Converting CSV to Parquet using Pandas
We are using python 3.6.x

## Run

python3.6 csv-to-parquet.py csv_input_path parquet_output_path

*example:* python3.6 csv-to-parquet.py /data/csv-to-parquet/test-simple.csv /data/csv-to-parquet/test-simple-csv.parquet


## Install Python 3.6 on CentOS7
(if you dont hace Python3 already)

yum -y install yum-utils

yum -y groupinstall development

yum -y install https://centos7.iuscommunity.org/ius-release.rpm

yum -y install python36u

yum -y install python36u-pip

pip3.6 install pandas

yum -y install python36u-devel

pip3.6 install pyarrow

pip3.6 install fastparquet

(and Run the Proogram Now)
