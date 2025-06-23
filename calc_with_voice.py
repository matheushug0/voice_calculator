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

expression = speech.listen_and_convert()
result = calc.calculator([expression])
print(f"Resultado do cálculo (calculadora.py): {result}")
response = client.models.generate_content(model="gemini-2.0-flash", contents=f"""
    Gerei este resultado: {"".join(result)}, a partir da seguinte expressão matemática em Python: {expression}.
    Gere imediatamente um um texto curto para ser lido em voz alta pela aplicaçao, por exemplo 'O resultado da raiz quadrada de 49 somado a três vezes a diferença entre cinco e dois é vinte e quatro.'. Somente me gere o texto e ignore qualquer erro.
    """)
print(response.text)
os.system(f'espeak-ng -v pt-br -s 150 "{response.text}"')
calc.save_results([result])