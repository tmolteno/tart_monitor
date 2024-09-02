# Pulling Ubuntu image
FROM debian:bookworm

# Update packages and Install cron
RUN apt-get update && apt-get install -y python3-requests

# Setting up work directory
WORKDIR /src

# Copy the the app source into the container
COPY update_tart.py .

# Run cron, and tail the primary cron log
CMD ["python3", "update_tart.py"]
