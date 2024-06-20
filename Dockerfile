FROM python:3.10
COPY affinity affinity/
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt
# COPY Makefile Makefile
COPY setup.py setup.py
RUN pip install .
RUN python -m spacy download en_core_web_sm
#RUN make reinstall_package
CMD uvicorn affinity.api.fast:app --host 0.0.0.0 --port $PORT
