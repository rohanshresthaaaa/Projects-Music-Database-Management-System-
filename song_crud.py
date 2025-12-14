from db import get_connection
from artist_crud import list_artists
from category_crud import list_categories
from album_crud import list_albums

def create_song():
    title = input("Enter song title: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Song (Title) VALUES (%s)", (title,))
    conn.commit()

    song_id = cur.lastrowid
    print(f"\nSong created! SongID = {song_id}")

    # Links to artist
    print("\nSelect Artist:")
    list_artists()
    artist_id = input("Enter ArtistID: ")
    cur.execute("INSERT INTO Plays (SongID, ArtistID) VALUES (%s, %s)", (song_id, artist_id))

    # Links to category
    print("\nSelect Category:")
    list_categories()
    category_id = input("Enter CategoryID: ")
    cur.execute("INSERT INTO IsIn (SongID, CategoryID) VALUES (%s, %s)", (song_id, category_id))

    # Links to album
    print("\nSelect Album:")
    list_albums()
    album_id = input("Enter AlbumID: ")
    cur.execute("INSERT INTO IsOn (SongID, AlbumID) VALUES (%s, %s)", (song_id, album_id))

    conn.commit()
    print("Song fully linked!")
    conn.close()


def list_songs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT SongID, Title
        FROM Song
        ORDER BY SongID ASC
    """)
    rows = cur.fetchall()

    print("\nSongs:")
    for r in rows:
        print(f"{r[0]} - {r[1]}")

    conn.close()


def update_song():
    list_songs()
    song_id = input("\nEnter SongID to update: ")

    print("\n1. Update song title")
    print("2. Change song's artist")
    print("3. Change song's category")
    print("4. Change song's album")
    choice = input("Choice: ")

    conn = get_connection()
    cur = conn.cursor()

    # Updates title
    if choice == "1":
        new_title = input("Enter new song title: ")
        cur.execute("UPDATE Song SET Title=%s WHERE SongID=%s", (new_title, song_id))
        conn.commit()
        print("Song title updated.")

    # Updates artist
    elif choice == "2":
        print("\nSelect new artist:")
        list_artists()
        new_artist = input("Enter new ArtistID: ")

        # Deletes old artist link
        cur.execute("DELETE FROM Plays WHERE SongID=%s", (song_id,))
        # Inserts new link
        cur.execute("INSERT INTO Plays (SongID, ArtistID) VALUES (%s, %s)", (song_id, new_artist))
        conn.commit()
        print("Song artist updated.")

    # Updates category
    elif choice == "3":
        print("\nSelect new category:")
        list_categories()
        new_cat = input("Enter new CategoryID: ")

        cur.execute("DELETE FROM IsIn WHERE SongID=%s", (song_id,))
        cur.execute("INSERT INTO IsIn (SongID, CategoryID) VALUES (%s, %s)", (song_id, new_cat))
        conn.commit()
        print("Song category updated.")

    # Updates album
    elif choice == "4":
        print("\nSelect new album:")
        list_albums()
        new_album = input("Enter new AlbumID: ")

        cur.execute("DELETE FROM IsOn WHERE SongID=%s", (song_id,))
        cur.execute("INSERT INTO IsOn (SongID, AlbumID) VALUES (%s, %s)", (song_id, new_album))
        conn.commit()
        print("Song album updated.")

    conn.close()


def delete_song():
    list_songs()
    song_id = input("\nEnter SongID to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM Plays WHERE SongID=%s", (song_id,))
    cur.execute("DELETE FROM IsIn WHERE SongID=%s", (song_id,))
    cur.execute("DELETE FROM IsOn WHERE SongID=%s", (song_id,))


    cur.execute("DELETE FROM Song WHERE SongID=%s", (song_id,))
    conn.commit()

    print("Song deleted successfully.")
    conn.close()