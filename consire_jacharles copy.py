import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ocr_pil copy 5 import load_image_and_extract_text


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("Arquivo novo:", event.src_path)

if __name__ == "__main__":
    path = '/home/joao/Imagens/Capturas de tela'  # Substitua pelo caminho correto
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
