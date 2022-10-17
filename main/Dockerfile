FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirementst.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD flask run --host=0.0.0.0 --port=8080