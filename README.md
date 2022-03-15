# Projeto - Mackenzie Prática Profissional Em Análise Desenvolvimento De Sistemas Turma 05H - 2022/1
---
Proposta de desenvolvimento:
GoodBrowserGames - Uma comunidade para usuários compartilhar suas experiencias jogando browser games.

---

**Índice**

- [1. Introdução](#1-introdução)
- [2. Objetivos funcionais](#2-informações-sobre-a-empresa)
- [3. Casos de uso](#8-casos-de-uso)
- [4. Wireframes](#9-wireframes)
- [5. Diagrama de classes de domínio](#10-diagrama-de-classes-de-domínio)

# 1. Introdução
Atualmente há vários jogos disponíveis na web que podem ser jogados a partir do navegador, sem a necessidade de instalar nada mais. É o que estamos chamando neste documento de browser games.GoodBrowserGames deverá ser uma comunidade web onde seus membros poderão compartilhar as suas impressões 
sobre os browser gamers que já jogaram, identificando o que gostaram e o que não gostaram. Com estas informações, o GoodBrowserGames poderá dar para cada membro recomendações de browser games que ele ainda não conhece e que provavelmente irá gostar. A sua equipe recebeu a responsabilidade de 
desenvolver o sistema GoodBrowserGames e este documento descreve o que é desejável ter neste novo sistema.

# 2. Objetivos funcionais

1. O administrador do GoodBrowserGames será responsável por cadastrar os browser games que serão avaliados pelos membros.


2. Os browser games serão organizados nas seguintes categorias iniciais: Strategy, Shooter, Puzzle, Arcade, Role Playing Game (RPG), Sports, Action, Adventure.No entanto, o administrador poderá editar esta lista, criando novas categorias ou alterando os nomes das categorias já cadastradas.


3. Ao cadastrar um browser game, o administrador deverá fornecer as seguintes informações: nome, categoria (conforme as opções do item anterior), URL de acesso ao jogo, URL do vídeo de demonstração (se houver), descrição em 255 caracteres e imagem ilustrativa.


4. Qualquer pessoa poderá se cadastrar como membro do GoodBrowserGames mediante o fornecimento das seguintes informações: nome completo, username que deseja utilizar, senha para acessar o sistema, data de nascimento, estado e país. Cada membro poderá atualizar posteriormente os dados fornecidos no cadastro.


5. O membro terá as seguintes opções para buscar pelos browser games cadastrados: (a) busca pelo nome ou por parte do nome, (b) busca pela categoria (ao selecionar uma das categorias cadastradas, é apresentada uma lista dos browser games desta categoria em ordem alfabética).


6. Após navegar até um determinado browser game, o membro poderá avaliá-lo definindo quantas estrelas (de 1 a 5) dará para o jogo e escrevendo um texto de até 255 caracteres. Caso o membro já tenha avaliado o browser game anteriormente, ele visualizará as informações da avaliação que havia feito e terá a opção de alterá-las (afinal, pode ser que tenha mudado a sua opinião sobre o jogo).


7. Após navegar até um determinado browser game, o membro poderá também visualizar uma lista com todas as avaliações que já foram feitas para o jogo selecionado pelos outros membros do GoodBrowserGames.


8. Se o membro achar que a avaliação feita pelo outro membro foi útil, será possível marcar a opção "Esta avaliação foi útil para mim".


9. O membro poderá solicitar uma lista das avaliações mais úteis do GoodBrowserGames, ordenadas e mostrando primeiro as que receberam mais marcações na opção "Esta avaliação foi útil para mim".


10. Ao escolher visualizar as recomendações que o GoodBrowserGames tem a oferecer, o membro visualizará uma lista com os browser games que ele ainda não avaliou e provavelmente irá gostar. Para dar recomendações de acordo com o "gosto" do membro, o GoodBrowserGames deverá utilizar um algoritmo escolhido pela equipe. O algoritmo escolhido deverá ser explicado em detalhes na documentação do projeto.


11. O administrador poderá obter os seguintes relatórios de um determinado período (ou seja, definindo as datas inicial e final) de operação do GoodBrowserGames:

a. 5 jogos que receberam maior número de avaliações.
b. 5 membros que realizaram o maior número de avaliações.
c. 5 jogos que têm a maior nota média de avaliação (neste caso, só devem ser levados em conta os jogos que já receberam pelo menos 4 avaliações no período)
d. 3 categorias que receberam maior número de avaliações

# 3. Casos de uso

A figura a seguir apresenta o diagrama de casos de uso:
![caso de uso](https://user-images.githubusercontent.com/45408379/117559006-060c1d80-b058-11eb-839a-d03cbd00bcd3.jpeg)
