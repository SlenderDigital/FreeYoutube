from fastapi import FastAPI, Query
from app.youtube.yt_logic import fetch_video_info, download_video

app = FastAPI()

@app.get("/yt/video-info")  
def get_video_info(video_url: str = Query(..., description="YouTube video URL")):
    try:
        print(f"Processing URL: {video_url}")
        Video = fetch_video_info(video_url)
        return {"Video Info": Video}
    except Exception as e:
        return {"Unexpected Error": str(e)}

@app.post("/yt/download")
def upload_video(
    video_url: str = Query(..., description="YouTube video URL"), 
    resolution: str = Query(..., description="Resolution to download")
    ):


    try:
        print(f"Downloading URL: {video_url}")
        Video = download_video(video_url, resolution)
        return {"Video Info": Video}
    except Exception as e:
        return {"Unexpected Error": str(e)}