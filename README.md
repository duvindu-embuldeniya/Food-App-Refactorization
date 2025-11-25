![Project Banner](https://drive.google.com/uc?export=view&id=1VAMKQ-RCDkaUvKgoj3aiHurk3Fk9md_d)

# Run & Deploy — Quick README

## To run the application locally
Clone the repo to your PC, then run:
```bash
docker-compose -f docker-compose build
docker-compose -f docker-compose up
```
Open in browser:
http://127.0.0.1:8000/

---

## To test deployment (Ubuntu / EC2)

Generate SSH key and show public key:
```bash
ssh-keygen -t rsa
cat /home/ubuntu/.ssh/id_rsa.pub
```
- copy the printed key and add it to your GitHub account.

Update system packages:
```bash
sudo apt update
sudo apt upgrade -y
```
- refresh package lists and upgrade installed packages.

Install Docker:
```bash
sudo apt install -y docker.io
```
- install Docker engine.

Enable and start Docker:
```bash
sudo systemctl enable docker
sudo systemctl start docker
```
- enable Docker on boot and start the service now.

Add your user to the docker group:
```bash
sudo usermod -aG docker $USER
```
- allow running docker without sudo.

Install Docker Compose (v1.29.1):
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
- download and make the docker-compose binary executable.

Verify installations:
```bash
docker --version
docker-compose --version
```
- confirm Docker and Compose are installed.

Clone the repo on the server and inspect:
```bash
git clone git@github.com:<github_username>/<repo_name>.git
cd <repo_name>
ls -la
```

Prepare environment file:
```bash
cp .env.sample .env
nano .env
```
- edit and change your environment variables (include your EC2 public IP in allowed hosts), then save & exit.

Before running compose: check docker group membership:
```bash
groups
# If you don’t see "docker":
sudo usermod -aG docker $USER
```

Log out and back in to apply group changes:
```bash
exit
# then re-login to the server
```

Verify groups again (after re-login):
```bash
cd <repo_name>
groups
```

Build and run the compose file (detached):
```bash
docker-compose -f docker-compose-deploy.yml up -d
```
- Paste your EC2 public IP address in the browser

---
