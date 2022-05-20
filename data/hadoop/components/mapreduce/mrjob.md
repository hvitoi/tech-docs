# mrjob

- `mrjob` is a python library that allows you to create map-reduce tasks

## Installation

- It must be installed inside of the worker node
- For HDP 2.6.5, it must be configured the following way

```shell
# install from pip
pip install "pathlib"
pip install "mrjob==0.7.4"
pip install "PyYAML==5.4.1"
```

## Running

```shell
# run locally
python "script.py" "data.csv"

# run across the cluster
python "script.py" \
  -r hadoop \ # use hadoop to run
  --hadoop-streaming-jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \ # for hdp only
  "hdfs://data.csv" # path of the data file to be processed
```
