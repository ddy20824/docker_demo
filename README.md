#Docker Flask CRUD Demo

##Steps
#### 1. clone from github
`git clone https://github.com/ddy20824/docker_demo.git`

#### 2. build docker image
```
cd docker_demo
docker image build -t dockerfile_demo .
```

#### 3. run docker image
`docker run -it --rm -d -p 34567:5000 --name demo dockerfile_demo`
