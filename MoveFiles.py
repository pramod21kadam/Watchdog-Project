from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
import time, os, json

class MyHandler(FileSystemEventHandler):
    def on_created(self,event):
        # Reads the json file for address based on file extension
        folder_destination = None
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(5)
        try:
            for filename in os.listdir(folder_to_track):
                try:
                    name, ext = os.path.splitext(filename)
                    found = False
                    address = None
                    for record in data_array:
                        if ext in record["type"]:
                            address = record["target_location"]
                            new_dest = record["target_location"] + "/" + filename
                            found = True
                            break
                    if found:
                        src = folder_to_track + "/" + filename
                        if not os.path.exists(address):
                            
                            os.mkdir(address)
                        os.rename(src,new_dest)
                except Exception as e:
                    print(e)
                    continue
            return True
        except:
            return False

folder_to_track = "/home/pramodkadam/Downloads"#address of folder to track
with open("data.json",'r') as file:
    data_array = json.loads(file.read())
eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler,folder_to_track,recursive=True)

observer.start()
try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()
