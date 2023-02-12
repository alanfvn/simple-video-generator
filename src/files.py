import os
import re
import unicodedata
import datetime
from vdata import VideoData

# constants
FILE_PATTERN = r"(\d+-\d+-\d+)_([\w]+)"
COURSES = [
    "Admin de tecnologias de la información", 
    "Ingeniería de software",
    "Inteligencia artificial",
    "Proyecto de graduación I",
    "Redes de computadoras II",
]

def strip_accents(value):
   return ''.join(c for c in unicodedata.normalize('NFD', value) if unicodedata.category(c) != 'Mn')

def find_course(name):
    name = name.lower()
    cname_words = name.split('_')
    course_words = [strip_accents(word).lower().split(' ') for word in COURSES]
    course = None
    for index, words in enumerate(course_words):
        if set(cname_words).issubset(words):
            course = index
    return course

def valid_file(file_name) -> VideoData:
    # test the pattern
    match = re.match(FILE_PATTERN, file_name)
    if not match:
        raise ValueError(f'Invalid file name, "{file_name}"')
    # group values from regex
    date_val, cname = match.groups()
    course_id = find_course(cname)
    course_date = None

    # check course name
    if course_id is None:
        raise ValueError(f'Invalid course name, "{cname}"')
    # check if the date of the file is correct
    try:
        course_date = datetime.date.fromisoformat(date_val)
    except ValueError as error:
        raise error
    # return the data
    return VideoData(COURSES[course_id], course_date, file_name)

def get_files(dir):
    files = [file for file in os.listdir(dir) if file.endswith('mp3')]
    vdatas = [valid_file(video) for video in files]
    return vdatas
