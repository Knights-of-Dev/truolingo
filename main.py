import tkinter as tk
import pygame
import os
import sys

def fullpath(dire: str, filename: str):
    a = os.path.join(dire, filename)
    assert os.path.isfile(a), f"File not found at {dire}"
    return a

def close():
    pygame.mixer.music.stop()
    pygame.quit()
    root.destroy()
    sys.exit()

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW', close)
root.title("truolingo")
embed = tk.Frame(root, width=640, height=360)
embed.pack()
root.resizable(False, False)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

try:
    root.iconbitmap("icon.ico")
except Exception as e:
    print(f"uh oh: {e}")

root.update()

pygame.init()
screen = pygame.display.set_mode((640, 360))

class Loadspinner(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.or_image = pygame.image.load(fullpath('assets/image', 'spinner.bmp')).convert()
        self.image = self.or_image
        self.rect = self.image.get_rect(center=position)
        self.angle = 0

    def update(self):
        self.angle += 7
        self.angle %= 360
        self.rotate()

    def rotate(self):
        self.image = pygame.transform.rotate(self.or_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

all_sprites = pygame.sprite.Group()
spinner = Loadspinner((100, 100))
all_sprites.add(spinner)

status = 'loading_init'

def pygame_loop():
    global status
    screen.fill((0, 0, 0))
    match status:
        case 'loading_init':
            pygame.mixer.music.load(fullpath('assets/ogg', 'main_menu.ogg'))
            pygame.mixer.music.play(-1)
            spinner = Loadspinner((100, 100))
            all_sprites.add(spinner)
            status = 'loading'
        case 'loading':
            spinner.update()
        case _:
            pass
    all_sprites.draw(screen)
    pygame.display.flip()
    root.after(20, pygame_loop)

running = True

pygame_loop()
root.mainloop()
