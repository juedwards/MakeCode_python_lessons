![Minecraft Education Logo](images/education-minecraft-logo.png)

### 📁 Lesson 12: Movement Tracker - Record Your Adventures! 🗺️

**Last Updated**: June 20, 2025  
**Current User**: juedwards

#### 🎯 Learning Objectives:

* Learn how to read and write files in MakeCode Python
* Create a movement tracking system that saves your locations
* Build a trail recorder that remembers where you've been
* Save and load your favorite locations

---

#### 📚 Step 1: Understanding File Operations

In this lesson, we'll create a simple movement tracker that saves your positions to a file. This is like leaving breadcrumbs in the forest!

**What we'll build:**
- A system that records your position when you type a command
- A way to save multiple locations with names
- A trail viewer to see where you've been
- A teleport system to return to saved locations

Create a new MakeCode project called "Movement_Tracker"

Switch to Python and clear the default code.

---

#### 🏃 Step 2: Basic Position Recorder

Let's start by recording your current position to a file.

```python
# Your Desktop file path
FILE_PATH = "C:/Users/juedwards/Desktop/"

# Record current position
def record_position():
    # Get player's current position
    player_pos = player.position()
    x = player_pos.get_value(Axis.X)
    y = player_pos.get_value(Axis.Y)
    z = player_pos.get_value(Axis.Z)
    
    # Create position string
    position_data = str(x) + "," + str(y) + "," + str(z)
    
    # Save to file
    file.writeFile(FILE_PATH + "my_position.txt", position_data)
    player.say("📍 Position saved: " + position_data)

# Command to record position
def on_chat_mark():
    record_position()
player.on_chat("mark", on_chat_mark)

# Test message
player.say("Type 'mark' to save your position!")
```

---

#### 📖 Step 3: Load and Teleport to Saved Position

Now let's add the ability to return to your saved position.

```python
# Add this to your existing code

# Load and teleport to saved position
def return_to_position():
    try:
        # Read the saved position
        saved_data = file.readFile(FILE_PATH + "my_position.txt")
        
        # Split the coordinates
        coords = saved_data.split(",")
        x = int(coords[0])
        y = int(coords[1])
        z = int(coords[2])
        
        # Teleport to saved position
        player.teleport(pos(x, y, z))
        player.say("✅ Returned to saved position!")
    except:
        player.say("❌ No saved position found! Use 'mark' first")

# Command to return
def on_chat_return():
    return_to_position()
player.on_chat("return", on_chat_return)
```

---

#### 🗺️ Step 4: Create a Trail System

Let's upgrade our system to record multiple positions as a trail.

```python
# Trail counter
trail_count = 0

# Initialize trail file
def start_trail():
    global trail_count
    trail_count = 0
    # Create header for trail file
    header = "=== MOVEMENT TRAIL ===\nStarted: June 20, 2025\n\n"
    file.writeFile(FILE_PATH + "movement_trail.txt", header)
    player.say("🚶 New trail started!")

# Add position to trail
def add_to_trail():
    global trail_count
    try:
        # Read existing trail
        existing = file.readFile(FILE_PATH + "movement_trail.txt")
        
        # Get current position
        player_pos = player.position()
        x = player_pos.get_value(Axis.X)
        y = player_pos.get_value(Axis.Y)
        z = player_pos.get_value(Axis.Z)
        
        # Increment trail count
        trail_count = trail_count + 1
        
        # Add new position with number
        new_entry = existing + "Point " + str(trail_count) + ": " + str(x) + "," + str(y) + "," + str(z) + "\n"
        
        # Save updated trail
        file.writeFile(FILE_PATH + "movement_trail.txt", new_entry)
        player.say("📍 Point " + str(trail_count) + " added to trail!")
    except:
        player.say("❌ No trail found! Use 'start_trail' first")

# View trail summary
def view_trail():
    try:
        trail_data = file.readFile(FILE_PATH + "movement_trail.txt")
        player.say("🗺️ Trail Points: " + str(trail_count))
        # Show last position only (due to chat limits)
        lines = trail_data.split("\n")
        if len(lines) > 3:
            player.say("Last: " + lines[len(lines) - 2])
    except:
        player.say("❌ No trail found!")

# Trail commands
def on_chat_start_trail():
    start_trail()
player.on_chat("start_trail", on_chat_start_trail)

def on_chat_trail():
    add_to_trail()
player.on_chat("trail", on_chat_trail)

def on_chat_view_trail():
    view_trail()
player.on_chat("view_trail", on_chat_view_trail)
```

