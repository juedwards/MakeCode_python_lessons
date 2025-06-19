![Minecraft Education Logo](images/education-minecraft-logo.png)

### 📁 Lesson 12: Minecraft Data Adventures - File Read & Write 💾

**Last Updated**: June 19, 2025  

#### 🎯 Learning Objectives:

* Master file reading and writing operations in MakeCode Python
* Create persistent player data (inventory, scores, achievements)
* Build an adventure journal system that saves between sessions
* Design a structure blueprint system for saving and loading builds
* Implement checkpoint and save game functionality

---

#### 📚 Step 1: Understanding File Operations

Before we start coding, let's understand what file operations do:
- **Write**: Save data to a file (like saving your game)
- **Read**: Load data from a file (like loading your saved game)

**⚠️ Important File Path Setup**:
Files will be saved to your computer. You need to update the file path to match your computer:
- **Windows**: `C:/Users/YOUR_USERNAME/Desktop/`
- **Example**: If your username is "student", use `C:/Users/student/Desktop/`

Create a new MakeCode project called "Data_Adventures"

Switch to Python and clear the default code.

**First, let's set up our file path variable:**

```python
# CHANGE THIS TO YOUR USERNAME!
MY_USERNAME = "YOUR_USERNAME_HERE"
FILE_PATH = "C:/Users/" + MY_USERNAME + "/Desktop/"

# Test message
player.say("Files will save to: " + FILE_PATH)
```

---

#### 🏰 Step 2: Create Your First Save System

Let's start with a simple player checkpoint system. This code will save your position and score to a file.

**What this code does:**
- Saves your current checkpoint number
- Saves your score
- Saves your exact position (X, Y, Z coordinates)
- Creates a text file on your desktop

```python
# CHANGE THIS TO YOUR USERNAME!
MY_USERNAME = "YOUR_USERNAME_HERE"
FILE_PATH = "C:/Users/" + MY_USERNAME + "/Desktop/"

# Initialize variables FIRST (before any functions)
current_checkpoint = 0
player_score = 0

# Save checkpoint function
def save_checkpoint():
    global current_checkpoint, player_score
    # Get player's current position
    player_pos = player.position()
    
    # Create save data as a comma-separated string
    # Format: checkpoint,score,x,y,z
    save_data = str(current_checkpoint) + "," + str(player_score) + "," + str(player_pos.get_value(Axis.X)) + "," + str(player_pos.get_value(Axis.Y)) + "," + str(player_pos.get_value(Axis.Z))
    
    # Write to file on desktop
    file.writeFile(FILE_PATH + "checkpoint.txt", save_data)
    player.say("⭐ Checkpoint Saved to Desktop!")

# Command to save
def on_chat_save():
    save_checkpoint()
player.on_chat("save", on_chat_save)

# Test it!
player.say("Type 'save' to save your checkpoint!")
```

---

#### 📖 Step 3: Load Your Saved Data

Now let's create a function to load our checkpoint. This reads the file and restores your game state.

