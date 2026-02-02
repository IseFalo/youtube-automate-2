import yt_dlp

def download_youtube_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Enter YouTube video URL: ").strip()
    download_youtube_audio(link)
