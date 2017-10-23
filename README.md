# ScrapTwitterWordCloud

Exercício proposto por Fernando Masanori, docente da Faculdade de Tecnologia de São José dos Campos - Prof. Jessen Vidal, disciplina de Estrutura de Dados, terceiro semestre.

Etapa 1: Raspagem de dados.</br>
Etapa 2: Manipular os dados raspados e fazer uma representação visual deles.</br>

_______________________________________________________________________________________

<h3><strong>Exercício programa 1 - Raspagem</strong></h3>

Objetivo: Raspar Tweets, de uma determinada hashtag ou assunto, sem utilização da API do Twitter.

Inspiração:
Palestra dada na Python Vale por Bianca Berdugo: 'Raspadinha de Dados'.
Através dessa palestra, conhecemos o Selenium, uma ferramenta que lida melhor
com JavaScript, facilitando nosso processo de raspagem.


<h3><strong>Exercício Programa 2 - Manipulação de dados</strong></h3>

Objetivo: Decidimos fazer uma Nuvem de Palavras, Word Cloud, que será composta por trending words de um determinado assunto, que foi pesquisado na primeira etapa.

Referência:
https://github.com/amueller/word_cloud

_______________________________________________


<h3><strong>Como Rodar?</strong></h3>

<h3>1 - Raspando Twitter</h3>
<h5>Requer:</h5>

- Selenium;

- Google Chrome;

- Chromedriver (https://sites.google.com/a/chromium.org/chromedriver/home)

    . É necessário adicionar o diretório do Chromedrive no PATH.
    
    . Adicionando no Path: https://www.youtube.com/watch?v=L2Lzy_Icn88

<h3>2 e 3 - Manipulando Dados/Gerando nuvem</h3>
<h5>Requer:</h5>

- Ter no mesmo diretório do arquivo python:
  
  . stopwords.txt
  
  . fontenuvem

- Instalar packages:
  . wordcloud (que já vem numpy, matplotlib, pillow  e outros packages necessários)
    
    É necessário ter um compilador C na máquina, caso não tenha:
    
     . Acessar: http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
      
     . Baixar o arquivo .whl, na versão do seu python e sistema operacional
      
          . Exemplo: Windows 64 bits e Python é 3.6. Baixar arquivo: wordcloud‑1.3.2‑cp36‑cp36m‑win_amd64.whl
        
     . Instalação: pip install (seu arquivo .whl aqui)
        
          . Exemplo: pip install wordcloud‑1.3.2‑cp36‑cp36m‑win_amd64.whl
