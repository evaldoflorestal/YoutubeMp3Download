from pytube import YouTube
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os

# Insira o link do vídeo do YouTube que você deseja baixar o áudio
link = input("Insira o link do YouTube: ")

# Cria um objeto do YouTube
yt = YouTube(link)

# Obtém o objeto da melhor qualidade de áudio
audio = yt.streams.filter(only_audio=True).first()

# Baixa o arquivo de áudio em formato mp4
audio_file = audio.download()

# Cria um objeto AudioFileClip com o arquivo mp4 de áudio
audio_clip = AudioFileClip(audio_file)

# Escreve o arquivo de áudio em mp3 a partir do objeto de áudio
mp3_file = audio_clip.write_audiofile(audio_file.replace(".mp4", ".mp3"))

# Fecha o objeto de áudio e exclui o arquivo de áudio em mp4
audio_clip.close()
os.remove(audio_file)

print("Áudio baixado com sucesso em formato mp3!")


