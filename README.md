# Simple video generator

Simple script to generate videos from audio files.

## Setup the project

First you need to create the virtual environment with the following command:

```bash
python -m venv env_name
```
then you should activate the environment with:

```bash
./env_name/Scripts/activate
```

lastly you need to install the script requirements with:

```bash
pip install -r requirements.txt
```

## Usage

First you must put your audio files in the `input` folder.

> **Note**
> The files must be named with the pattern `YYYY-MM-DD_[\w]+` to be recognized by the script.

Once your files are under the `input` folder you need 
to run the `main.py` file to generate all the videos, when the process ends you 
can find the generated videos inside the `output` folder.

```bash
# Command to run the script
python ./src/main.py
```
