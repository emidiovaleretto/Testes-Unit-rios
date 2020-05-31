from langdetect import detect


class LangDetect:

    def __init__(self, text):
        self.text = text

    def predict(self):

        """Função verifica se o parâmetro texto é do tipo String.

            >>> detect('“yeah, I’m young, rich, beautiful, and famous. People think rich people are happy.“')
            'en'

            >>> detect('La navicella è entrata in orbita e viaggia verso la Stazione spaziale internazionale (Iss).')
            'it'

            >>> detect('Dois ou um')
            'pt'

            """

        assert isinstance(self.text, str), 'O valor digitado não pode ser de outro tipo, exceto String.'
        return detect(self.text)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
