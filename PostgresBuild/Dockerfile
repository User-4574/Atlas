FROM postgres:latest

ARG UserId=1000
ARG GroupId=1000
ARG AppUserName=Atlas
# Create group/user matching host
RUN groupadd -g ${GroupId} ${AppUserName} \
 && useradd -u ${UserId} -g ${AppUserName} -m ${AppUserName}

# Prepare directories
RUN mkdir -p /var/lib/postgresql/data \
 && chown -R ${AppUsername}:${GroupId} /var/lib/postgresql

# Tell Postgres where data lives
ENV PGDATA=/var/lib/postgresql/data


USER ${AppUsername}