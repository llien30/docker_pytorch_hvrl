FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt-get -y install --no-install-recommends software-properties-common libgl1-mesa-dev wget libssl-dev git

RUN add-apt-repository -y ppa:deadsnakes/ppa && apt-get -y install --no-install-recommends python3.9-dev python3.9-distutils python3-pip python3.9-venv
# change default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# clear cache
RUN rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip distlib setuptools

WORKDIR /workspace

# install dependencies
COPY requirements.txt /workspace
RUN pip3 install -r requirements.txt

CMD ["/bin/bash", "-c"]
