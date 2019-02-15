import os
import text
import subprocess
from gtts import gTTS


def check_files():

    ok = True

    missing_words = []
    missing_letters = []
    missing_phrases = []

    words = text.word
    letters = text.letter
    phrases = text.phrases

    for c in letters:

        wav_path = 'sound/keys/{}.wav'.format(c)

        if not os.path.exists(wav_path):
            missing_letters.append(c)
            ok = False

    for c in words:

        wav_path = 'sound/words/{}.wav'.format(c)

        if not os.path.exists(wav_path):
            missing_words.append(c)
            ok = False

    for row in phrases:

        wav_path = 'sound/phrases/{}.wav'.format(row[0])

        if not os.path.exists(wav_path):
            missing_phrases.append(row)
            ok = False

    return ok, missing_letters, missing_words, missing_phrases


def generate_files(missing_letters, missing_words, missing_phrases):

    if not os.path.exists('sound'):
        os.makedirs('sound')

    if not os.path.exists('sound/keys'):
        os.makedirs('sound/keys')

    if not os.path.exists('sound/phrases'):
        os.makedirs('sound/phrases')

    if not os.path.exists('sound/words'):
        os.makedirs('sound/words')

    words = missing_words
    letters = missing_letters
    phrases = missing_phrases

    devnull = open(os.devnull, 'w')

    for index, c in enumerate(letters):

        print('Gerando arquivos de letras. {}/{}'.format(index + 1, len(letters)), end='\r')

        mp3_path = 'sound/keys/{}.mp3'.format(c)
        wav_path = 'sound/keys/{}.wav'.format(c)

        tts = gTTS(text=c, lang='pt-br')
        tts.save(mp3_path)

        subprocess.call(['ffmpeg', '-y', '-i', mp3_path, wav_path], stdout=devnull, stderr=devnull)

        if os.path.exists(mp3_path):
            os.remove(mp3_path)

    print('\n')

    for index, c in enumerate(words):

        print('Gerando arquivos de palavras. {}/{}'.format(index + 1, len(words)), end='\r')

        mp3_path = 'sound/words/{}.mp3'.format(c)
        wav_path = 'sound/words/{}.wav'.format(c)

        tts = gTTS(text=c, lang='pt-br')
        tts.save(mp3_path)

        subprocess.call(['ffmpeg', '-y', '-i', mp3_path, wav_path], stdout=devnull, stderr=devnull)

        if os.path.exists(mp3_path):
            os.remove(mp3_path)

    print('\n')

    for index, row in enumerate(phrases):

        print('Gerando arquivos de frases. {}/{}'.format(index + 1, len(phrases)), end='\r')

        mp3_path = 'sound/phrases/{}.mp3'.format(row[0])
        wav_path = 'sound/phrases/{}.wav'.format(row[0])

        tts = gTTS(text=row[1], lang='pt-br')
        tts.save(mp3_path)

        subprocess.call(['ffmpeg', '-y', '-i', mp3_path, wav_path], stdout=devnull, stderr=devnull)

        if os.path.exists(mp3_path):
            os.remove(mp3_path)

    print('\nFinalizado.')
