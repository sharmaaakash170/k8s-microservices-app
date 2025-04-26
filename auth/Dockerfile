FROM python:3.13

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    iputils-ping \
    dnsutils \
    netcat-traditional \
    postgresql-client \
    redis-tools


WORKDIR /app 

COPY app.py .   

RUN pip install flask redis psycopg2-binary

CMD ["python", "app.py"]