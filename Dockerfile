# Use the official Python image as the base image for building
FROM python:3.12.0-slim-bookworm as builder

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

# Set the working directory inside the container
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

# Install Poetry and dependencies
RUN pip install poetry

RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN . /venv/bin/activate && poetry install --no-dev --no-root

#COPY . .
#RUN . /venv/bin/activate && poetry build

# --- Second stage to create a smaller image ---

# Use a new lightweight image
FROM python:3.12.0-slim-bookworm as runtime

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

COPY --from=builder /venv /venv
#COPY --from=builder /app/dist .
COPY src ./src
COPY run_fastapi.sh ./

ENV PATH="/venv/bin"

RUN #. /venv/bin/activate
CMD ["uvicorn", "src.fastapi.app:fastapi_app", "--host", "0.0.0.0", "--port", "80"]
