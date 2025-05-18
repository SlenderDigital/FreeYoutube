from pytubefix import YouTube
from app.youtube.utils import *
from app.schemas import *
from app.config import RESOLUTIONS, VIDEO_STORAGE
import os
import subprocess

def fetch_video_info(video_url: str) -> Video:

    video = YouTube(video_url)
    resolutions = available_resolution(video, RESOLUTIONS)
    
    return Video(
        title=video.title,
        duration=readable_duration(video.length),
        formats=[
            Format(
                resolution=res,
                file_size=size
            ) for res, size in resolutions.items()
        ],
        video_url=video_url,
        file_path=None,
        download_status=False
    )

def download_video(url, resolution):
    try:
        print("Connecting to YouTube...")
        video = YouTube(url)
        
        # Get the video stream
        video_stream = video.streams.filter(res=resolution, only_video=True).first()
        # Get the audio stream
        audio_stream = video.streams.filter(only_audio=True).first()
        
        if not video_stream:
            print(f"{resolution} stream not available for this video.")
            return
            
        if not audio_stream:
            print("Audio stream not available for this video.")
            return
            
        print(f"Downloading: {video.title}")
        
        # Sanitize the video title for use as a filename
        sanitized_title = sanitize_filename(video.title)
        
        # Download video and audio separately
        video_file = video_stream.download(output_path=VIDEO_STORAGE, filename_prefix="video_")
        audio_file = audio_stream.download(output_path=VIDEO_STORAGE, filename_prefix="audio_")
        
        # Output filename
        output_file = os.path.join(VIDEO_STORAGE, f"{sanitized_title}_{resolution}.mp4")
        
        # Merge video and audio using ffmpeg
        print("Merging video and audio...")
        subprocess.run([
            'ffmpeg', '-i', video_file, 
            '-i', audio_file, 
            '-c:v', 'copy',
            '-c:a', 'aac',
            output_file,
        ], check=True)
        
        # Clean up temporary files
        os.remove(video_file)
        os.remove(audio_file)
        
        print(f"Download and merge complete! File saved at: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")