FROM postgres:14

# install python & pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    zip \
    && rm -rf /var/lib/apt/lists/*


# install azure storage module
RUN pip3 install azure-storage-blob

WORKDIR /app

COPY script/main.py /app/main.py
COPY image/14/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT /app/entrypoint.sh