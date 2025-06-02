import os
import re

def sanitize_filename(filename):
    name, ext = os.path.splitext(filename)
    name = name.lower().replace(' ', '_')
    name = re.sub(r'[^a-z0-9_\-]', '', name)  # keep alphanum, _ and -
    return name + ext.lower()

def create_m3u_file(playlist_folder):
    mp3_files = [f for f in os.listdir(playlist_folder)
                 if f.lower().endswith(".mp3") and not f.startswith("._")]
    if not mp3_files:
        return

    sanitized_entries = []
    for original in mp3_files:
        sanitized = sanitize_filename(original)
        original_path = os.path.join(playlist_folder, original)
        sanitized_path = os.path.join(playlist_folder, sanitized)

        # Rename if necessary
        if original != sanitized:
            os.rename(original_path, sanitized_path)
            print(f"Renamed: {original} -> {sanitized}")
        sanitized_entries.append(sanitized)

    sanitized_entries.sort()
    lines = [f"{entry}\r\n" for entry in sanitized_entries]

    folder_name = os.path.basename(playlist_folder)
    m3u_path = os.path.join(playlist_folder, f"{folder_name.upper()}.M3U")
    with open(m3u_path, "w", encoding="utf-8-sig", newline='') as f:
        f.writelines(lines)

    print(f"Created playlist: {m3u_path}")

def main():
    music_root = input("Enter the path to the Music/ folder on the SanDisk: ").strip()
    if not os.path.isdir(music_root):
        print("Invalid folder path.")
        return

    for root, dirs, _ in os.walk(music_root):
        for d in dirs:
            folder_path = os.path.join(root, d)
            create_m3u_file(folder_path)
        break  # Only process first level of folders inside Music/

if __name__ == "__main__":
    main()
