A small lecture on Linear Algebra mostly based on [this](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&ab_channel=3Blue1Brown) playlist.
<br>
<br>
![](https://github.com/marisbaier/Brueckenkursvortraege/blob/main/src/example.gif) 
<br>

## Setup
Available as a whole on [this](https://people.physik.hu-berlin.de/~baierluc) website.
To compile on your own, a fairly recent install of [ffmpeg](https://ffmpeg.org/download.html) is required, aswell as a running [LaTeX installation](https://www.latex-project.org/get/). Also cairo and pango is needed (!), which is a pain in the ass. I'm sorry.

Tested with Python 3.9.13.
```bash
pip install -r requirements.txt
```

Then, compile the scenes with
```bash
./render.sh
```

followed by
```bash
manim-slides [Scenes]
```
...to run the presentation
