import asyncio
import importlib
import os
from threading import Thread
from flask import Flask
from pyrogram import Client, idle
from aiohttp import ClientSession  # New Import

# Zaid package ko import karna padega taaki variable update kar sakein
import Zaid 
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, app, ids

# --- Flask Keep Alive Setup ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Zaid Bot Is Running Successfully!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.start()
# ------------------------------

async def start_bot():
    print("LOG: Initializing Client Session...")
    
    # --- FIX: Session yahan create karein ---
    if Zaid.aiosession is None:
        Zaid.aiosession = ClientSession()
    # ----------------------------------------

    await app.start()
    print("LOG: Founded Bot token Booting ◉ 𝐎𝐕𝐄𝐑 𝐏𝐎𝐖𝐄𝐑𝐄𝐃 ◉")
    
    for all_module in ALL_MODULES:
        importlib.import_module("Zaid.modules" + all_module)
        print(f"Successfully Imported ◉ 𝐎𝐕𝐄𝐑 𝐏𝐎𝐖𝐄𝐑𝐄𝐃 ◉ {all_module} 💥")
        
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
            
    await idle()
    
    # Bot band hone par session close karein
    await Zaid.aiosession.close()

if __name__ == "__main__":
    print("LOG: Starting Flask Server...")
    keep_alive()
    
    print("LOG: Starting Pyrogram Loop...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    
