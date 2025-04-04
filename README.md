# 🥳 Party Planner Web App

Welcome to the **Party Planner** web application! This simple and fun project lets users select party essentials, calculate a unique party code using bitwise operations, and receive a custom message based on their selections — all through a user-friendly web interface!

---

## 🚀 Features

- ✅ Displays a predefined list of 15 party items.
- ✅ Allows users to select items using checkboxes.
- ✅ Calculates a **Base Party Code** using the bitwise AND (`&`) operation.
- ✅ Adjusts the code with conditional logic and returns a fun message.
- ✅ Shows the server's **public IP address** on the form.
- ✅ Renders the final output in clean, styled HTML.

---

## 📦 Files Included

- `party_form.php`  
  → Frontend form using HTML + PHP to collect user selections.

- `party_planner.py`  
  → Backend CGI Python script to process selections and render results in HTML.

---

## 🧠 Party Item Index & Bitwise Values

| Index | Item              | Bitwise Value |
|-------|-------------------|----------------|
| 0     | Cake              | 20             |
| 1     | Balloons          | 21             |
| 2     | Music System      | 10             |
| 3     | Lights            | 5              |
| 4     | Catering Service  | 8              |
| 5     | DJ                | 3              |
| 6     | Photo Booth       | 15             |
| 7     | Tables            | 7              |
| 8     | Chairs            | 12             |
| 9     | Drinks            | 6              |
| 10    | Party Hats        | 9              |
| 11    | Streamers         | 18             |
| 12    | Invitation Cards  | 4              |
| 13    | Party Games       | 2              |
| 14    | Cleaning Service  | 11             |

---

## 🧮 Logic & Messages

1. Bitwise AND is performed across selected item values.
2. Based on the result (`base_code`), a message is shown:
   - `base_code == 0` → Add `5`, message: **"Epic Party Incoming!"**
   - `base_code > 5` → Subtract `2`, message: **"Let's keep it classy!"**
   - `1 ≤ base_code ≤ 5` → Message: **"Chill vibes only!"**

---

## 🌐 Usage

### 🛠 Requirements
- PHP-enabled web server
- CGI support for Python scripts
- Python 3 installed
- `curl` command available for fetching public IP

### 📂 Setup

1. Place `party_form.php` and `party_planner.py` in your web server directory.
2. Make `party_planner.py` executable:
   ```bash
   chmod +x party_planner.py

~ Have Fun ~

Nelson!
😁