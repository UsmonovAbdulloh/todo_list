# Use the official Python base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /code/

# Expose the container's port (optional)
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]