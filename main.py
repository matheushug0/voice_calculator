import time
import calc_with_voice as c
from colorama import Fore, Style, Back
import questionary as q
from tqdm import tqdm
import pyfiglet

def loading_title(title, description):
  print(pyfiglet.figlet_format(title, font="slant"))
  c.os_speaking(description)

def loading_animation(text):
    for _ in tqdm(range(10), desc=text, unit="ticks", colour="GREEN"):
        time.sleep(0.1)

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def print_colored_with_background(text, color, background):
    print(f"{color}{background}{text}{Style.RESET_ALL}")

def print_colored_with_background_and_bold(text, color, background):
    print(f"{color}{background}{Style.BRIGHT}{text}{Style.RESET_ALL}")
    
loading_animation("Carregando Dependências")
loading_title("Voice Calculator", "Bem-vindo ao Voice Calculêitor, uma calculadora de voz.")

while True:
  option = q.select(
    "Escolha uma opção:",
    choices=["Calcular com Voz", "Calcular pelo Terminal", "Sair"]
  ).ask()
  if option == "Calcular com Voz":
    c.voice_calculator()
  if option == "Sair":
    break