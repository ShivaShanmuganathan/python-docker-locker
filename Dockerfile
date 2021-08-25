FROM python:3.8.10

WORKDIR /usr/src/app

COPY document.txt .
COPY raze.png .

ADD encrypt.py .

RUN pip install cryptography ed25519

CMD ["python", "./encrypt.py"]

