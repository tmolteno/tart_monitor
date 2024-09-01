# Pulling Ubuntu image
FROM debian:bookworm

# Update packages and Install cron
RUN apt-get update && apt-get install -y cron

# Setting up work directory
WORKDIR /src

# Copy the the app source into the container
COPY . .

# Ensure the scripts are executable
RUN chmod +x /src/scripts/*.sh

# Copy the crontab into place
COPY Crontab /etc/cron.d/

# <!-- Custom Application Setup Code Here -->

# Run cron, and tail the primary cron log
CMD cron && tail -f /var/log/cron.log
