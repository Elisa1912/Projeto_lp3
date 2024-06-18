from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

app = Flask("Minha App") # nome da minha aplicação/projeto - pode ser qualquer coisa
cpf = CPF()
cnpj = CNPJ()
# página do flask: rota + função

# /home page - página inicial
@app.route("/")
def home():
    return render_template("home.html")

# /contato - página de contato
@app.route("/contato")
def cont():
    return render_template ("contato.html")

# /produtos - página de produtos
@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome": "Coca-cola", "descricao": "Mata a sede"},
        {"nome": "Doritos", "descricao": "Suja a mão"},
        {"nome": "Chocolate", "descricao": "Da diabetes"}
    ]
    return render_template ("produto.html", produtos=lista_produtos)

# /produtos - página de produtos
@app.route("/servicos")
def service():
    return "<h1>Nossos Serviços<h1>"

# /produtos - página de produtos
@app.route("/gerar-cpf")
def gcpf():
    return cpf.generate(True)
# /produtos - página de produtos
@app.route("/gerar-cnpj")
def gcnpj():
    return cnpj.generate(True)
app.run()