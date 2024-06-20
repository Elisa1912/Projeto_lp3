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
    return render_template ("produtos.html", produtos=lista_produtos)

# /produtos - página de produtos
@app.route("/servicos")
def service():
    return "<h1>Nossos Serviços</h1>"

# /produtos - página de produtos
@app.route("/cpf")
def gerarcpf():
    envio = cpf.generate(True)
    return render_template("cpf.html", cpf =envio)

# /produtos - página de produtos
@app.route("/cnpj")
def gcnpj():
    envio = cnpj.generate(True)
    return render_template("cnpj.html", cnpj =envio)

@app.route("/TermoU")
def TermoU():
    return render_template ("TermoU.html")

@app.route("/politica_P")
def politica_P():
    return render_template ("politica_P.html")

@app.route("/como_utilizar")
def ComoUtilizar():
    return render_template ("como_utilizar.html")

app.run()
