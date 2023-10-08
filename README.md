# Curso de Git
Este repositório foi criado para hospedar o esqueleto do projeto que será utilizado para explicar e ensinar o uso básico do Git dentro da Comunidade DS

### Definição

O Git é um sistema de controle de versão distribuído amplamente utilizado na indústria de desenvolvimento de software e em projetos de ciência de dados. Ele foi criado por Linus Torvalds em 2005 e é uma ferramenta essencial para rastrear e gerenciar mudanças em código-fonte e outros tipos de arquivos.

Aqui está uma explicação detalhada sobre o Git:

**O que é um Sistema de Controle de Versão (SCV)?**
Um sistema de controle de versão é uma ferramenta que permite registrar e acompanhar as mudanças feitas em arquivos ao longo do tempo. Ele mantém um histórico completo das alterações, permitindo que os usuários vejam quem fez o que, quando e por quê. Isso é extremamente útil para colaboração em equipe, rastreamento de bugs e para garantir que o código seja versionado de forma segura.

**Git como Sistema de Controle de Versão:**
O Git é um sistema de controle de versão distribuído, o que significa que ele não depende de um servidor central. Cada cópia de um repositório Git é um repositório completo por si só, o que torna a colaboração e o trabalho offline mais fáceis.

**Conceitos Chave do Git:**

1. **Repositório (Repository):** Um repositório Git é um diretório onde seus arquivos e histórico de versão são armazenados. Pode ser local (no seu computador) ou remoto (em um servidor).
2. **Commit:** Um commit é uma operação que registra uma alteração no repositório. Ele contém informações sobre o que foi alterado e quem fez a alteração. Os commits formam o histórico de versão do projeto.
3. **Branch (Ramificação):** Um branch é uma linha independente de desenvolvimento. É uma cópia do repositório em um determinado momento e permite que você trabalhe em novos recursos ou correções de bugs sem afetar a versão principal (branch principal ou "master").
4. **Merge (Mesclagem):** A mesclagem é o processo de combinar duas ou mais ramificações em uma só. Isso é feito para incorporar as alterações feitas em uma ramificação em outra, como quando você deseja adicionar novos recursos ao branch principal.
5. **Pull Request (Solicitação de Pull):** Em sistemas de controle de versão baseados em Git, como o GitHub, uma pull request é uma maneira de solicitar que as alterações feitas em um branch sejam mescladas no branch principal. Ela permite revisar as alterações antes da mesclagem.

**Fluxo de Trabalho Básico do Git:**

1. **Clonando um Repositório:** Para começar a trabalhar com um projeto Git, você normalmente clona um repositório existente para sua máquina local.
2. **Criando Branches:** Você cria branches para trabalhar em novos recursos ou correções de bugs. Cada branch é uma cópia independente do código no momento em que foi criado.
3. **Fazendo Commits:** À medida que faz alterações nos arquivos, você registra essas alterações em commits com mensagens descritivas.
4. **Mesclagem (Merge) e Pull Requests:** Quando seu trabalho em um branch estiver concluído, você pode mesclar as alterações no branch principal, geralmente por meio de uma pull request.
5. **Atualizando e Sincronizando:** É importante manter seu repositório atualizado com as mudanças feitas por outros colaboradores, e você pode fazer isso através de operações como pull e fetch.
6. **Resolvendo Conflitos:** Quando duas alterações entram em conflito, o Git pedirá que você resolva esses conflitos manualmente.

Em resumo, o Git é uma ferramenta poderosa que ajuda os cientistas de dados e desenvolvedores a gerenciar o controle de versão de seus projetos, facilitando a colaboração em equipe, rastreamento de mudanças e garantindo a integridade do código ao longo do tempo. É uma parte fundamental do arsenal de ferramentas de qualquer cientista de dados e profissional de desenvolvimento de software.

---

### Principais Comandos

Aqui estão alguns dos principais comandos do Git que são amplamente usados no dia a dia:

1. **git init:** Inicializa um novo repositório Git em um diretório local, criando um novo repositório vazio.
2. **git clone:** Clona um repositório Git existente de um local remoto para sua máquina local.
3. **git add:** Adiciona arquivos ou alterações específicas ao "staging area," preparando-os para um commit.
4. **git commit:** Registra as alterações no repositório, criando um novo commit com uma mensagem descritiva.
5. **git status:** Exibe o estado atual do repositório, mostrando arquivos não rastreados, arquivos no staging area e o branch atual.
6. **git log:** Mostra um registro completo de todos os commits no histórico do repositório.
7. **git branch:** Lista todos os branches no repositório e indica qual é o branch atual.
8. **git checkout:** Muda de branch ou restaura arquivos do repositório para um estado específico.
9. **git merge:** Mescla as alterações de um branch em outro.
10. **git pull:** Atualiza seu repositório local com as alterações do repositório remoto, também realizando uma mesclagem, se necessário.
11. **git push:** Envia seus commits locais para um repositório remoto.
12. **git fetch:** Obtém informações sobre as alterações no repositório remoto sem mesclá-las em seu branch local.
13. **git remote:** Gerencia repositórios remotos, permitindo adicionar, listar ou remover conexões com repositórios remotos.
14. **git reset:** Permite reverter commits, alterando o estado do repositório para um commit anterior.
15. **git stash:** Temporariamente guarda alterações não comprometidas em um local de armazenamento ("stash"), permitindo que você mude de branch ou resolva problemas sem fazer um commit.
16. **git tag:** Cria, lista ou apaga tags (etiquetas) para marcar pontos específicos no histórico do repositório, geralmente usadas para versões estáveis.

Estes são alguns dos comandos Git mais comuns, e eles formam a base para gerenciar o controle de versão em projetos Git. Cada comando tem várias opções e funcionalidades adicionais, e é importante entender como usá-los para aproveitar ao máximo o Git no desenvolvimento de software e projetos de ciência de dados.
