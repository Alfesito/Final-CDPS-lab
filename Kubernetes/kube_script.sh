# Instalamos las imagenes de docker
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
kubectl apply -f reviews-v3-deployment.yaml