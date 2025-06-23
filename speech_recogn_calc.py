import speech_recognition as sr

def listen_and_convert():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='pt-BR')
            print("Texto falado:", text)
            text = text_filter(text)
            print("Texto falado após formatação:", text)
            return text
        except:
            print("Sorry, I didn't catch that.")
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