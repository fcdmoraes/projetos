from tkinter import *
import requests
import json

def cambio(fc,tc,value):
	key = '8PNO25GJOZBIS0NM'
	url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(fc,tc,key)
	r = requests.get(url)
	dic = json.loads(r.text)
	# print(dic)
	if 'Realtime Currency Exchange Rate' in dic:
		texto = "{:.2f}".format(float(dic['Realtime Currency Exchange Rate']['5. Exchange Rate'])*float(value))
	else:
		texto = (dic['Information'])
	print(texto)
	label['text'] = texto

janela = Tk()
janela.winfo_toplevel().title("Let's Exchange")
janela.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")

Label(janela, text = "Let's Exchange", font = (20)).pack(pady = 10)
frame = Frame(janela)
frame.pack()
Label(frame, text = "From Currency", width = 15).grid(row = 0, column = 0, padx = 10)
Label(frame, text = "To Currency", width = 15).grid(row = 0, column = 1, padx = 10)

fc = StringVar(frame)
tc = StringVar(frame)

OptionMenu(frame, fc, 'USD','BRL','EUR').grid(row = 1, column = 0, sticky = W+E, padx = 10)
OptionMenu(frame, tc, 'USD','BRL','EUR').grid(row = 1, column = 1, sticky = W+E, padx = 10)

Label(frame, text = 'value:').grid(row = 2, column = 0)
Label(frame, text = 'result:').grid(row = 2, column = 1)
value = Entry(frame, width = 15, justify = CENTER)
value.grid(row = 3, column = 0)
label = Label(frame, text = '', width = 15, bd = 1, relief = SUNKEN)
label.grid(row = 3, column = 1)
Button(frame, text = 'convert', command = lambda: cambio(fc.get(),tc.get(),value.get())).grid(row = 4, column = 0, columnspan = 2, pady = 10)

frame.mainloop()