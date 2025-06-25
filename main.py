import calc_with_voice as cv
import calc_with_txt as ct
import questionary as q
import ui
    
ui.loading_animation("Carregando Dependências", 10, "BLUE")
ui.loading_title("Voice Calculator", "Bem-vindo ao Voice Calculêitor, uma calculadora de voz.")

while True:
  option = q.select(
    "Escolha uma opção:",
    choices=["Calcular com Voz", "Calcular Arquivo de Texto (.txt)", "Sair", " "]
  ).ask()
  if option == "Calcular com Voz":
    cv.voice_calculator()
  if option == "Calcular Arquivo de Texto (.txt)":
    ct.txt_calculator()
  if option == "Sair":
    break
  if option == " ":
    cv.get_bitcoin_price()