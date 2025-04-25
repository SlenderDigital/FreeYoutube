from fastapi import FastAPI, Query, HTTPException
from app.yt_logic import extract_video_info, download_yt_video
from app.config import VIDEO_STORAGE, readable_size

app = FastAPI()

@app.get("/yt/video-info")  
def get_video_info(video_url: str = Query(..., description="YouTube video URL")):
    try:
        print(f"Processing URL: {video_url}")
        Video = extract_video_info(video_url)
        return {"Video Info": Video}
    except Exception as e:
        return {"Unexpected Error": str(e)}
    
@app.get("/yt/video-info/size")
def get_video_size(title: str = Query(..., description="Title of the video")):
    """Search server storage for video by title"""
    target_file = VIDEO_STORAGE / f"{title}.mp4"
    
    if not target_file.exists():
        raise HTTPException(404, detail="Video not found")
    
    return {
        "title": title,
        "size": readable_size(target_file.stat().st_size)
    }
    
@app.post("/yt/download") # * Local Download
def get_video(
    video_url: str = Query(..., description="YouTube video URL"),
    resolution: int = Query(..., description="Video resolution")
):
    try:
        download_yt_video(video_url, resolution=resolution)
        return {"message": "Download finalized", "video_url": video_url, "resolution": resolution}
    except Exception as e:
        return {"error": str(e)}
