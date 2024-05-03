import streamlit as st
from whisper_cpp import Whisper
from ffmpeg import FFmpeg
import os
import datetime
import random
import string
import datetime

def genRANstring(n):
    """
    n = int number of char to randomize
    """
    N = n
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    return res

@st.cache_resource 
def create_whisper():   
    whisper = Whisper("models/ggml-base.en-q5_1.bin")
    return whisper

@st.cache_resource
def ffmpegconvert(x):
    ffmpeg = FFmpeg().input(x).output("temp.wav", {"codec:a": "pcm_s16le",
                                                            'ar':16000,
                                                            'ac':1})
    ffmpeg.execute()
    pass

if "gentime" not in st.session_state:
    st.session_state.gentime = "**:green[none yet]**"
if "audiofile" not in st.session_state:
    st.session_state.audiofile = ''    

def main():

    st.set_page_config(layout="wide", page_title="AI Whisper Transcriber")
    whisper = create_whisper()
    st.write("# 🌇🏙️ Transcribe your Audio files with whisper.CPP")

    st.sidebar.write("## Upload an audio file :gear:")
    file1=None
    transcribe_btn = st.button('Start Audio AI', type='primary')
    message1 = st.empty()
    message2 = st.empty()
    message3 = st.empty()
    audioplayer = st.empty()
    transcribed = st.empty()

    # Upload the images
    file1 = st.sidebar.file_uploader("Upload Audio file", type=["mp3", "wav"],accept_multiple_files=False)
    gentimetext = st.sidebar.empty()

    if (transcribe_btn and file1):
        with st.spinner("Transcribing..."):
            print(file1.name)
            if 'mp3' in file1.name:
                print('The file is an MP3: starting ffmpeg')
                out = ffmpegconvert(file1.name)
                message1.success('Audio encoded into WAV')
                start = datetime.datetime.now()
                print('Start transcribing...')
                whisper.transcribe('temp.wav', 
                                diarize=False,
                                print_progress=False) #spanish.wav
                delta = datetime.datetime.now() - start
                st.session_state.gentime = f"**:green[{str(delta)}]**"
                gentimetext.write(st.session_state.gentime)
                message2.success('Audio transcripted by AI')
                print('removing temp files...')
                os.remove('temp.wav')
                print('writing text file out...')
                result = whisper.output(output_txt=True)
                transcribed.write(result)
                print('completed')

            else:
                start = datetime.datetime.now()
                whisper.transcribe(file1.name, 
                                diarize=False,
                                print_progress=False) #spanish.wav 
                delta = datetime.datetime.now() - start
                st.session_state.gentime = f"**:green[{str(delta)}]**" 
                gentimetext.write(st.session_state.gentime)
                message2.success('Audio transcripted by AI')                
                result = whisper.output(output_txt=True)
                transcribed.write(result)

    if  not file1:
        message3.warning("Upload an audio file")
            

if __name__ == "__main__":
    main()