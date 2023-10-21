# Use an official Python runtime as a parent image
FROM python:3.12.0

WORKDIR /finance_app/

# Copy the current directory contents into the container at /app
COPY ./requirements.txt /finance_app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY ./lib /finance_app/lib/

RUN chmod +x /finance_app/lib/docker/entrypoint.sh

# Set the entrypoint to run the custom entrypoint script
ENTRYPOINT ["/finance_app/lib/docker/entrypoint.sh"]
