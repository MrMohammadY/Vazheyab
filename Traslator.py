from googletrans import Translator, LANGUAGES

Translate = Translator()


def languages():
    """
    create a list of code languages and languages like (en : english)
    :return:
    """
    for lan, cod in LANGUAGES.items():
        print(f'{lan}: {cod} |')


def translator_text(text, destination):
    """
    translate text
    :param text: text to translate
    :param destination: destination translate
    :return: result
    """
    result = Translate.translate(text, destination)
    print(f'Your Text: {text}\n'
          f'Translate Text: {result.text}\n'
          f'From {result.src} To {result.dest}')


def translator_file(file, destination):
    """
    take file and translate that
    :param file: address file
    :param destination: destination to translate
    :return:
    """
    with open(file, 'r') as f:
        text = f.read()
        result = Translate.translate(text, destination)
        print(f'Your Text: {text}\n'
              f'Translate Text: {result.text}\n'
              f'From {result.src} To {result.dest}')
