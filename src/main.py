import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import AudioFileClip, afx, ImageClip
# my modules
from vdata import VideoData
from dirs import get_input_dir, get_output_dir
from files import get_files

# folders
output = get_output_dir() 
input = get_input_dir()

def generate_video(vdata: VideoData):
    # constants
    SIZE = (1280, 720)
    W,H = SIZE
    FONT = ImageFont.truetype("times.ttf", 55)
    PAD = 80
    # video data 
    course = vdata.course_name
    vid_date = str(vdata.course_date)
    file = vdata.audio_file_name
    # image generation 
    image  = Image.new('RGB', SIZE, 'black')
    draw = ImageDraw.Draw(image)
    # text calcs
    _, _, w, h = draw.textbbox((0,0), course, font=FONT)
    _, _, w1, _ = draw.textbbox((0,0), vid_date, font=FONT)
    h_calc = (H-h)/2
    # text draw
    draw.text(((W-w)/2, h_calc), course, font=FONT, fill='white')
    draw.text(((W-w1)/2, h_calc+PAD), vid_date, font=FONT, fill='white')
    # video stuff
    audio = AudioFileClip(f"{input}/{file}").fx(afx.volumex, 4.0)
    clip = ImageClip(np.array(image)).set_duration(audio.duration)
    clip = clip.set_audio(audio)
    clip.write_videofile(f"{output}/{vdata.get_file_name()}.mp4", fps=24)

def get_videos():
    videos = get_files(input)
    print(f"{len(videos)} audio files found... starting the conversion\n")
    for video in videos:
        generate_video(video)
    print("Done!")

get_videos()
