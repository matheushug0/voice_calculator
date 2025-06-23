import speech_recogn_calc as speech
import calculator as calc
import pyttsx3
import os
import configs
from google import genai

client = genai.Client(api_key=configs.get_api_key())

def speak_result(result):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[95].id)
  engine.setProperty('rate', 120)
  engine.setProperty('volume', 1.0)
  engine.say(result)
  engine.runAndWait()

def os_speaking(text):
  os.system(f'espeak-ng -v pt-br -s 150 "{text}"')

def voice_calculator():
  expression = speech.listen_and_convert()
  result = calc.calculator([expression])
  try:
    response = client.models.generate_content(model="gemini-2.0-flash", contents=f"""
    Gerei este resultado: {"".join(result)}, a partir da seguinte expressão matemática em Python: {expression}.
    Gere imediatamente um um texto curto para ser lido em voz alta pela aplicaçao, por exemplo 'O resultado da raiz quadrada de 49 somado a três vezes a diferença entre cinco e dois é vinte e quatro.'. Somente me gere o texto e ignore qualquer erro.
    """)
  except Exception:
    response = "Desculpe, meus processadores estã sobrecarregados. Tente novamente."
    print(rf"""
       [⚠ ERRO DETECTADO ⚠]
              ______
           .-'      '-.
          /            \
         |   X      X   |
         |     .--.     |
         |   | ==== |   |
         |   | ==== |   |
         |   | ==== |   |
          \   `.__.'   /
           '-.______.-'
{response}
    """)
    os_speaking(response)
    return
  print(rf"""
              ______
           .-'      '-.
          /            \
         |              |
         |,  .-.  .-.  ,|
         | )(_o/  \o_)( |
         |/     /\     \|
         (_     ^^     _)
          \__|IIIIII|__/
           | \IIIIII/ |
           \          /
            `--------`
{response.text}
""")
  os_speaking(response.text)
  calc.save_results([result])