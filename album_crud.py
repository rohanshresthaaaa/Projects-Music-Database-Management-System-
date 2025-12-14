from db import get_connection

def create_album():
    title = input("Enter album title: ")
    year = input("Enter album year: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Album (Title, Year) VALUES (%s, %s)", (title, year))
    conn.commit()
    print("Album created!")
    conn.close()


def list_albums():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT AlbumID, Title, Year FROM Album ORDER BY AlbumID ASC")
    rows = cur.fetchall()

    print("\nAlbums:")
    for r in rows:
        print(f"{r[0]} - {r[1]} ({r[2]})")

    conn.close()



def update_album():
    list_albums()
    album_id = input("Enter AlbumID to update: ")
    title = input("New title: ")
    year = input("New year: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Album SET Title=%s, Year=%s WHERE AlbumID=%s",
                (title, year, album_id))
    conn.commit()
    print("Album updated.")
    conn.close()


def delete_album():
    list_albums()
    album_id = input("AlbumID to delete: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Album WHERE AlbumID=%s", (album_id,))
    conn.commit()
    print("Album deleted.")
    conn.close()