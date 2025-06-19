![Minecraft Education Logo](images/education-minecraft-logo.png)

### 📁 Lesson 12: Minecraft Data Adventures - File Read & Write 💾

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
- **Append**: Add new data to existing file (like adding to a journal)

Create a new MakeCode project called "Data_Adventures"

Switch to Python and clear the default code.

---

#### 🏰 Step 2: Create Your First Save System

Let's start with a simple player checkpoint system:

```python
# Initialize variables
current_checkpoint = 0
player_score = 0

# Save checkpoint function
def save_checkpoint():
    global current_checkpoint, player_score
    # Create save data
    save_data = str(current_checkpoint) + "," + str(player_score) + "," + str(player.position())
    
    # Write to file
    file.write_to_file("checkpoint.txt", save_data)
    player.say("Checkpoint Saved!")

# Command to save
player.on_chat("save", save_checkpoint)
```

---

#### 📖 Step 3: Load Your Saved Data

Now let's create a function to load our checkpoint:

```python
# Load checkpoint function
def load_checkpoint():
    global current_checkpoint, player_score
    
    # Check if save file exists
    if file.exists("checkpoint.txt"):
        # Read the file
        save_data = file.read_from_file("checkpoint.txt")
        
        # Split the data
        data_parts = save_data.split(",")
        
        # Restore values
        current_checkpoint = int(data_parts[0])
        player_score = int(data_parts[1])
        
        # Teleport player to saved position
        # Parse position data (format: ~x ~y ~z)
        pos_string = data_parts[2]
        player.say("Checkpoint Loaded! Score: " + str(player_score))
    else:
        player.say("No save file found!")

# Command to load
player.on_chat("load", load_checkpoint)
```

---

#### 📝 Step 4: Create an Adventure Journal

Let's build a journal system that records your adventures:

```python
# Initialize journal
def init_journal():
    if not file.exists("adventure_journal.txt"):
        file.write_to_file("adventure_journal.txt", "=== MINECRAFT ADVENTURE JOURNAL ===\n")
        file.append_to_file("adventure_journal.txt", "Started on: Day 1\n")
        file.append_to_file("adventure_journal.txt", "-------------------\n")
        player.say("📔 New journal created!")

# Add journal entry
def add_journal_entry(entry_text):
    # Get current game time
    time_string = "Day " + str(gameplay.time_query(DAY_TIME))
    
    # Format the entry
    entry = "\n[" + time_string + "] " + entry_text + "\n"
    
    # Append to journal
    file.append_to_file("adventure_journal.txt", entry)
    player.say("✍️ Journal updated!")

# Journal commands
player.on_chat("journal_init", init_journal)

def on_journal_write():
    add_journal_entry("Found diamonds at bedrock level!")
player.on_chat("journal", on_journal_write)

# Read journal
def read_journal():
    if file.exists("adventure_journal.txt"):
        journal_content = file.read_from_file("adventure_journal.txt")
        player.say("📖 Journal Contents:")
        # Note: In game, this would show in chat
        player.say(journal_content[:100] + "...")  # Show first 100 chars
    else:
        player.say("❌ No journal found! Use 'journal_init' first")

player.on_chat("read_journal", read_journal)
```

---

#### 🏗️ Step 5: Blueprint System - Save Your Builds!

Create a system to save and load structures:

