refer link : https://t.me/hamsTer_kombat_bot/start?startapp=kentId6825195625

cerdit to chatgpt for fixing my english and generating this text lol

## Overview

The **Hamster Combat Automation Bot**  will automate tasks in Hamster Combat. it was code to be hosted in cloud 24/7.

## Features
- **Auto Tap**: Automatically tap.
- **Auto Claim Daily Rewards**: Ensures you never miss a daily reward.
- **Auto Cipher**: auto claim/complete chiper.
- **Auto Upgrade with Priority Function**: Upgrades stuff based on set priorities.
- **Auto Boost Upgrades**: upgrade boosts automatically.

## To Do
- **Test the code**
- **auto complete daily combo**


Set priority from line 18 in main.py 

Example of priority upgrade option
priority = ["Specials", "PR&Team", "Markets", "Legal"]  this is Default
priority = []  for all upgrade section
priority = None  for no upgrade
priority = ["Specials"]  for single priority upgrade
priority = ["Specials","Markets"]  for multiple priority upgrade, will follow the order of list
priority = "YouTube 25 Million" for single priority upgrade, will keep upgrading



## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/CodeCarbon/hamster-combat-automation-bot.git
    cd hamster-combat-automation-bot
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Capture the Authorization Token**

### Mobile

**If Rooted:**
Use [Reqable API Testing & Capture](https://play.google.com/store/apps/details?id=com.reqable.android&hl=en). Look for the header named "Authorization" to find your token.

**If Non-Rooted:**
Ask someone.

### PC

Download Telegram for PC from the Microsoft Store and follow these steps:

1. Navigate to `Settings > Advanced > Experimental > Enable Web Specting`.
2. Click play on Hamster Combat.
3. Open a new window, right-click, and select `Inspect`.
4. In the `Console`, paste the following script:
    ```javascript
    window.Telegram.WebApp.initData
    ```
   This will return something like:
    ```text
    'query_id=xyz&user=xyzfirst_name%xyzlast_name%xyz&auth_date=xyz&hash=xyz'
    ```

5. Paste this data into `initData.txt` without the **quotes**.
6. Run the script to generate the auth token:
    ```bash
    python authgen.py
    ```

## Configuration

In the main.py, locate line 32 where it reads:
"Authorization": f"Bearer YOUR_AUTH_TOKEN_HERE"

Replace YOUR_AUTH_TOKEN_HERE with the token generated from authgen.py.


Now simply run `python main.py`


My discord `_mrunknown_`
