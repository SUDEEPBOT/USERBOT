FROM python:3.9-slim-bullseye

# Working directory
WORKDIR /app/

# Timezone set karein (Important for Pyrogram)
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# System dependencies install
# Added 'tzdata' for time synchronization
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    git curl python3-pip ffmpeg \
    libcairo2-dev pkg-config python3-dev build-essential \
    tzdata \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Requirements install
COPY requirements.txt .
RUN pip3 install -U pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Copy code
COPY . .

# Start command
CMD ["bash", "start.sh"]

