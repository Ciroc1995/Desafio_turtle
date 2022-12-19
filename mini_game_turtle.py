from turtle import Turtle

t = Turtle()
t.speed(1)
while True:
    direcao = input('Para onde deseja movimentar a tartaruga? Selecione "f" para frente ou "t" para trás ')
    if direcao == 'f':
        distancia = int(input('Quantos pixels deseja movimentar a tartaruga? '))
        rotacao = input('Para que lado deseja rotacionar a tartaruga? Selecione "e" para esquerda ou "d" para direita ')
        if rotacao == 'e':
            angulo = int(input("Deseja rotacionar a tartaruga em quantos graus para esquerda? "))
            t.left(angulo)
        elif rotacao == 'd':
            angulo = int(input("Deseja rotacionar a tartaruga em quantos graus para direita? "))
            t.right(angulo)
        t.forward(distancia)
    elif direcao == 't':
        distancia = int(input('Quantos pixels deseja movimentar a tartaruga? '))
        rotacao = input('Para que lado deseja rotacionar a tartaruga? Selecione "e" para esquerda ou "d" para direita ')
        if rotacao == 'e':
            angulo = int(input("Deseja rotacionar a tartaruga em quantos graus para esquerda? "))
            t.left(angulo)
        elif rotacao == 'd':
            angulo = int(input("Deseja rotacionar a tartaruga em quantos graus para direita? "))
            t.right(angulo)
        t.backward(distancia)
    resposta = input('Deseja continuar andando? "s/sim" ou "n/não" ')
    if resposta == 's':
        continue
    else:
        break
