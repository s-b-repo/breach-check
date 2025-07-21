
# 🔒 Local Password Breach Checker

A **100% local, private, and blazing-fast** web app for checking if your password appears in a massive breach list (8+ billion passwords supported).  
Search your password securely—nothing ever leaves your computer!


---

## ✨ Features

- **Lightning-fast:** Search 8+ billion passwords instantly with SQLite index.
- **Modern UI:** Hacker-themed, mobile-friendly interface.
- **100% Private:** Runs on your machine. No cloud. No logging. No uploads.
- **Easy to use:** One-time import; then just run and search.
- **Secure by default:** Password field never shows input, no browser storage, no history.

---

## 🚀 Getting Started

### 1. Clone and Install Dependencies

```
git clone https://github.com/s-b-repo/breach-check.git
cd breach-check
pip install flask
````

### 2. Import Your Password List

> **Note:** Importing 8 billion lines may take several hours (but only needs to be done once).

Place your `.txt` file (one password per line) in the folder and update the filename in `import_to_db.py`.

```
python database_converter.py
```

This will create a local `passwords.db` SQLite database with a fast search index.

### 3. Run the Web App

```
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## password magnet link
magnet:?xt=urn:btih:4e3915a8ecf6bc174687533d93975b1ff0bde38a&dn=rockyou2024.zip&xl=48976652032

---

## 🛡️ Security Notes

* **Fully Local:** All checks happen on your machine, never sent anywhere.
* **Open Source:** Review or modify code to your requirements.
* **No logging:** No access logs, no tracking, no history, no cloud.
* **Password field:** Uses secure HTML `<input type="password">`.

**Want to hash passwords before storage/search for extra privacy?**
[See the FAQ below](#faq).

---

## ⚙️ Advanced Usage

* Supports any size `.txt` file (as big as your disk allows)
* UI is fully responsive and dark themed
* For **ultra-huge lists**, consider SSD for best performance

---

## 📖 FAQ

**Q: Is this the same as HaveIBeenPwned?**
A: No—this is *local only* and never queries any remote service.

**Q: Can I hash my password before checking?**
A: Yes, the app can be modified to hash with SHA1/SHA256 (see comments in code).

**Q: Can I use LevelDB/RocksDB or Bloom filters for even faster performance?**
A: Yes! Open an issue or PR, or ask for sample code.

---

## 💡 Credits

* UI inspired by cyberpunk/hacker themes
* Developed in Python & Flask
* Made with ❤️ for privacy by \[your name or team]

---

## 📜 License

MIT License. See [LICENSE](LICENSE).

```

---
