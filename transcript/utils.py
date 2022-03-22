
from vosk import Model, SpkModel, KaldiRecognizer
import wave
import shlex
import pipes
import json
from subprocess import check_call
import numpy as np

def transcription(filename):
    model = Model("vosk-model-ru-0.22")
    file_path = './media/{}'.format(filename)
    wavfile = filename.split(".", 1)[0] + '.wav'

    command = 'ffmpeg -y -i {} -ar 48000 -ac 1 {}'.format(pipes.quote(file_path), pipes.quote(wavfile))
    check_call(shlex.split(command))

    wf = wave.open(wavfile, "rb")
    rcgn_fr = wf.getframerate() * wf.getnchannels()
    rec = KaldiRecognizer(model, rcgn_fr)
    result = ''
    last_n = False
    # read_block_size = 4000
    read_block_size = wf.getnframes()
    while True:  # Можно читать файл блоками, тогда можно выводить распознанный текст частями, но слова на границе блоков могут быть распознаны некорректно
        data = wf.readframes(read_block_size)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())

            if res['text'] != '':
                result += f" {res['text']}"
                if read_block_size < 200000:
                    print(res['text'] + " \n")

                last_n = False
            elif not last_n:
                result += '\n'
                last_n = True

    res = json.loads(rec.FinalResult())
    result += f" {res['text']}"
    return result
