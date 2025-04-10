from fastapi import FastAPI
from pydantic import BaseModel
from app.yt_logic import get_available_resolutions, extract_video_info

app = FastAPI()

@app.get("/yt/video-info/{video_url}")
async def get_video_info(video_url: str):
    try:
        video_info = await extract_video_info(video_url)  # Await the async function
        return {
            "title": video_info.get("title"),
            "duration": video_info.get("duration"),
            "thumbnail": video_info.get("thumbnail"),
            "description": video_info.get("description"),
            "formats": video_info.get("formats")
        }
    except Exception as e:
        return {"error": str(e)}


@app.get("/yt/qualities/{video_url}")
async def get_resolutions(video_url: str): 
    try:
        resolutions = await get_available_resolutions(video_url)  # Await the async function
        return {"resolutions": resolutions}
    except Exception as e:
        return {"error": str(e)}
    


@app.post("/yt-link/qualities/")
async def read_item():
    return {"item_id": "", "q": "sss"}



@app.post("/yt/download/{video_url}/{resolution}")
async def download_video_endpoint(video_url: str, resolution: int):
    try:
        from app.yt_logic import download_video
        await download_video(video_url, resolution=resolution)  # Await if download_video is async
        return {"message": "Download initiated."}
    except Exception as e:
        return {"error": str(e)}
