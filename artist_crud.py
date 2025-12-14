from db import get_connection

def create_artist():
    name = input("Enter artist name: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Artist (Name) VALUES (%s)", (name,))
    conn.commit()
    print("Artist created successfully!")
    conn.close()


def list_artists():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT ArtistID, Name FROM Artist ORDER BY ArtistID ASC")
    rows = cur.fetchall()

    print("\nAll Artists:")
    for r in rows:
        print(f"{r[0]} - {r[1]}")

    conn.close()


def update_artist():
    list_artists()
    artist_id = input("Enter ArtistID to update: ")
    name = input("Enter new name: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Artist SET Name=%s WHERE ArtistID=%s", (name, artist_id))
    conn.commit()
    print("Artist updated.")
    conn.close()


def delete_artist():
    list_artists()
    artist_id = input("Enter ArtistID to delete: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Artist WHERE ArtistID=%s", (artist_id,))
    conn.commit()
    print("Artist deleted.")
    conn.close()
