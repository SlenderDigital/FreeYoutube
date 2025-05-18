from pytubefix import YouTube
from app.schemas import Video
import re

def readable_size(size_in_bytes: int) -> str:
    """Convert bytes to human readable string."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} PB"

def readable_duration(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"

def available_resolution(video: Video, RESOLUTIONS: list) -> dict:
    available_resolution = {}
    try:# Create a YouTube object
        for res in RESOLUTIONS:
            stream = video.streams.filter(res=res).first()
            if stream:
                size = readable_size(stream.filesize) if stream.filesize else "Unknown"
                available_resolution[res] = size
    except Exception as e:
        print(f"Error processing video URL: {e}")
    return available_resolution

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[\\/*?:"<>|]', '_', filename)
