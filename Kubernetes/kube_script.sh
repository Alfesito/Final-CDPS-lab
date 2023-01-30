#!/bin/bash
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
kubectl delete deployment reviews
if [[ $1 = v1 ]];
then
  kubectl apply -f reviews-v1-deployment.yaml
elif [[ $1 = v2 ]];
then
  kubectl apply -f reviews-v2-deployment.yaml
else
  kubectl apply -f reviews-v3-deployment.yaml
fi