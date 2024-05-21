FROM python:3.9.10-alpine3.14
ARG ENV
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip

RUN if [ "$ENV" = "development" ]; then pip install debugpy; fi

RUN pip install -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=$ENV
CMD ["python","app.py"]