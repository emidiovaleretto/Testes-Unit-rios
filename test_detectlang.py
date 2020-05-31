import unittest
from detectlang import LangDetect


class TestDetectLang(unittest.TestCase):

    def test_predict_texto_em_ingles_deve_retornar_en(self):
        lang_detect = LangDetect('The book is on the table')
        self.assertEqual(lang_detect.predict(), 'en')

    def test_predict_texto_em_espanhol_deve_retornar_es(self):
        lang_detect = LangDetect('Aquí puedes acceder a una serie de textos en español')
        self.assertEqual(lang_detect.predict(), 'es')

    def test_predict_verifica_varios_textos_diferentes(self):

        txt_lang = (
            ("Ispirato a un'antica leggenda popolare cinese.", 'it'),
            ('Das ist die Hauptstadt von Frankreich.', 'de'),
            ('Notre outil de constitution de vocabulaire vous permet.', 'fr'),
            ('Esse texto está em português.', 'pt'),
            ('Het leren van de Nederlandse taal gaat goed.', 'nl'),
        )

        for txt_lang in txt_lang:
            with self.subTest(txt_lang=txt_lang):
                txt, lang = txt_lang
                lang_detect = LangDetect(txt)
                self.assertEqual(lang_detect.predict(), lang)

    def test_predict_parametro_nao_e_str_e_deve_retornar_um_assertionerror(self):
        with self.assertRaises(AssertionError):
            lang_detect = LangDetect(2)
            lang_detect.predict()

    def test_predict_parametro_contem_erro_de_gramatica(self):
        lang_detect = LangDetect("Fal a galerina tud o bem com oces?")
        self.assertEqual(lang_detect.predict(), 'pt')

    # BIBLIOTECA TEM PROBLEMAS INTERPRETANDO MAIS DE UM IDIOMA
    def test_predict_parametro_contem_mais_de_um_idioma_com_mais_palavras_em_ingles(self):
        lang_detect = LangDetect("What up guys tudo bom?")
        self.assertEqual(lang_detect.predict(), 'en')

    # BIBLIOTECA TEM PROBLEMAS INTERPRETANDO MAIS DE UM IDIOMA
    def test_predict_parametro_contem_mais_de_um_idioma_com_mais_palavras_em_portugues(self):  
        lang_detect = LangDetect("Fala galera vamos pro Code Review today?") 
        self.assertEqual(lang_detect.predict(), 'es')

unittest.main()
