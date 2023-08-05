import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time 

class FileSystem (FileSystemEventHandler) :
    def on_created(self, event):
       print(event)
    def on_deleted(self, event):
       print(event.src_path)

spath = 'C:/Users/Admin/Downloads'
eventhandle = FileSystem()

ob = Observer()
ob.schedule(eventhandle,spath,recursive=True)
ob.start()

while(True):
    print('Running')
    time.sleep(1)