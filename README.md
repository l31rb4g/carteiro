# Carteiro
----------

# Configuração
--------------
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

Variáveis
------------
- CARTEIRO_PORTA=9990
- CARTEIRO_DOMINIO=example.com
- CARTEIRO_SENHA=123carteiro

