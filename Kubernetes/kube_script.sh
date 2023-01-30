#!/bin/bash
# Pasa como parametro la version de reviews que se quiere
version = $1
# Instalamos las imagenes de docker hub
docker pull alfesito/productpage
docker pull alfesito/details
docker pull alfesito/ratings
docker pull alfesito/reviews:v1
docker pull alfesito/reviews:v2
docker pull alfesito/reviews:v3

# Aplicamos los manifiestos
kubectl apply -f productpage.yaml
kubectl apply -f details.yaml
kubectl apply -f ratings.yaml
kubectl apply -f reviews-svc.yaml
kubectl delete reviews-v1-deployment.yaml
kubectl delete reviews-v2-deployment.yaml
kubectl delete reviews-v3-deployment.yaml
kubectl apply -f reviews-$version-deployment.yaml