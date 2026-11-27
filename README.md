
# End-to-End DevOps Automation Platform

## Project Overview
This project implements an end-to-end DevOps automation platform using a Student Management System.

## Application
A Python Flask web application that allows users to add, view and delete student records using SQLite.

## Technologies
- Python Flask
- Git and GitHub
- Jenkins
- Docker
- Kubernetes
- Terraform
- Ansible
- Prometheus
- Grafana
- ELK Stack
- Trivy
- Blue-Green Deployment

## Application Features
- Add student records
- View registered students
- Delete student records
- SQLite database integration
- Application health monitoring endpoint

## Local Execution

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r application/requirements.txt
python application/app.py
```

Open http://localhost:5000

Health check:
http://localhost:5000/health

## Project Status
Application development and GitHub integration completed.
DevOps automation components are being implemented.
