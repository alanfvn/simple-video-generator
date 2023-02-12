import os

def get_output_dir():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output'))
    return path

def get_input_dir():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'input'))
    return path
