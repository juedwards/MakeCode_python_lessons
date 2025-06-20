### 📁 Lesson 12: Movement Tracker – Record Your Adventures in Data! 🗺️

**Last Updated**: June 20, 2025

---

## 🎯 Learning Objectives

* **Read & write files** in MakeCode Python
* **Record where you walk** in Minecraft
* **Save your favourite spots** (home, mine, farm…)
* **Jump back** to any saved place

> **Why this is cool:**
> Imagine leaving glowing breadcrumbs everywhere you go.
> With code, your crumbs never disappear!

---

## 📚 Step 1: Understanding File Operations

In this lesson we'll create a movement tracker that drops an *invisible breadcrumb* (a line in a text file) whenever you tell it to.

### What we'll build

* **Position marker** – saves *one* spot
* **Trail recorder** – saves a whole trip
* **Named locations** – saves spots like "home" or "mine"
* **Teleporter** – jumps you back to any saved spot

Create a new MakeCode project called **"Movement\_Tracker"**.
Switch to **Python** and clear the default code.

### 🧩 Code Explained – Step 1

| Fancy Word | Plain-English Meaning                                      |
| ---------- | ---------------------------------------------------------- |
| **File**   | A text note saved on your computer (like a notebook page). |
| **Write**  | Put new words on that page.                                |
| **Read**   | Look at the words already on the page.                     |

Think of the file as your digital map book. We'll write in it ("I was at X,Y,Z") and read from it ("take me back there"). Easy!

---

## 🏃 Step 2: Basic Position Recorder

```python
# CHANGE THIS TO YOUR USERNAME!
MY_USERNAME = "put_your_windows_name_here"
FILE_PATH = "C:/Users/" + MY_USERNAME + "/Desktop/"

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
    player.say("Position saved: " + position_data)

# Command to record position
def on_chat_mark():
    record_position()
player.on_chat("mark", on_chat_mark)

# Test message
player.say("Type 'mark' to save your position!")
```

### 🧩 Code Explained – Step 2

1. **`MY_USERNAME` and `FILE_PATH`**
   *Address of your notebook.* Change MY_USERNAME to your Windows username. This tells the computer where to save files.

2. **`player.position()`**
   *Ask Minecraft, "Where am I?"* It gives X (east/west), Y (up/down), Z (north/south).

3. **`position_data = str(x)+","+str(y)+","+str(z)`**
   Squish the three numbers together with commas – like writing "125,64,-200".

4. **`file.writeFile(...)`**
   *Grab a pen and write the line* into **my\_position.txt**.

5. **`player.on_chat("mark", ...)`**
   Whenever you type **mark** in chat, the function runs.
   Think of it as yelling "SAVE!" and the game scribbles your spot.

---

## 📖 Step 3: Load and Teleport to Saved Position

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
        player.say("Returned to saved position!")
    except:
        player.say("No saved position found! Use 'mark' first")

# Command to return
def on_chat_return():
    return_to_position()
player.on_chat("return", on_chat_return)
```

### 🧩 Code Explained – Step 3

1. **`file.readFile(...)`**
   *Open the notebook* and read the line we wrote earlier.

2. **`split(",")`**
   Cut the line at each comma → `[x, y, z]`.

3. **`int()`**
   Change the words "125" into the number **125** the computer can count with.

4. **`player.teleport(pos(x, y, z))`**
   Boom! Instantly hop to those coordinates.

5. **`try / except`**
   *Polite error checker.* If the file isn't there yet, we don't crash – we just say "Use mark first."

---

## 🗺️ Step 4: Create a Trail System

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
    player.say("New trail started!")

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
        player.say("Point " + str(trail_count) + " added to trail!")
    except:
        player.say("No trail found! Use 'start_trail' first")

# View trail summary
def view_trail():
    try:
        trail_data = file.readFile(FILE_PATH + "movement_trail.txt")
        player.say("Trail Points: " + str(trail_count))
        # Show last position only (due to chat limits)
        lines = trail_data.split("\n")
        if len(lines) > 3:
            player.say("Last: " + lines[len(lines) - 2])
    except:
        player.say("No trail found!")

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

### 🧩 Code Explained – Step 4

| Part                 | What It Does                                                        | Kid-Friendly Picture                        |
| -------------------- | ------------------------------------------------------------------- | ------------------------------------------- |
| **`trail_count`**    | Keeps how many crumbs you dropped.                                  | A score counter.                            |
| **`start_trail()`**  | Clears the old trail and writes a header.                           | Turning to a fresh page in your notebook.   |
| **`add_to_trail()`** | Reads the current page, adds "Point N: X,Y,Z", then saves the page. | Writing the next line in your travel diary. |
| **`view_trail()`**   | Tells you how many points and shows the last one.                   | Skimming the diary to the last entry.       |

Commands:

* `start_trail` – new diary page
* `trail` – "write down this spot!"
* `view_trail` – "how many spots did I write?"

---

## 🏠 Step 5: Named Locations System

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
    player.say("Location '" + name + "' saved!")

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
        player.say("Teleported to '" + name + "'!")
    except:
        player.say("Location '" + name + "' not found!")

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

### 🧩 Code Explained – Step 5

* **One file per place** – We name the file **location\_home.txt** or **location\_mine.txt**.
  Think of each as a sticky note on your desk.

* **`save_location("home")`**
  Writes your current spot onto the "home" sticky note.

* **`go_to_location("home")`**
  Reads the note and teleports you there.

* **Commands**

  * `save_home`, `go_home`
  * `save_mine`, `go_mine`
    You can invent more: `save_castle`, `go_castle`, etc.

---

## ✅ Complete Movement Tracker System

Here's the complete code with all features combined:

```python
# === MOVEMENT TRACKER SYSTEM ===
# CHANGE THIS TO YOUR USERNAME!
MY_USERNAME = "put_your_windows_name_here"
FILE_PATH = "C:/Users/" + MY_USERNAME + "/Desktop/"

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
    player.say("Position saved: " + position_data)

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
        player.say("Returned to saved position!")
    except:
        player.say("No saved position found! Use 'mark' first")

