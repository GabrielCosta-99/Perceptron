# Importando biblioteca
from sklearn.linear_model import Perceptron

# Dados de entrada
X = [[0,0,0], [0,1,0], [1,0,0], [1,1,0], [0,0,1],[0,1,1],[1,0,1],[1,1,1]]

# Saídas desejadas
Y = [0,1,1,1,0,0,0,0]

# Criando e treinando o perceptron
modelo = Perceptron()
modelo.fit(X, Y)

# Testando o modelo
print("Previsões:")
testes =  [[0,0,0], [0,1,0], [1,0,0], [1, 1,0], [0,0,1],[0,1,1],[1,0,1],[1,1,1]]
for teste in testes:
  previsao = modelo.predict([teste])
  print(f"Tempo insolarado: {teste[0]}, Dia da semana: {teste[1]}, Parque lotado: {teste[2]} => Ir ao parque? {'Sim' if previsao[0] == 1 else 'Não'}")
