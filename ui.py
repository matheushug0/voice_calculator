from tqdm import tqdm
from colorama import Fore, Style
import time
import calc_with_voice as cv
import pyfiglet

def loading_animation(text, range_loading, color):
  for _ in tqdm(range(range_loading), desc=text, unit="ticks", colour=color):
    time.sleep(0.1)
    
def print_colored_green(text):
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")

def print_colored_yellow(text):
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")
    
def print_colored_red(text):
    print(f"{Fore.RED}{text}{Style.RESET_ALL}")
    
def loading_title(title, description):
  print(pyfiglet.figlet_format(title, font="slant"))
  print_colored_yellow(description)
  cv.os_speaking(description)