---

#### 🏠 Step 5: Named Locations System

Let's create a system to save locations with custom names like "home", "mine", etc.

```python
# Save a named location
def save_location(name):
    # Get current position
    player_pos = player.position()
    x = player_pos.get_value(Axis.X)
    y = player_pos.get_value(Axis.Y)
    z = player_pos.get_value(Axis.Z)
    
    # Create location data
    location_data = str(x) + "," + str(y) + "," + str(z)
    
    # Save with custom filename
    filename = FILE_PATH + "location_" + name + ".txt"
    file.writeFile(filename, location_data)
    player.say("🏠 Location '" + name + "' saved!")

# Load a named location
def go_to_location(name):
    try:
        # Read the location file
        filename = FILE_PATH + "location_" + name + ".txt"
        location_data = file.readFile(filename)
        
        # Split coordinates
        coords = location_data.split(",")
        x = int(coords[0])
        y = int(coords[1])
        z = int(coords[2])
        
        # Teleport
        player.teleport(pos(x, y, z))
        player.say("✅ Teleported to '" + name + "'!")
    except:
        player.say("❌ Location '" + name + "' not found!")

# Commands for named locations
def on_chat_save_home():
    save_location("home")
player.on_chat("save_home", on_chat_save_home)

def on_chat_go_home():
    go_to_location("home")
player.on_chat("go_home", on_chat_go_home)

def on_chat_save_mine():
    save_location("mine")
player.on_chat("save_mine", on_chat_save_mine)

def on_chat_go_mine():
    go_to_location("mine")
player.on_chat("go_mine", on_chat_go_mine)
```

---

#### ✅ Complete Movement Tracker System

Here's the full code with all features combined:

