FROM ubuntu:22.04

# 🔧 Installer Python, ngrok, ttyd, et outils essentiels
RUN apt-get update && apt-get install -y \
    python3 python3-pip curl wget unzip git nano build-essential cmake libwebsockets-dev && \
    pip3 install flask psutil && \
    wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip && \
    unzip ngrok-stable-linux-amd64.zip && mv ngrok /usr/bin/ngrok && rm ngrok-stable-linux-amd64.zip && \
    git clone https://github.com/tsl0922/ttyd.git && cd ttyd && mkdir build && cd build && cmake .. && make && make install

# 🔐 Ajouter ton authtoken ngrok
RUN ngrok config add-authtoken 34PevzEs9iXvQbdsMd0ZJgkRIsn_7LDhoeaJemaNyr1Tr1G2T

# 📁 Dossier de travail
WORKDIR /app

# 📦 Copier le backend
COPY gopu-backend.py /app/

# 🔥 Exposer les ports
EXPOSE 8080 7681

# 🚀 Lancer le backend + terminal web + tunnel
CMD ttyd bash & ngrok http 8080 & python3 gopu-backend.py
