FROM ubuntu:16.04

RUN apt update && apt install -y \
    build-essential \
    wget \
    cmake \
    git \
    curl \
    vim \
    ca-certificates \
    python-qt4 \
    libjpeg-dev \
    zip \
    unzip \
    nginx \
    libpng-dev

RUN INSTALL_PATH=/opt/conda \
    && wget http://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
    && bash Miniconda2-latest* -fbp $INSTALL_PATH

# Set up the program in the image
COPY conv_net /opt/program
WORKDIR /opt/program
RUN chmod 755 serve

RUN cd /opt/program && /opt/conda/bin/conda env create -f environment.yml

ENV PATH /opt/conda/envs/lfseec/bin:$PATH

CMD source ~/.bashrc

# Here we install the extra python packages to run the inference code
RUN pip install flask gevent gunicorn tensorflow yolov4 opencv-python && \
    rm -rf /root/.cache

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"
