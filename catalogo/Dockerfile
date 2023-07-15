FROM python:3.11-buster

ENV DEBIAN_FRONTEND=no-interative
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
    libpq-dev \
    && apt autoremove -y \
    && apt clean \
    && rm /var/lib/apt/lists/* -r \
    && rm -rf /usr/share/man/*

COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir setuptools
RUN pip3 install --no-cache-dir -r requirements.txt


RUN useradd -u ${USER_ID} -ms /bin/bash ${USER_NAME} \
    && adduser ${USER_NAME} sudo \
    && echo "%sudo ALL=(ALL) NOPASSWORD:ALL" >> /etc/sudousers \
    && chown -R ${USER_NAME}:${USER_NAME} /home


USER ${USER_NAME}

WORKDIR /home/${USER_NAME}/project

CMD ["bash"]