from tkinter import *
import tkinter.messagebox as msg
from pygame import mixer
from tkinter import filedialog
from tkinter.ttk import Progressbar
from mutagen.mp3 import MP3
import datetime
Total_music_Lenght = 0
currentvolume = 0

mixer.init()


def VolumeUp():
    Currentvolume1 = mixer.music.get_volume()
    mixer.music.set_volume(Currentvolume1 + 0.1)
    integerNumber = int(mixer.music.get_volume()*100)
    volumeinfo_bar.configure(text = f'{integerNumber}%')
    progress_bar['value'] = integerNumber

def Volumedown():
    CurrentVolume1 = mixer.music.get_volume()
    mixer.music.set_volume(CurrentVolume1 - 0.1)
    integerNumber = int(mixer.music.get_volume()*100)
    volumeinfo_bar.configure(text = f'{integerNumber}%')
    progress_bar['value'] = integerNumber

def StopMusic():
    if len(dir_12.get()) == 0:
        MusicStatus.configure(text='Please Select the Music...')
    else:
        mixer.music.pause()
        mixer.music.stop()
        pos = mixer.music.get_pos()
        # LabelStartMusic.configure(text=f'{datetime.timedelta(seconds=pos)}')
        MusicStatus.configure(text='Stopped...')
        


def MuteMusic():
    global currentvolume
    main.unmuteButton.grid()
    currentvolume = mixer.music.get_volume()
    mixer.music.set_volume(0)
    MusicStatus.configure(text='Muted...')


def UnmuteMusic():
    global currentvolume
    main.unmuteButton.grid_remove()
    mixer.music.set_volume(currentvolume)
    MusicStatus.configure(text='Unmuted...')


def SearchopenFile():
    mixer.music.stop()
    dir_1 = filedialog.askopenfilename()
    dir_12.set(dir_1)


def playMusic():
    if len(dir_12.get()) == 0:
        MusicStatus.configure(text='Please select track !!!')

    else:
        mixer.music.load(dir_12.get())
        mixer.music.play()
        LabelProgersstbarMusic.grid()
        LabelProgersstbar.grid()
        MusicStatus.configure(text='Playing...')
        main.resumeButton.grid()

        song = MP3(dir_12.get())
        Total_music_Lenght = int(song.info.length)
        print(Total_music_Lenght)
        progress_barTime['maximum'] = Total_music_Lenght
        LabelEndMusic.configure(text=f'{str(datetime.timedelta(seconds=Total_music_Lenght))}')

        

        def music_postion():
            currentPostion = mixer.music.get_pos()//1000
            progress_barTime['value'] = currentPostion
            LabelStartMusic.configure(text=f'{str(datetime.timedelta(seconds=currentPostion))}')
            progress_barTime.after(1,music_postion)
            

    music_postion()
# botton pause...
def pauseMusic():
    if len(dir_12.get()) == 0:
        MusicStatus.configure(text='Please Select the Music...')
    else:

        mixer.music.unpause()
        main.resumeButton.grid()
        MusicStatus.configure(text='Paused...')


# botton resume...

def resumeMusic():
    mixer.music.pause()
    main.resumeButton.grid_remove()
    MusicStatus.configure(text='Resumed...')


# -------------------------------------------------------------------------------
def rate():
    rate1 = msg.askquestion('Rating', 'Do you like This Music Player')
    if rate1 == 'yes':
        msg.showinfo(
            'rating', 'Thank you Please rate the GUI in Google Play Store')

    else:
        msg.showinfo(
            'rating', 'Please go to feedback option and sent the problem')


def inform():
    msg.showinfo('feedback', 'Thank you for freedback.')


def feedback():
    text1 = StringVar()
    feedback1 = msg.askquestion(
        'Feedback', 'Do you want to gives the feedback ?')
    if feedback1 == 'yes':
        fback = Tk()
        fback.title('Feedback.')
        fback.geometry('300x200')
        fback.resizable(False, False)

        Label(fback, text='Enter the Problem :-',
              font='arial 13').pack(anchor='nw')

        en = Entry(fback, width=20, font='arial 15',
                   textvariable=text1)
        en.pack(padx=20, pady=10)
        Button(fback, text='Submit', command=inform).pack(side='bottom')


def menu():
    mainMenu = Menu(main)

    m1 = Menu(mainMenu, tearoff=False)
    m1.add_command(label='Open File')
    m1.add_command(label='New Window')
    m1.add_command(label='Save')

    m2 = Menu(mainMenu, tearoff=False)
    m2.add_command(label='Rate', command=rate)
    m2.add_command(label='Freedback', command=feedback)

    m3 = Menu(mainMenu, tearoff=False)
    m3.add_command(label='help')
    m3.add_command(label='Documention')

    m4 = Menu(mainMenu, tearoff=False)
    m4.add_command(label='Code')

    mainMenu.add_cascade(label='File', menu=m1)
    mainMenu.add_cascade(label='Rate', menu=m2)
    mainMenu.add_cascade(label='Help', menu=m3)
    mainMenu.add_cascade(label='Code', menu=m4)

    main.config(menu=mainMenu)


