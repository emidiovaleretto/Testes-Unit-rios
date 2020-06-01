from dataclasses import dataclass
from langdetect import detect


@dataclass
class LangDetect:

    text: str

    def predict(self):
        """
        Função verifica se o parâmetro texto é do tipo String.

        >>> lang_detect = LangDetect('“I’m young, rich, beautiful, and famous. People think rich people are happy.“')
        >>> lang_detect.predict()
        'en'

        >>> lang_detect = LangDetect('La navicella è entrata in orbita e viaggia verso la Stazione spaziale internazionale')
        >>> lang_detect.predict()
        'it'

        >>> lang_detect = LangDetect('Dois ou um')
        >>> lang_detect.predict()
        'pt'

        """

        assert isinstance(self.text, str), 'O valor digitado não pode ser de outro tipo, exceto String.'
        return detect(self.text)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
