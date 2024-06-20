FROM python:3.8.12-buster
COPY affinity affinity
COPY requiriments.txt requiriments.txt
RUN apt-get update && apt-get install -y libhdf5-dev
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY Makefile Makefile
COPY setup.py setup.py
RUN make reinstall_package
