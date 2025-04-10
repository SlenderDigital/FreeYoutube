import yt_dlp
import json

def extract_video_info(video_url: str):
    """Extract video info including specific resolutions (480p, 720p, 1080p, 1440p, 2160p), title, description, duration, and file sizes."""
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(video_url, download=False)

        # Format duration as hours:minutes:seconds
        duration = info.get("duration", 0)
        formatted_duration = f"{duration // 3600}:{(duration % 3600) // 60}:{duration % 60}"

        video_details = {
            "title": info.get("title"),
            "description": info.get("description"),
            "duration": formatted_duration,
            "formats": []
        }

        # Resolutions to filter
        target_resolutions = {480, 720, 1080, 1440, 2160}
        best_formats = {}

        for fmt in info.get("formats", []):
            # Filter only mp4 formats and target resolutions
            if fmt.get("vcodec") != "none" and fmt.get("height") in target_resolutions and fmt.get("ext") == "mp4":
                resolution = fmt.get("height")
                file_size = fmt.get("filesize", 0)  # Keep raw file size as an integer
                if resolution not in best_formats or file_size > best_formats[resolution]["file_size"]:
                    best_formats[resolution] = {
                        "resolution": resolution,
                        "file_size": file_size,  # Store raw file size for comparison
                        "format_id": fmt.get("format_id"),
                        "ext": fmt.get("ext")
                    }

        # Format file sizes for output
        for fmt in best_formats.values():
            raw_size = fmt["file_size"]
            fmt["file_size"] = (
                f"{raw_size / (1024 ** 3):.2f} GB" if raw_size >= 1024 ** 3 else f"{raw_size / (1024 ** 2):.2f} MB"
            )

        video_details["formats"] = list(best_formats.values())

        # Export to JSON file
        with open("./video_info.json", "w") as json_file:
            json.dump(video_details, json_file, indent=4)

        return video_details
    except Exception as e:
        raise Exception(f"Error extracting video info: {str(e)}")

# Example usage
print(extract_video_info("https://youtu.be/V_qswK51Y54?si=xJqa-1kar9DUoNTo"))






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