# === TRAIL SYSTEM ===
def start_trail():
    global trail_count
    trail_count = 0
    # Create header for trail file
    header = "=== MOVEMENT TRAIL ===\nStarted: June 20, 2025\n\n"
    file.writeFile(FILE_PATH + "movement_trail.txt", header)
    player.say("New trail started!")

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
        player.say("Point " + str(trail_count) + " added to trail!")
    except:
        player.say("No trail found! Use 'start_trail' first")

def view_trail():
    try:
        trail_data = file.readFile(FILE_PATH + "movement_trail.txt")
        player.say("Trail Points: " + str(trail_count))
        # Show last position only (due to chat limits)
        lines = trail_data.split("\n")
        if len(lines) > 3:
            player.say("Last: " + lines[len(lines) - 2])
    except:
        player.say("No trail found!")

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
    player.say("Location '" + name + "' saved!")

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
        player.say("Teleported to '" + name + "'!")
        
        # Show when it was saved (if available)
        if len(parts) > 3:
            player.say("Saved at game time: " + parts[3])
    except:
        player.say("Location '" + name + "' not found!")

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
    player.say("Added to locations list!")

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
    player.say("BASIC: mark, return")
    player.say("TRAIL: start_trail, trail, view_trail")
    player.say("LOCATIONS: save_home, go_home")
    player.say("save_mine, go_mine")
    player.say("save_farm, go_farm")
    player.say("save_list - Add to master list")

player.on_chat("help", on_chat_help)

# Initialize
player.say("Movement Tracker Ready!")
player.say("Type 'help' for commands")
player.say("Files save to: " + FILE_PATH)
```

### 🧩 Code Explained – All Together

When you load the world, the script says **"Movement Tracker Ready!"**
Now you can:

* **Mark** one-off spots
* **Start & add to a trail** as you wander
* **Save & teleport to named locations**
* **List** everything to keep your map book tidy

---

## 🕹️ How to Use the Movement Tracker

| Category      | Command                | What Happens                    |
| ------------- | ---------------------- | ------------------------------- |
| **Basic**     | `mark`                 | Save current spot               |
|               | `return`               | Teleport to your marked spot    |
| **Trail**     | `start_trail`          | Begin a new diary page          |
|               | `trail`                | Add current spot to diary       |
|               | `view_trail`           | Show points & last entry        |
| **Locations** | `save_home`, `go_home` | Save / jump to home             |
|               | `save_mine`, `go_mine` | Save / jump to mine             |
|               | `save_farm`, `go_farm` | Save / jump to farm             |
| **Extra**     | `save_list`            | Add current spot to master list |
|               | `help`                 | Show all commands               |

---

## 🧠 Fun Challenges

1. **Treasure Hunt**
   Save spots `treasure1`-`treasure5`, share the files with a friend, and race them!

2. **Trail Art**
   Walk a square or star, then open **movement\_trail.txt**.
   Your coordinates draw the shape like connect-the-dots.

3. **Base Network**
   Have **base1 / base2 / base3** and hop between them lightning-fast.

4. **Add More Locations**

```python
def on_chat_save_castle():
    save_location("castle")
player.on_chat("save_castle", on_chat_save_castle)

def on_chat_go_castle():
    go_to_location("castle")
