import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Developer Credentials
SPOTIFY_CLIENT_ID = 'd78245b856764a3f80754d64e8c68021'
SPOTIFY_CLIENT_SECRET = '046d9b61035042088aa15eb6135d3f8e'
SPOTIFY_REDIRECT_URI = 'http://127.0.0.1:8000/callback'

# Define the needed scope to read user's playlists and tracks
scope = "playlist-read-private playlist-read-collaborative"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=scope
))

def fetch_all_user_playlists():
    playlists = []
    results = sp.current_user_playlists()
    while results:
        playlists.extend(results['items'])
        if results['next']:
            results = sp.next(results)
        else:
            break
    return playlists


def fetch_tracks_from_playlist(playlist_id):
    tracks = []
    results = sp.playlist_items(playlist_id)
    while results:
        for item in results['items']:
            track = item.get('track')
            if not track:
                continue

            title = track.get('name', 'Unknown Title')

            # Check if it's a music track with artists
            if 'artists' in track:
                artists = ', '.join(artist['name'] for artist in track['artists'])
                tracks.append(f"{artists} - {title}")
            else:
                # It's probably a podcast or non-music item
                tracks.append(f"[NON-MUSIC] {title}")

        if results['next']:
            results = sp.next(results)
        else:
            break
    return tracks


def main():
    playlists = fetch_all_user_playlists()
    print(f"Found {len(playlists)} playlists.")
    all_tracks = []

    for pl in playlists:
        name = pl['name']
        print(f"📂 Fetching: {name}")
        tracks = fetch_tracks_from_playlist(pl['id'])
        all_tracks.append(f"\n=== {name} ===")
        all_tracks.extend(tracks)

    # Save to file
    with open('all_playlist_songs.txt', 'w', encoding='utf-8') as f:
        for line in all_tracks:
            f.write(line + '\n')
    print("✅ Saved all songs to all_playlist_songs.txt")

if __name__ == '__main__':
    main()
