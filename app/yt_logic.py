import yt_dlp

def extract_video_info(video_url):
    """Extract video info without downloading."""
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        return ydl.extract_info(video_url, download=False)

async def get_available_resolutions(video_url):
    """Fetch available resolutions asynchronously."""
    try:
        # Use yt_dlp asynchronously
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = await ydl.extract_info(video_url, download=False)  # Ensure this is awaited if supported
        
        resolutions = set()
        for fmt in info.get('formats', []):
            if fmt.get('vcodec') != 'none':  # Video formats only
                res = fmt.get('height')
                if res and res >= 720:  # Only consider resolutions up to 720p
                    resolutions.add(res)
        return sorted(resolutions, reverse=True)
    except Exception as e:
        raise e


def download_video(video_url, save_path="/videos", resolution=None):
    """Download video with specified resolution."""
    try:
        info = extract_video_info(video_url)
        if resolution:
            ydl_opts = {
                'format': f'bestvideo[height={resolution}]+bestaudio/best',
                'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                'merge_output_format': 'mp4',
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            print(f"\n✅ Download complete! Saved in: {save_path}")
        else:
            print("Resolution must be specified for download.")
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
