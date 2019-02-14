import setup
from pynput import keyboard
import simpleaudio as sa


def main():

    if not setup.check_files():
        setup.generate_files()

    print('Teclado iniciado')

    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


def on_press(key):

    try:
        play_async('sound/keys/{}.wav'.format(str.upper(key.char)))

    except AttributeError as error:
        pass


def play_async(file):
    sa.stop_all()
    wave_obj = sa.WaveObject.from_wave_file(file)
    wave_obj.play()


if __name__ == '__main__':
    main()
