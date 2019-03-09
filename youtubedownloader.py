#gui framework  in python tkinter
import tkinter as tk

from pytube import YouTube

#root is the name of main window object!!!
root=tk.Tk()

def downloadVid():
    link=E1.get()#to get the link enter in user_box
    yt = YouTube(str(link))#YOUTUBE object called yt
    print(yt.title)
    stream = yt.streams.first()#res 720p ...you cna check another qualiies by typing  .second()
    stream.download(r'C:\Users\Chetan\Downloads')
    print('DOWNLOADED')


    

#widgets
w=tk.Label(root,text='Youtube video downloader')
w.pack()


#entry input box
E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)


#button
button=tk.Button(root,text='Download',fg='black',command=downloadVid )
button.pack(side=tk.BOTTOM)



#to run infinite times
root.mainloop()