player.on_chat("go_castle", on_chat_go_castle)
```

---

## 📊 Understanding the Files

| File                    | Example Contents  | Meaning             |
| ----------------------- | ----------------- | ------------------- |
| **my\_position.txt**    | `125,64,-200`     | One saved spot      |
| **movement\_trail.txt** | See below         | All trail points    |
| **location\_home.txt**  | `150,70,-50,1200` | Home plus game-time |

```
=== MOVEMENT TRAIL ===
Started: June 20, 2025

Point 1: 100,64,100
Point 2: 110,64,100
Point 3: 120,64,100
```

---

## 💡 Pro Tips

1. **Clear Names** – "home", "mine", "farm" are easy to remember.
2. **Trail Corners** – Drop a `trail` crumb whenever you turn.
3. **Emergency Mark** – Always `mark` before diving into caves.
4. **Explore Smart** – `start_trail` before long hikes so you can trace your path.
5. **Check Desktop** – All the text files pop up there; open them with Notepad!

---

## 🎓 What You Learned

☑️ Writing & reading files  
☑️ Asking Minecraft for your position  
☑️ Splitting strings into numbers  
☑️ Avoiding crashes with `try/except`  
☑️ Teleporting with coordinates  
☑️ Making lots of handy chat commands  

---

## 🚀 Next Steps

* Add **more named spots** (villages, strongholds, portals)
* Show your **live coordinates** on screen
* Auto-trail that records **every block** you walk
* Make a **multiplayer meeting point**
* Design a **race checkpoint timer**

Remember: every adventure leaves footprints – now you can see yours! 🗺️🎉
**Current User**: put_your_windows_name_here

---

## 🎯 Learning Objectives

* **Read & write files** in MakeCode Python
* **Record where you walk** in Minecraft
* **Save your favourite spots** (home, mine, farm…)
* **Jump back** to any saved place

> **Why this is cool:**
> Imagine leaving glowing breadcrumbs everywhere you go.
> With code, your crumbs never disappear!

---

## 📚 Step 1: Understanding File Operations

In this lesson we’ll create a movement tracker that drops an *invisible breadcrumb* (a line in a text file) whenever you tell it to.

### What we’ll build

* **Position marker** – saves *one* spot
* **Trail recorder** – saves a whole trip
* **Named locations** – saves spots like “home” or “mine”
* **Teleporter** – jumps you back to any saved spot

Create a new MakeCode project called **“Movement\_Tracker”**.
Switch to **Python** and clear the default code.

### 🧩 Code Explained – Step 1

| Fancy Word | Plain-English Meaning                                      |
| ---------- | ---------------------------------------------------------- |
| **File**   | A text note saved on your computer (like a notebook page). |
| **Write**  | Put new words on that page.                                |
| **Read**   | Look at the words already on the page.                     |

Think of the file as your digital map book. We’ll write in it (“I was at X,Y,Z”) and read from it (“take me back there”). Easy!

---

## 🏃 Step 2: Basic Position Recorder

```python
# Your Desktop file path
FILE_PATH = "C:/Users/put_your_windows_name_here/Desktop/"

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

### 🧩 Code Explained – Step 2

1. **`FILE_PATH`**
   *Address of your notebook.* It tells the computer, “Put my notes on the Desktop.”

2. **`player.position()`**
   *Ask Minecraft, “Where am I?”* It gives X (east/west), Y (up/down), Z (north/south).

3. **`position_data = str(x)+","+str(y)+","+str(z)`**
   Squish the three numbers together with commas – like writing “125,64,-200”.

4. **`file.writeFile(...)`**
   *Grab a pen and write the line* into **my\_position.txt**.

5. **`player.on_chat("mark", ...)`**
   Whenever you type **mark** in chat, the function runs.
   Think of it as yelling “SAVE!” and the game scribbles your spot.

---

## 📖 Step 3: Load and Teleport to Saved Position

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

### 🧩 Code Explained – Step 3

1. **`file.readFile(...)`**
   *Open the notebook* and read the line we wrote earlier.

2. **`split(",")`**
   Cut the line at each comma → `[x, y, z]`.

3. **`int()`**
   Change the words “125” into the number **125** the computer can count with.

4. **`player.teleport(pos(x, y, z))`**
   Boom! Instantly hop to those coordinates.

5. **`try / except`**
   *Polite error checker.* If the file isn’t there yet, we don’t crash – we just say “Use mark first.”

---

## 🗺️ Step 4: Create a Trail System

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

### 🧩 Code Explained – Step 4

