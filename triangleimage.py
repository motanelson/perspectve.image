import pygame

# Inicializar o Pygame
pygame.init()

# Configuração da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Imagem em Triângulos com Pontos")

# Cores
BLACK = (0, 0, 0)

# Carregar a imagem
image_path = "imagem.png"  # Substitua pelo caminho do seu arquivo PNG
image = pygame.image.load(image_path).convert_alpha()
image = pygame.transform.scale(image, (400, 600))  # Redimensionar para 400x600
image_width = image.get_width()
image_height = image.get_height()

# Função para desenhar a imagem em triângulos com pontos
def draw_triangles_with_points(screen, image):
    half_width = screen_width // 2
    for x in range(half_width):
        left_height = int(screen_height * (x / half_width))
        right_height = int(screen_height * ((half_width - x) / half_width))

        # Parte esquerda do triângulo (encolhendo)
        for y in range(left_height):
            scaled_y = int(y / (left_height + 1) * image_height)
            color = image.get_at((int(x / half_width * image_width), scaled_y))
            screen.set_at((half_width + x, (screen_height - left_height) // 2 + y), color)

        # Parte direita do triângulo (encolhendo)
        for y in range(right_height):
            scaled_y = int(y / (right_height + 1) * image_height)
            color = image.get_at((int(( x / half_width) * image_width), scaled_y))
            screen.set_at(( x, (screen_height - right_height) // 2 + y), color)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher o fundo
    screen.fill(BLACK)

    # Desenhar os triângulos com pontos
    draw_triangles_with_points(screen, image)

    # Atualizar a tela
    pygame.display.flip()

# Sair do Pygame
pygame.quit()

