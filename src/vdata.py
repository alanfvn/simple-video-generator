class VideoData:

    def __init__(self, course_name, course_date, audio_file):
        self.course_name = course_name
        self.course_date = course_date
        self.audio_file_name = audio_file

    def get_file_name(self):
        course = self.course_name.replace(' ', '_')
        dte = self.course_date
        return f"{dte}.{course}"
