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

    if not os.path.exists('sound/verification/correto.wav'):
        return False

    if not os.path.exists('sound/verification/errado.wav'):
        return False

    if not os.path.exists('sound/verification/jogo.wav'):
        return False

    if not os.path.exists('sound/verification/aprender.wav'):
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

    if not os.path.exists('sound/verification'):
        os.makedirs('sound/verification')

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

    mp3_correto = 'sound/verification/Correto.mp3'
    wav_correto = 'sound/verification/Correto.wav'

    mp3_errado = 'sound/verification/Correto.mp3'
    wav_errado = 'sound/verification/Correto.wav'

    tts = gTTS('Muito bem', lang='pt-br')
    tts.save(mp3_correto)

    tts = gTTS('Você errou, tente novamente ou aperte enter para pular de palavra', lang='pt-br')
    tts.save(mp3_errado)

    subprocess.call(['ffmpeg', '-y', '-i', mp3_correto, wav_correto], stdout=devnull, stderr=devnull)
    subprocess.call(['ffmpeg', '-y', '-i', mp3_errado, wav_errado], stdout=devnull, stderr=devnull)

    mp3_aprender = 'sound/verification/aprender.mp3'
    wav_aprender = 'sound/verification/aprender.wav'

    mp3_jogo = 'sound/verification/jogo.mp3'
    wav_jogo = 'sound/verification/jogo.wav'

    tts = gTTS('Modo de aprendizado', lang='pt-br')
    tts.save(mp3_aprender)

    tts = gTTS('Modo jogo', lang='pt-br')
    tts.save(mp3_jogo)

    subprocess.call(['ffmpeg', '-y', '-i', mp3_aprender, wav_aprender], stdout=devnull, stderr=devnull)
    subprocess.call(['ffmpeg', '-y', '-i', mp3_jogo, wav_jogo], stdout=devnull, stderr=devnull)

    if os.path.exists(mp3_intro):
        os.remove(mp3_intro)

    if os.path.exists(mp3_correto):
        os.remove(mp3_correto)

    if os.path.exists(mp3_jogo):
        os.remove(mp3_jogo)

    if os.path.exists(mp3_aprender):
        os.remove(mp3_aprender)

    if os.path.exists(mp3_errado):
        os.remove(mp3_errado)

    print('Finalizado.')