| Part                 | What It Does                                                        | Kid-Friendly Picture                        |
| -------------------- | ------------------------------------------------------------------- | ------------------------------------------- |
| **`trail_count`**    | Keeps how many crumbs you dropped.                                  | A score counter.                            |
| **`start_trail()`**  | Clears the old trail and writes a header.                           | Turning to a fresh page in your notebook.   |
| **`add_to_trail()`** | Reads the current page, adds “Point N: X,Y,Z”, then saves the page. | Writing the next line in your travel diary. |
| **`view_trail()`**   | Tells you how many points and shows the last one.                   | Skimming the diary to the last entry.       |

Commands:

* `start_trail` – new diary page
* `trail` – “write down this spot!”
* `view_trail` – “how many spots did I write?”

---

## 🏠 Step 5: Named Locations System

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

### 🧩 Code Explained – Step 5

* **One file per place** – We name the file **location\_home.txt** or **location\_mine.txt**.
  Think of each as a sticky note on your desk.

* **`save_location("home")`**
  Writes your current spot onto the “home” sticky note.

* **`go_to_location("home")`**
  Reads the note and teleports you there.

* **Commands**

  * `save_home`, `go_home`
  * `save_mine`, `go_mine`
    You can invent more: `save_castle`, `go_castle`, etc.

---

## ✅ Complete Movement Tracker System

*(Code unchanged – see the full block below if you need it.)*
Everything from Steps 2-5 is glued together so all commands work at once.

<details>
<summary>Click to view the complete code</summary>

```python
# === MOVEMENT TRACKER SYSTEM ===
# File path to Desktop
FILE_PATH = "C:/Users/put_your_windows_name_here/Desktop/"

# Trail counter
trail_count = 0

# === BASIC POSITION RECORDING ===
def record_position():
    ...
# (code identical to lesson above)
```

</details>

### 🧩 Code Explained – All Together

When you load the world, the script says **“Movement Tracker Ready!”**
Now you can:

* **Mark** one-off spots
* **Start & add to a trail** as you wander
* **Save & teleport to named locations**
* **List** everything to keep your map book tidy

---

## 🕹️ How to Use the Movement Tracker

| Category      | Command                | What Happens                    |
| ------------- | ---------------------- | ------------------------------- |
| **Basic**     | `mark`                 | Save current spot               |
|               | `return`               | Teleport to your marked spot    |
| **Trail**     | `start_trail`          | Begin a new diary page          |
|               | `trail`                | Add current spot to diary       |
|               | `view_trail`           | Show points & last entry        |
| **Locations** | `save_home`, `go_home` | Save / jump to home             |
|               | `save_mine`, `go_mine` | Save / jump to mine             |
|               | `save_farm`, `go_farm` | Save / jump to farm             |
| **Extra**     | `save_list`            | Add current spot to master list |
|               | `help`                 | Show all commands               |

---

## 🧠 Fun Challenges

1. **Treasure Hunt**
   Save spots `treasure1`-`treasure5`, share the files with a friend, and race them!

2. **Trail Art**
   Walk a square or star, then open **movement\_trail.txt**.
   Your coordinates draw the shape like connect-the-dots.

3. **Base Network**
   Have **base1 / base2 / base3** and hop between them lightning-fast.

4. **Add More Locations**

```python
def on_chat_save_castle():
    save_location("castle")
player.on_chat("save_castle", on_chat_save_castle)

def on_chat_go_castle():
    go_to_location("castle")
player.on_chat("go_castle", on_chat_go_castle)
```

---

## 📊 Understanding the Files

| File                    | Example Contents  | Meaning             |
| ----------------------- | ----------------- | ------------------- |
| **my\_position.txt**    | `125,64,-200`     | One saved spot      |
| **movement\_trail.txt** | See below         | All trail points    |
| **location\_home.txt**  | `150,70,-50,1200` | Home plus game-time |

```
=== MOVEMENT TRAIL ===
Started: June 20, 2025

Point 1: 100,64,100
Point 2: 110,64,100
Point 3: 120,64,100
```

---

## 💡 Pro Tips

1. **Clear Names** – “home”, “mine”, “farm” are easy to remember.
2. **Trail Corners** – Drop a `trail` crumb whenever you turn.
3. **Emergency Mark** – Always `mark` before diving into caves.
4. **Explore Smart** – `start_trail` before long hikes so you can trace your path.
5. **Check Desktop** – All the text files pop up there; open them with Notepad!

---

## 🎓 What You Learned

☑️ Writing & reading files
☑️ Asking Minecraft for your position
☑️ Splitting strings into numbers
☑️ Avoiding crashes with `try/except`
☑️ Teleporting with coordinates
☑️ Making lots of handy chat commands

---

## 🚀 Next Steps

* Add **more named spots** (villages, strongholds, portals)
* Show your **live coordinates** on screen
* Auto-trail that records **every block** you walk
* Make a **multiplayer meeting point**
* Design a **race checkpoint timer**

Remember: every adventure leaves footprints – now you can see yours! 🗺️🎉
