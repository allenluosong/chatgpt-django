FROM python:3.9.0
RUN mkdir /app
COPY . /app 
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
