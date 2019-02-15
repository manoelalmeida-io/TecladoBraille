import setup
import random
import text as word
from pynput import keyboard
import simpleaudio as sa

palavra = ''
mode = 0
words = word.word


def main():

    if not setup.check_files():
        setup.generate_files()

    print('Teclado iniciado')
    play_async('sound/phrases/Bem_vindo.wav')

    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


def on_press(key):

    global palavra
    global mode

    if mode == 0:
        learn(key)
    else:
        game(key)


def play_async(file):
    sa.stop_all()
    wave_obj = sa.WaveObject.from_wave_file(file)
    wave_obj.play()


def play(file):
    sa.stop_all()
    wave_obj = sa.WaveObject.from_wave_file(file)
    obj_play = wave_obj.play()
    obj_play.wait_done()


def game(key):

    global palavra
    global mode

    try:
        global words

        if key == keyboard.Key.space:
            mode = 0
            print('APRENDER')
            play_async('sound/phrases/modo_aprender.wav')

        if key == keyboard.Key.enter:
            if palavra == words[0]:
                print('correto!')
                play('sound/phrases/correto.wav')
                shuffle()
            else:
                if palavra == '':
                    shuffle()
                else:
                    print('errado')
                    print(words[0])
                    play_async('sound/phrases/incorreto.wav')
            palavra = ''

        if key == keyboard.Key.backspace:
            palavra = palavra[:-1]

        play_async('sound/keys/{}.wav'.format(str.upper(key.char)))
        palavra += key.char

    except AttributeError as error:
        pass
    except FileNotFoundError as e:
        pass


def shuffle():

    global words

    random.shuffle(words)
    print(words[0])
    play_async('sound/words/{}.wav'.format(words[0]))


def learn(key):

    global mode

    try:
        if key == keyboard.Key.space:
            mode = 1
            print('JOGAR')
            play('sound/phrases/modo_jogo.wav')
            shuffle()

        play_async('sound/keys/{}.wav'.format(str.upper(key.char)))

    except AttributeError as error:
        pass
    except FileNotFoundError as e:
        pass


if __name__ == '__main__':
    main()
