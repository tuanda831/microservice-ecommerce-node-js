FROM bitnami/kubectl:1.20.9 as kubectl
FROM alpine/helm as helm
FROM vault as vault

FROM ubuntu:latest

# Install Kubectl
COPY --from=kubectl /opt/bitnami/kubectl/bin/kubectl /usr/local/bin/

# Intall Helm
COPY --from=helm /usr/bin/helm /usr/local/bin/

# Install vault cli
COPY --from=vault /bin/vault /usr/local/bin

RUN apt-get update && apt-get install -y curl \
    apt-transport-https \
    gpg \
    wget \
    zsh \
    openssl \
    ssh \
    vim neovim \
    jq \
    gcc g++ \
    python3 \
    python3-pip \
    golang \
    software-properties-common \
    ffmpeg \
    ca-certificates gnupg \
    lsb-release \
    zip \
    git

# Pre-Install Ansible
RUN add-apt-repository --yes --update ppa:ansible/ansible

# Pre-Install Gcp cli
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | tee /usr/share/keyrings/cloud.google.gpg

RUN apt-get update

# Install Ansible
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q ansible

# Install Gcloud cli tools
RUN apt-get install -y google-cloud-cli

# Install Skaffold
RUN curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64
RUN install skaffold /usr/local/bin/

# Install Youtube download
RUN wget -O /usr/local/bin/youtube-dl https://yt-dl.org/downloads/latest/youtube-dl
RUN chmod +x /usr/local/bin/youtube-dl
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Aws cli tools
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update

# Install Azure cli tools
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

