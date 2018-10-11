FROM ubuntu:16.04

LABEL mapr.os=ubuntu16 mapr.version=6.1.0 mapr.mep_version=6.0.0

RUN apt-get install -y gcc python-dev python-setuptools python-numpy python-pip
RUN pip install opencv-python scipy pandas matplotlib

RUN echo "[global]" >> /etc/pip.conf
RUN echo "extra-index-url = http://cv:Artifactory4CV!@34.197.167.22/artifactory/api/pypi/pypi-mapr-local/simple" >> /etc/pip.conf
RUN echo "trusted-host = 34.197.167.22" >> /etc/pip.conf

ENV $DAG_HOST $MAPRUSER $MAPRPASS $TABLEPATH
