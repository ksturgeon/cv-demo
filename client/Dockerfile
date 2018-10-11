FROM ubuntu:16.04

RUN apt-get update -y && \
  apt-get install -y apt-utils git build-essential python-dev python-setuptools python-numpy python-pip && \
  pip install opencv-python scipy pandas maprdb-python-client 

ENV DAG_HOST=$DAG_HOST MAPR_USER=$MAPR_USER MAPR_PASS=$MAPR_PASS TABLE_PATH=$TABLE_PATH

CMD ["/bin/bash"]
