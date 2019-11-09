FROM python:3.7.4-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi

RUN addgroup -S django && adduser -S -G django django

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt && rm /requirements.txt

COPY ./docker/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./docker/start-local /startlocal
RUN sed -i 's/\r//' /startlocal
RUN chmod +x /startlocal
RUN chown django /startlocal

COPY ./docker/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown django /start

COPY . /app

RUN chown -R django /app

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]