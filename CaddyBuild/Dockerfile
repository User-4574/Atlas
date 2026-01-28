FROM caddy:2-builder AS builder

#Metadata
LABEL maintainer="jamie@justanotherdomain.us"
LABEL description="Atlas Caddy proxy builder container"

ARG CustomCA=False
#Copy in custom certificates
COPY Certificates/ /tmp
RUN if [ "$CustomCA" != "False" ]; then \
        echo "Installing custom CA: $CustomCA"; \
        cp "/tmp/$CustomCA" "/usr/local/share/ca-certificates/$CustomCA"; \
        update-ca-certificates; \
    else \
        echo "No custom CA provided; skipping."; \
    fi

#Build Caddy with extra plugins
RUN xcaddy build \
    --with github.com/caddy-dns/cloudflare \
    --with github.com/caddyserver/transform-encoder \
    --with github.com/caddyserver/replace-response \
    --with github.com/caddy-dns/acmeproxy


FROM caddy:2

LABEL maintainer="jamie@justanotherdomain.us"
LABEL description="Atlas Caddy proxy runtime container"
ARG CustomCA=False
#Copy in custom certificates
COPY Certificates/ /tmp

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
RUN if [ "$CustomCA" != "False" ]; then \
        echo "Installing custom CA: $CustomCA"; \
        cp "/tmp/$CustomCA" "/usr/local/share/ca-certificates/$CustomCA"; \
        update-ca-certificates; \
    else \
        echo "No custom CA provided; skipping."; \
    fi
RUN /sbin/apk add --no-cache nss-tools ca-certificates