docker rm -f share
docker rmi -f share
docker build dockershare -t share
docker run --name share -p 5022:22 -d --restart=always --mount source=download,target=/drive share
