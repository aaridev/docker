docker build -t app:v1 .
docker images
docker run -d -p 3000:80 --name sudhan app:v1
docker ps -a
