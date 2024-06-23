
FROM node:16 as build-stage

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .

RUN cp -f src/constants/baseUrl.prod.js src/constants/baseUrl.js && npm run build


FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN apt-get update && apt-get install -y sqlite3
RUN pip install -r requirements.txt && pip install gunicorn
RUN rm -rf /app/migrations/versions/ && mkdir -p /app/migrations/versions && rm -rf /app/instance/ && mkdir -p /app/instance/

COPY backend/ .

COPY --from=build-stage /app/dist/spa /app/src/static

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "-c", "flask --app=manage db migrate && flask --app=manage db upgrade && gunicorn -w 4 -b 0.0.0.0:8000 manage:app"]