# Kubernetes-Ready Microservices App

Welcome to the **k8s-microservices-app**, a hands-on project demonstrating a full end-to-end microservices deployment pipeline using Docker and Kubernetes.

---

## 🔍 Overview

A multi-tier application consisting of:
- **Authentication Service** (Flask)
- **API Service** (Flask)
- **Frontend** (NGINX + React)
- **Redis** for caching
- **PostgreSQL** for persistence

Features:
- Containerization with Docker
- Kubernetes Deployments & Services
- Ingress routing via NGINX
- Horizontal Pod Autoscaling (HPA)
- Monitoring setup with Metrics Server

---

## 🗂️ Folder Structure

```
k8s-microservices-app/
│
├── auth/
│   ├── Dockerfile
│   └── app.py
│
├── api/
│   ├── Dockerfile
│   └── app.py
│
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf
│   └── index.html
│
├── k8s/
│   ├── auth/
|   |   ├── deployment.yaml
|   |   ├── hpa.yml    
|   │   └── service.yaml
│   ├── ingress/
|   │   └── ingress.yaml
|   ├── metric-server/
|   │   ├── deployment.yaml
|   │   └── service.yaml
│   ├── postgres/
|   |   ├── deployment.yaml
|   |   ├── hpa.yml    
|   │   └── service.yaml
│   └── redis/
|       ├── deployment.yaml
|       ├── hpa.yml    
|       └── service.yaml
|
├── docker-compose.yml
│
└── README.md
```

---

## 🚀 Prerequisites

- Docker  
- kubectl  
- A running Kubernetes cluster (e.g., Kind, Minikube, or remote)  

---

## 📦 Deployment Steps

1. **Build Docker Images**  
   ```bash
   docker build -t auth:latest ./auth
   docker build -t api:latest  ./api
   docker build -t frontend:latest ./frontend
   ```

2. **Apply Kubernetes Manifests**  
   ```bash
   kubectl apply -f auth/deployment.yaml
   kubectl apply -f auth/service.yaml
   # Repeat for api, frontend, redis, postgres
   ```

3. **Ingress Controller**  
   ```bash
   kubectl apply -f ingress/ingress.yaml
   ```

4. **Configure HPA**  
   ```bash
   kubectl apply -f hpa/auth-hpa.yaml
   ```

5. **Monitoring**  
   ```bash
   kubectl apply -f monitoring/metrics-server.yaml
   ```

---

## 🔗 Accessing Services

- **Auth**: `http://auth.local/auth/ping`  
- **API**: `http://api.local/api/ping`  
- **Frontend**: `http://frontend.local/`  

_Add host entries in `/etc/hosts` for local testing:_
```
127.0.0.1 auth.local api.local frontend.local
```

---

## 📈 Next Steps

- Integrate **Prometheus & Grafana** for advanced metrics  
- Add **TLS certificates** via cert-manager  
- Implement **CI/CD** with GitHub Actions or GitLab CI  

---

## 📄 License

This project is licensed under the MIT License.
