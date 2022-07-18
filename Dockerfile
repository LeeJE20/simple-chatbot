# how to build image
#   go to the path where Dockerfile exist
#   docker build --tag [image_name] .
#   ex) docker build --tag fastapi-tf-torch-gpu .

# how to run the container
#   docker run --gpus all --name [container_name] -p [host_port]:8000 -p [host_port]:8888 -v [host_dir]:/app [image_name]
#   ex) docker run --gpus all --name pydev_v1 -p 8000:8000 -p 8888:8888 -v /mnt/c/Project/simple-chatbot:/app fastapi-tf-torch-gpu

# how to use jupyter
#   1. go to container shell
#     sudo docker exec -it pydev_v1 /bin/bash
#   2. open jupyter
#     jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

# base docker image
FROM tensorflow/tensorflow:latest-gpu-jupyter

# root directory
WORKDIR /app/

# copy main.py file from ./ (host directory) to /app/ (container directory)
COPY ./* /app/

# update
RUN apt-get update
RUN apt-get upgrade -y
RUN pip install --upgrade pip

# add package by pip (use requiremnents.txt file)
RUN pip install -r requirements.txt
RUN pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html



