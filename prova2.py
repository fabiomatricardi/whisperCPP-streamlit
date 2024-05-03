# https://github.com/sphantix/whisper-cpp-pybind/tree/main
from whisper_cpp import Whisper
# https://github.com/jonghwanhyeon/python-ffmpeg/tree/main
# https://python-ffmpeg.readthedocs.io/en/latest/api/

from ffmpeg import FFmpeg
import datetime
import os

from whisper_cpp import Whisper

whisper = Whisper("models/ggml-base.en-q5_1.bin")

audioname = 'My favorite scene from Good Will Hunting.mp3'
audio = audioname
if 'mp3' in audioname:
    print('ffmpeg to convert to wav...')
    try:
        ffmpeg = FFmpeg().input(audioname).output("temp.wav", {"codec:a": "pcm_s16le",
                                                            'ar':16000,
                                                            'ac':1})
    except:
        print('NOT POSSIBLE TO LOAD AUDIO')


    whisper.transcribe('temp.wav', 
                    diarize=False,
                    print_progress=False) #spanish.wav
    os.remove('temp.wav')
else:
    whisper.transcribe(audioname, 
                    diarize=False,
                    print_progress=False) #spanish.wav    
# Additional Options
# output_csv=True, output_jsn=True, output_lrc=True, output_srt=True, output_txt=True, output_vtt=True, log_score=True
result = whisper.output(output_txt=True)
print('Removing temp files...')

print(result)