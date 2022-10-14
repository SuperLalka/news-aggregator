FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /home/news_aggregator
ENV PYTHONPATH = /home/news_aggregator

RUN mkdir -p static
RUN mkdir -p media

COPY ./requirements /requirements

RUN pip install --no-cache-dir --upgrade -r /requirements/local.txt

COPY ./app /home/news_aggregator/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
