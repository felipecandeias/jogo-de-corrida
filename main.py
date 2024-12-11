import pygame
import random

# Inicialização do Pygame
pygame.init()

# Dimensões da janela
LARGURA = 800
ALTURA = 600

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurações da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Corrida")
clock = pygame.time.Clock()

# Classe do carro do jogador
class CarroJogador:
    def __init__(self):
        self.largura = 50
        self.altura = 100
        self.x = LARGURA // 2 - self.largura // 2
        self.y = ALTURA - self.altura - 20
        self.velocidade = 5

    def desenhar(self):
        pygame.draw.rect(tela, AZUL, (self.x, self.y, self.largura, self.altura))

    def mover(self, direcao):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.velocidade
        if direcao == "direita" and self.x < LARGURA - self.largura:
            self.x += self.velocidade

# Classe dos obstáculos
class Obstaculo:
    def __init__(self):
        self.largura = 50
        self.altura = 100
        self.x = random.randint(0, LARGURA - self.largura)
        self.y = -self.altura
        self.velocidade = 7

    def desenhar(self):
        pygame.draw.rect(tela, VERMELHO, (self.x, self.y, self.largura, self.altura))

    def mover(self):
        self.y += self.velocidade

# Função principal
def jogo():
    rodando = True
    jogador = CarroJogador()
    obstaculos = []
    pontuacao = 0

    while rodando:
        tela.fill(BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentação do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jogador.mover("esquerda")
        if teclas[pygame.K_RIGHT]:
            jogador.mover("direita")

        # Gerar obstáculos
        if random.randint(1, 50) == 1:
            obstaculos.append(Obstaculo())

        # Atualizar obstáculos
        for obstaculo in obstaculos[:]:
            obstaculo.mover()
            obstaculo.desenhar()

            # Verificar colisão
            if (
                jogador.x < obstaculo.x + obstaculo.largura and
                jogador.x + jogador.largura > obstaculo.x and
                jogador.y < obstaculo.y + obstaculo.altura and
                jogador.y + jogador.altura > obstaculo.y
            ):
                print("Game Over! Pontuação:", pontuacao)
                rodando = False

            # Remover obstáculos fora da tela
            if obstaculo.y > ALTURA:
                obstaculos.remove(obstaculo)
                pontuacao += 1

        # Desenhar o jogador
        jogador.desenhar()

        # Exibir pontuação
        fonte = pygame.font.SysFont(None, 36)
        texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, PRETO)
        tela.blit(texto_pontuacao, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Executar o jogo
jogo()