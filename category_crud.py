from db import get_connection

def create_category():
    name = input("Enter category name: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Category (CategoryName) VALUES (%s)", (name,))
    conn.commit()
    print("Category created!")
    conn.close()


def list_categories():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT CategoryID, CategoryName FROM Category ORDER BY CategoryID ASC")
    rows = cur.fetchall()

    print("\nCategories:")
    for r in rows:
        print(f"{r[0]} - {r[1]}")

    conn.close()


def update_category():
    list_categories()
    cid = input("Enter CategoryID to update: ")
    name = input("Enter new name: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE Category SET CategoryName=%s WHERE CategoryID=%s", (name, cid))
    conn.commit()
    print("Category updated.")
    conn.close()


def delete_category():
    list_categories()
    cid = input("CategoryID to delete: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Category WHERE CategoryID=%s", (cid,))
    conn.commit()
    print("Category deleted.")
    conn.close()