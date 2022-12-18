FROM python:3.9

WORKDIR /app/triangleClassificationAPI

COPY ./triangleClassificationAPI .
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8080
ENV PYTHONPATH /app

CMD [ "gunicorn", "-c", "gunicorn_config.py", "run_server:app"]