ARG PYTHON_VERSION=3.11.10-slim-bullseye
FROM python:${PYTHON_VERSION}

# Create a virtual environment inside Docker
RUN python -m venv /opt/venv

# Activate the venv
ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# OS dependencies for PostgreSQL and Pillow (image processing)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

# Copy app code into container
COPY . .

# Collect static files for production
RUN python manage.py collectstatic --noinput

# Copy runtime script
COPY ./boot/docker-run.sh /opt/docker-run.sh
RUN chmod +x /opt/docker-run.sh

# Run the runtime script when container starts
CMD ["/opt/docker-run.sh"]