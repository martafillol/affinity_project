FROM python:3.8.12-buster
COPY taxifare taxifare/
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y libhdf5-dev
RUN pip install --no-binary h5py h5py
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY Makefile Makefile
COPY setup.py setup.py
RUN make reinstall_package
CMD uvicorn taxifare.api.fast:app --host 0.0.0.0 --port $PORT
