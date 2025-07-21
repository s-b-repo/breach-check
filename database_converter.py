import sqlite3
import os

db_file = "passwords.db"
txt_file = "rockyou2024.txt"

def import_to_db():
    if os.path.exists(db_file):
        print("DB already exists.")
        return

    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS passwords (pw TEXT PRIMARY KEY)")

    with open(txt_file, "r", encoding="utf-8", errors="ignore") as f:
        batch = []
        for i, line in enumerate(f):
            pw = line.strip()
            batch.append((pw,))
            if len(batch) == 100000:
                c.executemany("INSERT OR IGNORE INTO passwords (pw) VALUES (?)", batch)
                conn.commit()
                print(f"Inserted {i+1} passwords")
                batch.clear()
        if batch:
            c.executemany("INSERT OR IGNORE INTO passwords (pw) VALUES (?)", batch)
            conn.commit()

    c.execute("CREATE INDEX IF NOT EXISTS pw_idx ON passwords (pw)")
    conn.commit()
    conn.close()
    print("Import finished.")

if __name__ == "__main__":
    import_to_db()
