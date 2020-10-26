from Traslator import translator_text, languages
from Wordfinder import send_requests
from time import sleep
from config import db_names


def trans():
    """
    take destination and text and send to func
    :return:
    """
    des = input('please enter destination for translate\n'
                'like en(english) or fa(persian) or ar(arabic)\n'
                'if you want see list language press (0): ')
    if des == '0':
        languages()
        return trans()

    text = input('please enter your text for translate: ')

    print(f'\n{"#" * 30}\n')
    translator_text(text, des)
    print(f'\n{"#" * 30}')


def word():
    """
    take database name and text and send to func
    :return:
    """
    db = input('please enter db name \n'
               'and if you want see list of db name press (0): ').strip()
    if db == '0':
        for n in db_names:
            print(n)
            sleep(0.5)
        return word()

    text = input('please enter your text for translate: ')

    print(f'\n{"#"*30}\n')
    print(f'Your Text: {text}\n'
          f'DB Name: {db}\n'
          f'Result: {send_requests(text, db)}')
    print(f'\n{"#" * 30}')


def run():
    print(f'1.Translate with google translator\n'
          f'2. Word finder with Vazheyab\n')

    choice = input('Press Yur Choice(1/2): ').strip()

    if choice == '1':
        trans()

    if choice == '2':
        word()


if __name__ == '__main__':
    run()
