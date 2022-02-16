# docker-flask

Imagem Docker com Flask para aplicações web com Python.

## Descrição

Com essa imagem é possível criar um ou vários ambientes de desenvolvimento.

O único requisito é ter o `Docker` instalado e configurado.

Para criar o ambiente clone este repositório com o comando `git clone https://github.com/MayconPCampos/Ambiente-docker-flask.git`
no git bash e abra com o seu Visual Studio Code.

Você vai encontrar a seguinte estrutura de arquivos:

```
.
├── flask
│    ├── app
│    │    ├─── __init__.py
│    │    ├── views.py
│    ├── .dockerignore
│    ├── dockerfile
│    ├── requirements.txt
│    ├── run.py
├── .env
├── docker-compose.yaml

```

Dentro do diretório `app` é onde o web aplicativo é desenvolvido, como a pasta contem o arquivo `__init__.py`
esse diretório agora serve como um pacote permitindo o acesso à instancia criada do Flask em qualquer parte
do projeto usando `from app import app`.

`run.py` é o arquivo de entrada que inicia o aplicativo flask

O arquivo `dockerfile` é usado para construir a imagem e `docker-compose.yaml` é o arquivo usado no gerenciamento
de um ou mais containers caso existam.

`.dockerignore` funciona exatamente igual ao `.gitignore` controlando o que será copiado para dentro do container.

O arquivo `.env` é usado para as variáveis de ambiente e é acessado dentro do `docker-composer.yaml`
    
```
   environment:
      - FLASK_APP=${FLASK_APP}
      - FLASK_ENV=${FLASK_ENV}
```

Para criar a imagem e ativar o container basta usar o comando `docker-composer up` no terminal. O app flask inicia com
o modo DEBUG ligado na porta 5000 do localhost pronto para o desenvolvimento onde as mudanças feitas dentro do volume
compartilhado, ou seja, o diretório `flask` serão refletidas dentro do container.
