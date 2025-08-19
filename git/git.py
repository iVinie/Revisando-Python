'''
git init: iNICIALIZA O REPOSITÓRIO 
git status: exibe a situação atual do working tree (o que foi modificado e o que está preparado)
git add: Adiciona um ou mais arquivos modificados à área de preparação (staging area)
git rm --cached: remove um ou mais arquivos da área de preparação (desfaz o comando add)
git commit: registra as alterações preparadas no histórico do repositório de forma definitiva
git restore: reverte as alrerações em um arquivo, voltando ele para como estava no útimo commit
git log: mostra o histórico de commits
git diff: mostra as alterações entre diferentes commits, entre um commit e a working tree, etc

'''

'''
    Configurando o git na maquina:
    Adicionando um email e nome
    ~git config --global user.name "user"
    ~git config --global user.email "email@email.com"
    Todos os commits irão com esse user e esse email, para que outros colaboladores vejam quem comitou
    Podemos ver como está nossa configuração
    ~git config list



     Criando um novo repositório
    ~git init



    Realizando o primeiro commit
    Abra a pasta
    ~git init
    add um arquivo
    ~git status
    vai aparecer o arquivo que ainda não foi upado
    ~git add . (add todos os arquivos)
    ~git add nome_do_arquivo (add arquivo especifico)
    se colocamos dnv o ~git status, vai aparecer que um novo arquivo está sendo monitorado para ser upado
    para commitar
    ~git commit -m "texto"
    sr colocar novamente ~git status, não vai aparecer mais nada, pois ele ja foi commitado



     Visualizando os logs 
    dentro da pasta do projeto
    ~git log
    Aparecerar o historico
    ou para organizar mais, mostrando somente as principais infos
    ~git log --pretty=oneline (mostra de forma resumida)
    ~git log --pretty=oneline -1 (mostra o ultimo commit)
    ~git log --stat (o que foi feito no projeto)



     Visualizando as diferenças
    mostra o que mudou no arquivo que está na máquina e que está no head(comitado)
    ~git diff
    ~git diff nome_do_arquivo (mostra de um arquivo específico)
    git diff --name-only (mostra somente o nome do arquivo que foi alterado)



     Desfazendo alterações
    Um exemplo: fiz um commit e depois lembrei que tem outro arquivo para alterar nesse commit
    ~git commit --amend (abrirá uma aba para alteração do commit)
    se abrir o ~git log não teremos dois commits, apenas um, o que ajudará em um grande projeto
    Outro exemplo: mudamos um arquivo e rodamos o comando ~git add nome_do_arquivo e depois lembrei que tenho que adicionar mais coisas
    ~git reset HEAD nome_do_arquivo
    as mudanças vão está no arquivo local, mas não vão mais está na área de commit
    Agora, suponha que queremos voltar o arquivo como está no ultimo commit
    ~git checkout -- nome_do_arquivo
    ele voltará ao estado do ultimo commit



     Branchs 
    São "ramificações" do código principal, para que um colaborador não apague ou atrapalhe o outro e depois juntaremos tudo na main/master
    Agora, como podemos utilizar? criar, deletar, mudar de branch?
    ~git branch (aparecerá todas as branchs, se n criamos nenhuma, so aparecerá a master)
    para criar, utilizaremos
    ~git branch nome_da_branch
    para entrar na branch
    ~git checkout nome_da_branch
    se eu adicionar alguma mudança e rodar os comando ~git add . ~git commit -m '' ela só vai ser salva na branch que eu estou
    para deletar uma branch, voltaremos para master ~git checkout master
    ~git branch -D nome_da_branch
    se eu quiser criar a branch e ja entrar nela
    -git checkout -b nome_da_branch

    comando MERGE
    depois de rodar todos os comando, criação de branch, fazer alterações e agora quero juntar com a master
    voltaremos para a branch master
    ~git merge nome_da_branch
    no log vai aparecer que foi juntado as informações da branch criada com a master


//OBS.:Quando criamos um repositório ~git init não teremos uma master, então antes de criar uma nova branch, temos que adicionar os arquivos principais no repositório


      Repositório GitHub 
    Até agora so usamos o git, agora vamos ver como o github funciona e como trabalhar de modo colabolativo com outros devs
    Podemos trabalhar em alguns projetos open-source tb, como por exemplo create-react-app


      Clonando o repositório github 
    Copia o http
    ~git clone http//...
    ja clonamos


      Criando um novo repositório
    La no site do github, temos uma aba para criar, new repository
    temos algumas configs, como privado ou publico, criar um README.md
    depois podemos da um clone e trabalhar nele
    o README.md é básicamente para explicar o que tem no projeto
    se ja temos um projeto no pc e queremos linkar ao github
    ~git remote add origin http//...
    e para upar os arquivos
    ~git push origin master(ou main)



      Baixando as atualizações de um projeto
    Digamos que estamos trabalhando em grupo e alguem juntou um branch com o master e queremos baixar o que esse desenvolvedor atualizou
    ~git pull origin master
    caso tivemos um arquivo novo la no master, ele vai puxar o que ta no github para minha máquina
    podemos também upar uma branch
    ~git push origin nome_da_branch



     ignorando os arquivos
    supanhamos que queremos upar uma nova versão, mas não queremos mandar o arquivo node_modules, por exemplo, criaremos um arquivo chamado .gitignore
    so colocar o nome do arquivo la







Tipos de versões:


Major (Versão Principal): Indicada pela primeira parte do número da versão. Esta versão inclui mudanças significativas, grandes novas funcionalidades ou reestruturações que podem quebrar a compatibilidade com versões anteriores.

Minor (Versão Secundária): Indicada pela segunda parte do número da versão. Esta versão adiciona funcionalidades ou melhorias novas, mas mantém a compatibilidade com versões anteriores.

Patch (Correção de Bugs): Indicada pela terceira parte do número da versão. Esta versão é focada na correção de bugs e pequenas melhorias que não afetam a compatibilidade com versões anteriores.


'''