```python
# Structure blueprint system
structure_data = {}

def save_structure(name, corner1, corner2):
    """Save a structure between two corners"""
    blocks_list = []
    
    # Scan all blocks in the area
    for x in range(corner1.get_value(Axis.X), corner2.get_value(Axis.X) + 1):
        for y in range(corner1.get_value(Axis.Y), corner2.get_value(Axis.Y) + 1):
            for z in range(corner1.get_value(Axis.Z), corner2.get_value(Axis.Z) + 1):
                current_pos = pos(x, y, z)
                block = blocks.test_for_block(GRASS, current_pos)
                
                # Save block type and relative position
                if block != AIR:
                    rel_pos = str(x - corner1.get_value(Axis.X)) + "," + \
                             str(y - corner1.get_value(Axis.Y)) + "," + \
                             str(z - corner1.get_value(Axis.Z))
                    blocks_list.append(rel_pos + ":" + str(block))
    
    # Save to file
    filename = "blueprint_" + name + ".txt"
    file.write_to_file(filename, "\n".join(blocks_list))
    player.say("Blueprint '" + name + "' saved!")

def load_structure(name, position):
    """Load a structure at the given position"""
    filename = "blueprint_" + name + ".txt"
    
    if file.exists(filename):
        blueprint_data = file.read_from_file(filename)
        blocks_list = blueprint_data.split("\n")
        
        for block_data in blocks_list:
            if ":" in block_data:
                pos_data, block_type = block_data.split(":")
                x, y, z = pos_data.split(",")
                
                # Place block at relative position
                place_pos = position.add(pos(int(x), int(y), int(z)))
                blocks.place(STONE, place_pos)  # Replace with actual block type
        
        player.say("Blueprint '" + name + "' loaded!")
    else:
        player.say("Blueprint not found!")

# Commands for blueprints
def on_save_house():
    # Save a 5x5x5 area around player
    player_pos = player.position()
    corner1 = player_pos.add(pos(-2, -1, -2))
    corner2 = player_pos.add(pos(2, 3, 2))
    save_structure("house", corner1, corner2)

player.on_chat("save_house", on_save_house)

def on_load_house():
    load_structure("house", player.position())

player.on_chat("load_house", on_load_house)
```

---

#### 🎮 Step 6: Player Stats Tracker

Create a comprehensive stats system:

```python
# Player statistics
player_stats = {
    "blocks_mined": 0,
    "blocks_placed": 0,
    "distance_traveled": 0,
    "mobs_defeated": 0,
    "deaths": 0,
    "play_time": 0
}

def save_stats():
    """Save player statistics to file"""
    stats_lines = []
    for stat, value in player_stats.items():
        stats_lines.append(stat + "=" + str(value))
    
    file.write_to_file("player_stats.txt", "\n".join(stats_lines))
    player.say("📊 Stats saved!")

def load_stats():
    """Load player statistics from file"""
    global player_stats
    
    if file.exists("player_stats.txt"):
        stats_data = file.read_from_file("player_stats.txt")
        stats_lines = stats_data.split("\n")
        
        for line in stats_lines:
            if "=" in line:
                stat, value = line.split("=")
                player_stats[stat] = int(value)
        
        player.say("📊 Stats loaded!")
        show_stats()
    else:
        player.say("Creating new stats file...")
        save_stats()

def show_stats():
    """Display player statistics"""
    player.say("=== PLAYER STATS ===")
    player.say("Blocks Mined: " + str(player_stats["blocks_mined"]))
    player.say("Blocks Placed: " + str(player_stats["blocks_placed"]))
    player.say("Mobs Defeated: " + str(player_stats["mobs_defeated"]))
    player.say("Deaths: " + str(player_stats["deaths"]))

# Track events
def on_block_broken():
    player_stats["blocks_mined"] += 1
    if player_stats["blocks_mined"] % 100 == 0:
        save_stats()  # Auto-save every 100 blocks

blocks.on_block_broken(GRASS, on_block_broken)

# Commands
player.on_chat("stats", show_stats)
player.on_chat("save_stats", save_stats)
player.on_chat("load_stats", load_stats)
```

---

#### 🏆 Step 7: Achievement System

Create an achievement tracker:

```python
# Achievement system
achievements = {
    "first_save": {"name": "Data Keeper", "completed": False},
    "mine_100": {"name": "Century Miner", "completed": False},
    "build_house": {"name": "Architect", "completed": False},
    "explore_far": {"name": "Explorer", "completed": False}
}

def check_achievement(achievement_id):
    """Check and award achievement"""
    if achievement_id in achievements and not achievements[achievement_id]["completed"]:
        achievements[achievement_id]["completed"] = True
        player.say("Achievement Unlocked: " + achievements[achievement_id]["name"] + "!")
        save_achievements()

def save_achievements():
    """Save achievements to file"""
    achv_lines = []
    for achv_id, achv_data in achievements.items():
        achv_lines.append(achv_id + "=" + str(achv_data["completed"]))
    
    file.write_to_file("achievements.txt", "\n".join(achv_lines))

def load_achievements():
    """Load achievements from file"""
    global achievements
    
    if file.exists("achievements.txt"):
        achv_data = file.read_from_file("achievements.txt")
        achv_lines = achv_data.split("\n")
        
        for line in achv_lines:
            if "=" in line:
                achv_id, completed = line.split("=")
                if achv_id in achievements:
                    achievements[achv_id]["completed"] = completed == "True"
        
        player.say("Achievements loaded!")

# Check achievements based on stats
def update_achievements():
    if player_stats["blocks_mined"] >= 100:
        check_achievement("mine_100")
    
    if current_checkpoint > 0:
        check_achievement("first_save")

player.on_chat("achievements", lambda: show_achievements())

def show_achievements():
    player.say("=== ACHIEVEMENTS ===")
    for achv_id, achv_data in achievements.items():
        status = "YES" if achv_data["completed"] else "NO"
        player.say(status + " " + achv_data["name"])
```

