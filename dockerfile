# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /testapp

# Copy the current directory contents into the container
COPY . /testapp/

# Install any needed packages specified in requirements/base.txt
RUN pip install --no-cache-dir -r requirements/prod.txt

# Install any needed packages specified in requirements/base.txt
RUN apt-get update && apt-get install -y mariadb-client

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["./init-db.sh"]