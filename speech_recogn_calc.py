import speech_recognition as sr
import calc_with_voice as c
import ui

def listen_and_convert():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        ui.print_colored_green("Diga algo:")
        c.os_speaking("Diga algo:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='pt-BR')
            text = text_filter(text)
            ui.print_colored_yellow(text)
            return text
        except Exception:
            ui.print_colored_yellow("Não entendi o que você disse.")
            c.os_speaking("Desculpe, não entendi o que você disse.")
            return None

def text_filter(input):
    substitutions = {
        "abre parênteses": "(",
        "fecha parênteses": ")",
        "mais": "+",
        "menos": "-",
        "vezes": "*",
        "x": "*",
        "X": "*",
        "dividido por": "/",
        "raiz quadrada de": "math.sqrt(",
        "√": "math.sqrt(",
        "elevado ao quadrado": "**2",
        "elevado ao cubo": "**3"
    }
    for word, simbol in substitutions.items():
        input = input.replace(word, simbol)
    while input.count("math.sqrt(") > input.count(")"):
        input += ")"
    return input