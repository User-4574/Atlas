FROM ubuntu:24.04 AS builder
#Ubuntu is chosen for LTS support, and custom rolled for latest python. We use multi build options to keep the end image smaller
#Option for setting an APT-cacher locally for building faster
#This specifies a custom apt proxy. To speed things up and work in air gaps. I also like test building using a local apt proxy to speed things up.
ARG AptProxy=False
#This customCA certificate installer allows for internalized systems that might require it. I also run a local transparent squid proxy, so it was required.
ARG CustomCA=False
COPY Certificates/$CustomCA /tmp



#Metadata
LABEL maintainer="jamie@justanotherdomain.us"
LABEL description="Atlas Django main container"

#Prevent interactive prompts during build (e.g., timezone selection)
ENV DEBIAN_FRONTEND=noninteractive

#If an Apt proxy is specified, use it.
RUN if [ "$AptProxy" != "False"]; then \
      echo "Acquire::http::Proxy \"$AptProxy\";" > /etc/apt/apt.conf.d/01proxy; \
      echo "Acquire::https::Proxy \"$AptProxy\";" >> /etc/apt/apt.conf.d/01proxy; \
    fi
RUN    apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    git \
    unzip \
    ca-certificates \
    software-properties-common \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    vim \
    python3 \
    python3-venv \
    python3-dev
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
#Had to place here so the certificates package would be installed.
RUN if [ "$CustomCA" != "False" ]; then \
        echo "Installing custom CA: $CustomCA"; \
        cp "/tmp/$CustomCA" "/usr/local/share/ca-certificates/$CustomCA"; \
        update-ca-certificates; \
    else \
        echo "No custom CA provided; skipping."; \
    fi


RUN mkdir /scripts
RUN mkdir /AtlasPython
RUN mkdir /PythonVirtualEnv
COPY PythonVirtualEnv /PythonVirtualEnv
#Set the python environment

#Python version Django will run under.
ARG PythonVersion=3.14.1
#Location where Python will be installed
ARG PythonRoot=/python

#Install specified python version in specified python folder and make it default
ENV PYENV_ROOT=$PythonRoot
ENV PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"
RUN mkdir $PythonRoot
RUN /PythonVirtualEnv/bin/pyenv install "$PythonVersion"
COPY requirements.txt /$PythonRoot/requirements.txt
#Multi-stage pip install for speed during testing and building.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/wheels \
    /$PythonRoot/versions/$PythonVersion/bin/pip wheel -r /$PythonRoot/requirements.txt -w /wheels
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/wheels \
    /$PythonRoot/versions/$PythonVersion/bin/pip install --no-index --find-links=/wheels -r /$PythonRoot/requirements.txt

#####This is the final base image
FROM ubuntu:24.04
#Python version Django will run under.
ARG PythonVersion=3.14.1
ARG DevMode=false
ARG UserId=1000
ARG GroupId=1000
ARG AppUserName=Atlas
ARG PythonRoot=/python
ARG CustomCA=False
#Prevent interactive prompts during build (e.g., timezone selection)
ENV DEBIAN_FRONTEND=noninteractive
COPY Certificates/$CustomCA /tmp
#Location where Python will be installed
COPY --from=builder $PythonRoot $PythonRoot
COPY scripts /scripts
ENV PATH="$PythonRoot/versions/$PythonVersion/bin:$PATH"
#User ID,group ID and username Django will run as
RUN if getent passwd $UserId >/dev/null 2>&1; then \
        existing_user=$(getent passwd $UserId | cut -d: -f1) && \
        usermod -l $AppUserName -d /home/$AppUserName -m $existing_user; \
    else \
        groupadd -r -g $GroupId $AppUserName && \
        useradd -r -u $UserId -g $AppUserName -d /home/$AppUserName -m $AppUserName; \
    fi \
    && chown -R $AppUserName $PythonRoot/versions \
    && chown -R $AppUserName /scripts \
    && chmod -R 755 /scripts \
    && if [ "$DevMode" = "True" ]; then \
        apt-get update \
        && apt-get install -y sudo \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && echo "$AppUserName ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$AppUserName \
        && chmod 440 /etc/sudoers.d/$AppUserName; \
    fi;\
    if [ "$CustomCA" != "False" ]; then \
        echo "Installing custom CA: $CustomCA" \
        && apt-get update \
        && apt-get install ca-certificates -y \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && cp "/tmp/$CustomCA" "/usr/local/share/ca-certificates/$CustomCA" \
        && update-ca-certificates; \
    else \
        echo "No custom CA provided; skipping."; \
    fi
#User we run the container as.
USER $AppUserName

#Start script
CMD ["/scripts/start"]
