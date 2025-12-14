from db import get_connection

def report_songs_by_artist():
    name = input("Enter artist name: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT s.Title, a.Name
        FROM Song s
        JOIN Plays p ON s.SongID = p.SongID
        JOIN Artist a ON a.ArtistID = p.ArtistID
        WHERE a.Name = %s
    """, (name,))

    rows = cur.fetchall()
    print("\nSongs by Artist:")
    for r in rows:
        print(f"{r[0]} - {r[1]}")
    conn.close()


def report_artists_by_year():
    year = input("Enter album year: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT a.Name
        FROM Artist a
        JOIN Plays p ON a.ArtistID = p.ArtistID
        JOIN IsOn io ON p.SongID = io.SongID
        JOIN Album al ON io.AlbumID = al.AlbumID
        WHERE al.Year = %s
    """, (year,))

    rows = cur.fetchall()
    print("\nArtists with albums in that year:")
    for r in rows:
        print(r[0])
    conn.close()


def report_albums_by_category():
    category = input("Enter category name: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT al.Title, ar.Name
        FROM Album al
        JOIN IsOn io ON al.AlbumID = io.AlbumID
        JOIN Song s ON s.SongID = io.SongID
        JOIN IsIn ic ON ic.SongID = s.SongID
        JOIN Category c ON c.CategoryID = ic.CategoryID
        JOIN Plays p ON p.SongID = s.SongID
        JOIN Artist ar ON ar.ArtistID = p.ArtistID
        WHERE c.CategoryName = %s
    """, (category,))

    rows = cur.fetchall()
    print("\nAlbums with songs in category:")
    for r in rows:
        print(f"{r[0]} - by {r[1]}")
    conn.close()
