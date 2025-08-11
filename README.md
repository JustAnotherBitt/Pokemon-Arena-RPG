# 🎮 Pokémon Arena RPG

## 🧭 Overview

Welcome to the **Pokémon Terminal Game**! This is a terminal-based game written entirely in Python where you can explore the world of Pokémon, battle enemies, earn monetary rewards, find new Pokémon, and much more. The game's progress is saved in a database, ensuring you always resume from where you left off.

## 👀 First look

<p align="center">
<img src="https://github.com/user-attachments/assets/4455425d-2b8e-4975-8b99-ad7c9c554cd4" alt="" width="850">
</p>

## ✨ Features

- **Exploration**: Explore the Pokémon world and discover new areas.
- **Battles**: Engage in exciting battles with enemies and earn rewards.
- **Rewards**: Earn money and use it to enhance your gaming experience.
- **Pokémon**: Find and capture new Pokémon during your journey.
- **Pokéagenda**: View your current Pokémon and manage your team.
- **Saving**: Progress is automatically saved in a database file (`game_data.db`).
- **Expanded Menu Options**: Access new options like viewing your wallet and unlocked achievements.
- **Database Management**: Saves, loads, lists, and deletes players using a structured SQLite database.

### 🖥️ Initial Screen

The first time you play, the game will display the message:

```
Save not found.
```

You will need to provide a name for your player. After the initial setup, your login will be saved, and in future sessions, you will continue from the progress saved in the database.

## 📥 Installation

**Clone the Repository**

```bash
git clone https://github.com/JustAnotherBitt/Pokemon-Arena-RPG.git
cd Pokemon-Arena-RPG
```

## 📥Requirements

- `Python3`: https://www.python.org/downloads
- `pyfiglet` library: https://pypi.org/project/pyfiglet
 
## 🚀 Running the Game

To start the game on your **IDE** or **PowerShell**, execute the `main.py` file.

```bash
python main.py
```

If it doesn't work directly, use the following PowerShell command instead:

```bash
$env:PYTHONPATH = (Get-Location).Path; python main.py
```

To start the game on your **Linux terminal**, execute the following command: 

```bash
PYTHONPATH=$(pwd) python3 main.py
```

## 🧩 Feature Examples

### 1. **Login Screen**

On the first run, you will be prompted to provide a name for your player.

### 2. **World Exploration**

While exploring the world, you can find new areas and Pokémon.

### 3. **Battles**

Face enemies and engage in battles.

### 4. **Pokéagenda**

View your current Pokémon with the Pokéagenda.

### 5. **Wallet**

You can now check your current money balance through the menu.

### 6. **Achievements**

View the achievements you have unlocked throughout your journey.

### 7. **Progress Saving**

Progress is saved automatically in a database, allowing you to continue from where you left off in the next game session.

## 🛠️ Observation

- Language update in progress!!


## ⚡ What's Coming Next?

- Better organization of the code, with a cleaner `main.py` and categorized functions.
- New achievements to unlock and expand your adventure.
- General optimization and performance improvements.

_The journey is far from over — and it’s only getting better._

---

🔹 **By <a href="https://github.com/JustAnotherBitt">JustAnotherBitt</a>.** 🔹

