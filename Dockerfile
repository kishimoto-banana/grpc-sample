FROM python:3.9-slim

COPY pyproject.toml poetry.lock ./
RUN pip --disable-pip-version-check --no-cache-dir install poetry==1.0.10 && \
    poetry config virtualenvs.create false && \
    poetry install --no-ansi

COPY app ./app

CMD ["python", "app/sample_server.py"]
