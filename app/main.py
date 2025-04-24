from fastapi import FastAPI
from app.yt_logic import extract_video_info

app = FastAPI()

@app.get("/yt/video-info")
def get_video_info(video_url = "https://youtu.be/GEDSmE9KSHI?si=ejh8skpuMMOqfTQN"):
    try:
        Video = extract_video_info(video_url)  # Call the sync function
        return {"Video Info": Video}
    except Exception as e:
        return {"Unexpected Error": str(e)}
    
@app.post("/yt/download/{video_url}/{resolution}")
def download_video(video_url: str, resolution: int | None):
    try:
        if resolution:
            download_video(video_url, resolution)
            return {"message": "Download started"}
        else:
            return {"error": "Resolution must be specified for download."}
    except Exception as e:
        return {"error": str(e)}

@app.get("/yt/test")
def test():
    return {"message": "Hello, World!"}