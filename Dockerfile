FROM ubuntu:16.04

RUN apt-get update -y && \
apt-get install -y apt-utils git build-essential python-dev python-setuptools python-numpy python-pip && \
pip install opencv-python scipy pandas maprdb-python-client

ADD ./container-capture-camera-to-dag.py container-capture-camera-to-dag-db.py 
ENV DAG_HOST=$DAG_HOST MAPR_USER=$MAPR_USER MAPR_PASS=$MAPR_PASS TABLE_PATH=$TABLE_PATH

#ENTRYPOINT ["python", "container-capture-camera-to-dag-db.py", $DAG_HOST]
CMD ["/bin/bash"]
