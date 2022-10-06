# Backup job for postgresql



## Build Dockerfile
In order to include scripts / etc you need to be in the root directory (this directory) and execute docker build with the file param:

Example for building pg 14 version:
```bash
docker build -f image/14/Dockerfile -t isitar/backup-postgresql-k8s-job .
```