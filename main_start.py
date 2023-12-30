import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ocr_pil_4 import load_image_and_extract_text

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            print(f"Última imagem adicionada: {event.src_path}")
            load_image_and_extract_text(event.src_path)  # Passa o caminho real do arquivo
            print("Repita o processo quantas vezes quizer!!!")

if __name__ == "__main__":
    path = '/home/joao/Imagens/Capturas de tela'  # Substitua pelo caminho correto
    event_handler = MyHandler()  # Definição de event_handler
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() 
    print("aperte a tecla [print Screen} e selecione um trecho do extrato ")
