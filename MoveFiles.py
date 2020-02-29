from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
import time,os,json

class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        folder_destination = { ".txt": (folder_to_track + "/txt") ,
        ".pdf":(folder_to_track + "/PDF Documents") ,
        ".zip":(folder_to_track + "/ZIP files"),
        ".vsix":(folder_to_track + "/VS Code Extensions"),
        ".png":(folder_to_track +"/Images"),
        ".jpeg":(folder_to_track +"/Images"),
        ".jpg":(folder_to_track +"/Images")}
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if filename.endswith(".txt"):
                new_dest = folder_destination[".txt"] + "/" + filename
                os.rename(src,new_dest)
            elif filename.endswith(".pdf"):
                new_dest = folder_destination[".pdf"] + "/" + filename
                os.rename(src,new_dest)
            elif filename.endswith(".zip"):
                new_dest = folder_destination[".zip"] + "/" + filename
                os.rename(src,new_dest)
            elif filename.endswith(".jpeg"):
                new_dest = folder_destination[".jpeg"] + "/" + filename
                os.rename(src,new_dest)
            elif filename.endswith(".jpg"):
                new_dest = folder_destination[".jpg"] + "/" + filename
                os.rename(src,new_dest)
            elif filename.endswith(".png"):
                new_dest = folder_destination[".png"] + "/" + filename
                os.rename(src,new_dest)
            elif filename.endswith(".vsix"):
                new_dest = folder_destination[".vsix"] + "/" + filename
                os.rename(src,new_dest)
        return True


try:
    folder_to_track = input("Enter path of folder to track: ")
    eventHandler = MyHandler()
    observer = Observer()
    observer.schedule(eventHandler,folder_to_track,recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
except:
    print("Error")