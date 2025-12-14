from artist_crud import *
from album_crud import *
from category_crud import *
from song_crud import *
from reports import *

def main():
    while True:
        print("\n==== MENU ====")
        print("1. Artist CRUD")
        print("2. Album CRUD")
        print("3. Category CRUD")
        print("4. Song CRUD")
        print("5. Reports")
        print("0. Exit")

        choice = input("Choice: ")

        
        # ARTIST CRUD
       
        if choice == "1":
            print("\n1. Create Artist")
            print("2. List Artists")
            print("3. Update Artist")
            print("4. Delete Artist")
            sub = input("Choice: ")

            if sub == "1": create_artist()
            elif sub == "2": list_artists()
            elif sub == "3": update_artist()
            elif sub == "4": delete_artist()

      
        # ALBUM CRUD
       
        elif choice == "2":
            print("\n1. Create Album")
            print("2. List Albums")
            print("3. Update Album")
            print("4. Delete Album")
            sub = input("Choice: ")

            if sub == "1": create_album()
            elif sub == "2": list_albums()
            elif sub == "3": update_album()
            elif sub == "4": delete_album()

       
        # CATEGORY CRUD
      
        elif choice == "3":
            print("\n1. Create Category")
            print("2. List Categories")
            print("3. Update Category")
            print("4. Delete Category")
            sub = input("Choice: ")

            if sub == "1": create_category()
            elif sub == "2": list_categories()
            elif sub == "3": update_category()
            elif sub == "4": delete_category()

        
        # SONG CRUD
       
        elif choice == "4":
            print("\n1. Create Song")
            print("2. List Songs")
            print("3. Update Song")
            print("4. Delete Song")
            sub = input("Choice: ")

            if sub == "1": create_song()
            elif sub == "2": list_songs()
            elif sub == "3": update_song()
            elif sub == "4": delete_song()

       
        # REPORTS
       
        elif choice == "5":
            print("\n1. Songs by Artist")
            print("2. Artists by Year")
            print("3. Albums by Category")
            sub = input("Choice: ")

            if sub == "1": report_songs_by_artist()
            elif sub == "2": report_artists_by_year()
            elif sub == "3": report_albums_by_category()

        elif choice == "0":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

main()