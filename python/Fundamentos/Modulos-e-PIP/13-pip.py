'''
https://pypi.org/
'''

'''
A principal vantagem de ter um ambiente virtual de desenvolvimento, é que isolamos as bibliotecas que serão utilizadas em um projeto, o que vai facilitar bastante quando se quiser fazer o deploy de um projeto.

Em nosso caso, o deploy do aplicativo será a geração do arquivo instalador da aplicação do Tkinter. Por isso, vamos nos certificar de que apenas as bibliotecas necessárias sejam utilizadas no projeto.

Para criar o ambiente virtual de desenvolvimento, pode-se executar o comando no terminal: python -m venv .venv

Estamos indicando que vamos criar um diretório .venv, que vai ser o diretório que armazenará as bibliotecas que instalarmos nesse ambiente de desenvolvimento.

Para ativar o ambiente virtual de desenvolvimento, pode ser executado o comando: ./.venv/Scripts/activate

Como pode ser visto na imagem abaixo, já estamos dentro do ambiente virtual de desenvolvimento.
'''


'''
é uma boa pratica colocar o .venv no gitignore?
O ChatGPT disse:

Sim, é uma ótima prática e praticamente obrigatória. ✅

Por quê?

Evita arquivos desnecessários no repositório

O .venv contém todos os pacotes instalados e arquivos binários do Python.

Isso deixa o repositório enorme e desorganizado.

Evita conflitos entre máquinas

Cada desenvolvedor pode ter sistemas operacionais ou versões de Python diferentes.

O .venv de uma máquina pode não funcionar em outra.

O correto é versionar só as dependências

Use requirements.txt ou pyproject.toml para registrar os pacotes que o projeto precisa.

Quem clona o projeto pode criar o próprio .venv local e instalar tudo com:

pip install -r requirements.txt





Então eu preciso criar um arquivo com esse nome?
O ChatGPT disse:

Exato ✅, você precisa criar um arquivo chamado requirements.txt (o nome é padrão) e listar nele os pacotes que seu projeto precisa.

Como fazer:

Se você já está no ambiente virtual do projeto (venv) e já instalou os pacotes que vai usar, rode:

pip freeze > requirements.txt


Isso vai gerar um arquivo requirements.txt com todas as bibliotecas e versões do seu ambiente virtual.
'''