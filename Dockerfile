FROM python:3.7-slim

RUN mkdir -p /opt/src /input /output

WORKDIR /opt/src

COPY requirements.txt /opt/src/
RUN python -m pip install -r requirements.txt

ADD src /opt/src/

ENTRYPOINT "python" "-m" "run_submission"
