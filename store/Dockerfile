FROM golang:1.21.0-bullseye as builder

ENV DEBIAN_FRONTEND=no-interative
ENV GO11MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64
ARG USER_ID
ARG USER_NAME


RUN apt update && apt install -y \
    build-essential \
    cmake \
    git \
    curl \
    nano \
    zip \ 
    wget \
    unzip \
    libcurl3-dev \
    && apt autoremove -y \
    && apt clean \
    && rm /var/lib/apt/lists/* -r \
    && rm -rf /usr/share/man/*

WORKDIR /home/${USER_NAME}/project

COPY store/app/go.mod /home/${USER_NAME}/project
COPY store/app/go.sum /home/${USER_NAME}/project


RUN go mod download 
# RUN go mod download github.com/gin-gonic/gin
RUN go get -u github.com/gin-gonic/gin
RUN go get -u gorm.io/gorm
RUN go get -u gorm.io/driver/postgres
RUN go get -u github.com/spf13/viper




RUN useradd -u ${USER_ID} -ms /bin/bash ${USER_NAME} \
    && adduser ${USER_NAME} sudo \
    && echo "%sudo ALL=(ALL) NOPASSWORD:ALL" >> /etc/sudousers \
    && chown -R ${USER_NAME}:${USER_NAME} /home


USER ${USER_NAME}


CMD ["bash"]