```python
# === MOVEMENT TRACKER SYSTEM ===
# File path to Desktop
FILE_PATH = "C:/Users/juedwards/Desktop/"

# Trail counter
trail_count = 0

# === BASIC POSITION RECORDING ===
def record_position():
    # Get player's current position
    player_pos = player.position()
    x = player_pos.get_value(Axis.X)
    y = player_pos.get_value(Axis.Y)
    z = player_pos.get_value(Axis.Z)
    
    # Create position string
    position_data = str(x) + "," + str(y) + "," + str(z)
    
    # Save to file
    file.writeFile(FILE_PATH + "my_position.txt", position_data)
    player.say("📍 Position saved: " + position_data)

def return_to_position():
    try:
        # Read the saved position
        saved_data = file.readFile(FILE_PATH + "my_position.txt")
        
        # Split the coordinates
        coords = saved_data.split(",")
        x = int(coords[0])
        y = int(coords[1])
        z = int(coords[2])
        
        # Teleport to saved position
        player.teleport(pos(x, y, z))
        player.say("✅ Returned to saved position!")
    except:
        player.say("❌ No saved position found! Use 'mark' first")

# === TRAIL SYSTEM ===
def start_trail():
    global trail_count
    trail_count = 0
    # Create header for trail file
    header = "=== MOVEMENT TRAIL ===\nStarted: June 20, 2025\n\n"
    file.writeFile(FILE_PATH + "movement_trail.txt", header)
    player.say("🚶 New trail started!")

def add_to_trail():
    global trail_count
    try:
        # Read existing trail
        existing = file.readFile(FILE_PATH + "movement_trail.txt")
        
        # Get current position
        player_pos = player.position()
        x = player_pos.get_value(Axis.X)
        y = player_pos.get_value(Axis.Y)
        z = player_pos.get_value(Axis.Z)
        
        # Increment trail count
        trail_count = trail_count + 1
        
        # Add new position with number
        new_entry = existing + "Point " + str(trail_count) + ": " + str(x) + "," + str(y) + "," + str(z) + "\n"
        
        # Save updated trail
        file.writeFile(FILE_PATH + "movement_trail.txt", new_entry)
        player.say("📍 Point " + str(trail_count) + " added to trail!")
    except:
        player.say("❌ No trail found! Use 'start_trail' first")

def view_trail():
    try:
        trail_data = file.readFile(FILE_PATH + "movement_trail.txt")
        player.say("🗺️ Trail Points: " + str(trail_count))
        # Show last position only (due to chat limits)
        lines = trail_data.split("\n")
        if len(lines) > 3:
            player.say("Last: " + lines[len(lines) - 2])
    except:
        player.say("❌ No trail found!")

# === NAMED LOCATIONS ===
def save_location(name):
    # Get current position
    player_pos = player.position()
    x = player_pos.get_value(Axis.X)
    y = player_pos.get_value(Axis.Y)
    z = player_pos.get_value(Axis.Z)
    
    # Create location data with game time
    time_stamp = str(gameplay.time_query(GAME_TIME))
    location_data = str(x) + "," + str(y) + "," + str(z) + "," + time_stamp
    
    # Save with custom filename
    filename = FILE_PATH + "location_" + name + ".txt"
    file.writeFile(filename, location_data)
    player.say("🏠 Location '" + name + "' saved!")

def go_to_location(name):
    try:
        # Read the location file
        filename = FILE_PATH + "location_" + name + ".txt"
        location_data = file.readFile(filename)
        
        # Split data
        parts = location_data.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        
        # Teleport
        player.teleport(pos(x, y, z))
        player.say("✅ Teleported to '" + name + "'!")
        
        # Show when it was saved (if available)
        if len(parts) > 3:
            player.say("📅 Saved at game time: " + parts[3])
    except:
        player.say("❌ Location '" + name + "' not found!")

# === ALL LOCATIONS LIST ===
def save_all_locations():
    try:
        # Read existing list
        existing = file.readFile(FILE_PATH + "all_locations.txt")
    except:
        # Create new file if doesn't exist
        existing = "=== ALL SAVED LOCATIONS ===\n\n"
    
    # Get current position
    player_pos = player.position()
    x = player_pos.get_value(Axis.X)
    y = player_pos.get_value(Axis.Y)
    z = player_pos.get_value(Axis.Z)
    
    # Add to list with timestamp
    time_stamp = str(gameplay.time_query(GAME_TIME))
    new_entry = existing + "Time " + time_stamp + ": " + str(x) + "," + str(y) + "," + str(z) + "\n"
    
    # Save updated list
    file.writeFile(FILE_PATH + "all_locations.txt", new_entry)
    player.say("📝 Added to locations list!")

# === COMMANDS ===
# Basic position commands
def on_chat_mark():
    record_position()
player.on_chat("mark", on_chat_mark)

def on_chat_return():
    return_to_position()
player.on_chat("return", on_chat_return)

# Trail commands
def on_chat_start_trail():
    start_trail()
player.on_chat("start_trail", on_chat_start_trail)

def on_chat_trail():
    add_to_trail()
player.on_chat("trail", on_chat_trail)

def on_chat_view_trail():
    view_trail()
player.on_chat("view_trail", on_chat_view_trail)

# Named location commands
def on_chat_save_home():
    save_location("home")
player.on_chat("save_home", on_chat_save_home)

def on_chat_go_home():
    go_to_location("home")
player.on_chat("go_home", on_chat_go_home)

def on_chat_save_mine():
    save_location("mine")
player.on_chat("save_mine", on_chat_save_mine)

def on_chat_go_mine():
    go_to_location("mine")
player.on_chat("go_mine", on_chat_go_mine)

def on_chat_save_farm():
    save_location("farm")
player.on_chat("save_farm", on_chat_save_farm)

def on_chat_go_farm():
    go_to_location("farm")
player.on_chat("go_farm", on_chat_go_farm)

# List locations
def on_chat_save_list():
    save_all_locations()
player.on_chat("save_list", on_chat_save_list)

# Help command
def on_chat_help():
    player.say("=== MOVEMENT TRACKER ===")
    player.say("📍 BASIC: mark, return")
    player.say("🚶 TRAIL: start_trail, trail, view_trail")
    player.say("🏠 LOCATIONS: save_home, go_home")
    player.say("⛏️ save_mine, go_mine")
    player.say("🌾 save_farm, go_farm")
    player.say("📝 save_list - Add to master list")

player.on_chat("help", on_chat_help)

# Initialize
player.say("🗺️ Movement Tracker Ready!")
player.say("💡 Type 'help' for commands")
player.say("📁 Files save to Desktop")
```

