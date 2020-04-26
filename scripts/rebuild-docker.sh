# epw is docker image name
container_id=$(docker ps | grep epw | gawk '{print($1)}')
docker rm -f "$container_id"
docker rmi -f epw
docker build . -t epw
docker run --publish 80:8080 --restart=always -d --mount source=download,target=/app/view/static/download epw

