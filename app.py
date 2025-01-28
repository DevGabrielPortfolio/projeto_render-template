from flask import Flask, render_template
import random as rd
import os

app = Flask(__name__)

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

@app.route('/')
def primeiroweb():

    #escolhendo curiosidade
    curiosidade = rd.choice(curiosidades_basquete)

    # CRIANDO UMA ROTA
    pasta_imagens = os.path.join(app.static_folder, 'images')
    # Lista as imagens na pasta
    imagens = [img for img in os.listdir(pasta_imagens) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    # Escolhe uma imagem aleatória
    imagem_aleatoria = rd.choice(imagens)
    # Retorna para o template, passando o nome da imagem aleatória
    return render_template('index.html', imagem=imagem_aleatoria, texto_curiosidade=curiosidade)

@app.route('/sobre')
def sobre():
    # Você pode passar algumas informações para o template sobre a página "SOBRE".
    return render_template('sobre.html')


# Executa o app
if __name__ == '__main__':
    app.run(debug=True)
