# Variables
PYTHON = python
PIP = pip
DJANGO_MANAGE = python manage.py

# Development server
runserver:
    $(DJANGO_MANAGE) runserver

# Run tests
test:
    $(DJANGO_MANAGE) test

# Make migrations
makemigrations:
    $(DJANGO_MANAGE) makemigrations

# Apply migrations
migrate:
    $(DJANGO_MANAGE) migrate

# Install dependencies
install:
    $(PIP) install -r requirements.txt

# Clean up pycache and other temporary files
clean:
    find . -name "*.pyc" -exec rm -f {} +
    find . -name "__pycache__" -exec rm -rf {} +
    rm -rf .coverage htmlcov

# Create a superuser
createsuperuser:
    $(DJANGO_MANAGE) createsuperuser

# Collect static files
collectstatic:
    $(DJANGO_MANAGE) collectstatic

# Run linting
lint:
    pylint your_app_name
