# Sandisk M3U Generator

This simple script can be used to create or update `.m3u` playlist files for your SanDisk Clip Sport when new music is added.

---

## 🚀 How to Use

1. Run `main.py` using Python:
   ```bash
   python main.py
   ```

2. When prompted, enter the **absolute path** to your SanDisk `MUSIC` folder.

---

## 📁 Folder Structure

Your music should be organized like this:

```plaintext
Music/
├── Playlist1/
│   ├── song1.mp3
│   ├── song2.mp3
│   └── ...
├── Playlist2/
│   ├── another1.mp3
│   ├── another2.mp3
│   └── ...
└── ...
```

Each subfolder of `Music/` is treated as a separate playlist, and a `.M3U` file will be created inside each one using the correct:

- **Encoding:** UTF-8 with BOM  
- **Line endings:** CRLF (`\r\n`)  
- **Path format:** Just the filename (e.g., `song1.mp3`)  
- **Sanitized filenames:** Special characters are removed, and spaces are replaced with underscores  

---

## ✅ Output Example

For each playlist folder, a file named `PLAYLISTNAME.M3U` (in all caps) is generated, for example:

```plaintext
Music/
└── Chill/
    ├── chill_song_1.mp3
    ├── chill_song_2.mp3
    └── CHILL.M3U
```

This ensures compatibility with SanDisk devices that are picky about encoding and path format.
