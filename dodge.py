import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎯 공 피하기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 플레이어 설정
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 100
player_speed = 7

# 장애물 설정
obstacle_size = 50
obstacles = []
obstacle_speed = 5
obstacle_spawn_time = 30  # 프레임 단위
frame_count = 0

# 점수
score = 0
font = pygame.font.Font(None, 36)

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 키보드 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # 장애물 생성
    frame_count += 1
    if frame_count % obstacle_spawn_time == 0:
        obstacle_x = random.randint(0, WIDTH - obstacle_size)
        obstacles.append([obstacle_x, 0])
    
    # 장애물 이동
    for obstacle in obstacles[:]:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)
            score += 1
    
    # 충돌 감지
    for obstacle in obstacles:
        if (player_x < obstacle[0] + obstacle_size and
            player_x + player_size > obstacle[0] and
            player_y < obstacle[1] + obstacle_size and
            player_y + player_size > obstacle[1]):
            print(f"💀 게임 오버! 최종 점수: {score}")
            running = False
    
    # 화면 그리기
    screen.fill(WHITE)
    
    # 플레이어 그리기
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    # 장애물 그리기
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))
    
    # 점수 표시
    score_text = font.render(f"점수: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
