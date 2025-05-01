import yt_dlp
from app.schemas import Video, Format
from app.config import readable_size


def fetch_video_info(video_url: str):
    """Fetch video metadata using yt_dlp."""
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            return ydl.extract_info(url=video_url, download=False)
    except Exception as e:
        raise Exception(f"Failed to fetch video info: {str(e)}")

def format_duration(raw_duration: int) -> str:
    """Format duration as hours:minutes:seconds."""
    return f"{raw_duration // 3600}:{(raw_duration % 3600) // 60}:{raw_duration % 60}"

def filter_formats(formats: list, target_resolutions: set) -> list[Format]:
    """Filter and process video formats."""
    best_formats = {}

    for fmt in formats:
        if fmt.get("vcodec") != "none" and fmt.get("height") in target_resolutions and fmt.get("ext") == "mp4":
            resolution = fmt.get("height")
            file_size = fmt.get("filesize") or 0  # Handle missing filesize

            # Keep the best format for each resolution
            if resolution not in best_formats or file_size > best_formats[resolution].file_size:
                best_formats[resolution] = Format(
                    resolution=str(resolution),  # Convert to string
                    file_size=str(file_size),  # Convert to string
                    ext=fmt.get("ext"),
                    format_id=fmt.get("format_id")
                )

    # Convert file sizes to human-readable format
    for fmt in best_formats.values():
        fmt.file_size = readable_size(int(fmt.file_size))

    return list(best_formats.values())

def extract_video_info(video_url: str) -> Video:
    """Extract video information and return a Video object."""
    info = fetch_video_info(video_url)

    # Filter formats
    target_resolutions = {480, 720, 1080, 1440, 2160}
    formats = filter_formats(info.get("formats", []), target_resolutions)

    # Create Video object
    video_details = Video(
        title = info.get("title"),
        description = info.get("description"),
        duration = format_duration(info.get("duration", 0)),
        formats=formats,
        video_url=video_url,
        download_status=False 
    )

    return video_details

def download_yt_video(video_url: str, save_path="videos/", resolution=int|None):
    """Download video with the specified resolution."""
    try:
        video_info = extract_video_info(video_url)

        if resolution:
            ydl_opts = {
                'format': f'bestvideo[height={resolution}]+bestaudio/best',
                'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                'merge_output_format': 'mp4',
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            print(f"Download complete! Saved in: {save_path}")
        else:
            print("Resolution must be specified for download.")
    except Exception as e:
        print(f"Error: {str(e)}")

