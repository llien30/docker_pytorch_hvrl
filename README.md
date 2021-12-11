# Docker file for HVRL members
## How to use?
1. Copy `Dockerfile` and `requirements.txt` to your directory.
2. Run the following commands.


To create the docker container, please run 
```sh
cd [PATH FOR DIRECTORY]
docker image build -t [REPOSITORY NAME]:[TAG NAME] .
docker container run -itd -v $PWD:/workspace --name [IMAGE NAME] [REPOSITORY NAME]:[TAG NAME] /bin/bash
```

To run the script in docker container, please run
```sh
docker container exec -it [IMAGE NAME] bash
```

## About this Dockerfile
This `Dockerfile` will be constantly updated to work on the HVRL lab servers.
The current versions are...
```
cuda == 11.2
ubuntu == 16.04
```
For the convenience, the standard `requirements.txt` file is for pytorch; if you want to use tensorflow or jax, please prepare your own `requirements.txt` file.


## What is Docker?

### Overview
<img src="imgs/docker_overview.png" width="600">

### How to work on the machine?

1. **Sharing** the GPU/Storage of the machine
2. **Not sharing** the libraries

<img src="imgs/docker_container.png" width="300">

#### 1. Sharing the GPU/Storage of the machine
Because continers are running on the same OS/Infrastructure, they sharing the GPU and storage of the machine.
Please keep an eye on the GPU memory and the storage.

#### 2. Not sharing the libraries
Libraries are not dependent on others. Feel free to create your own environment.

## Useful Commands
Will be added soon...

## For Lab Members
Please contact the server team with `lab-server` in the following cases:

* Need an updated version of CUDA/ubuntu
* This Dockerfile is not work for you
* You come up with a better way to manage servers
* etc...

**IMPORTANT**
Please send me pull requests if you find any flaws in the description of Docker.
(I am a newbie to Docker...)

## License
This repository is released under the MIT License.