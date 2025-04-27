#!/bin/bash
set -e

HTPASSWD_USER="${HTPASSWD_USER:-admin}"
HTPASSWD_PASS="${HTPASSWD_PASS:-password}"

if [ "${ENABLE_NGINX_AUTH}" = "1" ]; then
    echo "Добавляю basic auth для nginx"
    htpasswd -b -c /etc/nginx/.htpasswd \
      "$HTPASSWD_USER" "$HTPASSWD_PASS"
    export AUTH_BASIC_BLOCK='    auth_basic "Restricted";'
    export AUTH_BASIC_BLOCK2='    auth_basic_user_file /etc/nginx/.htpasswd;'
else
    export AUTH_BASIC_BLOCK=""
    export AUTH_BASIC_BLOCK2=""
fi

envsubst '$AUTH_BASIC_BLOCK $AUTH_BASIC_BLOCK2' \
  < /etc/nginx/nginx.conf.template \
  > /etc/nginx/nginx.conf

exec nginx -g 'daemon off;'