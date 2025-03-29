# Full-Stack Mentor Project

A comprehensive full-stack application built with modern technologies.

## Tech Stack

- **Frontend**: React
- **Backend**: Python (FastAPI)
- **Database**: PostgreSQL (structured data)
- **Infrastructure**: Docker, Kubernetes with Minikube
- **CI/CD**: GitHub Actions
- **Version Control**: Git/GitHub

## Project Structure

```
mentor-project/
├── frontend/          # React application
├── backend/           # Python FastAPI application
├── database/          # Database migration scripts and schema
└── infrastructure/    # Docker, K8s configuration files
```

## Development Setup

### Prerequisites

- Node.js (v14+)
- Python (3.8+)
- Docker & Docker Compose
- Minikube (for local Kubernetes)
- PostgreSQL
- Git

### Getting Started

1. Clone the repository
2. Set up the frontend: `cd frontend && npm install`
3. Set up the backend: `cd backend && pip install -r requirements.txt`
4. Start the database: `docker-compose up -d database`
5. Run the backend: `cd backend && python main.py`
6. Run the frontend: `cd frontend && npm start`

## Deployment

Refer to documentation in the `infrastructure/` directory for deployment instructions using Docker and Kubernetes.