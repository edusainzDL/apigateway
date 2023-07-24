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
    default-jdk \
    && apt autoremove -y \
    && apt clean \
    && rm /var/lib/apt/lists/* -r \
    && rm -rf /usr/share/man/*



COPY books/requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir setuptools
RUN pip3 install --no-cache-dir -r requirements.txt


RUN useradd -u ${USER_ID} -ms /bin/bash ${USER_NAME} \
    && adduser ${USER_NAME} sudo \
    && echo "%sudo ALL=(ALL) NOPASSWORD:ALL" >> /etc/sudousers \
    && chown -R ${USER_NAME}:${USER_NAME} /home


WORKDIR /home/${USER_NAME}/liquibase
COPY books/liquibase-4.23.0.tar.gz /home/${USER_NAME}/liquibase/.
RUN tar -xvzf liquibase-4.23.0.tar.gz
RUN echo "export PATH=$PATH:/home/${USER_NAME}/liquibase" >> /home/${USER_NAME}/.bashrc 

USER ${USER_NAME}
WORKDIR /home/${USER_NAME}/project

CMD ["bash"]