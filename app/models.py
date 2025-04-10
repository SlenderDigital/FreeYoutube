from pydantic import BaseModel

class video(BaseModel):                 ## * Properties for backend logic managment
    video_url: str                      ## * Why the video_url matter
    resolutions: list[int]              ## * Why there's multiple resolutions and not just a single one
    title: str
    duration: int | None = None         ## * Why the duration is optional       |    Needed for optimistic network communication
    file_size: int | None = None        ## * Why the file_size is optional      |    Needed for optimistic network communication
    file_path: str 
    download_status: bool = False       # TODO: frontend have to check this in local user storage but needed for deleted item in history