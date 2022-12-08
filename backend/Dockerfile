FROM python:3.7

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /backend

WORKDIR /backend

EXPOSE 8000
