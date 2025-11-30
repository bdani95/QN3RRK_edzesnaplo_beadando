import tkinter as tk

def show_weight_progress(entries, exercise_name):
    filtered = [e for e in entries if e.exercise == exercise_name]
    if not filtered:
        return

    dates = [e.date for e in filtered]
    weights = [e.weight for e in filtered]

    win = tk.Toplevel()
    win.title(f"Súlygrafikon – {exercise_name}")

    width = 600
    height = 400
    margin = 50

    canvas = tk.Canvas(win, width=width, height=height, bg="white")
    canvas.pack()

    max_w = max(weights)
    min_w = min(weights)

    if max_w == min_w:
        max_w += 1

    def map_x(i):
        return margin + i * (width - 2*margin) / (len(weights) - 1 if len(weights) > 1 else 1)

    def map_y(w):
        return height - margin - (w - min_w) * (height - 2*margin) / (max_w - min_w)

    canvas.create_line(margin, margin, margin, height-margin, width=2)
    canvas.create_line(margin, height-margin, width-margin, height-margin, width=2)

    for i in range(len(weights) - 1):
        canvas.create_line(map_x(i), map_y(weights[i]),
                           map_x(i+1), map_y(weights[i+1]),
                           fill="blue", width=2)

    for i, w in enumerate(weights):
        x, y = map_x(i), map_y(w)
        canvas.create_oval(x-4, y-4, x+4, y+4, fill="red")
        canvas.create_text(x, y-10, text=str(w))

    for i, d in enumerate(dates):
        x = map_x(i)
        canvas.create_text(x, height-margin+15, text=d, font=("Arial", 8))
