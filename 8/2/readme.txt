kubectl apply -f grafana.yaml
kubectl apply -f node_exporter.yaml
kubectl apply -f prometheus.yaml
kubectl port-forward --address 193.34.234.206  deployment/grafana-deploy 3000:3000
