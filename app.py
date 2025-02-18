from flask import Flask, render_template, request, redirect, url_for, session
import random as rd
import os
from DATA import listas_configuracao

app = Flask(__name__)

USERS_FILE = "./BD/usuarios.txt"
app.secret_key = os.urandom(24)


frasesCadastro = []
coresCadastro = []


# Função para salvar usuário
def save_user(nome):
    with open(USERS_FILE, "a") as file:
        file.write(nome + "\n")

# Função para verificar se o usuário existe
def user_exists(nome):
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            users = file.readlines()
            return nome + "\n" in users
    return False

@app.route('/')
def paginaCadastro():
    return render_template('cadastro-usuario.html')

@app.route('/cadastroUser', methods=['POST'])
def cadastroUser():
    # Escolhendo curiosidade, cor e imagem
    curiosidade = rd.choice(listas_configuracao.curiosidades_basquete)
    cor = rd.choice(listas_configuracao.cores_fundo)
    imagem = rd.choice(listas_configuracao.lista_imagens)

    nome = request.form['nome']
    if not user_exists(nome):
        save_user(nome)
        # Armazenando o nome do usuário na sessão
        session['nome'] = nome
        return redirect('/curiosidades')
    else:
        return f"Nome já existe! <a href='/'>Voltar</a>"

@app.route('/login', methods=['POST'])
def login():
    # Escolhendo curiosidade, cor e imagem
    curiosidade = rd.choice(listas_configuracao.curiosidades_basquete)
    cor = rd.choice(listas_configuracao.cores_fundo)
    imagem = rd.choice(listas_configuracao.lista_imagens)

    nome = request.form['nome']
    if user_exists(nome):
        # Armazenando o nome do usuário na sessão
        session['nome'] = nome
        return redirect('/curiosidades')
    else:
        return f"Usuário não encontrado! <a href='/'>Voltar</a>"

@app.route('/curiosidades')
def primeiroweb():
    # Verificando se o usuário está logado
    if 'nome' not in session:
        return redirect('/')  # Redireciona para a página de login/cadastro

    # Escolhendo curiosidade, cor e imagem
    curiosidade = rd.choice(listas_configuracao.curiosidades_basquete)
    cor = rd.choice(listas_configuracao.cores_fundo)
    imagem = rd.choice(listas_configuracao.lista_imagens)

    # Pegando o nome da sessão
    nome = session['nome']  
    return render_template('index.html', texto_curiosidade=curiosidade, imagem=imagem, cor_fundo=cor, boasVindas=f"Seja bem-vindo(a) {nome}")

@app.route('/logout')
def logout():
    # Remover o nome do usuário da sessão
    session.pop('nome', None)
    return redirect('/')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', itens=frasesCadastro)

@app.route('/receber', methods=['POST'])
def receber():
    frase = request.form['nome']
    if(frase.lower() == 'clear'):
        frasesCadastro.clear()
    else:
        frasesCadastro.append(frase)

    return redirect(url_for('cadastro'))

@app.route('/cadastroCor')
def cadastroCor():
    return render_template('cadastro-cor.html', itens=coresCadastro)

@app.route('/receberCor', methods=['POST'])
def receberCor():
    corNome = request.form['nomeCor']
    if(corNome.lower() == 'clear'):
        coresCadastro.clear()
    else:
        coresCadastro.append(corNome)
        

    return redirect(url_for('cadastroCor'))


@app.route('/excluirCor/<cor>', methods=['POST'])
def excluirCor(cor):
    if cor in coresCadastro:
        coresCadastro.remove(cor)
    return redirect(url_for('cadastroCor'))

# Executa o app
if __name__ == '__main__':
    app.run(debug=True)