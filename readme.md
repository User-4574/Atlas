[TOC]

# Atlas

This project is, generally speaking, a business intelligence system meant to inventory everything from systems, to users, to projects, git repositories, and even files on servers. It's meant to provide businesses a platform for organizing operations.



# Necessary file secrets.env

Secrets.env is necessary for the environment. It is not included in the Git repository for obvious reasons. A sample of that file is as follows:

```
#Devmode installs and configures sudo at build time. Configures the system to use manage.py instead of gunicorn+nginx
DevMode=True
#Installs a custom CA certificate into the container if behind a MITM proxy or other such need, so software will install without erroring out on cert problems
CustomCA=ca.crt

AppUserName=Atlas
PythonRoot=/python
PythonVersion=3.14.1

#The internal port that atlas will listen on, and Caddy will connect to.
AtlasPortInt=8000
#Database port that DJango will connect to
CaddyHTTPSPort=443

#Its really dumb that Postgresql is folder versioning DBS now. This keeps Postgres from doing dumb things.
PGDATA=/var/lib/postgresql/data

POSTGRES_DB=Atlas
POSTGRES_USER=Atlas
POSTGRES_PASSWORD=your_password
POSTGRES_INITDB_ARGS=--encoding=UTF-8
POSTGRES_HOST=db

#The CaddyFile version can be one of:
#CaddyFileDev - A caddy file for local development. Expects Atlas to be in Dev mode. HTTP only.
#CaddyFileDevSSL - A caddy file for local development. Expects Atlas to be in Dev mode. HTTPs with local certificates.
#CaddyFileDevLetsSSL - A caddy file for local development, with LetsEncrypt
#CaddyFileProdLocalCert - Caddy for Prudction with local certificates
#CaddyFileProdLetsSSL - A caddy file for production, with LetsEncrypt
CaddyFileVersion=CaddyFileDev



AtlasDomain=yourname.yourdomain.whatever
SiteName=yourname.yourdomain.whatever


#Apt Proxy (if any). Leave blank if none.
AptProxy=http://192.168.2.202:3142

#Timezone
TimeZone=America/Chicago
```

