FROM python:3.11-slim

# Install SSH server
RUN apt-get update && apt-get install -y openssh-server supervisor && \
    mkdir /var/run/sshd && \
    echo 'root:python123' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 5000 22

CMD ["/usr/bin/supervisord"]
