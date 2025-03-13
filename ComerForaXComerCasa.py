# Importando biblioteca
from sklearn.linear_model import Perceptron

# Dados de entrada
X = [[0,1,1,1], [1,0,1,1], [1,1,0,1], [0,0,1,0], [1,1,1,1],[0,1,0,0],[1,0,0,1],[0,0,0,1]]

# Saídas desejadas
Y = [0,1,0,1,1,0,0,0]

# Criando e treinando o perceptron
modelo = Perceptron()
modelo.fit(X, Y)

# Testando o modelo
print("Previsões:")
testes =  [[0,1,1,1], [1,0,1,1], [1,1,0,1], [0,0,1,0], [1,1,1,1],[0,1,0,0],[1,0,0,1],[0,0,0,1]]
for teste in testes:
  previsao = modelo.predict([teste])
  print(f"Cansado do trabalho: {teste[0]}, Dispõe de ingredientes em casa : {teste[1]}, Restaurante próximo aberto: {teste[2]}, Dia de pagamento recente: {teste[3]} => Comer fora ou comer em casa? {'Sim' if previsao[0] == 1 else 'Não'}")
