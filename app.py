from flask import Flask, render_template, request, redirect, url_for, session
import random as rd
import os

app = Flask(__name__)

USERS_FILE = "./BD/usuarios.txt"
app.secret_key = os.urandom(24)


curiosidades_basquete = [
    "1. Inventor do basquete: O basquete foi inventado por James Naismith, um professor de educação física canadense, em dezembro de 1891, para manter seus alunos ativos durante o inverno.",
    "2. Primeiro jogo de basquete: O primeiro jogo de basquete foi jogado com uma bola de futebol e duas cestas de pêssego vazias como “cestas”.",
    "3. Altura média dos jogadores: A altura média de um jogador de basquete da NBA é cerca de 2 metros (6 pés 7 polegadas), mas os jogadores podem variar muito, com alguns com menos de 1,80m.",
    "4. Primeiro time feminino de basquete: O primeiro time feminino de basquete foi formado em 1893 em Massachusetts, apenas dois anos após a invenção do jogo.",
    "5. A origem das cestas: As cestas de basquete eram originalmente cestas de pêssego, e os jogadores precisavam de uma escada para pegar a bola de dentro depois de cada ponto.",
    "6. A NBA foi criada em 1946: A National Basketball Association (NBA) foi formada em 1946 como a Basketball Association of America (BAA) antes de se fundir com a National Basketball League (NBL) em 1949.",
    "7. O 'airball': Quando um jogador arremessa a bola e ela não acerta nem o aro nem a tabela, isso é chamado de “airball”, ou 'bola no ar'.",
    "8. Maior pontuação em um jogo da NBA: O maior número de pontos já marcados por um único jogador em um jogo da NBA é 100, feito por Wilt Chamberlain em 1962.",
    "9. O basquete na Olimpíada: O basquete foi incluído nos Jogos Olímpicos pela primeira vez em 1936, durante os Jogos de Berlim.",
    "10. O 'triple-double': Um 'triple-double' é quando um jogador registra dois dígitos (10 ou mais) em três categorias estatísticas diferentes, como pontos, assistências e rebotes, em um único jogo.",
    "11. A linha de três pontos: A linha de três pontos foi introduzida na NBA em 1979 e deu uma nova dimensão ao jogo, permitindo que os jogadores marcassem de fora da área.",
    "12. Primeiro jogador a ganhar o MVP de todas as temporadas: LeBron James é um dos poucos jogadores a ganhar o prêmio de MVP da temporada regular em múltiplos times, com o Cleveland Cavaliers e o Miami Heat.",
    "13. A origem do termo 'slam dunk': O termo 'slam dunk' foi popularizado nos anos 1970, mas a técnica de 'enterrar' a bola (dunk) já era praticada desde os primórdios do basquete.",
    "14. A famosa camisa número 23: O número 23 é icônico no basquete, principalmente por causa de Michael Jordan, que usava essa camisa durante a maior parte de sua carreira.",
    "15. O basquete no espaço: Em 1997, astronautas americanos jogaram uma partida de basquete a bordo da estação espacial Mir. Eles usaram um minibasketball para fazer a atividade em microgravidade."
]

cores_fundo = [
    "#2C3E50",
    "#ECF0F1",
    "#1ABC9C",
    "#34495E",
    "#95A5A6",
    "#E74C3C",
    "#F39C12",
    "#8E44AD",
    "#3498DB",
    "#BDC3C7"
]

lista_imagens = [
    "imagem1.jpg",
    "imagem2.jpg",
    "imagem3.jpg"
]

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
    curiosidade = rd.choice(curiosidades_basquete)
    cor = rd.choice(cores_fundo)
    imagem = rd.choice(lista_imagens)

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
    curiosidade = rd.choice(curiosidades_basquete)
    cor = rd.choice(cores_fundo)
    imagem = rd.choice(lista_imagens)

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
    curiosidade = rd.choice(curiosidades_basquete)
    cor = rd.choice(cores_fundo)
    imagem = rd.choice(lista_imagens)

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