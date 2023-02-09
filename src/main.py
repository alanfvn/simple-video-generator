import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import AudioFileClip, afx, ImageClip

def get_file_name(name, date_val):
    val1 = name.lower().replace(" ", ".")
    val2 = date_val.replace("/", "_")
    return f"{val2}-{val1}"

def get_text_size(draw, message, font):
    _, _, w, h = draw.textbbox((0,0), message, font=font)
    return (w,h)

# inputs
course_num = int(input("Enter the number of the class you want: "))
date_value = input("Enter the date of the video: ")

# constants
COURSES = [
    "Admin. de tecnologias de la información", 
    "Ingeniería de software",
    "Inteligencia artificial",
    "Proyecto de graduación 1",
    "Redes de computadoras II",
]

SIZE = (1280, 720)
W,H = SIZE
FONT = ImageFont.truetype("times.ttf", 55)
PAD = 80

# vars
image  = Image.new('RGB', SIZE, 'black')
draw = ImageDraw.Draw(image)
course = COURSES[course_num]
file_name = get_file_name(course, date_value)

# text calcs
w,h = get_text_size(draw, course, FONT)
w1,h1 = get_text_size(draw, date_value, FONT)
h_calc = (H-h)/2

# text draw
draw.text(((W-w)/2, h_calc), course, font=FONT, fill='white')
draw.text(((W-w1)/2, h_calc+PAD), date_value, font=FONT, fill='white')

#files
files = os.listdir('./input/')
fname = files[0]

# video stuff
audio = AudioFileClip(f'./input/{fname}').fx(afx.volumex, 4.0)
clip = ImageClip(np.array(image)).set_duration(audio.duration)
clip = clip.set_audio(audio)
clip.write_videofile(f'./output/{file_name}.mp4', fps=24)
