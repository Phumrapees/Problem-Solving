import streamlit as st
import os

# ---------- Setup ----------
SONG_FOLDER = "Songs"
os.makedirs(SONG_FOLDER, exist_ok=True)

# ---------- Song Class ----------
class Song:
    def __init__(self, title, artist, file_path):
        self.title = title
        self.artist = artist
        self.file_path = file_path
        self.next_song = None

    def __str__(self):
        return f"{self.title} - {self.artist}"

# ---------- Playlist Class ----------
class MusicPlaylist:
    def __init__(self):
        self.head = None
        self.current_song = None
        self.length = 0

    def add_song(self, title, artist, file_path):
        song = Song(title, artist, file_path)
        if not self.head:
            self.head = song
            self.current_song = song
        else:
            cur = self.head
            while cur.next_song:
                cur = cur.next_song
            cur.next_song = song
        self.length += 1

    def next_song(self):
        if not self.current_song:
            return
        self.current_song = (
            self.current_song.next_song
            if self.current_song.next_song
            else self.head
        )

    def prev_song(self):
        if self.current_song == self.head:
            return
        cur = self.head
        while cur.next_song != self.current_song:
            cur = cur.next_song
        self.current_song = cur

    def playlist_view(self):
        cur = self.head
        i = 1
        out = []
        while cur:
            mark = "▶️" if cur == self.current_song else ""
            out.append(f"{i}. {cur.title} - {cur.artist} {mark}")
            cur = cur.next_song
            i += 1
        return out

# ---------- Streamlit State ----------
if "playlist" not in st.session_state:
    st.session_state.playlist = MusicPlaylist()

if "current_audio" not in st.session_state:
    st.session_state.current_audio = None

# ---------- UI ----------
st.title("🎶 Music Playlist App")

# Sidebar - Add Song
st.sidebar.header("Add Song")
title = st.sidebar.text_input("Title")
artist = st.sidebar.text_input("Artist")
file = st.sidebar.file_uploader("Song file", type=["mp3", "wav", "ogg"])

if st.sidebar.button("Add"):
    if title and artist and file:
        path = os.path.join(SONG_FOLDER, file.name)
        with open(path, "wb") as f:
            f.write(file.getbuffer())
        st.session_state.playlist.add_song(title, artist, path)
        st.sidebar.success("Song added")
    else:
        st.sidebar.warning("Fill all fields")

# Playlist
st.header("📜 Playlist")
pl = st.session_state.playlist.playlist_view()
if pl:
    for s in pl:
        st.write(s)
else:
    st.write("No songs")

# Controls
st.markdown("---")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("⏪ Previous"):
        st.session_state.playlist.prev_song()
        cs = st.session_state.playlist.current_song
        if cs:
            st.session_state.current_audio = cs.file_path

with c2:
    if st.button("▶️ Play"):
        cs = st.session_state.playlist.current_song
        if cs:
            st.session_state.current_audio = cs.file_path

with c3:
    if st.button("⏩ Next"):
        st.session_state.playlist.next_song()
        cs = st.session_state.playlist.current_song
        if cs:
            st.session_state.current_audio = cs.file_path

# Fixed audio position (center)
st.markdown("---")
st.header("🎧 Now Playing")

if st.session_state.current_audio:
    with open(st.session_state.current_audio, "rb") as audio:
        st.audio(audio.read(), autoplay=True)
else:
    st.write("No song playing")

st.markdown("---")
st.write(f"Total songs: {st.session_state.playlist.length}")