# menu wigit...
# -------------------------------------------------------------------------------
main = Tk()
main.geometry('800x540')
main.resizable(False, False)
main.title('Music Player')
main.configure(bg='skyblue')
# global imagepause
# ----------------------------------------- All button icons and images resization
imagepause = PhotoImage(file='play-button (2).png')
imagestop = PhotoImage(file='stop.png')
imageSearch = PhotoImage(file='search.png')
imageMute = PhotoImage(file='mute.png')
imagevolumeup = PhotoImage(file='volume-up (2).png')
imagevolumedown = PhotoImage(file='volume-down (1).png')
imagepauseSplay = PhotoImage(file='play-button (2).png')
imageResume = PhotoImage(file='pause (1).png')
imageUnMute = PhotoImage(file='volume-off.png')

dir_12 = StringVar()

# -------------------------------------------- All button icon and image resiztion end....

# All labels and button -------------------------------------

Label(main, text='Select the Track :-', font='arial 16 bold',
      bg='skyblue').grid(row=0, column=1, padx=20, pady=20)

MusicStatus = Label(main, text='', font='arial 16 italic bold', bg='skyblue')
MusicStatus.grid(row=4, column=2)

Entry(main, width=35, font='arial 12 italic bold',
      textvariable=dir_12).grid(row=0, column=2, padx=30)

Button(main, text='Search', width=130, height=60, borderwidth=5, bg='yellow',
       activebackground='purple', font='arial 10 bold', image=imageSearch, compound=RIGHT, command=SearchopenFile).grid(
    pady=20, row=0, column=3, padx=20)

Button(main, text='Play', width=130, height=60, borderwidth=5, bg='red',
       activebackground='purple', image=imagepause, command=playMusic, compound=RIGHT, font='arial 10 bold').grid(row=3,
                                                                                                                  column=1,
                                                                                                                  padx=20,
                                                                                                                  pady=14)

Button(main, text='Stop', width=130, height=60, borderwidth=5, bg='red',
       activebackground='blue', font='arial 10 bold', image=imagestop, compound=RIGHT, command=StopMusic).grid(row=4,
                                                                                                               column=1,
                                                                                                               padx=20,
                                                                                                               pady=20)
main.muteButton = Button(main, text='Mute', width=130, height=60, borderwidth=5,
                         bg='gray', activebackground='black', font='arial 10 bold', image=imageMute, compound=RIGHT,
                         command=MuteMusic)
main.muteButton.grid(row=3, column=3)

main.unmuteButton = Button(main, text='Unmute', width=130, height=60, command=UnmuteMusic, borderwidth=5,
                           bg='gray', activebackground='black', font='arial 10 bold', image=imageUnMute, compound=RIGHT)
main.unmuteButton.grid(row=3, column=3)

main.unmuteButton.grid_remove()

Button(main, text='Volume Up', width=130, height=60, borderwidth=5, bg='yellow',

       activebackground='orange', font='arial 10 bold', image=imagevolumeup, compound=RIGHT, command=VolumeUp).grid(
    row=6, column=1, padx=20, pady=30)

Button(main, text='Volume Down', width=155, height=60, borderwidth=5, bg='yellow',
       activebackground='orange', font='arial 10 bold', image=imagevolumedown, compound=RIGHT, command=Volumedown).grid(
    row=6, column=3)

main.pauseButton = Button(main, width=105, height=70, bg='skyblue', command=pauseMusic, activebackground='skyblue',
                          image=imagepauseSplay)

main.pauseButton.grid(row=6, column=2)

main.resumeButton = Button(main, width=105, height=70, bg='skyblue', command=resumeMusic, activebackground='skyblue',
                           image=imageResume)

main.resumeButton.grid(row=6, column=2)

main.resumeButton.grid_remove()

LabelProgersstbar = Label(main,text='',bg='red')
LabelProgersstbar.grid(row=4,column=3)

progress_bar = Progressbar(LabelProgersstbar,orient=VERTICAL,mode='determinate',value=100,length=150)
progress_bar.grid(row=0,column=0)

volumeinfo_bar = Label(LabelProgersstbar,text='100%',width=3)
volumeinfo_bar.grid(row=0,column=0)

LabelProgersstbar.grid_remove()

LabelProgersstbarMusic = Label(main,text='',bg='red')
LabelProgersstbarMusic.grid(row=5,column=1,columnspan=4,pady=16)

LabelStartMusic = Label(LabelProgersstbarMusic,text='0:00',bg='red',fg='white',width=5)
LabelStartMusic.grid(row=0,column=0)

progress_barTime = Progressbar(LabelProgersstbarMusic,orient=HORIZONTAL,mode='determinate',value=0)
progress_barTime.grid(row=0,column=1,ipadx=300)

LabelEndMusic = Label(LabelProgersstbarMusic,text='0:00',bg='red',fg='white')
LabelEndMusic.grid(row=0,column=2)

LabelProgersstbarMusic.grid_remove()

# -------------------------------------------------------------------------- end...

intro = 'Abhinav Music Player'
count = 0
text = ''
Sliderlabel = Label(main, text=intro, bg='skyblue',
                    font='arial 20 italic bold')
Sliderlabel.grid(row=3, column=2)


def introLabel():
    global count, text
    if count >= len(intro):
        count = -1
        text = ''
        Sliderlabel.configure(text=text)
    else:

        text = text + intro[count]
        Sliderlabel.configure(text=text)
    count += 1
    Sliderlabel.after(200, introLabel)


introLabel()
menu()

main.mainloop()
