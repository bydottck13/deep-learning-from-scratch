# Introduction to Deep Learning from National Research University Higher School of Economics courses

------

## Environments: Docker container
Download and Install Docker container from [here](https://hub.docker.com/r/zimovnov/coursera-aml-docker/); [Ubuntu Version Xenial 16.04 (LTS)](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

* Set up the respository
```
$ sudo apt-get remove docker docker-engine docker.io
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo apt-key fingerprint 0EBFCD88
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

* Install Docker CE
```
$ sudo apt-get update
$ sudo apt-get install docker-ce
$ sudo apt-get install docker-ce="18.03.0~ce-0~ubuntu"
$ sudo docker run hello-world
```

* Post-installation steps for Linux
```
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
```

* On a desktop Linux environment such as X Windows, log out of your session completely and then log back in.
```
$ docker run hello-world
```

* Use the OverlayFS storage driver
```
$ sudo systemctl stop docker
$ cp -au /var/lib/docker /var/lib/docker.bk
$ sudo gedit /etc/docker/daemon.json
```

	{
	  "storage-driver": "overlay2"
	}

* Start Docker
```
$ sudo systemctl start docker
$ docker info

Containers: 0
Images: 0
Storage Driver: overlay2
 Backing Filesystem: extfs
<output truncated>
```

* Configure Docker to start on boot
```
$ sudo systemctl enable docker
$ sudo systemctl edit docker.service
```

	[Service]
	ExecStart=
	ExecStart=/usr/bin/dockerd -H fd:// -H tcp://127.0.0.1:2375

* Reload the systemctl configuration
```
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker.service
$ sudo netstat -lntp | grep dockerd
tcp        0      0 127.0.0.1:2375          0.0.0.0:*               LISTEN      3758/dockerd
```

* Running container for the first time
```
$ docker pull zimovnov/coursera-aml-docker
$ docker run -it -p 127.0.0.1:8080:8080 --name coursera-aml-1 zimovnov/coursera-aml-docker.
```

* Stopping and starting the container
```
$ docker stop coursera-aml-1
$ docker start -a coursera-aml-1
```

## Reference
* [Introduction to Deep Learning](https://www.coursera.org/learn/intro-to-deep-learning)
* [Introduction to Deep Learning course resources](https://github.com/hse-aml/intro-to-dl)
