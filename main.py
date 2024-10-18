from pytube import YouTube
import tkinter as tk 
from tkinter import filedialog

def baixar_video(url,caminho):
    try: 
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=true, file_extension="mp4")
        maior_qualidade_stream = streams.get_highest_resolution()
        maior_qualidade_stream.download(output_path=caminho)
        print("Vídeo baixado com sucesso!")
    except Exception as e:
        print(e)

def definir_caminho():
    pasta = filedialog.askdirectory()
    if pasta:
        print(f"Pasta selecionada: {pasta}")

        return pasta
    
if __name__ == "__main__": 
    root = tk.Tk()
    root.withdraw()

    video_link = input("Insira um link de vídeo: ")
    caminho = definir_caminho()

    if caminho: 
        baixar_video(video_link, caminho)
    else: 
        print("Caminho inválido! Por favor tente novamente.")