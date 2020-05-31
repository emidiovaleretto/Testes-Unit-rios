from detectlang import LangDetect

try:
    txt = LangDetect(None)
    print(txt.predict())
except AssertionError as e:
    print(f'Erro: {e}')