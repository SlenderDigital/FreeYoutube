from pydantic import BaseModel

class Format(BaseModel):
    resolution: str
    file_size: str

class Video(BaseModel):                         
    title: str
    duration: str                
    formats: list[Format]         
    video_url: str                              
    file_path: str | None = None
    download_status: bool = False

