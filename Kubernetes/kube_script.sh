# Para crear las imagenes con los Dockerfile (tarda más)
docker build -t details -f ../DockerCompose/Dockerfiles/Details/Dockerfile.details .
docker build -t productpage -f ../DockerCompose/Dockerfiles/Productpage/Dockerfile.productpage .
docker build -t ratings -f ../DockerCompose/Dockerfiles/Ratings/Dockerfile.ratings .
docker build -t reviews -f ../DockerCompose/Dockerfiles/Reviews/Dockerfile.reviews .


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
kubectl apply -f reviews-v3-deployment.yaml