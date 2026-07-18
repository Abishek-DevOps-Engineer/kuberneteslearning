# Kubernetes Deployment Architecture

This project deploys a simple Flask-based application on Kubernetes with an Ingress that routes traffic to two separate services.

## Architecture Overview
- An Ingress resource named `myappingresss` receives incoming HTTP traffic for the host `foo.bar.com`.
- The Ingress routes requests based on the URL path:
  - `/greet` -> `python-service`
  - `/weather` -> `weatherappservice`
- Each service exposes the application workload through a Kubernetes `Service` and forwards traffic to the matching container port.

## Components
- `python-deployment` runs the greeting application container.
- `weatherappdeployment` runs the weather application container.
- `python-service` exposes the greeting app on port 80.
- `weatherappservice` exposes the weather app on port 80.

## Request Flow
1. A client sends a request to `foo.bar.com`.
2. The Ingress evaluates the path.
3. Traffic is forwarded to the correct backend service.
4. The service forwards the request to the appropriate pod.

## Summary
This setup demonstrates a basic multi-service Kubernetes architecture where one ingress entry point distributes traffic to multiple backend applications.
