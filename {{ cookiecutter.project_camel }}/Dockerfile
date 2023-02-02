FROM python:{{ cookiecutter.python_version }}-slim-bullseye as base

# SETUP ENV
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

FROM base AS python-deps

RUN python -m pip install --upgrade pip && pip install --upgrade pipenv

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser/code
COPY . .
RUN pipenv install 
USER appuser
