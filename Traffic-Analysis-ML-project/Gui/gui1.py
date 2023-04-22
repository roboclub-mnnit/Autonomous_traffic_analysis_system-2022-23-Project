import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import customtkinter as ct
import os
import shutil
import subprocess
from PIL import ImageTk, Image
import cv2

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

# create a window
window = tk.Tk()
# set the title of the window
window.title("Traffic Analysis System")
# Set the icon bitmap for the window
window.iconbitmap("icon.ico")

# load the background image
bg_image = Image.open(r"bg.webp")
alpha = 0.18
# create a transparent version of the image
bg_image.putalpha(int(255 * alpha))
bg_image = bg_image.resize((1290,720), Image.LANCZOS)
background_image = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(window, image=background_image,)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# set the size of the window
window.geometry("1290x720")


def select_file():
    file_path = filedialog.askopenfilename(title="Select Video File")
    # add a label to the window
    label = tk.Label(window, foreground='red',background = 'black',text="Video Analysed Successfully !")

    # apply the style to the label
    label.config(font=('ariel', 15))
    label.place(x=500, y=320)
    
    return file_path

def Volume_Study():
     subprocess.run(["python", r"..\Vehicle Detection\Traffic-counter.py"])
def Speed_study():
    subprocess.run(["python",r"..\Speed Estimation\speed.py"])    

def open_pdf():
    path = r"..\Results\result.pdf"
    subprocess.Popen([path], shell=True)
    
def open_video1():
    # open the video file using OpenCV
    video = cv2.VideoCapture(r"..\Vehicle Detection\vehicle-counting-result1.mp4")

    # loop through the frames of the video
    while True:
        # read the next frame of the video
        ret, frame = video.read()

        # check if the frame was successfully read
        if not ret:
            break

        # display the frame
        cv2.imshow('Video', frame)

        # wait for a key press and check if the 'q' key was pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # release the video file and close the window
    video.release()
    cv2.destroyAllWindows()
def open_video2():
    
    # open the video file using OpenCV
    video = cv2.VideoCapture(r"..\Speed Estimation\outpy.avi")

    # loop through the frames of the video
    while True:
        # read the next frame of the video
        ret, frame = video.read()

        # check if the frame was successfully read
        if not ret:
            break

        # display the frame
        cv2.imshow('Video', frame)

        # wait for a key press and check if the 'q' key was pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # release the video file and close the window
    video.release()
    cv2.destroyAllWindows()
        

    # loop through the frames of the video
    while True:
        # read the next frame of the video
        ret, frame = video.read()

        # check if the frame was successfully read
        if not ret:
            break

        # display the frame
        cv2.imshow('Video', frame)

        # wait for a key press and check if the 'q' key was pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # release the video file and close the window
    video.release()
    cv2.destroyAllWindows()
            
        
def result():
    subprocess.run(["python", r"..\Results\VOLUME STUDY\volume.py"])
    subprocess.run(["python", r"..\Results\SPOT SPEED STUDY\spot speed study.py"])
    
    
    # add a label to the window
    label = tk.Label(window, foreground="white",background = 'black', text="Download Traffic Analysis Report")
    # apply the style to the label
    label.config(font=('ariel', 15))
    label.place(x=485, y=400)
    # add a button to copy the video file to the destination directory
    result= ct.CTkButton(window, text="download",command=open_pdf)
    result.place(x=560, y=460)
    # add a label to the window
    label = tk.Label(window, foreground="white",background = 'black',text="if you want to see result videos click on ")

    # apply the style to the label
    label.config(font=('ariel', 15))
    label.place(x =460 , y = 550)
    
    select = ct.CTkButton(master = window, text="Vehicle-Detection", command=open_video1)
    select.place(x=370, y=620)

    select = ct.CTkButton(master = window, text="Speed Estimation", command=open_video2)
    select.place(x=770, y=620)
    
def copy_file():
    file_path = select_file()
    default_name = "vehicle-counting.mp4"  # Set a default name for the video file
    dest_path = os.path.join(r"..\Vehicle Detection", default_name)
    shutil.copy(file_path, dest_path)
   
    Volume_Study()
    Speed_study()
    result()
    
# add a label to the window
label = tk.Label(window, text="TRAFFIC ANALYSIS SYSTEM",pady=10, padx=20, borderwidth = 2)

# apply the style to the label
label.config(foreground="black", background="white", font=('Century Gothic bold', 40), pady=10)
label.pack()

# add a label to the window
label = tk.Label(window, foreground="white",background = 'black',text="Click On the Button to Select your video file")

# apply the style to the label
label.config(font=('ariel', 15))
label.place(x=435, y=220)
# add a button to copy the video file to the destination directory
select = ct.CTkButton(master = window, text="select video file", command=copy_file)
select.place(x=560, y=280)


# run the main event loop

window.mainloop()
