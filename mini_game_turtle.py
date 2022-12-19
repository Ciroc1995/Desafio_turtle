from turtle import Turtle

t = Turtle()
t.speed(1)

def obter_distancia():
    resposta = int(input('Quantos pixels deseja movimentar a tartaruga? '))
    return resposta

def rotacionar_turtle(turtle):
    rotacao = input('Para que lado deseja rotacionar a tartaruga? Selecione "e" para esquerda ou "d" para direita ')
    if rotacao == 'e':
        rotacionar_para_esquerda(t)
    elif rotacao == 'd':
        rotacionar_para_direita(t)

def rotacionar_para_esquerda(turtle):
    angulo = int(input("Deseja rotacionar a tartaruga em quantos graus para esquerda? "))
    t.left(angulo)

def rotacionar_para_direita(turtle):
    angulo = int(input("Deseja rotacionar a tartaruga em quantos graus para direita? "))
    t.right(angulo)

while True:
    direcao = input('Para onde deseja movimentar a tartaruga? Selecione "f" para frente ou "t" para trás ')
    if direcao == 'f':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)
    if direcao == 't':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distancia)
    resposta = input('Deseja continuar andando? "s/sim" ou "n/não" ')
    if resposta == 's':
        continue
    else:
        break