---

#### Complete Adventure System Code

Here's the full integrated system:

```python
# Initialize all systems
current_checkpoint = 0
player_score = 0
player_stats = {
    "blocks_mined": 0,
    "blocks_placed": 0,
    "distance_traveled": 0,
    "mobs_defeated": 0,
    "deaths": 0,
    "play_time": 0
}
achievements = {
    "first_save": {"name": "Data Keeper", "completed": False},
    "mine_100": {"name": "Century Miner", "completed": False},
    "build_house": {"name": "Architect", "completed": False},
    "explore_far": {"name": "Explorer", "completed": False}
}

# === CHECKPOINT SYSTEM ===
def save_checkpoint():
    global current_checkpoint, player_score
    save_data = str(current_checkpoint) + "," + str(player_score) + "," + str(player.position())
    file.write_to_file("checkpoint.txt", save_data)
    player.say("Checkpoint Saved!")
    check_achievement("first_save")

def load_checkpoint():
    global current_checkpoint, player_score
    if file.exists("checkpoint.txt"):
        save_data = file.read_from_file("checkpoint.txt")
        data_parts = save_data.split(",")
        current_checkpoint = int(data_parts[0])
        player_score = int(data_parts[1])
        player.say("Checkpoint Loaded! Score: " + str(player_score))
    else:
        player.say("No save file found!")

# === JOURNAL SYSTEM ===
def init_journal():
    if not file.exists("adventure_journal.txt"):
        file.write_to_file("adventure_journal.txt", "=== MINECRAFT ADVENTURE JOURNAL ===\n")
        file.append_to_file("adventure_journal.txt", "Started on: Day 1\n")
        file.append_to_file("adventure_journal.txt", "-------------------\n")
        player.say("New journal created!")

def add_journal_entry(entry_text):
    time_string = "Day " + str(gameplay.time_query(DAY_TIME))
    entry = "\n[" + time_string + "] " + entry_text + "\n"
    file.append_to_file("adventure_journal.txt", entry)
    player.say("Journal updated!")

# === STATS SYSTEM ===
def save_stats():
    stats_lines = []
    for stat, value in player_stats.items():
        stats_lines.append(stat + "=" + str(value))
    file.write_to_file("player_stats.txt", "\n".join(stats_lines))
    player.say("Stats saved!")

def load_stats():
    global player_stats
    if file.exists("player_stats.txt"):
        stats_data = file.read_from_file("player_stats.txt")
        stats_lines = stats_data.split("\n")
        for line in stats_lines:
            if "=" in line:
                stat, value = line.split("=")
                player_stats[stat] = int(value)
        player.say("Stats loaded!")

# === ACHIEVEMENT SYSTEM ===
def check_achievement(achievement_id):
    if achievement_id in achievements and not achievements[achievement_id]["completed"]:
        achievements[achievement_id]["completed"] = True
        player.say("Achievement Unlocked: " + achievements[achievement_id]["name"] + "!")
        save_achievements()

def save_achievements():
    achv_lines = []
    for achv_id, achv_data in achievements.items():
        achv_lines.append(achv_id + "=" + str(achv_data["completed"]))
    file.write_to_file("achievements.txt", "\n".join(achv_lines))

# === MASTER SAVE/LOAD ===
def save_all():
    """Save everything at once"""
    save_checkpoint()
    save_stats()
    save_achievements()
    player.say("All data saved successfully!")

def load_all():
    """Load everything at once"""
    load_checkpoint()
    load_stats()
    load_achievements()
    player.say("All data loaded successfully!")

# === COMMANDS ===
player.on_chat("save", save_checkpoint)
player.on_chat("load", load_checkpoint)
player.on_chat("journal_init", init_journal)
player.on_chat("journal", lambda: add_journal_entry("Exploring new territories!"))
player.on_chat("stats", lambda: show_stats())
player.on_chat("achievements", lambda: show_achievements())
player.on_chat("save_all", save_all)
player.on_chat("load_all", load_all)

# === EVENT TRACKING ===
def on_block_broken():
    player_stats["blocks_mined"] += 1
    if player_stats["blocks_mined"] >= 100:
        check_achievement("mine_100")
    if player_stats["blocks_mined"] % 50 == 0:
        save_stats()

blocks.on_block_broken(GRASS, on_block_broken)

def show_stats():
    player.say("=== PLAYER STATS ===")
    player.say("Blocks Mined: " + str(player_stats["blocks_mined"]))
    player.say("Blocks Placed: " + str(player_stats["blocks_placed"]))
    player.say("🗡Mobs Defeated: " + str(player_stats["mobs_defeated"]))

def show_achievements():
    player.say("=== ACHIEVEMENTS ===")
    for achv_id, achv_data in achievements.items():
        status = "YES" if achv_data["completed"] else "NO"
        player.say(status + " " + achv_data["name"])

# Initialize on start
def on_start():
    player.say("Data Adventure System Ready!")
    player.say("Type 'help' for commands")

def on_help():
    player.say("=== COMMANDS ===")
    player.say("save/load - Checkpoint system")
    player.say("journal_init/journal - Adventure log")
    player.say("stats - View statistics")
    player.say("achievements - View achievements")
    player.say("save_all/load_all - Complete save")

player.on_chat("help", on_help)

# Run initialization
on_start()
```

