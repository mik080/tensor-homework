minikube docker-env
eval $(minikube -p minikube docker-env)
docker build . -t devops-school/count-pods
kubectl apply -f permissions.yaml
kubectl apply -f count-pods.yaml