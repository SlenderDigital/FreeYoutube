from pydantic import BaseModel

class Format(BaseModel):
    resolution: int
    file_size: int
    ext: str

class Video(BaseModel):                         
    title: str
    # description: str | None = None        Maybe the Frontend will use it but it has to be reformated
    duration: str                
    formats: list[Format]         
    video_url: str                              
    file_path: str | None = None
    download_status: bool = False

