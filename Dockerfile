# Use an official Python runtime as a parent image
FROM python:3.9

WORKDIR /lib

# Copy the current directory contents into the container at /app
COPY ./lib /lib
COPY ./requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "main.py"]