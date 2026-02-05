import yt_dlp
import os

def download_youtube_audio(url, output_folder):
    """Download audio from a single YouTube URL to a specific folder"""
    try:
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
            'no_warnings': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"✓ Successfully downloaded: {url}\n")
        return True

    except Exception as e:
        print(f"✗ Error downloading {url}: {e}\n")
        return False


def download_batch(url_list, channel_name="", folder_name=""):
    """Download audio from a list of YouTube URLs to a specific folder"""
    total = len(url_list)
    successful = 0
    failed = 0
    
    # Use folder_name if provided, otherwise use channel_name
    output_folder = folder_name if folder_name else channel_name
    
    if channel_name:
        print(f"\n{'='*60}")
        print(f"Starting download for: {channel_name}")
        print(f"Output folder: {output_folder}")
        print(f"Total videos: {total}")
        print(f"{'='*60}\n")
    
    for index, url in enumerate(url_list, 1):
        print(f"[{index}/{total}] Processing: {url}")
        
        if download_youtube_audio(url, output_folder):
            successful += 1
        else:
            failed += 1
    
    print(f"\n{channel_name} - Complete!")
    print(f"Successful: {successful} | Failed: {failed}\n")
    
    return successful, failed


if __name__ == "__main__":
    # Beat FM - 12 videos
    beat_fm_urls = [
        "https://www.youtube.com/watch?v=oR0gNoxLfEs",
        "https://www.youtube.com/watch?v=I0oFekKKvtE",
        "https://www.youtube.com/watch?v=Y34xNB-roz8",
        "https://www.youtube.com/watch?v=wjdlDDqXY6Q",
        "https://www.youtube.com/watch?v=TQwSoKEXRS8",
        "https://www.youtube.com/watch?v=H370uQdGsyU",
        "https://www.youtube.com/watch?v=OR3Q3m_mREo",
        "https://www.youtube.com/watch?v=_UtfTux9Jqw",
        "https://www.youtube.com/watch?v=jz9xNh7HuNI",
        "https://www.youtube.com/watch?v=xfXkRwa2On0",
        "https://www.youtube.com/watch?v=-qpJ48Gi_nM",
        "https://www.youtube.com/watch?v=oXqyrbfwzHU",
    ]
    
    # Nigeria Info FM - 12 videos
    nigeria_info_urls = [
        "https://www.youtube.com/watch?v=wfY6tm06IPY",
        "https://www.youtube.com/watch?v=E-TehUy-u7Y",
        "https://www.youtube.com/watch?v=GLzGEdYefaw",
        "https://www.youtube.com/watch?v=POsNFuZnauI",
        "https://www.youtube.com/watch?v=n0Ec__hLZjE",
        "https://www.youtube.com/watch?v=0PVZwYqldQE",
        "https://www.youtube.com/watch?v=HZCGkuaMKkM",
        "https://www.youtube.com/watch?v=c1cvYpzzfVA",
        "https://www.youtube.com/watch?v=8rVQvDkq7_c",
        "https://www.youtube.com/watch?v=e5RDIqAMZhc",
        "https://www.youtube.com/watch?v=lFjm-23R4iY",
        "https://www.youtube.com/watch?v=al6eC8xDUpc",
    ]
    
    # Berekete - 12 videos
    berekete_urls = [
        "https://www.youtube.com/watch?v=DQR_LMY8M4A",
        "https://www.youtube.com/watch?v=J-XQd4Z-p80",
        "https://www.youtube.com/watch?v=PWW64oEf8G0",
        "https://www.youtube.com/watch?v=AR2pLHqoyuA",
        "https://www.youtube.com/watch?v=p_pULhqc-zc",
        "https://www.youtube.com/watch?v=bebsFxvXm1E",
        "https://www.youtube.com/watch?v=jAMIT8QDYN0",
        "https://www.youtube.com/watch?v=le1VmFOyCLk",
        "https://www.youtube.com/watch?v=T9dnCUvgNJQ",
        "https://www.youtube.com/watch?v=3Ju0UGdcsG8",
        "https://www.youtube.com/watch?v=TfSiS87TcW8",
        "https://www.youtube.com/watch?v=mHm-fMbO5oQ",
    ]
    
    # 3FM 92.7 - 12 videos
    three_fm_urls = [
        "https://www.youtube.com/watch?v=-j9ShhlBvNA",
        "https://www.youtube.com/watch?v=g5fTLce8174",
        "https://www.youtube.com/watch?v=a_AvD-kglXw",
        "https://www.youtube.com/watch?v=1RjQiVuqmuA",
        "https://www.youtube.com/watch?v=fkHL17XTydg",
        "https://www.youtube.com/watch?v=fVN9LoM4b_Q",
        "https://www.youtube.com/watch?v=Wo2gar_ae3E",
        "https://www.youtube.com/watch?v=SyNSpQUUvVM",
        "https://www.youtube.com/watch?v=x_M-aAKC0tc",
        "https://www.youtube.com/watch?v=nMNt227KgFA",
        "http://youtube.com/watch?v=hoQJWacRl_0",
        "https://www.youtube.com/watch?v=p7c0N7U7zNY",
    ]
    
    # Track overall statistics
    total_successful = 0
    total_failed = 0
    
    # Download from each channel
    print("\n" + "="*60)
    print("STARTING BATCH DOWNLOAD - 4 CHANNELS, 48 VIDEOS TOTAL")
    print("="*60)
    
    # Beat FM
    success, failed = download_batch(beat_fm_urls, "Beat FM", "Beat_FM")
    total_successful += success
    total_failed += failed
    
    # Nigeria Info FM
    success, failed = download_batch(nigeria_info_urls, "Nigeria Info FM", "Nigeria_Info_FM")
    total_successful += success
    total_failed += failed
    
    # Berekete
    success, failed = download_batch(berekete_urls, "Berekete", "Berekete")
    total_successful += success
    total_failed += failed
    
    # 3FM 92.7
    success, failed = download_batch(three_fm_urls, "3FM 92.7", "3FM_92.7")
    total_successful += success
    total_failed += failed
    
    # Final summary
    print("\n" + "="*60)
    print("ALL DOWNLOADS COMPLETE!")
    print("="*60)
    print(f"Total Videos: 48")
    print(f"Successful: {total_successful}")
    print(f"Failed: {total_failed}")
    print("="*60)