FROM ubuntu:24.04

#2. Metadata (Optional but recommended)
LABEL maintainer="jamie@justanotherdomain.us"
LABEL description="Atlas Django main container"
#User ID Django will run as
ARG USER_ID=1000
ARG GROUP_ID=1000
ARG APPUSERNAME=Atlas

#3. Prevent interactive prompts during build (e.g., timezone selection)
ENV DEBIAN_FRONTEND=noninteractive

COPY PythonVirtualEnv /PythonVirtualEnv
COPY scripts /scripts
COPY requirements.txt /tmp/requirements.txt
#4. Install updates and essential tools
#We combine these into a single RUN instruction to reduce image layers

#The insecure on the pyenv build is because my build system is behind a transparent https squid proxy.

RUN apt-get update && apt-get install -y --no-install-recommends \
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
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /PythonVirtualEnv \
    && mkdir /scripts \
    && mkdir -p /AtlasPython \
    && /PythonVirtualEnv/bin/pyenv install 3.14.1 \
    && chown -R $APPUSERNAME /AtlasPython \
    && chown -R $APPUSERNAME /PythonVirtualEnv \
    && if getent passwd $USER_ID >/dev/null 2>&1; then \
        existing_user=$(getent passwd $USER_ID | cut -d: -f1) && \
        usermod -l $APPUSERNAME -d /home/$APPUSERNAME -m $existing_user; \
    else \
        groupadd -r -g $GROUP_ID $APPUSERNAME && \
        useradd -r -u $USER_ID -g $APPUSERNAME -d /home/$APPUSERNAME -m $APPUSERNAME; \
    fi



#USER $APPUSERNAME

# 7. Define the default command to run when the container starts
CMD ["/scripts/start"]
