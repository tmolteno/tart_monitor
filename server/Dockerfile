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
RUN . /opt/venv/bin/activate && pip3 install  sqlalchemy

ENV CONFIG_DIR=/config_data

WORKDIR /python_code
ADD monitor_app monitor_app

RUN ls -l
EXPOSE 8000
CMD ["/opt/venv/bin/uvicorn", "monitor_app.main:app", "--port=8000", "--host=0.0.0.0"]
