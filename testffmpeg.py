from ffmpeg import FFmpeg

audioname = 'My favorite scene from Good Will Hunting.mp3'

ffmpeg = FFmpeg().input(audioname).output("temp.wav", {"codec:a": "pcm_s16le",
                                                       'ar':16000,
                                                       'ac':1})

"""
ffmpeg = (
    FFmpeg()
    .option("y")
    .input("audioname")
    .output(
        "output.wav",
        {"codec:v": "libx264"},
        vf="scale=1280:-1",
        preset="veryslow",
        crf=24,
    )
)
"""
ffmpeg.execute()

