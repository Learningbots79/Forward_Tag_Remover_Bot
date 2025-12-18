<div align="center">

<a href="https://files.catbox.moe/se9021.jpg">
  <img src="https://files.catbox.moe/se9021.jpg" width="300" height="300" />
</a>

![Stars](https://img.shields.io/github/stars/LearningBotsOfficial/Forward_Tag_Remover_Bot)
![Forks](https://img.shields.io/github/forks/LearningBotsOfficial/Forward_Tag_Remover_Bot)

----------------------------------------------------
A **Forward Tag Remover Bot** built with **Pyrogram** + **MongoDB**

</div>

---

## ⭐ Features
- 🚫 **Removes Forward Tags** from any forwarded message  
- 📂 Supports **all media types**: text, photo, video, audio, sticker, documents  
- 👤 **Automatic User Saving** in MongoDB  
- 🔒 **Force Subscribe System**  
- 📢 **Owner-Only Broadcast System**  
- ⚡ **Pyrogram async optimized**  
- 🧩 Fully modular structure with handlers  

---

<details>
<summary><b>🔸 Deploy on VPS / Localhost</b></summary>

### 1. Fork & Star ⭐  
- Click **Fork**  
- Click **Star** ⭐ to support this project  

---

### 2. Get Your Fork URL
https://github.com/LearningBotsOfficial/Forward_Tag_Remover_Bot


---

### 3. Setup Your VPS  
Install system packages:

~~~
sudo apt update && sudo apt upgrade -y
~~~
~~~
sudo apt install -y git python3 python3-pip python3-venv tmux nano
~~~

---

### 4. Clone Your Fork
~~~
git clone your_fork_repo
~~~
~~~
cd Forward_Tag_Remover_Bot
~~~
~~~
python3 -m venv venv
~~~
~~~
source venv/bin/activate
~~~
---

### 5. Install Dependencies
~~~
pip install --upgrade pip && pip install -r requirements.txt
~~~
---

### 6. Configure the Bot
~~~
nano config.py
~~~
⚙️ required fields

API_ID = your_api_id
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
OWNER_ID = 123456789
BOT_USERNAME = "your_bot_username"
FORCE_SUB_CHANNELS = ["yourchannel"]
UPDATES_CHANNEL = "your_updates_channel"
DEV_USERNAME = "your_username"
MONGO_URI = "your_mongo_uri"
DB_NAME = "ForwardRemoverBot"


Save → `Ctrl + O`  
Exit → `Ctrl + X`

---

### 7. Run the Bot
~~~
tmux new -s tagbot
~~~
~~~
source venv/bin/activate
~~~
~~~
python3 main.py
~~~

➡️ Detach (keep running): `Ctrl + B`, then `D`

</details>


---

## ---------------------

## 📱 Connect with Me

<p align="center">
<a href="https://www.instagram.com/learning_bots"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href="https://t.me/LearningBotsCommunity"><img src="https://img.shields.io/badge/Telegram%20Group-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
<a href="https://t.me/learning_bots"><img src="https://img.shields.io/badge/Telegram%20Channel-0088cc?style=for-the-badge&logo=telegram&logoColor=white"></a>
<a href="https://youtube.com/@learning_bots?si=aNUuRSfZD7na78GM"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>
</p>

---

## ⚠️ License / Usage Terms

This project is open-source under a **custom license** by [Yash](https://github.com/LearningBotsOfficial).

✅ You Can:
- Use this code for personal or educational purposes  
- Host your own version **with proper credits**  
- Modify or improve the code (while keeping credit intact)

🚫 You Cannot:
- Remove author credits or change project name  
- Sell, rent, or resell this code or any modified version  
- Claim ownership or re-upload it without permission  

If you want to use this project commercially,  
please contact the author at [LearningBotsOfficial](https://t.me/LearningBotsOfficial).

---

**Author:** [LearningBotsOfficial](https://github.com/LearningBotsOfficial)  
**Support Group:** [@LearningBotsCommunity](https://t.me/LearningBotsCommunity)  
**Update Channel:** [@learning_bots](https://t.me/learning_bots)  
**YouTube:** [Learning Bots](https://youtube.com/@learning_bots)


<div align="center">

## ---------------------

<a href="https://files.catbox.moe/wpaoo2.jpg" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45" width="190" alt="Buy Me a Coffee" />
</a>

</div>
