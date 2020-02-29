from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
import time,os,json

class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        # Reads the json file for address based on file extension
        folder_destination = None
        with open("data.json",'r') as file:
            folder_destination = json.loads(file.read())

        try:
            for filename in os.listdir(folder_to_track):
                try:
                    name, ext = os.path.splitext(filename)
                    new_dest = folder_destination[ext] + "/" + filename
                    src = folder_to_track + "/" + filename
                    os.rename(src,new_dest)
                except KeyError:
                    continue
            return True
        except:
            return False

folder_to_track = "/home/pramodkadam/Downloads"#address of folder to track

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
