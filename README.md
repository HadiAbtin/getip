Get IP of any host or container

``` bash
# Use on docker
docker build -t getip:TAG -build-arg PYTHON_VERSION=slim . # build image
docker run -d --rm --name getip -p 8080:8080 getip:TAG # create container
curl localhost:8080/getip # test API
```
