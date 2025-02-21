# Pokémon Arena RPG

## Overview

Welcome to the **Pokémon Terminal Game**! This is a terminal-based game written entirely in Python where you can explore the world of Pokémon, battle enemies, earn monetary rewards, find new Pokémon, and much more. The game's progress is saved in a database, ensuring you always resume from where you left off.

## First look

<p align="center">
<img src="https://github.com/user-attachments/assets/4455425d-2b8e-4975-8b99-ad7c9c554cd4" alt="" width="850">
</p>


## Features

- **Exploration**: Explore the Pokémon world and discover new areas.
- **Battles**: Engage in exciting battles with enemies and earn rewards.
- **Rewards**: Earn money and use it to enhance your gaming experience.
- **Pokémon**: Find and capture new Pokémon during your journey.
- **Pokéagenda**: View your current Pokémon and manage your team.
- **Saving**: Progress is automatically saved in a database file (`database.db`).


### Initial Screen

The first time you play, the game will display the message:

```
Save not found.
```


You will need to provide a name for your player. After the initial setup, your login will be saved, and in future sessions, you will continue from the progress saved in the database.

## Installation

**Clone the Repository**

```bash
git clone https://github.com/JustAnotherBitt/Pokemon-Arena-RPG.git
cd Pokemon-Arena-RPG
```


## Running the Game

- To start the game on your **IDE**, execute the `main.py` file. 

```bash
python main.py
```
If it doesn't work, use the PowerShell command instead.

- To start the game on your **PowerShell**, execute the following command:

```bash
$env:PYTHONPATH = (Get-Location).Path; python main.py
```

- To start the game on your **linux terminal**, execute the following command: 

```bash
PYTHONPATH=$(pwd) python3 main.py
```


## Feature Examples

### 1. **Login Screen**

On the first run, you will be prompted to provide a name for your player.

### 2. **World Exploration**

While exploring the world, you can find new areas and Pokémon.

### 3. **Battles**

Face enemies and engage in battles.

### 4. **Pokéagenda**

View your current Pokémon with the Pokéagenda.

### 5. **Progress Saving**

Progress is saved automatically, allowing you to continue from where you left off in the next game session. 

## Observation

Language update in progress!!
