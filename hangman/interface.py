from tkinter import*

class forca():
	step = 0
	letras = [chr(i+ord('a')) for i in range(26)]
	def __init__(self, palavra):
		self.verificar = False
		self.root = Tk()
		self.fig = PhotoImage(file = forca.file())
		self.image = Label(self.root, image = self.fig)
		self.image.pack(pady = 20, padx = 30)
		self.palavra = 'Palavra: ' + palavra
		self.texto = Label(self.root, text = self.palavra, font = ('20'))
		self.texto.pack()
		teste = Frame(self.root)
		teste.pack()
		self.letra = StringVar(self.root)
		self.letra.set('letra')
		self.chute = OptionMenu(teste, self.letra, *forca.letras)
		self.chute.config(width = 5)
		self.chute.grid(row = 0, column = 0)
		Button(teste, text = "Chute", command = self.check).grid(row = 0, column = 1)
	def errou(self):
		try:
			forca.step += 1
			self.fig = PhotoImage(file = forca.file())
			self.image['image']=self.fig
		except:
			self.root.destroy()
	def acertou(self, palavra):
		self.palavra = 'Palavra: ' + palavra
		self.texto['text'] = self.palavra
	def file():
		return 'Hangman'+str(forca.step)+'.gif'
	def update(self):
		self.root.update()
	def check(self):
		self.verificar = True
	def chutou(self):
		v = self.verificar
		self.verificar = False
		return v
	def input(self):
		return self.letra.get()
	def end(self):
		self.fig = PhotoImage(file = "HangmanSafe.gif")
		forca.step = 10
		self.image['image']=self.fig
