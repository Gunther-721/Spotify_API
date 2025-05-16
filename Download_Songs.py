
import yt_dlp
import os

# Set FFmpeg binary path manually
os.environ["PATH"] += os.pathsep + r"C:\Users\username\Downloads\ffmpeg-2025-05-12-git-8ce32a7cbb-essentials_build\ffmpeg-2025-05-12-git-8ce32a7cbb-essentials_build\bin"

# List of songs to download (example)
songs = [
    "Shakira, Pitbull - Rabiosa (feat. Pitbull)",
    "Luis Fonsi, Demi Lovato - Échame La Culpa",
    "David Guetta, Sia - Titanium (feat. Sia)",
    "Don Omar, Lucenzo - Danza Kuduro",
    "Pitbull, Kesha - Timber",
    "Shakira, Wyclef Jean - Hips Don't Lie (feat. Wyclef Jean)",
    "Black Eyed Peas - I Gotta Feeling",
    "Rihanna, Calvin Harris - We Found Love",
    "Calvin Harris - Summer",
    "Enrique Iglesias - Bailamos - From 'Wild Wild West'",
    "Shakira - Whenever, Wherever",
    "Flo Rida, Kesha - Right Round",
    "Jennifer Lopez, Pitbull - On The Floor",
    "Pitbull, AFROJACK, Ne-Yo, Nayer - Give Me Everything (feat. Nayer)",
    "Fly Project - Toca Toca - Radio Edit",
    "Shakira, Carlinhos Brown - La La La (Brasil 2014) (feat. Carlinhos Brown)",
    "Alexandra Stan - Mr. Saxobeat - Radio Edit",
    "Flo Rida - Good Feeling",
    "Enrique Iglesias, Descemer Bueno, Gente De Zona - Bailando - Spanish Version",
    "Pitbull, Christina Aguilera - Feel This Moment (feat. Christina Aguilera)",
    "Shakira - Suerte (Whenever, Wherever)",
    "Lady Gaga - Poker Face",
    "LMFAO, Lauren Bennett, GoonRock - Party Rock Anthem",
    "David Guetta, Kid Cudi - Memories (feat. Kid Cudi)",
    "Enrique Iglesias, Pitbull - I Like It",
    "Shakira - Ciega, Sordomuda",
    "Stromae - Alors on danse - Radio Edit",
    "Calvin Harris - Feel So Close - Radio Edit",
    "Juanes - La Camisa Negra",
    "Kesha - TiK ToK",
    "Shakira - Las de la Intuición",
    "Enrique Iglesias, Pitbull - I'm A Freak",
    "Selena Gomez & The Scene - Love You Like A Love Song",
    "LMFAO - Sexy And I Know It",
    "Black Eyed Peas - Pump It",
    "Shakira - Loba",
    "Timbaland, Keri Hilson, D.O.E. - The Way I Are",
    "Enrique Iglesias, Ludacris, DJ Frank E - Tonight (I'm Fuckin' You)",
    "Sean Paul, Alexis Jordan - Got 2 Luv U (feat. Alexis Jordan)",
    "Pitbull - I Know You Want Me (Calle Ocho)",
    "Shakira - Addicted to You",
    "David Guetta, AFROJACK, Bebe Rexha, Nicki Minaj - Hey Mama (feat. Nicki Minaj, Bebe Rexha & Afrojack)",
    "Maroon 5, Christina Aguilera - Moves Like Jagger - Studio Recording From 'The Voice' Performance",
    "Manu Chao - Me Gustas Tu",
    "Sean Paul - Temperature",
    "Shakira, Freshlyground - Waka Waka (Esto es Africa) (feat. Freshlyground)",
    "Nelly Furtado - Say It Right",
    "David Guetta, Ne-Yo, Akon - Play Hard (feat. Ne-Yo & Akon)",
    "Don Omar - Hasta Que Salga El Sol",
    "Pitbull, John Ryan - Fireball (feat. John Ryan)"
]


# Output folder
output_dir = "Downloaded_Songs"
os.makedirs(output_dir, exist_ok=True)

# yt-dlp options
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    'quiet': False,
    'noplaylist': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def download_song(query):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"\n🔍 Searching and downloading: {query}")
            ydl.download([f"ytsearch1:{query}"])
        except Exception as e:
            print(f"❌ Failed to download {query}: {e}")

# Loop through all songs
for song in songs:
    download_song(song)
