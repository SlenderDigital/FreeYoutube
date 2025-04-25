from pathlib import Path

"""DIRECTORIES"""
VIDEO_STORAGE = Path("app/videos")

"""FUNCTIONS"""

# * Get readable size
def readable_size(size_in_bytes: int) -> str:
    """Convert bytes to human readable string."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} PB"
