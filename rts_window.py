import rts4xs_objects
import tkinter as tk


root = tk.Tk()
root.title("Time")
upper_left = tk.Frame(root)
upper_left.grid(row=0, column = 0)
upper_right = tk.Frame(root)
upper_right.grid(row =0, column = 1)
time_label = tk.Label(upper_right)

time = rts4xs_objects.Countable("Year", e = 2200.0)
playing = False
time_label.configure(text = str(time.getElement()))


    

def play():
    global playing
    global time
    global time_label
    if not playing:
        return
    time.increment(.1)
    time.setElement(round(time.getElement(), 1))
    time_label.configure(text=str(time.getElement()))
    root.after(1000, play)

def pause():
    global playing
    playing = False

def pressed_play():
    global playing
    playing = True
    play()

time_label.pack()
play_button = tk.Button(upper_right, text = 'Play', width= 25, command = pressed_play)
play_button.pack(side=tk.RIGHT)
pause = tk.Button(upper_right, text='Pause', width=25, command=pause)
pause.pack(side=tk.LEFT)
root.mainloop()