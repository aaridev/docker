docker build -t app:v2 .
docker images
docker run -d -p 2000:80 --name sudhan app:v2
docker ps -a
