# whisperCPP-streamlit


Repo of the code from the Medium article


This is what comes out from this repo

<img src='https://github.com/fabiomatricardi/whisperCPP-streamlit/raw/main/whisperCPP-streamlit.gif' width=950>


## Instructions

> this code is tested on windows, with python 3.10


Create a virtual environment and install the following packages
```
pip install whisper-cpp-pybind  #good for pytho 3.10
pip install python-ffmpeg
pip install streamlit==1.26.0
```


You also need to install FFmpeg, and ad it to path
```
winget install "FFmpeg (Essentials Build)"
```

or download it and install as described in official website https://ffmpeg.org/download.html


Download the models already quantized from the official Hugging Face repo of ggerganov

https://huggingface.co/ggerganov/whisper.cpp/tree/main

The models come in different sizes, and quantization methods

download them into a subfolder called `models`

> for this app i used ggml-tiny.en-q8_0.bin

## run the streamlit app

from the terminal, with `venv` activated run
```
streamlit run stWhisper.py
```

---

<img src='https://github.com/fabiomatricardi/whisperCPP-streamlit/raw/main/whisperCPP-social.jpg' width=800>

---

### Full tutorial will be available on Medium | Artificial Intelligence in Plain English



