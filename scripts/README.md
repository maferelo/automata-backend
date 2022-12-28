# Raspberrypi setup

## Prerequisites

Clone repository

```bash
git clone https://github.com/maferelo/automata.git
cd automata
```

- [Docker](https://www.docker.com/)
- [ex-fuse](https://packages.debian.org/source/buster/fuse-exfat)
- [Pyenv](https://github.com/pyenv/pyenv)
- [Python3.8.13](https://www.python.org/)

```bash
ssh pi@192.168.1.3
sudo bash scripts/prestart-rpi.sh
```

## Start services

```bash
docker compose -f docker-compose.rpi.yml up
```

## Usage

### Features

- reset_jobs: Set the scripts to run consecutive by day of month.

### Scripts

- update: Update the rpi
- cleanup: Clean after reboot from update
- backup: Clone rpi to hdd
