FROM python:3.10-alpine

ENV DATABASE_HOST=$DATABASE_HOST
ENV DATABASE_PORT=$DATABASE_PORT
ENV DATABASE_USER=$DATABASE_USER
ENV DATABASE_NAME=$DATABASE_NAME
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD

ONBUILD EXPOSE 8000
ONBUILD RUN apk update && \
            apk add postgresql postgresql-contrib
ONBUILD RUN python3.10 -m pip install -r requirements.txt


ENTRYPOINT ["gunicorn"]
CMD ["integrator:app:create_app"]


