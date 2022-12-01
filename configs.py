import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.
    
    
    
🤖 My Name: <a href='https://t.me/search_mdisk_bot'>Mdisk Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>Help</b>
<b>Join our Group @mx_movie_request</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @MX_Networks</a></b>
"""


    START_MSG = """
<b>𝐇𝐞𝐥𝐥𝐨 { }

🍿Welcome to the largest movies and series search engine on the net!

👻 Send me a movie or series name to search...🍳

👉 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐥𝐬𝐨 𝒂𝒅𝒅 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 𝐢𝐧 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑𝒔 𝐰𝐢𝐭𝐡 𝒚𝒐𝒖𝒓 𝒍𝒊𝒏𝒌𝒔.

📌 For More Info :- @Ayita_P_S</b>
"""