---

#### 🕹️ How to Use the Data System

1. Click the green play ▶️ button to run the code
2. Use these chat commands:
   - `help` - Show all available commands
   - `save` - Save your current checkpoint
   - `load` - Load your last checkpoint
   - `journal_init` - Create a new journal
   - `journal` - Add entry to journal
   - `stats` - View your statistics
   - `achievements` - View achievements
   - `save_all` - Save everything
   - `load_all` - Load everything

---

#### 🧠 Advanced Challenges

1. **Inventory Manager**: Create a system to save and load player inventory
```python
def save_inventory():
    # Save current items in hotbar
    inventory_data = []
    for i in range(9):  # 9 hotbar slots
        # Get item in slot i
        item_info = "slot_" + str(i) + ":DIAMOND"  # Example
        inventory_data.append(item_info)
    file.write_to_file("inventory.txt", "\n".join(inventory_data))
```

2. **World Backup System**: Save entire regions
```python
def backup_region(region_name, size):
    # Create a backup of a large area
    player_pos = player.position()
    for x in range(-size, size):
        for z in range(-size, size):
            # Save chunk data
            chunk_data = "chunk_" + str(x) + "_" + str(z)
            file.append_to_file("world_backup.txt", chunk_data)
```

3. **Trading Post**: Create persistent shops
```python
def create_shop(shop_name, items):
    # Save shop data with prices
    shop_data = []
    for item, price in items.items():
        shop_data.append(item + ":" + str(price))
    file.write_to_file("shop_" + shop_name + ".txt", "\n".join(shop_data))
```

4. **Quest System**: Track quest progress
```python
quests = {
    "dragon_slayer": {"description": "Defeat the Ender Dragon", "progress": 0, "target": 1},
    "diamond_collector": {"description": "Collect 64 diamonds", "progress": 0, "target": 64}
}

def update_quest(quest_id, amount):
    if quest_id in quests:
        quests[quest_id]["progress"] += amount
        if quests[quest_id]["progress"] >= quests[quest_id]["target"]:
            player.say("🎯 Quest Complete: " + quests[quest_id]["description"])
        save_quests()
```

---

#### 💡 Pro Tips

1. **File Naming**: Use descriptive names like `player_<username>_stats.txt`
2. **Data Format**: Use consistent separators (commas, equals, colons)
3. **Error Handling**: Always check if files exist before reading
4. **Auto-Save**: Save important data periodically, not just on command
5. **Backup Files**: Create `.bak` versions of important saves

---

#### 🚨 Important Notes

- Files are saved in the world's data folder
- Each world has its own file storage
- Files persist between game sessions
- Maximum file size limits may apply
- Use `file.exists()` before reading to avoid errors

---

#### 🎓 What You've Learned

- ✅ Writing data to files for persistence
- ✅ Reading and parsing saved data
- ✅ Appending to existing files
- ✅ Creating save/load game systems
- ✅ Building achievement and stats trackers
- ✅ Implementing journal and logging systems
- ✅ Error handling with file operations
- ✅ Data formatting and parsing techniques
