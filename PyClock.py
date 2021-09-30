from tkinter import Tk, Canvas, Frame, BOTH, W, Label, TOP, YES, X, font
import time
import datetime

time_string = time.strftime('%H:%M:%S')
root = Tk()

hour = 0

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')
        self.aMpM = 'T'
        self.day = 'D'
        self.mFrame = Frame(root, width=600, height=1024)
        self.mFrame.pack()

        self.watch = Label(self.mFrame, text=self.time2, font=('Gidole Regular', 12))

        self.watchHalf = Label(self.mFrame, text=self.aMpM, font=('Gidole Regular', 12))

        self.watchDay = Label(self.mFrame, text=self.day, font=('Gidole Regular', 12))
       # self.watch.pack()

        self.changeLabel()  # first call it manually

    def changeLabel(self):
        #self.time2 = time.strftime('%I:%M:%S')

        self.time2 = (time.strftime(' %I:%M').replace(' 0', ' '))
        #hour = int(time.strftime('%I').replace(' 0', ' '))
        #hour = int(time.strftime('%I').replace(' 0', ' '))

        now = datetime.datetime.now()
        if(int(now.hour) > 12):
            self.aMpM = "PM"
        else:
            self.aMpM = "AM"

        self.day = now.strftime('%A')
        self.watch.configure(font=("PantonNarrowDemo-Black", 100))
        self.watchHalf.configure(font=("PantonNarrowDemo-Black", 40))
        self.watchDay.configure(font=("PantonNarrowDemo-Light", 40))
        self.watch.place(x=50, y=50)
        self.watchHalf.place(x=380, y=77)
        self.watchDay.place(x=380, y=150, height=40)
        #self.watch.pack()
        self.watch.configure(text=self.time2)
        self.watchHalf.configure(text=self.aMpM)
        self.watchDay.configure(text=self.day)
        self.mFrame.after(200, self.changeLabel)  # it'll call itself continuously


def main():

    font.families()
    ex = Example()
    root.geometry("600x1024")
    root.update()
    root.mainloop()


if __name__ == '__main__':
    main()