---

#### 🕹️ How to Use the Movement Tracker

**Basic Commands:**
- `mark` - Save your current position
- `return` - Teleport back to marked position

**Trail Commands:**
- `start_trail` - Begin a new trail
- `trail` - Add current position to trail
- `view_trail` - See how many points in trail

**Location Commands:**
- `save_home` - Save current position as "home"
- `go_home` - Teleport to home
- `save_mine` - Save as "mine"
- `go_mine` - Teleport to mine
- `save_farm` - Save as "farm"
- `go_farm` - Teleport to farm

**Other:**
- `save_list` - Add position to master list
- `help` - Show all commands

---

#### 🧠 Fun Challenges

1. **Create a Treasure Hunt**:
   - Save 5 locations as treasure1, treasure2, etc.
   - Give the coordinate files to a friend
   - See if they can find all your treasures!

2. **Trail Art**:
   - Start a trail
   - Walk in a pattern (square, circle, star)
   - Open the trail file to see your path!

3. **Base Network**:
   - Save multiple bases (base1, base2, base3)
   - Create a quick travel system between them

4. **Add More Locations**:
```python
# Add custom locations
def on_chat_save_castle():
    save_location("castle")
player.on_chat("save_castle", on_chat_save_castle)

def on_chat_go_castle():
    go_to_location("castle")
player.on_chat("go_castle", on_chat_go_castle)
```

---

#### 📊 Understanding the Files

**my_position.txt**:
```
125,64,-200
```
Simple X,Y,Z coordinates

**movement_trail.txt**:
```
=== MOVEMENT TRAIL ===
Started: June 20, 2025

Point 1: 100,64,100
Point 2: 110,64,100
Point 3: 120,64,100
```

**location_home.txt**:
```
150,70,-50,1200
```
X,Y,Z coordinates plus game time

---

#### 💡 Pro Tips

1. **Organization**: Name your locations clearly (home, mine, farm)
2. **Trail Markers**: Use `trail` at corners or important spots
3. **Backup**: The `mark` command is great for temporary saves
4. **Exploration**: Start a trail before exploring new areas
5. **File Names**: Check your Desktop for all the .txt files created!

---

#### 🎓 What You've Learned

- ✅ File writing with `file.writeFile()`
- ✅ File reading with `file.readFile()`
- ✅ Position tracking with `player.position()`
- ✅ String manipulation with `split()`
- ✅ Error handling with try/except
- ✅ Creating reusable teleport systems
- ✅ Building a breadcrumb trail
- ✅ Managing multiple save files

---

#### 🚀 Next Steps

Now that you understand file operations, you could:
- Add more named locations
- Create a coordinate display system
- Build an automatic trail recorder
- Make a multiplayer meeting point system
- Design a race checkpoint tracker

Remember: Every adventure is worth recording! 🗺️
