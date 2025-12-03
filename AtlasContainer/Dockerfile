FROM ubuntu:24.04

# 2. Metadata (Optional but recommended)
LABEL maintainer="jamie@justanotherdomain.us"
LABEL description="Atlas Django main container"
#User ID Django will run as
ARG USER_ID=1000
ARG GROUP_ID=1000

# 3. Prevent interactive prompts during build (e.g., timezone selection)
ENV DEBIAN_FRONTEND=noninteractive

# 4. Install updates and essential tools
# We combine these into a single RUN instruction to reduce image layers
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    git \
    vim \
    nano \
    unzip \
    ca-certificates \
    software-properties-common \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 5. Set the working directory

# 6. (Optional) Create a non-root user for security
# It is best practice not to run applications as root
# Create the group and user using the variables
RUN groupadd -r -g $GROUP_ID appuser && \
    useradd -r -u $USER_ID -g appuser -d /home/appuser -m appuser
# Switch to this user
USER appuser

# 7. Define the default command to run when the container starts
CMD ["/bin/bash"]
