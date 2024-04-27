import os

import pygame
import requests

api_key = "a563b92d-f3ea-46f8-9428-619a2d6f74cf"
map_request = f"https://static-maps.yandex.ru/1.x/?ll=37.617635,55.755814&z=11&size=450,450&l=map&pt=37.500379,55.801243,pm2rdm~37.559379,55.791243,pm2rdm~37.549354,55.713248,pm2rdm~55.81782,37.439194"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((450, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)