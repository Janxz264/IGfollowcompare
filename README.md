# IGfollowcompare
Compare raw JSON lists from IG to textdiff for unmatching followers/following accounts.

# Instagram Follower Diff Tool

🧭 A lightweight, local script to compare your Instagram **followers** and **following** lists using the official data export. Helps identify:

- Accounts that don’t follow you back (`following - followers`)
- Accounts that follow you but you don’t follow (`followers - following`)

⚠️ This tool does **not** scrape or use the Instagram API, and respects platform limitations. It’s safe for personal use and requires zero login or automation.

---

## ✨ Features

- Parses Instagram's downloaded JSON archive
- Outputs clean lists for:
  - ✅ Not following you back
  - ✅ Fans you don't follow
- No network requests, login, or scraping
- Supports multiple `followers_*.json` files
- Can be extended for historical tracking or GUI

---

## 🛠 Requirements

- Python 3.x
- Instagram data archive (JSON format)

---

## 📥 How to Use

1. [Request your Instagram data](https://www.instagram.com/download/request/) → Select **JSON** format
2. Extract the ZIP archive
3. Run the script:

```bash
python compare.py /path/to/extracted/data```

Example:
```bash
python compare.py "C:\Users\jan\Downloads\instagram-myacc" ```

Following: 543
Followers: 521

Not following you back (41):
- username1
- username2
...

Fans you don't follow (19):
- fanA
- fanB
...