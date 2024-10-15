FROM python:latest

WORKDIR /app 

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install flask

COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8081

CMD ["python3", "app.py"]