FROM python:3.9-slim-bullseye

# Working directory set karte hain
WORKDIR /app/

# System dependencies update aur install
# Maine yahan 'pkg-config', 'libcairo2-dev', 'build-essential' add kiya hai
# jo aapke pichle error (pycairo failure) ko fix karega.
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git curl python3-pip ffmpeg \
    libcairo2-dev pkg-config python3-dev build-essential \
    && apt-get clean

# Pehle sirf requirements copy kar rahe hain (Build speed badhane ke liye)
COPY requirements.txt .

# Pip update aur requirements install
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt

# Ab baaki saara code copy karein
COPY . .

# Start command
CMD ["bash", "start.sh"]

