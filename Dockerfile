FROM python:3.10
WORKDIR /app
COPY requirements.txt app/requirements.txt
COPY app/ app/
RUN pip install --no-cache-dir -r app/requirements.txt
CMD [ "python", "app/main.py" ]