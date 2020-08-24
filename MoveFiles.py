from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
from json import loads
from os import listdir, path, mkdir, rename
from time import sleep as sleep

class files(object):
    def __init__(self):
        self.data_array = None
        with open("/home/pramodkadam/Workspace/git/Watchdog-Project/data.json",'r') as file:
            self.data_array = loads(file.read())

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        obj = files()
        self.data_array = obj.data_array

    def on_created(self,event):
        # Reads the json file for address based on file extension
        file_size:int = -1
        while file_size != path.getsize(event.src_path):
            file_size = path.getsize(event.src_path)
            sleep(5)
        try:
            for filename in listdir(folder_to_track):
                try:
                    name, ext = path.splitext(filename)
                    found:bool = False
                    for record in self.data_array:
                        if ext in record["type"]:
                            address = record["target_location"]
                            new_dest = record["target_location"] + "/" + filename
                            found = True
                            break
                    if found:
                        src:str = folder_to_track + "/" + filename
                        if not path.exists(address):
                            mkdir(address)
                        rename(src,new_dest)
                except Exception as e:
                    print(e)
                    continue
            return True
        except:
            return False

folder_to_track = "/home/pramodkadam/Downloads"#address of folder to track
eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler,folder_to_track,recursive=False)
observer.start()
try:
    while True:
        sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()