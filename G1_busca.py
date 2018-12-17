### Buscador G1 - WordCloud das manchetes do G1 - update a cada 5s
import requests
from bs4 import BeautifulSoup
import time
### NO MAC - Comentar a linha abaixo e a linha 42
# import winsound

import matplotlib.pyplot as plt
import matplotlib.animation as anim
import wordcloud as wc

all_titles = []
all_resumos = []

def plot():
	fig = plt.figure(figsize=(16,12))
	ax = fig.add_subplot(1,1,1)
	def update(x):
		crawler_g1()
		text = " ".join(all_titles)
		wordcloud = wc.WordCloud(max_font_size=60).generate(text)
		ax.clear()
		ax.imshow(wordcloud, interpolation="bilinear")
		time.sleep(5)
	plt.axis("off")
	a = anim.FuncAnimation(fig, update)
	plt.show()

def crawler_g1():
	r = requests.get("https://g1.globo.com/economia/")
	soup = BeautifulSoup(r.text, 'html.parser')
	titles = soup.find_all('div', class_ = 'feed-post-body-title')
	resumos = soup.find_all('div', class_ = 'feed-post-body-resumo')

	for i in range(len(titles)):
		texto = titles[i].get_text()
		# resumo = resumos[i].get_text()
		global all_titles
		if texto not in all_titles:
			all_titles.append(texto)
			# all_resumos.append(resumo)
			# winsound.Beep(440, 500)
		print(time.ctime())


plot()



	