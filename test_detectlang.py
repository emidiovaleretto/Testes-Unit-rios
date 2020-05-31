import unittest
from detectlang import LangDetect


class TestDetectLang(unittest.TestCase):

    def test_predict_texto_em_ingles_deve_retornar_en(self):
        txt = LangDetect('The book is on the table')
        self.assertEqual(txt.predict(), 'en')

    def test_predict_texto_em_espanhol_deve_retornar_es(self):
        txt = LangDetect('Aquí puedes acceder a una serie de textos en español')
        self.assertEqual(txt.predict(), 'es')

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
                txt2 = LangDetect(txt)
                self.assertEqual(txt2.predict(), lang)

    def test_predict_parametro_nao_e_str_e_deve_retornar_um_assertionerror(self):
        with self.assertRaises(AssertionError):
            num = LangDetect(2)
            num.predict()


unittest.main()
