FROM python:3.9

WORKDIR /app 

# Установка необходимых системных зависимостей и Python библиотек
RUN apt-get update -y &&  \
    pip install --no-cache-dir flask && \
    useradd app_user && \
    apt-get autoremove -y && \
    apt-get clean

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

USER app_user

EXPOSE 8082

CMD ["python", "app.py"]
