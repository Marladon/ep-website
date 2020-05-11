# epw is docker image name
docker rm -f epw
docker rmi -f epw
docker build . -t epw
docker run --name epw --publish 80:8080 --publish 443:8443 --restart=always -d --mount source=download,target=/app/view/static/download epw