**What this code does:**
- Reads the saved file from your desktop
- Splits the data to get individual values
- Restores your checkpoint number and score
- Teleports you back to your saved position
- Uses try/except for error handling (in case file doesn't exist)

```python
# Add this to your existing code

# Load checkpoint function
def load_checkpoint():
    global current_checkpoint, player_score
    
    try:
        # Read the file from desktop
        save_data = file.readFile(FILE_PATH + "checkpoint.txt")
        
        # Split the data by commas
        # save_data looks like: "0,100,50,64,-20"
        data_parts = save_data.split(",")
        
        # Restore values (convert strings back to numbers)
        current_checkpoint = int(data_parts[0])
        player_score = int(data_parts[1])
        
        # Restore position
        saved_x = int(data_parts[2])
        saved_y = int(data_parts[3])
        saved_z = int(data_parts[4])
        
        # Teleport player to saved position
        player.teleport(pos(saved_x, saved_y, saved_z))
        
        player.say("✅ Checkpoint Loaded! Score: " + str(player_score))
    except:
        # This runs if the file doesn't exist or has an error
        player.say("❌ No save file found! Use 'save' first")

# Command to load
def on_chat_load():
    load_checkpoint()
player.on_chat("load", on_chat_load)
```

---

#### 📝 Step 4: Create an Adventure Journal

Let's build a journal system that records your adventures with timestamps.

**What this code does:**
- Creates a new journal file with a header
- Adds entries with game time stamps
- Appends new entries without deleting old ones
- Can read and display journal contents

```python
# Add this to your existing code

# Initialize journal - creates a new journal file
def init_journal():
    journal_header = "=== MINECRAFT ADVENTURE JOURNAL ===\nStarted on: Day 1\n-------------------\n"
    file.writeFile(FILE_PATH + "adventure_journal.txt", journal_header)
    player.say("📔 New journal created on Desktop!")

# Add journal entry
def add_journal_entry(entry_text):
    try:
        # Read existing journal content
        existing = file.readFile(FILE_PATH + "adventure_journal.txt")
        
        # Get current game time
        time_string = "Time: " + str(gameplay.time_query(GAME_TIME))
        
        # Format the new entry with timestamp
        new_entry = existing + "\n[" + time_string + "] " + entry_text + "\n"
        
        # Write updated journal (old content + new entry)
        file.writeFile(FILE_PATH + "adventure_journal.txt", new_entry)
        player.say("✍️ Journal updated!")
    except:
        player.say("❌ No journal found! Use 'journal_init' first")

# Read journal preview
def read_journal():
    try:
        journal_content = file.readFile(FILE_PATH + "adventure_journal.txt")
        player.say("📖 Journal Contents:")
        # Show first 100 characters in chat (chat has character limit)
        if len(journal_content) > 100:
            player.say(journal_content[0:100] + "...")
        else:
            player.say(journal_content)
    except:
        player.say("❌ No journal found! Use 'journal_init' first")

# Journal commands
def on_chat_journal_init():
    init_journal()
player.on_chat("journal_init", on_chat_journal_init)

def on_chat_journal():
    add_journal_entry("Found diamonds at bedrock level!")
player.on_chat("journal", on_chat_journal)

def on_chat_read():
    read_journal()
player.on_chat("read_journal", on_chat_read)
```

---

#### 🏗️ Step 5: Blueprint System - Save Your Builds!

Create a system to save and load structures. This scans blocks in a 5x5x5 area around you.

**What this code does:**
- Scans a 5x5x5 area around the player
- Saves the relative position of each non-air block
- Stores blueprint data in a text file
- Can recreate the structure at a new location

```python
# Add this to your existing code

# Save structure function
def save_simple_structure(name):
    """Save a 5x5x5 structure around the player"""
    blocks_data = []
    player_pos = player.position()
    # Get player's position as numbers
    base_x = player_pos.get_value(Axis.X)
    base_y = player_pos.get_value(Axis.Y)
    base_z = player_pos.get_value(Axis.Z)
    
    # Scan a 5x5x5 area around player
    # -2 to 2 gives us 5 blocks in each direction
    for x in range(-2, 3):
        for y in range(-1, 4):
            for z in range(-2, 3):
                # Calculate absolute position
                check_pos = pos(base_x + x, base_y + y, base_z + z)
                # Check if block is not air
                if not blocks.test_for_block(AIR, check_pos):
                    # Save relative position and block type
                    # Format: "x,y,z:BLOCKTYPE"
                    block_entry = str(x) + "," + str(y) + "," + str(z) + ":STONE"
                    blocks_data.append(block_entry)
    
    # Join all blocks with newlines
    all_blocks = "\n".join(blocks_data)
    
    # Save to file
    filename = FILE_PATH + "blueprint_" + name + ".txt"
    file.writeFile(filename, all_blocks)
    player.say("🏗️ Blueprint '" + name + "' saved to Desktop!")

# Load structure function
def load_simple_structure(name):
    """Load a structure at the player's position"""
    filename = FILE_PATH + "blueprint_" + name + ".txt"
    player_pos = player.position()
    # Get player's position as numbers
    base_x = player_pos.get_value(Axis.X)
    base_y = player_pos.get_value(Axis.Y)
    base_z = player_pos.get_value(Axis.Z)
    
    try:
        # Read blueprint file
        blueprint_data = file.readFile(filename)
        blocks_list = blueprint_data.split("\n")
        
        # Process each block
        for block_data in blocks_list:
            if ":" in block_data:
                # Split position and block type
                # Format: "x,y,z:BLOCKTYPE"
                parts = block_data.split(":")
                pos_string = parts[0]
                block_type = parts[1]
                
                # Split coordinates
                coords = pos_string.split(",")
                x = int(coords[0])
                y = int(coords[1])
                z = int(coords[2])
                
                # Place block at relative position
                place_pos = pos(base_x + x, base_y + y, base_z + z)
                blocks.place(STONE, place_pos)
        
        player.say("✅ Blueprint '" + name + "' loaded!")
    except:
        player.say("❌ Blueprint '" + name + "' not found!")

# Commands for blueprints
def on_chat_save_house():
    save_simple_structure("house")
player.on_chat("save_house", on_chat_save_house)

def on_chat_load_house():
    load_simple_structure("house")
player.on_chat("load_house", on_chat_load_house)
```

---

#### 🎮 Step 6: Player Stats Tracker (CSV Format)

Create a comprehensive stats system using CSV format for easy spreadsheet viewing.

**What this code does:**
- Tracks multiple player statistics
- Saves data in CSV format (can open in Excel)
- Auto-saves every 50 blocks mined
- Updates stats based on game events

```python
# IMPORTANT: Add these variables at the TOP of your code
blocks_mined = 0
blocks_placed = 0
mobs_defeated = 0
deaths = 0

def save_stats_csv():
    """Save player statistics to CSV file"""
    global blocks_mined, blocks_placed, mobs_defeated, deaths
    # Create CSV data with header row
    csv_data = "Statistic,Value\n"
    csv_data = csv_data + "blocks_mined," + str(blocks_mined) + "\n"
    csv_data = csv_data + "blocks_placed," + str(blocks_placed) + "\n"
    csv_data = csv_data + "mobs_defeated," + str(mobs_defeated) + "\n"
    csv_data = csv_data + "deaths," + str(deaths)
    
    file.writeFile(FILE_PATH + "player_stats.csv", csv_data)
    player.say("📊 Stats saved as CSV! Open in Excel!")

def load_stats_csv():
    """Load player statistics from CSV file"""
    global blocks_mined, blocks_placed, mobs_defeated, deaths
    
    try:
        stats_data = file.readFile(FILE_PATH + "player_stats.csv")
        lines = stats_data.split("\n")
        
        # Skip header line (line 0) and process data
        for i in range(1, len(lines)):
            if "," in lines[i]:
                parts = lines[i].split(",")
                stat_name = parts[0]
                stat_value = int(parts[1])
                
                # Update the correct stat
                if stat_name == "blocks_mined":
                    blocks_mined = stat_value
                elif stat_name == "blocks_placed":
                    blocks_placed = stat_value
                elif stat_name == "mobs_defeated":
                    mobs_defeated = stat_value
                elif stat_name == "deaths":
                    deaths = stat_value
        
        player.say("📊 Stats loaded from CSV!")
        show_stats()
    except:
        player.say("🆕 Creating new stats file...")
        save_stats_csv()

def show_stats():
    """Display player statistics"""
    global blocks_mined, blocks_placed, mobs_defeated, deaths
    player.say("=== PLAYER STATS ===")
    player.say("⛏️ Blocks Mined: " + str(blocks_mined))
    player.say("🧱 Blocks Placed: " + str(blocks_placed))
    player.say("🗡️ Mobs Defeated: " + str(mobs_defeated))
    player.say("💀 Deaths: " + str(deaths))

# Track events - these run automatically when events happen
def on_block_broken_grass():
    global blocks_mined
    blocks_mined = blocks_mined + 1
    # Auto-save every 50 blocks
    if blocks_mined % 50 == 0:
        save_stats_csv()

blocks.on_block_broken(GRASS, on_block_broken_grass)

def on_block_placed_stone():
    global blocks_placed
    blocks_placed = blocks_placed + 1

blocks.on_block_placed(STONE, on_block_placed_stone)

# Commands
def on_chat_stats():
    show_stats()
player.on_chat("stats", on_chat_stats)

def on_chat_save_stats():
    save_stats_csv()
player.on_chat("save_stats", on_chat_save_stats)

def on_chat_load_stats():
    load_stats_csv()
player.on_chat("load_stats", on_chat_load_stats)
```

---

#### 🏆 Step 7: Achievement System with Timestamps

Create an achievement tracker that saves when you earned each achievement.

**What this code does:**
- Tracks multiple achievements
- Records when each was earned
- Saves in CSV format
- Automatically checks for achievement completion

```python
# IMPORTANT: Add these variables at the TOP
achievement_first_save = False
achievement_mine_100 = False
achievement_build_house = False
achievement_date_first_save = ""
achievement_date_mine_100 = ""
achievement_date_build_house = ""

def get_timestamp():
    """Get current game time"""
    return "Time: " + str(gameplay.time_query(GAME_TIME))

def check_achievement_first_save():
    global achievement_first_save, achievement_date_first_save
    if not achievement_first_save:
        achievement_first_save = True
        achievement_date_first_save = get_timestamp()
        player.say("🏆 Achievement Unlocked: Data Keeper!")
        save_achievements_csv()

def check_achievement_mine_100():
    global achievement_mine_100, achievement_date_mine_100, blocks_mined
    if not achievement_mine_100 and blocks_mined >= 100:
        achievement_mine_100 = True
        achievement_date_mine_100 = get_timestamp()
        player.say("🏆 Achievement Unlocked: Century Miner!")
        save_achievements_csv()

def check_achievement_build_house():
    global achievement_build_house, achievement_date_build_house
    if not achievement_build_house:
        achievement_build_house = True
        achievement_date_build_house = get_timestamp()
        player.say("🏆 Achievement Unlocked: Architect!")
        save_achievements_csv()

def save_achievements_csv():
    """Save achievements to CSV file"""
    global achievement_first_save, achievement_mine_100, achievement_build_house
    global achievement_date_first_save, achievement_date_mine_100, achievement_date_build_house
    
    csv_data = "Achievement,Completed,Date Earned\n"
    csv_data = csv_data + "Data Keeper," + str(achievement_first_save) + "," + achievement_date_first_save + "\n"
    csv_data = csv_data + "Century Miner," + str(achievement_mine_100) + "," + achievement_date_mine_100 + "\n"
    csv_data = csv_data + "Architect," + str(achievement_build_house) + "," + achievement_date_build_house
    
    file.writeFile(FILE_PATH + "achievements.csv", csv_data)
    player.say("🏆 Achievements saved!")

def show_achievements():
    global achievement_first_save, achievement_mine_100, achievement_build_house
    global achievement_date_first_save, achievement_date_mine_100, achievement_date_build_house
    
    player.say("=== ACHIEVEMENTS ===")
    status1 = "✅" if achievement_first_save else "❌"
    status2 = "✅" if achievement_mine_100 else "❌"
    status3 = "✅" if achievement_build_house else "❌"
    
    date1 = " (" + achievement_date_first_save + ")" if achievement_first_save else ""
    date2 = " (" + achievement_date_mine_100 + ")" if achievement_mine_100 else ""
    date3 = " (" + achievement_date_build_house + ")" if achievement_build_house else ""
    
    player.say(status1 + " Data Keeper" + date1)
    player.say(status2 + " Century Miner" + date2)
    player.say(status3 + " Architect" + date3)

def on_chat_achievements():
    show_achievements()
player.on_chat("achievements", on_chat_achievements)
```

---

#### ✅ Complete Adventure System Code

Here's the full integrated system. Remember to change MY_USERNAME to your actual username!

```python
# === IMPORTANT: CHANGE THIS TO YOUR USERNAME! ===
MY_USERNAME = "YOUR_USERNAME_HERE"
FILE_PATH = "C:/Users/" + MY_USERNAME + "/Desktop/"

# === DECLARE ALL VARIABLES AT THE TOP ===
# Checkpoint system variables
current_checkpoint = 0
player_score = 0

# Stats system variables
blocks_mined = 0
blocks_placed = 0
mobs_defeated = 0
deaths = 0

# Achievement system variables
achievement_first_save = False
achievement_mine_100 = False
achievement_build_house = False
achievement_date_first_save = ""
achievement_date_mine_100 = ""
achievement_date_build_house = ""

# === CHECKPOINT SYSTEM ===
def save_checkpoint():
    global current_checkpoint, player_score
    player_pos = player.position()
    save_data = str(current_checkpoint) + "," + str(player_score) + "," + str(player_pos.get_value(Axis.X)) + "," + str(player_pos.get_value(Axis.Y)) + "," + str(player_pos.get_value(Axis.Z))
    file.writeFile(FILE_PATH + "checkpoint.txt", save_data)
    player.say("⭐ Checkpoint Saved to Desktop!")
    check_achievement_first_save()

def load_checkpoint():
    global current_checkpoint, player_score
    try:
        save_data = file.readFile(FILE_PATH + "checkpoint.txt")
        data_parts = save_data.split(",")
        current_checkpoint = int(data_parts[0])
        player_score = int(data_parts[1])
        saved_x = int(data_parts[2])
        saved_y = int(data_parts[3])
        saved_z = int(data_parts[4])
        player.teleport(pos(saved_x, saved_y, saved_z))
        player.say("✅ Checkpoint Loaded! Score: " + str(player_score))
    except:
        player.say("❌ No save file found!")

# === JOURNAL SYSTEM ===
def init_journal():
    journal_header = "=== MINECRAFT ADVENTURE JOURNAL ===\nStarted on: Day 1\n-------------------\n"
    file.writeFile(FILE_PATH + "adventure_journal.txt", journal_header)
    player.say("📔 New journal created on Desktop!")

def add_journal_entry(entry_text):
    try:
        existing = file.readFile(FILE_PATH + "adventure_journal.txt")
        time_string = "Time: " + str(gameplay.time_query(GAME_TIME))
        new_entry = existing + "\n[" + time_string + "] " + entry_text + "\n"
        file.writeFile(FILE_PATH + "adventure_journal.txt", new_entry)
        player.say("✍️ Journal updated!")
    except:
        player.say("❌ No journal found! Use 'journal_init' first")

def read_journal():
    try:
        journal_content = file.readFile(FILE_PATH + "adventure_journal.txt")
        player.say("📖 Journal Contents:")
        if len(journal_content) > 100:
            player.say(journal_content[0:100] + "...")
        else:
            player.say(journal_content)
    except:
        player.say("❌ No journal found! Use 'journal_init' first")

# === SIMPLIFIED BLUEPRINT SYSTEM ===
def save_simple_structure(name):
    """Save a 5x5x5 structure around the player"""
    blocks_data = []
    player_pos = player.position()
    base_x = player_pos.get_value(Axis.X)
    base_y = player_pos.get_value(Axis.Y)
    base_z = player_pos.get_value(Axis.Z)
    
    for x in range(-2, 3):
        for y in range(-1, 4):
            for z in range(-2, 3):
                check_pos = pos(base_x + x, base_y + y, base_z + z)
                if not blocks.test_for_block(AIR, check_pos):
                    block_entry = str(x) + "," + str(y) + "," + str(z) + ":STONE"
                    blocks_data.append(block_entry)
    
    all_blocks = "\n".join(blocks_data)
    filename = FILE_PATH + "blueprint_" + name + ".txt"
    file.writeFile(filename, all_blocks)
    player.say("🏗️ Blueprint '" + name + "' saved to Desktop!")

def load_simple_structure(name):
    """Load a structure at the player's position"""
    filename = FILE_PATH + "blueprint_" + name + ".txt"
    player_pos = player.position()
    base_x = player_pos.get_value(Axis.X)
    base_y = player_pos.get_value(Axis.Y)
    base_z = player_pos.get_value(Axis.Z)
    
    try:
        blueprint_data = file.readFile(filename)
        blocks_list = blueprint_data.split("\n")
        
        for block_data in blocks_list:
            if ":" in block_data:
                parts = block_data.split(":")
                pos_string = parts[0]
                coords = pos_string.split(",")
                x = int(coords[0])
                y = int(coords[1])
                z = int(coords[2])
                place_pos = pos(base_x + x, base_y + y, base_z + z)
                blocks.place(STONE, place_pos)
        
        player.say("✅ Blueprint '" + name + "' loaded!")
    except:
        player.say("❌ Blueprint '" + name + "' not found!")

# === STATS SYSTEM (CSV) ===
def save_stats_csv():
    global blocks_mined, blocks_placed, mobs_defeated, deaths
    csv_data = "Statistic,Value\n"
    csv_data = csv_data + "blocks_mined," + str(blocks_mined) + "\n"
    csv_data = csv_data + "blocks_placed," + str(blocks_placed) + "\n"
    csv_data = csv_data + "mobs_defeated," + str(mobs_defeated) + "\n"
    csv_data = csv_data + "deaths," + str(deaths)
    file.writeFile(FILE_PATH + "player_stats.csv", csv_data)
    player.say("📊 Stats saved as CSV!")

def load_stats_csv():
    global blocks_mined, blocks_placed, mobs_defeated, deaths
    try:
        stats_data = file.readFile(FILE_PATH + "player_stats.csv")
        lines = stats_data.split("\n")
        for i in range(1, len(lines)):
            if "," in lines[i]:
                parts = lines[i].split(",")
                if parts[0] == "blocks_mined":
                    blocks_mined = int(parts[1])
                elif parts[0] == "blocks_placed":
                    blocks_placed = int(parts[1])
                elif parts[0] == "mobs_defeated":
                    mobs_defeated = int(parts[1])
                elif parts[0] == "deaths":
                    deaths = int(parts[1])
        player.say("📊 Stats loaded!")
    except:
        save_stats_csv()

# === ACHIEVEMENT SYSTEM ===
def get_timestamp():
    return "Time: " + str(gameplay.time_query(GAME_TIME))

def check_achievement_first_save():
    global achievement_first_save, achievement_date_first_save
    if not achievement_first_save:
        achievement_first_save = True
        achievement_date_first_save = get_timestamp()
        player.say("🏆 Achievement Unlocked: Data Keeper!")
        save_achievements_csv()

def check_achievement_mine_100():
    global achievement_mine_100, achievement_date_mine_100, blocks_mined
    if not achievement_mine_100 and blocks_mined >= 100:
        achievement_mine_100 = True
        achievement_date_mine_100 = get_timestamp()
        player.say("🏆 Achievement Unlocked: Century Miner!")
        save_achievements_csv()

def check_achievement_build_house():
    global achievement_build_house, achievement_date_build_house
    if not achievement_build_house:
        achievement_build_house = True
        achievement_date_build_house = get_timestamp()
        player.say("🏆 Achievement Unlocked: Architect!")
        save_achievements_csv()

def save_achievements_csv():
    global achievement_first_save, achievement_mine_100, achievement_build_house
    global achievement_date_first_save, achievement_date_mine_100, achievement_date_build_house
    csv_data = "Achievement,Completed,Date Earned\n"
    csv_data = csv_data + "Data Keeper," + str(achievement_first_save) + "," + achievement_date_first_save + "\n"
    csv_data = csv_data + "Century Miner," + str(achievement_mine_100) + "," + achievement_date_mine_100 + "\n"
    csv_data = csv_data + "Architect," + str(achievement_build_house) + "," + achievement_date_build_house
    file.writeFile(FILE_PATH + "achievements.csv", csv_data)

def load_achievements_csv():
    global achievement_first_save, achievement_mine_100, achievement_build_house
    global achievement_date_first_save, achievement_date_mine_100, achievement_date_build_house
    
    try:
        achv_data = file.readFile(FILE_PATH + "achievements.csv")
        lines = achv_data.split("\n")
        
        for i in range(1, len(lines)):
            if "," in lines[i]:
                parts = lines[i].split(",")
                if len(parts) >= 3:
                    achv_name = parts[0]
                    completed = parts[1] == "True"
                    date = parts[2] if len(parts) > 2 else ""
                    
                    if achv_name == "Data Keeper":
                        achievement_first_save = completed
                        achievement_date_first_save = date
                    elif achv_name == "Century Miner":
                        achievement_mine_100 = completed
                        achievement_date_mine_100 = date
                    elif achv_name == "Architect":
                        achievement_build_house = completed
                        achievement_date_build_house = date
        
        player.say("🏆 Achievements loaded!")
    except:
        player.say("🆕 Creating new achievements file...")
        save_achievements_csv()

# === DISPLAY FUNCTIONS ===
def show_stats():
    global blocks_mined, blocks_placed, mobs_defeated, deaths
    player.say("=== PLAYER STATS ===")
    player.say("⛏️ Blocks Mined: " + str(blocks_mined))
    player.say("🧱 Blocks Placed: " + str(blocks_placed))
    player.say("🗡️ Mobs Defeated: " + str(mobs_defeated))
    player.say("💀 Deaths: " + str(deaths))

def show_achievements():
    global achievement_first_save, achievement_mine_100, achievement_build_house
    global achievement_date_first_save, achievement_date_mine_100, achievement_date_build_house
    
    player.say("=== ACHIEVEMENTS ===")
    status1 = "✅" if achievement_first_save else "❌"
    status2 = "✅" if achievement_mine_100 else "❌"
    status3 = "✅" if achievement_build_house else "❌"
    
    date1 = " (" + achievement_date_first_save + ")" if achievement_first_save else ""
    date2 = " (" + achievement_date_mine_100 + ")" if achievement_mine_100 else ""
    date3 = " (" + achievement_date_build_house + ")" if achievement_build_house else ""
    
    player.say(status1 + " Data Keeper" + date1)
    player.say(status2 + " Century Miner" + date2)
    player.say(status3 + " Architect" + date3)

# === MASTER SAVE/LOAD ===
def save_all():
    save_checkpoint()
    save_stats_csv()
    save_achievements_csv()
    player.say("💾 All data saved to Desktop!")

def load_all():
    load_checkpoint()
    load_stats_csv()
    load_achievements_csv()
    player.say("📂 All data loaded from Desktop!")

# === COMMANDS ===
def on_chat_save():
    save_checkpoint()
player.on_chat("save", on_chat_save)

def on_chat_load():
    load_checkpoint()
player.on_chat("load", on_chat_load)

def on_chat_journal_init():
    init_journal()
player.on_chat("journal_init", on_chat_journal_init)

def on_chat_journal():
    add_journal_entry("Exploring new territories!")
player.on_chat("journal", on_chat_journal)

def on_chat_read_journal():
    read_journal()
player.on_chat("read_journal", on_chat_read_journal)

def on_chat_stats():
    show_stats()
player.on_chat("stats", on_chat_stats)

def on_chat_achievements():
    show_achievements()
player.on_chat("achievements", on_chat_achievements)

def on_chat_save_all():
    save_all()
player.on_chat("save_all", on_chat_save_all)

def on_chat_load_all():
    load_all()
player.on_chat("load_all", on_chat_load_all)

def on_chat_save_house():
    save_simple_structure("house")
    check_achievement_build_house()

player.on_chat("save_house", on_chat_save_house)

def on_chat_load_house():
    load_simple_structure("house")

player.on_chat("load_house", on_chat_load_house)

# === EVENT TRACKING ===
def on_block_broken_grass():
    global blocks_mined
    blocks_mined = blocks_mined + 1
    check_achievement_mine_100()
    if blocks_mined % 50 == 0:
        save_stats_csv()

blocks.on_block_broken(GRASS, on_block_broken_grass)

def on_block_placed_stone():
    global blocks_placed
    blocks_placed = blocks_placed + 1

blocks.on_block_placed(STONE, on_block_placed_stone)

# === HELP SYSTEM ===
def on_chat_help():
    player.say("=== DATA ADVENTURE COMMANDS ===")
    player.say("save/load - Checkpoint system")
    player.say("journal_init/journal - Adventure log")
    player.say("read_journal - Read your journal")
    player.say("stats - View statistics")
    player.say("achievements - View achievements")
    player.say("save_house/load_house - Blueprint system")
    player.say("save_all/load_all - Complete save")
    player.say("📁 Files save to: " + FILE_PATH)

player.on_chat("help", on_chat_help)

# Initialize on start
player.say("🎮 Data Adventure System Ready!")
player.say("⚠️ IMPORTANT: Change MY_USERNAME in the code!")
player.say("💡 Type 'help' for commands")
player.say("📁 Files will save to: " + FILE_PATH)
```

---

#### 🕹️ How to Use the Data System

1. **FIRST**: Open the code and change `MY_USERNAME = "YOUR_USERNAME_HERE"` to your actual Windows username
2. Click the green play ▶️ button to run the code
3. Use these chat commands:
   - `help` - Show all available commands
   - `save` - Save checkpoint to Desktop
   - `load` - Load checkpoint from Desktop
   - `journal_init` - Create journal on Desktop
   - `journal` - Add entry to journal
   - `read_journal` - View journal contents
   - `stats` - View your statistics
   - `achievements` - View achievements
   - `save_house`/`load_house` - Save and load structures
   - `save_all` - Save everything
   - `load_all` - Load everything

---

#### 🧠 Advanced Challenges

1. **Multi-Player Save System**:
```python
def save_player_data(player_name):
    filename = FILE_PATH + "stats_" + player_name + ".csv"
    data = "Player," + player_name + "\nScore," + str(player_score)
    file.writeFile(filename, data)
```

2. **Automatic Backup System**:
```python
def create_backup():
    try:
        original = file.readFile(FILE_PATH + "checkpoint.txt")
        backup_name = FILE_PATH + "checkpoint_backup.txt"
        file.writeFile(backup_name, original)
        player.say("📋 Backup created!")
    except:
        player.say("❌ No checkpoint to backup!")
```

3. **High Score System**:
```python
def update_high_score(score):
    high_score = 0
    try:
        high_score_data = file.readFile(FILE_PATH + "highscore.txt")
        high_score = int(high_score_data)
    except:
        pass
    
    if score > high_score:
        file.writeFile(FILE_PATH + "highscore.txt", str(score))
        player.say("🏅 NEW HIGH SCORE: " + str(score))
```

4. **Custom Save Location**:
```python
# Let players choose their save location
SAVE_LOCATIONS = {
    "desktop": "C:/Users/" + MY_USERNAME + "/Desktop/",
    "documents": "C:/Users/" + MY_USERNAME + "/Documents/",
    "minecraft": "C:/Users/" + MY_USERNAME + "/Documents/Minecraft_Saves/"
}

# Use like: FILE_PATH = SAVE_LOCATIONS["documents"]
```

---

#### 💡 Pro Tips

1. **Username Setup**: ALWAYS change MY_USERNAME first!
2. **File Locations**: Default is Desktop, but you can change FILE_PATH
3. **CSV Format**: Stats and achievements open in Excel
4. **Error Handling**: Try/except blocks prevent crashes
5. **String Conversion**: Always use str() for numbers in files
6. **Testing**: Test save before load to avoid errors

---

#### 🚨 Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| "No save file found!" | Make sure you saved first with the save command |
| Files not appearing | Check that you changed MY_USERNAME correctly |
| Can't find Desktop folder | Try using Documents folder instead |
| Numbers showing as text in CSV | This is normal - Excel will recognize them |

---

#### 📊 Understanding the Data Files

**checkpoint.txt**:
```
0,100,125,64,-200
```
Format: checkpoint_number,score,x,y,z

**player_stats.csv**:
```
Statistic,Value
blocks_mined,150
blocks_placed,75
mobs_defeated,10
deaths,2
```

**adventure_journal.txt**:
```
=== MINECRAFT ADVENTURE JOURNAL ===
Started on: Day 1
-------------------

[Time: 1200] Found diamonds at bedrock level!
[Time: 1500] Built my first house!
```

---

#### 🎓 What You've Learned

- ✅ File I/O operations (read/write)
- ✅ Data persistence between game sessions
- ✅ CSV format for spreadsheet compatibility
- ✅ Error handling with try/except
- ✅ String manipulation and parsing
- ✅ Event-driven programming
- ✅ Global variables and scope
- ✅ Data serialization techniques
- ✅ File path management
- ✅ Automatic save systems
