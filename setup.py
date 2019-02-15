import os
import words as word
import subprocess
from gtts import gTTS


def check_files():

    words = word.word

    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for c in chars:

        wav_path = 'sound/keys/{}.wav'.format(c)

        if not os.path.exists(wav_path):
            return False

    for c in words:

        wav_path = 'sound/words/{}.wav'.format(c)

        if not os.path.exists(wav_path):
            return False

    if not os.path.exists('sound/phrases/Bem_vindo.wav'):
        return False

    return True


def generate_files():

    if not os.path.exists('sound'):
        os.makedirs('sound')

    if not os.path.exists('sound/keys'):
        os.makedirs('sound/keys')

    if not os.path.exists('sound/phrases'):
        os.makedirs('sound/phrases')

    if not os.path.exists('sound/words'):
        os.makedirs('sound/words')

    words = word.word

    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    devnull = open(os.devnull, 'w')

    for index, c in enumerate(chars):

        print('Gerando arquivos de letras. {}/26'.format(index), end='\r')

        mp3_path = 'sound/keys/{}.mp3'.format(c)
        wav_path = 'sound/keys/{}.wav'.format(c)

        tts = gTTS(text=c, lang='pt-br')
        tts.save(mp3_path)

        subprocess.call(['ffmpeg', '-y', '-i', mp3_path, wav_path], stdout=devnull, stderr=devnull)

        if os.path.exists(mp3_path):
            os.remove(mp3_path)

    for index, c in enumerate(words):

        print('Gerando arquivos de palavras. {}/{}'.format(index, len(words)), end='\r')

        mp3_path = 'sound/words/{}.mp3'.format(c)
        wav_path = 'sound/words/{}.wav'.format(c)

        tts = gTTS(text=c, lang='pt-br')
        tts.save(mp3_path)

        subprocess.call(['ffmpeg', '-y', '-i', mp3_path, wav_path], stdout=devnull, stderr=devnull)

        if os.path.exists(mp3_path):
            os.remove(mp3_path)

    mp3_intro = 'sound/phrases/Bem_vindo.mp3'
    wav_intro = 'sound/phrases/Bem_vindo.wav'

    tts = gTTS('bem vindo, teclado iniciado, aperte alguma tecla para ouvir a letra', lang='pt-br')
    tts.save(mp3_intro)

    subprocess.call(['ffmpeg', '-y', '-i', mp3_intro, wav_intro], stdout=devnull, stderr=devnull)


    if os.path.exists(mp3_intro):
        os.remove(mp3_intro)

    print('Finalizado.')
