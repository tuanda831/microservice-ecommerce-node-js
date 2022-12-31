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
    git

# Install Ansible
RUN add-apt-repository --yes --update ppa:ansible/ansible
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q ansible

# Install Skaffold
RUN curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64
RUN install skaffold /usr/local/bin/

# Install Youtube download
RUN wget -O /usr/local/bin/youtube-dl https://yt-dl.org/downloads/latest/youtube-dl
RUN chmod +x /usr/local/bin/youtube-dl
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Gcloud cli tools
# Install Aws cli tools
# Install Azure cli tools


