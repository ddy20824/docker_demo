# Docker Flask CRUD Demo

## Steps
#### 1. clone from github
```
git clone https://github.com/ddy20824/docker_demo.git
```

#### 2. build docker image
```
cd docker_demo
docker image build -t dockerfile_demo .
```

#### 3. run docker image
```
docker run -it --rm -d -p 34567:5000 --name demo dockerfile_demo
```
## CRUD API (RESTful API)
#### Read
```
POST http://localhost:34567/api/product
```
#### Create
```
GET http://localhost:34567/api/product
```
#### Update
```
PUT http://localhost:34567/api/product
```
#### Delete
```
DELETE http://localhost:34567/api/product
```

## Reference
 - docker official docs: https://docs.docker.com/
 - Azure關於docker的簡介: https://docs.microsoft.com/zh-tw/dotnet/architecture/containerized-lifecycle/what-is-docker
 - docker中運行flask參考：https://www.maxlist.xyz/2020/01/11/docker-flask/
 - flask official document: https://docs.microsoft.com/zh-tw/dotnet/architecture/containerized-lifecycle/what-is-docker
