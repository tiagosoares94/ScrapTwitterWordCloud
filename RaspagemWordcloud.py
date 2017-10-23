import re                                           #Regular Expressions, para retirar caracteres especiais
from unicodedata import normalize                   #Utilizada na função remove_acentos
import os                                           #Utilização: Possibilitar o uso de comandos do Sistema operacional
import time                                         #Utilizaçao: Adicionar timers ao nosso script para parecer mais "humano"
from selenium import webdriver                      #Utilização: Testar aplicações web, automatizando-as
from selenium.webdriver.common.keys import Keys     #Utilizar os comandos END e HOME, para lidar com o infinite scrolling do Twitter
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#1 - RASPANDO TWITTER

while True:
    escolha = input('Pesquisar no Twitter:\n 1 - Hashtag\n 2 - Assunto\nEscolha: ')
    if escolha == '1':
        assunto = input('Digite uma hashtag: #')
        nav = webdriver.Chrome()
        nav.get('https://twitter.com/hashtag/' + assunto + '?src=hash')
        break
    elif escolha == '2':
        assunto = input('digite um assunto: ')
        nav = webdriver.Chrome()
        nav.get('https://twitter.com/search?q=' + assunto + '&src=tyah')
        break
    else:
        print('Digite um número válido. 1 ou 2.\n')

print('\nNavegando pelos Tweets, Aguarde...')    

#No Twitter, só se carrega 20 tweets por página, por isso, é necessário expandir a página, para baixo.

for k in range(20): #Alterar numero para gerar mais ou menos tweets. Default: 20
    elm = nav.find_element_by_tag_name('html')
    elm.send_keys(Keys.END)
    time.sleep(5)
elm.send_keys(Keys.HOME)    


#Arquivo que irá salvar todos tweets
dados = open('dados.txt', 'w')  


#Pedir para nosso navegador procurar os tweets dentro de uma determinada classe
print('Raspagem Concluída!')
tweets = nav.find_elements_by_class_name('tweet-text')


#Foi necessário criar essa função pois o bloco de notas não aceitava alguns caracteres especiais. E por conta disso, não salvava no arquivo.
#Essa função é utilizada também para remover acentos das palavras, visto que na internet, algumas pessoas acentuam e outras não.
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')


#Salvar tweets em arquivo
print('Salvando Tweets...')

if not tweets:
    print("Nada foi encontrado.")
else:
    for i in tweets:
        dados.write(remover_acentos(str(i.text.upper())+'\n'))
dados.close()

print('Tweets salvos com sucesso!')


#2 - TRABALHANDO OS DADOS

#Stopwords são palavras 'irrelevantes' para serem mostradas em nossa wordcloud.
#Nesse arquivo, contém um conjunto de palavras a serem ignoradas. Para adicionar mais palavras, basta acrescentá-las no stopwords.txt.
stopwords = open('stopwords.txt')
sw = stopwords.read().split()
stopwords.close()

f1 = open('dados.txt', 'r')
f2 = open('dadosEditados.txt','w')
texto = f1.read()


#links são problemas na hora de fazer a nuvem. Esse bloco os remove.
for palavra in texto:
    if 'http' in palavra:
        texto.remove(palavra)

#Retirar risadas da nuvem kkkkkkkk
for palavra in texto:
    if 'kk' in palavra:
        texto.remove(palavra)


#remove caracteres especiais, utilizando regex
texto = re.sub(r'[^\w\s]',' ',texto)


#Após trabalhar nos dados do texo, ele é transformado numa lista, que será usada no próximo passo
texto = texto.split()


#Só irá adicionar ao novo arquivo, se a palavra não ser uma stopword.
for palavra in texto:
    if palavra not in sw:
        f2.write(palavra+" ")

f1.close()
f2.close()


#3 - GERANDO A NUVEM

print('Gerando nuvem...')

d = path.dirname(__file__)

# Leitura dos dados.
text = open(path.join(d, 'dadosEditados.txt')).read()

#Criando nuvem
wordcloud = WordCloud(width=800, height=400,font_path="fontenuvem.TTF",margin=10,background_color="black",max_font_size=100).generate(text)
plt.figure(figsize=(20,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

#Gerando imagem, visualizando e salvando
image = wordcloud.to_image()
image.show()
image.save(assunto+'.png')


os.remove('dados.txt')
os.remove('dadosEditados.txt')
