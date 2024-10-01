import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow
import matplotlib.patheffects as pe
import numpy as np
import tkinter as tk

fig, ax = plt.subplots()
fig.patch.set_facecolor('#212121')
ax.set_facecolor('#212121')

e_x_x, e_x_y = 0.3, 0
e_y_x, e_y_y = 0, 0.3
arrow_width = 0.01
label_padding = 0.05

def create_arrow(x, y, dx, dy, color):
    return FancyArrow(x, y, dx, dy, width=arrow_width, color=color, path_effects=[pe.withStroke(linewidth=2, foreground='black')])

def draw_grid():
    global grid_lines
    for line in grid_lines:
        line.remove()
    grid_lines = []

    # Draw vertical grid lines
    for i in np.linspace(-10, 10, 41):
        grid_lines.append(ax.plot([i*e_x_x-5*e_y_x,i*e_x_x+5*e_y_x], [i*e_x_y-5*e_y_y,i*e_x_y+5*e_y_y], color='gray', linestyle='--', linewidth=0.5)[0])
        grid_lines.append(ax.plot([-5*e_x_x+i*e_y_x,5*e_x_x+i*e_y_x], [-5*e_x_y+i*e_y_y,5*e_x_y+i*e_y_y], color='gray', linestyle='--', linewidth=0.5)[0])
ax.plot([-5,-3], [1,2])
e_x = create_arrow(0, 0, e_x_x, e_x_y, '#FFDD44')
e_y = create_arrow(0, 0, e_y_x, e_y_y, '#44DDFF')
ax.add_patch(e_x)
ax.add_patch(e_y)

# Add initial labels with LaTeX formatting and padding
label_e_x = ax.text(e_x_x + label_padding, e_x_y + label_padding, r'$e_x$', color='white', fontsize=10, ha='right', va='bottom', path_effects=[pe.withStroke(linewidth=2, foreground='black')])
label_e_y = ax.text(e_y_x + label_padding, e_y_y + label_padding, r'$e_y$', color='white', fontsize=10, ha='left', va='bottom', path_effects=[pe.withStroke(linewidth=2, foreground='black')])

# Set axis limits to extend to the border of the window
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Remove the axis

# Remove padding around the plot
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Initialize grid lines
grid_lines = []
draw_grid()

def on_key(event):
    global e_x, e_x_x, e_x_y, e_y, e_y_x, e_y_y, label_e_x, label_e_y
    dx1, dy1, dx2, dy2 = 0, 0, 0, 0
    if event.key == 'up':
        dy1 = 0.1
    elif event.key == 'down':
        dy1 = -0.1
    elif event.key == 'left':
        dx1 = -0.1
    elif event.key == 'right':
        dx1 = 0.1
    elif event.key == 'w':
        dy2 = 0.1
    elif event.key == 's':
        dy2 = -0.1
    elif event.key == 'a':
        dx2 = -0.1
    elif event.key == 'd':
        dx2 = 0.1

    e_x_x += dx1
    e_x_y += dy1
    e_y_x += dx2
    e_y_y += dy2

    # Remove old arrows
    e_x.remove()
    e_y.remove()

    # Create new arrows with updated positions
    e_x = create_arrow(0, 0, e_x_x, e_x_y, '#FFDD44')
    e_y = create_arrow(0, 0, e_y_x, e_y_y, '#44DDFF')
    ax.add_patch(e_x)
    ax.add_patch(e_y)

    # Update label positions
    label_e_x.set_position((e_x_x + label_padding, e_x_y + label_padding))
    label_e_y.set_position((e_y_x + label_padding, e_y_y + label_padding))

    # Redraw grid
    draw_grid()

    fig.canvas.draw()

# Disable the default "s" key binding
fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)

fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()