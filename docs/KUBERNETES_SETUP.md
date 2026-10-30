# DevDeploy - Kubernetes Deployment

## 1. Overview

This document explains how to deploy the DevDeploy Flask application
to Kubernetes using Minikube.

The application image is:

susrithag/devdeploy-app:latest

## 2. Kubernetes Resources

We created two Kubernetes resources:

### Deployment

File: `k8s/deployment.yaml`

- Deployment name: devdeploy
- Container name: devdeploy-app
- Docker image: susrithag/devdeploy-app:latest
- Initial replicas: 1
- Container port: 5000
- Readiness and liveness probes: /health

### Service

File: `k8s/service.yaml`

- Service name: devdeploy-service
- Service type: NodePort
- Service port: 80
- Target port: 5000
- NodePort: 30080

## 3. Start Minikube

```bash
minikube start --driver=docker
minikube status
```

## 4. Deploy the Application

Apply the Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Check deployments:

```bash
kubectl get deployments
```

Check Pods:

```bash
kubectl get pods -o wide
```

Check Services:

```bash
kubectl get services
```

## 5. Access the Application

Forward local port 8081 to the Kubernetes Service:

```bash
kubectl port-forward service/devdeploy-service 8081:80
```

Open:

http://localhost:8081

Test the health endpoint:

```bash
curl http://localhost:8081/health
```

Expected response:

```json
{ "status": "healthy" }
```

## 6. Scaling the Application

Initially, the Deployment runs one replica.

Scale the Deployment to three replicas:

```bash
kubectl scale deployment devdeploy --replicas=3
```

Verify the Deployment:

```bash
kubectl get deployments
```

Verify the Pods:

```bash
kubectl get pods -o wide
```

Expected result: 3/3 replicas ready.

## 7. Verify Service Endpoints

Check the EndpointSlices:

```bash
kubectl get endpointslices \
  -l kubernetes.io/service-name=devdeploy-service
```

The Service should have three ready Pod endpoints.

## 8. View Application Logs

```bash
kubectl logs deployment/devdeploy
```

## 9. Kubernetes Architecture

GitHub
|
v
Jenkins
|
v
Docker Hub
|
v
Kubernetes Deployment
|
v
Three Application Pods
|
v
Kubernetes Service
|
v
DevDeploy Flask Application

## 10. Conclusion

The DevDeploy application was successfully deployed
on Minikube using Kubernetes Deployment and Service resources.

The application was verified through its health endpoint.
The Deployment was scaled from one replica to three replicas,
and all three Pods were registered as Service endpoints.
