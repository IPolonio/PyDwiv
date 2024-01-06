import flet as ft
from pytube import YouTube
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def main(page):
    url = ft.TextField(label="URL", autofocus=True)
    submit = ft.ElevatedButton("Descargar video")
    submitq = ft.ElevatedButton("Descargar audio")
    progress_bar = ft.ProgressBar(width=400) 
#revisar funcion de progressbar
    def update_progress_bar(stream, chunk, bytes_remaining):
        total_bytes = stream.filesize
        downloaded_bytes = total_bytes - bytes_remaining
        progress = int((downloaded_bytes / total_bytes) * 100)
        progress_bar.value = progress
#boton de audio ,proximamente scrollbar con mas opciones
    def audio_clk(e):
        current_folder = os.getcwd()
        yt = YouTube(url.value, on_progress_callback=update_progress_bar)
        video = yt.streams.get_audio_only("mp4")
        video.download(output_path=current_folder)
#boton de video ,proximamente scrollbar con mas opciones 
    def bt_clk(e):
        current_folder = os.getcwd()
        yt = YouTube(url.value, on_progress_callback=update_progress_bar)
        video = yt.streams.get_lowest_resolution()
        video.download(output_path=current_folder)

    submit.on_click = bt_clk
    submitq.on_click = audio_clk

   


    page.add(
        url,
        ft.Row([submit, submitq]),
        progress_bar,  # Agrega la barra de carga a la interfaz,no funciona aun 
    )
#carga la app
ft.app(target=main)
