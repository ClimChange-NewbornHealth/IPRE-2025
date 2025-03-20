# Video -> GIF

# Install in the bash: pip install moviepy
import os
import glob
import subprocess

#Parámetros:
#    - input_path: Ruta del video MP4 de entrada.
#    - output_path: Ruta donde se guardará el GIF.
#    - fps: Cuadros por segundo (bajar para reducir tamaño).
#    - speed_factor: Factor de velocidad (mayor que 1 acelera, menor que 1 ralentiza).


def mp4_to_gif_ffmpeg(input_path, output_path, fps=10, speed_factor=2):
    
    speed_filter = f"setpts={1/speed_factor}*PTS"
    command = [
        "ffmpeg",
        "-i", input_path,
        "-vf", f"fps={fps},scale=900:-1:flags=lanczos",
        "-y", output_path
    ]
    subprocess.run(command, check=True)

# Carpeta donde están los videos
input_videos = "Results"

# Obtener todos los archivos .mp4 en la carpeta
mp4_files = glob.glob(os.path.join(input_videos, "*.mp4"))

# Crear carpeta de salida si no existe
output_folder = os.path.join(input_videos, "gifs")
os.makedirs(output_folder, exist_ok=True)

# Iterar sobre los archivos y convertirlos a GIF
for mp4_file in mp4_files:
    filename = os.path.basename(mp4_file).replace(".mp4", ".gif")  # Cambiar extensión
    output_path = os.path.join(output_folder, filename)  # Ruta correcta del GIF

    print(f"🎥 Convirtiendo: {mp4_file} → {output_path}")
    mp4_to_gif_ffmpeg(mp4_file, output_path, fps=20, speed_factor=0.1)

print("✅ Conversión completa.")
