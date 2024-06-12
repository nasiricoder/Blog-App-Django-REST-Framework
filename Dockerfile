ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001 
ARG GID=10001 
RUN addgroup \
    --system \
    --gid "${GID}" \
    app
RUN adduser \
    --system \
    --disabled-password \
    --home "/home/app" \
    --shell "/bin/bash" \
    --uid "${UID}" \
    --ingroup app \
    app


RUN pip install --upgrade pip 
RUN pip install pipenv
COPY --chown=app:app Pipfile Pipfile.lock /app/
RUN pipenv install --system --dev

RUN chown -R app:app .
USER app

COPY --chown=app:app . .

EXPOSE 8000