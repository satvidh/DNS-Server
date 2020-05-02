FROM python:3.8

RUN mkdir /app

COPY Server.py /app/Server.py
COPY dns_generator/* /app/dns_generator/
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip \
    && pip install --upgrade -r requirements.txt

EXPOSE 53

ENTRYPOINT ["python", "Server.py"]
