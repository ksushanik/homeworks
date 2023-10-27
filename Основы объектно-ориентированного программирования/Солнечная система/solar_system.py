import math
import pygame

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (165, 42, 42)
PURPLE = (128, 0, 128)

# Определение размеров экрана
WIDTH = 1000
HEIGHT = 860

# Определение класса планеты
class Planet:
    def __init__(self, name, radius, distance, color, angle_speed, description):
        self.name = name
        self.radius = radius
        self.distance = distance
        self.color = color
        self.angle = 0
        self.angle_speed = angle_speed
        self.description = description

    def update(self):
        self.angle += self.angle_speed

    def draw(self, screen):
        x = WIDTH // 2 + int(math.cos(math.radians(self.angle)) * self.distance)
        y = HEIGHT // 2 + int(math.sin(math.radians(self.angle)) * self.distance)
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

def display_info(screen, planet):
    font = pygame.font.Font(None, 36)
    text = font.render(planet.description, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
    screen.blit(text, text_rect)

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Создание планет
planets = [
    Planet("Sun", 50, 0, YELLOW, 0, "Солнце - звезда в центре Солнечной системы."),
    Planet("Mercury", 10, 100, GRAY, 1, "Меркурий - самая маленькая планета в Солнечной системе."),
    Planet("Venus", 15, 150, ORANGE, 0.8, "Венера известна своей плотной, токсичной атмосферой."),
    Planet("Earth", 20, 200, BLUE, 0.5, "Земля - единственная известная планета с жизнью."),
    Planet("Mars", 18, 250, RED, 0.4, "Марс часто называют 'Красной планетой'."),
    Planet("Jupiter", 30, 300, BROWN, 0.3, "Юпитер - крупнейшая планета в Солнечной системе."),
    Planet("Saturn", 25, 350, PURPLE, 0.2, "Сатурн известен своей характерной кольцевой системой."),
    Planet("Uranus", 22, 400, GREEN, 0.15, "Уран - газовый гигант с уникальной осью вращения.")
]

# Создание объекта часов для управления частотой кадров
clock = pygame.time.Clock()

# Счётчик дней Земли
earth_days = 0

# Счётчик оборотов Земли
earth_rotation_counter = 0

# Определение текстового объекта для отображения счётчика
font = pygame.font.Font(None, 36)
text_color = WHITE
text_x = 10
text_y = 10

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление планет
    for planet in planets:
        planet.update()

    # Увеличение счётчика оборотов Земли и дней
    earth_rotation_counter += planets[3].angle_speed  # Земля всегда четвёртая в списке
    if earth_rotation_counter >= 1:
        earth_days += 1
        earth_rotation_counter = 0

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка планет и информации
    for planet in planets:
        planet.draw(screen)

        # Проверка наведения мыши и отображение информации о планете
        planet_x = WIDTH // 2 + int(math.cos(math.radians(planet.angle)) * planet.distance)
        planet_y = HEIGHT // 2 + int(math.sin(math.radians(planet.angle)) * planet.distance)
        planet_rect = pygame.Rect(planet_x - planet.radius, planet_y - planet.radius, 2 * planet.radius, 2 * planet.radius)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if planet_rect.collidepoint(mouse_x, mouse_y):
            display_info(screen, planet)

    # Отображение счётчика дней Земли
    text = font.render(f"Earth Days: {earth_days}", True, text_color)
    screen.blit(text, (text_x, text_y))

    # Обновление экрана
    pygame.display.flip()

    # Управление частотой кадров
    clock.tick(60)

# Завершение игры
pygame.quit()
