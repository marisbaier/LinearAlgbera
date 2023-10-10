# Brueckenkursvortraege
A small lecture on Linear Algebra mostly based on [this](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&ab_channel=3Blue1Brown) playlist.
<br>
<br>
![](https://github.com/marisbaier/Brueckenkursvortraege/blob/main/example.gif) 
<br>

## Setup
Available as a whole on [this](https://hu-berlin.de/maris) website.
To compile on your own, a fairly recent install of [ffmpeg](https://ffmpeg.org/download.html) is required, aswell as a running [LaTeX installation](https://www.latex-project.org/get/)

Tested with Python 3.9.13. Does <ins>not</ins> work with python 3.11!
```bash
pip install -r requirements.txt
```

Then, compile the scenes with
```bash
manim --save_sections chapter6.py
```

followed by
```bash
manedit
```
...to run the presentation
