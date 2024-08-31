FROM debian:bookworm
LABEL Maintainer: Tim Molteno "tim@elec.ac.nz"
ARG DEBIAN_FRONTEND=noninteractive

# debian setup
RUN apt-get update -y && apt-get install -y \
    python3-pkgconfig \
    python3-venv

RUN rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv --system-site-packages $VIRTUAL_ENV

RUN . /opt/venv/bin/activate && pip3 install  fastapi[standard]

ENV CONFIG_DIR=/config_data

WORKDIR /python_code
COPY ./main.py .

EXPOSE 8000
CMD ["/opt/venv/bin/fastapi", "dev", "--port=5000", "main.py"]
