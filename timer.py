import time
import Tkinter as tk


def show_current_time(h, w, c, tag, text):
    global start_count, start_time
    c.delete(text)
    c.delete(tag)
    now = time.localtime(time.time())[3:6]
    if start_count:
        second = now[2] - start_time[2]
        if second<0:
            carry = 1
            second += 60
        else:
            carry = 0
        minute = now[1] - start_time[1] - carry
        if minute<0:
            carry = 1
            minute += 60
        else:
            carry = 0
        hour = now[0] - start_time[0] - carry
        tag = "Count Mode"
    else:
        hour, minute, second = now
        tag = "Clock Mode"
    w = c.winfo_width()
    h = c.winfo_height()
    tag_text = c.create_text(w/2, h/4, font=("Courier", h/2), text=tag)
    time_text = c.create_text(w / 2, h*3/4, font=("Courier", h/2), text='%02i:%02i:%02i' % (hour, minute, second))
    c.after(refresh_interval, lambda: show_current_time(h, w, c, tag_text, time_text))
    return time_text


def count():
    global start_count, start_count
    if not start_count:
        start_count = 1
        start_time[:] = time.localtime(time.time())[3:6]
    else:
        start_count = 0
        start_time[:] = [0, 0, 0]


def main():
    root = tk.Tk()
    c = tk.Canvas(root, width=wid, height=hei, bg='white')
    c.pack(fill='both', expand='yes')
    text = 0
    tag = 0
    show_current_time(hei, wid, c, tag, text)
    b = tk.Button(root, text='Start/Stop', command=lambda: count())
    b.pack()
    root.lift()
    root.mainloop()

wid = 300
hei = 75
refresh_interval = 1
start_count = 0
start_time = [0, 0, 0]
main()

