import sqlite3
import json # For converting player object to JSON format
from pathlib import Path # For handling file paths in a safe and OS-independent way

# Define the database file path (this will create the database in the root folder of the project)
DB_PATH = Path(__file__).parent / "game_data.db"

# This function initializes the database and creates the saves table if it doesn't exist
def init_database():
    # Same as "conn = sqlite3.connect(DB_PATH)", but with automatic close after the block
    with sqlite3.connect(DB_PATH) as conn:  
        # Creates a cursor to execute SQL commands in the database
        cursor = conn.cursor() 
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saves (  -- create a table only if it doesn't already exist
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- primary key, increases automatically
                language TEXT NOT NULL,                -- language of the game save
                player_name TEXT NOT NULL,             -- player's name
                player_data TEXT NOT NULL              -- all the player's data saved as JSON string
            )
        ''')
        conn.commit() # Saves the changes to the database

# This function saves the player's progress to the database
def save_player(language: str, name: str, data: dict):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        data_json = json.dumps(data) # Converts player data (dictionary) to a JSON string
        
        # If there's already a save with this language and name, remove it (we want to overwrite)
        cursor.execute("DELETE FROM saves WHERE language = ? AND player_name = ?", (language, name))
        # Insert the new player data into the saves table
        cursor.execute("INSERT INTO saves (language, player_name, player_data) VALUES (?, ?, ?)",
                       (language, name, data_json))
        conn.commit()

# Loads the game process
def load_player(language: str, name: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Search for the player in the table using the language and name
        cursor.execute("SELECT player_data FROM saves WHERE language = ? AND player_name = ?", (language, name))
        result = cursor.fetchone() # Returns the first match found, or None if not found
        
        if result:
            # Loads the JSON string as a Python dictionary so the game can access individual fields
            # (e.g., player["name"], player["money"]) instead of dealing with raw text
            return json.loads(result[0])
        return None
    
# Lists all saved players for a given language
def list_saves(language: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT player_name, player_data FROM saves WHERE language = ?", (language,))
        results = cursor.fetchall()
        
        saves = []
        for name, data_json in results:
            data = json.loads(data_json)
            saves.append({
                "name": name,
                "money": data.get("money", 0),
                "pokemons": len(data.get("pokemons", [])),
                "conquistas": data.get("conquistas", []),
                "data": data
            })
        return saves

def delete_player(language: str, name: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM saves WHERE language = ? AND player_name = ?", (language, name))
        conn.commit()
