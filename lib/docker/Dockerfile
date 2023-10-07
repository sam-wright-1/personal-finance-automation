# Use an official Python runtime as a parent image
FROM python:3.9

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY ./lib /app

# Define an entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint to run the custom entrypoint script
ENTRYPOINT ["/entrypoint.sh"]