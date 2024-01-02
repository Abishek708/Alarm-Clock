from tkinter import *
import datetime
import time
import winsound as ws

window = Tk()
window.geometry("500x400")
window.config(bg="#87BDD8")

def alarm():
    while True:
        time.sleep(1)
        alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        clock_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(clock_time, alarm_time)

        if alarm_time == clock_time:
            ws.PlaySound("sound.wav", ws.SND_ASYNC)
            break


Label(window, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red", bg="#87BDD8").pack(pady=10)
Label(window, text="Set Time", font=("Helvetica 15 bold"), bg="#87BDD8").place(x=65, y=100)

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(window, textvariable=hour, bg="#FEFBD8", width=4, font=(20)).place(x=170, y=100)
minuteTime = Entry(window, textvariable=minute, bg="#FEFBD8", width=4, font=(20)).place(x=227,y=100)
secondTime = Entry(window, textvariable=second, bg="#FEFBD8", width=4, font=(20)).place(x=290, y=100)

submit = Button(window, text="Set The Alarm", fg="white", bg="#82B74B", width=15, command=alarm,
                font=(20)).place(x=170, y=200)

window.mainloop()