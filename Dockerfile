FROM python:3.7.3-slim-stretch AS base

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    gcc \
    chromium=73.0.3683.75-1~deb9u1 \
    wget \
    unzip

RUN wget -q "https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
RUN mkdir /output

COPY example example

ENTRYPOINT ["python"]
CMD ["-m", "example"]
