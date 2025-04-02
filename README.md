
# YouTube Video Downloader Android App

![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-0095D5?style=for-the-badge&logo=kotlin&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

A professional Android application for downloading YouTube videos with advanced features and secure architecture.

## 📱 App Features
- **In-app YouTube browsing** with integrated search
- **Quality selection** (360p to 4K)
- **Background downloads** using WorkManager
- **Download management** (organize/delete videos)
- **Offline playback** with ExoPlayer
- **Playlist support** for bulk downloads

## 🛠 Technical Stack
| Component            | Technology                          |
|----------------------|-------------------------------------|
| Frontend             | Android (Kotlin)                    |
| Backend              | Python (FastAPI)                    |
| Database             | PostgreSQL                          |
| Video Processing     | youtube-dl                          |
| Local Cache          | Room Database                       |
| API Communication    | Retrofit + OkHttp                   |

## 📂 Project Structure
```
Service/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── models/
│   │   ├── database/
│   │   │   └── postgresql.py
│   │   └── utils/
│   │       └── youtube_dl_wrapper.py
├── android-app/
│   ├── app/
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── kotlin/
│   │   │   │   │   └── com/
│   │   │   │   │       └── example/
│   │   │   │   │           ├── di/
│   │   │   │   │           ├── ui/
│   │   │   │   │           ├── network/
│   │   │   │   │           └── service/
│   │   │   │   └── res/
│   │   │   └── androidTest/
│   ├── gradle/
│   └── build.gradle.kts
└── README.md
```

## 🚀 Implementation Details

### Backend (Python)
- **FastAPI** endpoints for:
  - `/search` - Video search
  - `/video-info` - Metadata retrieval
  - `/download` - Download initiation
- youtube-dl integration for format conversion
- PostgreSQL connection pooling

### Database Schema
```
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    hashed_password TEXT
);

CREATE TABLE downloads (
    id SERIAL PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    video_id TEXT,
    quality VARCHAR(10),
    download_date TIMESTAMP
);
```

### Frontend (Android)
```
// Example WorkManager implementation
val downloadRequest = OneTimeWorkRequestBuilder()
    .setInputData(
        workDataOf(
            "videoUrl" to videoUrl,
            "quality" to selectedQuality
        )
    )
    .build()

WorkManager.getInstance(context).enqueue(downloadRequest)
```

## 🔒 Security
- JWT authentication flow
- HTTPS enforcement via Nginx reverse proxy
- API key encryption using Android Keystore
- Regular security audits with OWASP ZAP

## ⚖ Legal Notice
> **Important**: This app is intended for personal use only. Downloading copyrighted content without permission may violate [YouTube's Terms of Service](https://www.youtube.com/t/terms) and applicable copyright laws. Users are solely responsible for the content they download.

## 🛠 Installation

### Backend Setup
```
docker-compose up -d
export YT_API_KEY=your_api_key
uvicorn app.main:app --reload
```

### Android Requirements
```
dependencies {
    implementation 'com.squareup.retrofit2:retrofit:2.9.0'
    implementation 'androidx.work:work-runtime-ktx:2.7.1'
    implementation 'com.google.android.exoplayer:exoplayer:2.18.1'
}
```

## 🚧 Future Roadmap
- [ ] Instagram video download support
- [ ] Cross-device sync via Firebase
- [ ] Smart quality recommendations
- [ ] Download scheduling system

