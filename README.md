
# Carteiro
> "É que eu quero evitar a fadiga..."

Carteiro é um submódulo docker compose que recebe e exibe e-mails próprios.


## Instalação
Clone com submodule do git
```
git submodule add https://github.com/l31rb4g/carteiro.git mail
```
⚠ Atenção para o `mail` no final do comando.


## DNS
Entrada MX apontando para cá:
```
$ dig mx example.com
> example.		300	IN	MX	10 example.com.
```

## Variáveis
- CARTEIRO_PORTA=9990
- CARTEIRO_DOMINIO=example.com
- CARTEIRO_SENHA=123carteiro


## Docker Compose
```
  mail:
    restart: always
    build:
      context: ./mail
    volumes:
      - ./mail:/mail
      - ./mail/inbox/root:/root/Maildir
    ports:
      - "25:25"
      - "${CARTEIRO_PORTA}:8000"
    env_file: .env
    networks:
      - default
```


## Proxy
```
server {
    listen       80;
    server_name  mail.example.com;

    location / {
        return 301 https://mail.example.com$request_uri;
    }
}

server {
    listen       443 ssl;
    server_name  mail.example.com;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_certificate     /certs/mail/fullchain.pem;
    ssl_certificate_key /certs/mail/privkey.pem;

    location / {
        proxy_pass http://mail:8000;
        add_header Cache-Control "max-age=5, must-revalidate";
    }
}
```
