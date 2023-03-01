import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if 'usd' in request.form:
		usd = float(request.form['usd'])
		brl = round(usd * reais, 2) # conversão fictícia para o exemplo
		return render_template('index.html', usd=usd, brl=brl) # Retorna o valor da taxa de câmbio como texto
	elif 'brl' in request.form:
		brl = float(request.form['brl'])
		usd = round(brl / reais, 2) # conversão fictícia para o exemplo
		return render_template('index.html', usd=usd, brl=brl) # Retorna o valor da taxa de câmbio como texto
	else:
		return render_template('index.html', usd=0.00, brl=0.00)

try:
	site = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
except:
	print("erro")
output = site.json()
reais = float(output['USD']['bid'])

app.run()