import tkinter as tk
import pygame
import os

root = tk.Tk()
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
pygame.mixer.music.load('/assets/ogg/main_menu.ogg')
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((640, 360))

def pygame_loop():
    screen.fill((0, 25, 0))
    pygame.display.flip()
    root.after(20, pygame_loop)

pygame_loop()
root.mainloop()
