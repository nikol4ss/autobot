FROM python:3.11-slim

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    cron \
    wget \
    unzip \
    curl \
    gnupg \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1 \
    libxss1 \
    libu2f-udev \
    libvulkan1 \
    xdg-utils \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Instala o Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia arquivos
COPY . /app
WORKDIR /app

# Copia e ativa o cron
COPY cronjob /etc/cron.d/rpa-cron
RUN chmod 0644 /etc/cron.d/rpa-cron && \
    crontab /etc/cron.d/rpa-cron

# Ativa cron em foreground
CMD ["cron", "-f"]
