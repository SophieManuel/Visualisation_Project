# COVID19 Movie

This directory contains a script that makes use of wwstatviz python package 
to generates a COVID19 (death in percentages per country) movie.

The `covid19_movie.py` script generates choropleth frames using wwstatviz.
Then, OpenCV is used to combine the generated frames into an AVI files
(5 frames per second).
The script also uses `imageio` python package to generate a GIF file (also, 5
frames per second).

The used data set in `covid19.csv` file.

## Requirements

```bash
pip install opencv-python
pip install imageio

apt-get install ffmpeg libsm6 libxext6
```

## Usage

```
python covid19_movie.py
```
