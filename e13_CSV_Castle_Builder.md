![Minecraft Education Logo](images/education-minecraft-logo.png)

### Lesson 13: Castle Builder - Design in CSV, Build in Minecraft!

**Last Updated**: June 20, 2025 

---

## Learning Objectives

* **Design structures** using CSV spreadsheets
* **Read CSV files** and parse the data
* **Build automatically** from your spreadsheet design
* **Create modular castle parts** (walls, towers, gates)
* **Learn coordinate systems** for 3D building

> **Why this is cool:**
> Instead of placing blocks one by one, you can design your castle in a spreadsheet and watch it build itself!

---

## Step 1: Understanding CSV Castle Building

CSV (Comma-Separated Values) files are like simple spreadsheets. We'll use them as blueprints for our castle!

### What we'll build

* **Castle walls** with walkways
* **Corner towers** with windows
* **Grand entrance** gate
* **Castle keep** (main tower)

Create a new MakeCode project called **"Castle_Builder"**.
Switch to **Python** and clear the default code.

### 🧩 How CSV Building Works

| CSV Column | What It Means | Example |
|------------|---------------|---------|
| X | East/West position | 10 |
| Y | Height | 64 |
| Z | North/South position | 20 |
| Block | What to place | STONE |

---

## Step 2: Basic CSV Reader

Let's start with code that reads a simple CSV file and builds from it.

```python
# CHANGE THIS TO YOUR USERNAME!
MY_USERNAME = "USERNAME"
FILE_PATH = "C:/Users/" + MY_USERNAME + "/Desktop/"

# Read and build from CSV
def build_from_csv(filename):
    try:
        # Read the CSV file
        csv_data = file.readFile(FILE_PATH + filename)
        
        # Split into lines
        lines = csv_data.split("\n")
        
        # Skip header line, process each data line
        for i in range(1, len(lines)):
            if lines[i] != "":
                # Split line by commas
                parts = lines[i].split(",")
                
                # Get coordinates and block type
                x = int(parts[0])
                y = int(parts[1]) 
                z = int(parts[2])
                block_type = parts[3]
                
                # Place the block
                if block_type == "STONE":
                    blocks.place(STONE, pos(x, y, z))
                elif block_type == "STONE_BRICKS":
                    blocks.place(STONE_BRICKS, pos(x, y, z))
                elif block_type == "COBBLESTONE":
                    blocks.place(COBBLESTONE, pos(x, y, z))
                
        player.say("Structure built from " + filename + "!")
        
    except:
        player.say("Could not read file: " + filename)

# Test command
def on_chat_build_test():
    build_from_csv("test_structure.csv")
player.on_chat("build_test", on_chat_build_test)

player.say("Castle Builder Ready!")
player.say("Create CSV files on your Desktop")
```

### Code Explained - Basic Reader

1. **`csv_data.split("\n")`** - Splits the file into separate lines
2. **`lines[i].split(",")`** - Splits each line at commas to get X,Y,Z,Block
3. **`int(parts[0])`** - Converts text "10" to number 10
4. **Block placement** - Checks block name and places correct type

---

## Step 3: Castle Wall Builder

Now let's create a function that builds castle walls from a CSV pattern.

```python
# Add this to your existing code

# Generate castle wall CSV data
def create_wall_csv(start_x, start_y, start_z, length, height):
    csv_content = "X,Y,Z,Block\n"
    
    # Build wall going in X direction
    for x in range(length):
        for y in range(height):
            # Main wall - stone bricks
            csv_content += str(start_x + x) + "," + str(start_y + y) + "," + str(start_z) + ",STONE_BRICKS\n"
            
            # Battlements on top
            if y == height - 1 and x % 2 == 0:
                csv_content += str(start_x + x) + "," + str(start_y + y + 1) + "," + str(start_z) + ",STONE_BRICKS\n"
    
    return csv_content

# Save wall design to CSV
def on_chat_design_wall():
    # Get player position as starting point
    player_pos = player.position()
    start_x = player_pos.get_value(Axis.X)
    start_y = player_pos.get_value(Axis.Y)
    start_z = player_pos.get_value(Axis.Z)
    
    # Create 20 blocks long, 8 blocks high wall
    wall_csv = create_wall_csv(start_x, start_y, start_z, 20, 8)
    
    # Save to file
    file.writeFile(FILE_PATH + "castle_wall.csv", wall_csv)
    player.say("Wall design saved to castle_wall.csv!")
    
player.on_chat("design_wall", on_chat_design_wall)

# Build the designed wall
def on_chat_build_wall():
    build_from_csv("castle_wall.csv")
player.on_chat("build_wall", on_chat_build_wall)
```

### Code Explained - Wall Builder

- **Battlements** - Every other block on top (x % 2 == 0)
- **Dynamic positioning** - Starts at player location
- **Two-step process** - Design first, then build

---

## Step 4: Tower Generator

Let's add circular towers to our castle!

```python
# Add this to your existing code

# Generate circular tower
def create_tower_csv(center_x, center_y, center_z, radius, height):
    csv_content = "X,Y,Z,Block\n"
    
    # For each height level
    for y in range(height):
        # Create circle at this height
        for angle in range(0, 360, 10):
            # Convert angle to radians for calculation
            radian = angle * 3.14159 / 180
            
            # Calculate circle points
            x = int(center_x + radius * Math.cos(radian))
            z = int(center_z + radius * Math.sin(radian))
            
            # Main tower blocks
            csv_content += str(x) + "," + str(center_y + y) + "," + str(z) + ",STONE_BRICKS\n"
            
            # Add windows every 4 blocks up
            if y % 4 == 2 and angle % 90 == 0:
                csv_content += str(x) + "," + str(center_y + y) + "," + str(z) + ",GLASS\n"
    
    # Add cone roof
    for level in range(radius):
        new_radius = radius - level
        for angle in range(0, 360, 15):
            radian = angle * 3.14159 / 180
            x = int(center_x + new_radius * Math.cos(radian))
            z = int(center_z + new_radius * Math.sin(radian))
            roof_y = center_y + height + level
            csv_content += str(x) + "," + str(roof_y) + "," + str(z) + ",RED_WOOL\n"
    
    return csv_content

# Design and save a tower
def on_chat_design_tower():
    player_pos = player.position()
    center_x = player_pos.get_value(Axis.X) + 5
    center_y = player_pos.get_value(Axis.Y)
    center_z = player_pos.get_value(Axis.Z) + 5
    
    tower_csv = create_tower_csv(center_x, center_y, center_z, 5, 15)
    file.writeFile(FILE_PATH + "castle_tower.csv", tower_csv)
    player.say("Tower design saved!")
    
player.on_chat("design_tower", on_chat_design_tower)

def on_chat_build_tower():
    build_from_csv("castle_tower.csv")
player.on_chat("build_tower", on_chat_build_tower)
```

---

## Step 5: Complete Castle System

Here's the full castle builder with all components!

```python
# === CASTLE BUILDER SYSTEM ===
# CHANGE THIS TO YOUR USERNAME!
MY_USERNAME = "USERNAME"
FILE_PATH = "C:/Users/" + MY_USERNAME + "/Desktop/"

# Castle settings
castle_size = 40
wall_height = 10
tower_radius = 6
tower_height = 20

# === BASIC CSV BUILDER ===
def build_from_csv(filename):
    try:
        # Read the CSV file
        csv_data = file.readFile(FILE_PATH + filename)
        lines = csv_data.split("\n")
        
        blocks_placed = 0
        
        # Process each line (skip header)
        for i in range(1, len(lines)):
            if lines[i] != "":
                parts = lines[i].split(",")
                
                # Get coordinates and block
                x = int(parts[0])
                y = int(parts[1]) 
                z = int(parts[2])
                block_type = parts[3]
                
                # Place appropriate block
                if block_type == "STONE":
                    blocks.place(STONE, pos(x, y, z))
                elif block_type == "STONE_BRICKS":
                    blocks.place(STONE_BRICKS, pos(x, y, z))
                elif block_type == "COBBLESTONE":
                    blocks.place(COBBLESTONE, pos(x, y, z))
                elif block_type == "GLASS":
                    blocks.place(GLASS, pos(x, y, z))
                elif block_type == "RED_WOOL":
                    blocks.place(RED_WOOL, pos(x, y, z))
                elif block_type == "OAK_DOOR":
                    blocks.place(OAK_DOOR, pos(x, y, z))
                elif block_type == "TORCH":
                    blocks.place(TORCH, pos(x, y, z))
                    
                blocks_placed += 1
                
                # Show progress every 100 blocks
                if blocks_placed % 100 == 0:
                    player.say("Placed " + str(blocks_placed) + " blocks...")
        
        player.say("Complete! " + str(blocks_placed) + " blocks placed.")
        
    except:
        player.say("Error reading: " + filename)

# === CASTLE COMPONENTS ===

# Create wall segment
def create_wall_csv(start_x, start_y, start_z, end_x, end_z, height):
    csv_content = "X,Y,Z,Block\n"
    
    # Calculate direction
    if end_x != start_x:
        # Wall goes in X direction
        length = abs(end_x - start_x)
        for i in range(length + 1):
            for y in range(height):
                x = start_x + i if end_x > start_x else start_x - i
                # Main wall
                csv_content += str(x) + "," + str(start_y + y) + "," + str(start_z) + ",STONE_BRICKS\n"
                # Battlements
                if y == height - 1 and i % 2 == 0:
                    csv_content += str(x) + "," + str(start_y + height) + "," + str(start_z) + ",STONE_BRICKS\n"
    else:
        # Wall goes in Z direction
        length = abs(end_z - start_z)
        for i in range(length + 1):
            for y in range(height):
                z = start_z + i if end_z > start_z else start_z - i
                # Main wall
                csv_content += str(start_x) + "," + str(start_y + y) + "," + str(z) + ",STONE_BRICKS\n"
                # Battlements
                if y == height - 1 and i % 2 == 0:
                    csv_content += str(start_x) + "," + str(start_y + height) + "," + str(z) + ",STONE_BRICKS\n"
    
    return csv_content

# Create circular tower
def create_tower_csv(center_x, center_y, center_z, radius, height):
    csv_content = "X,Y,Z,Block\n"
    
    # Tower walls
    for y in range(height):
        for angle in range(0, 360, 10):
            radian = angle * 3.14159 / 180
            x = int(center_x + radius * Math.cos(radian))
            z = int(center_z + radius * Math.sin(radian))
            
            # Windows every 4 blocks, at cardinal directions
            if y % 4 == 2 and angle % 90 == 0:
                csv_content += str(x) + "," + str(center_y + y) + "," + str(z) + ",GLASS\n"
            else:
                csv_content += str(x) + "," + str(center_y + y) + "," + str(z) + ",STONE_BRICKS\n"
    
    # Cone roof
    for level in range(radius):
        new_radius = radius - level
        for angle in range(0, 360, 15):
            radian = angle * 3.14159 / 180
            x = int(center_x + new_radius * Math.cos(radian))
            z = int(center_z + new_radius * Math.sin(radian))
            csv_content += str(x) + "," + str(center_y + height + level) + "," + str(z) + ",RED_WOOL\n"
    
    # Top point
    csv_content += str(center_x) + "," + str(center_y + height + radius) + "," + str(center_z) + ",GOLD_BLOCK\n"
    
    return csv_content

# Create gate entrance
def create_gate_csv(center_x, center_y, center_z, width, height):
    csv_content = "X,Y,Z,Block\n"
    
    # Gate pillars
    for y in range(height + 3):
        # Left pillar
        csv_content += str(center_x - width/2) + "," + str(center_y + y) + "," + str(center_z) + ",STONE_BRICKS\n"
        csv_content += str(center_x - width/2) + "," + str(center_y + y) + "," + str(center_z + 1) + ",STONE_BRICKS\n"
        # Right pillar
        csv_content += str(center_x + width/2) + "," + str(center_y + y) + "," + str(center_z) + ",STONE_BRICKS\n"
        csv_content += str(center_x + width/2) + "," + str(center_y + y) + "," + str(center_z + 1) + ",STONE_BRICKS\n"
    
    # Top arch
    for x in range(-width/2, width/2 + 1):
        csv_content += str(center_x + x) + "," + str(center_y + height) + "," + str(center_z) + ",STONE_BRICKS\n"
        csv_content += str(center_x + x) + "," + str(center_y + height + 1) + "," + str(center_z) + ",STONE_BRICKS\n"
    
    # Torches
    csv_content += str(center_x - width/2 + 1) + "," + str(center_y + height - 1) + "," + str(center_z + 1) + ",TORCH\n"
    csv_content += str(center_x + width/2 - 1) + "," + str(center_y + height - 1) + "," + str(center_z + 1) + ",TORCH\n"
    
    return csv_content

# === FULL CASTLE GENERATOR ===
def generate_full_castle():
    player_pos = player.position()
    base_x = player_pos.get_value(Axis.X)
    base_y = player_pos.get_value(Axis.Y)
    base_z = player_pos.get_value(Axis.Z)
    
    full_csv = "X,Y,Z,Block\n"
    
    # Generate 4 walls
    # Front wall with gate
    wall_front = create_wall_csv(base_x, base_y, base_z, base_x + castle_size, base_z, wall_height)
    # Back wall
    wall_back = create_wall_csv(base_x, base_y, base_z + castle_size, base_x + castle_size, base_z + castle_size, wall_height)
    # Left wall
    wall_left = create_wall_csv(base_x, base_y, base_z, base_x, base_z + castle_size, wall_height)
    # Right wall
    wall_right = create_wall_csv(base_x + castle_size, base_y, base_z, base_x + castle_size, base_z + castle_size, wall_height)
    
    # Generate 4 corner towers
    tower1 = create_tower_csv(base_x, base_y, base_z, tower_radius, tower_height)
    tower2 = create_tower_csv(base_x + castle_size, base_y, base_z, tower_radius, tower_height)
    tower3 = create_tower_csv(base_x, base_y, base_z + castle_size, tower_radius, tower_height)
    tower4 = create_tower_csv(base_x + castle_size, base_y, base_z + castle_size, tower_radius, tower_height)
    
    # Generate gate
    gate = create_gate_csv(base_x + castle_size/2, base_y, base_z, 6, wall_height)
    
    # Combine all parts (skip headers)
    full_csv += wall_front.split("\n", 1)[1]
    full_csv += wall_back.split("\n", 1)[1]
    full_csv += wall_left.split("\n", 1)[1]
    full_csv += wall_right.split("\n", 1)[1]
    full_csv += tower1.split("\n", 1)[1]
    full_csv += tower2.split("\n", 1)[1]
    full_csv += tower3.split("\n", 1)[1]
    full_csv += tower4.split("\n", 1)[1]
    full_csv += gate.split("\n", 1)[1]
    
    # Save complete castle
    file.writeFile(FILE_PATH + "complete_castle.csv", full_csv)
    player.say("Complete castle design saved!")
    player.say("File has " + str(len(full_csv.split("\n")) - 1) + " blocks")

# === COMMANDS ===
def on_chat_design_castle():
    generate_full_castle()
player.on_chat("design", on_chat_design_castle)

def on_chat_build_castle():
    player.say("Building castle... this may take a moment!")
    build_from_csv("complete_castle.csv")
player.on_chat("build", on_chat_build_castle)

def on_chat_clear():
    player_pos = player.position()
    x = player_pos.get_value(Axis.X)
    y = player_pos.get_value(Axis.Y)
    z = player_pos.get_value(Axis.Z)
    # Clear a large area
    blocks.fill(AIR, pos(x-50, y, z-50), pos(x+50, y+30, z+50))
    player.say("Area cleared!")
player.on_chat("clear", on_chat_clear)

# Help command
def on_chat_help():
    player.say("=== CASTLE BUILDER ===")
    player.say("design - Create castle blueprint")
    player.say("build - Build from blueprint")
    player.say("clear - Clear building area")
    player.say("Files save to: " + FILE_PATH)

player.on_chat("help", on_chat_help)

# Initialize
player.say("Castle Builder Ready!")
player.say("Type 'help' for commands")
player.say("Type 'design' then 'build'!")
```

---

## 📊 Example CSV File Format

Here's what a simple tower CSV looks like:

```csv
X,Y,Z,Block
100,64,100,STONE_BRICKS
101,64,100,STONE_BRICKS
102,64,100,STONE_BRICKS
100,65,100,STONE_BRICKS
101,65,100,GLASS
102,65,100,STONE_BRICKS
```

---

## 🕹How to Use Castle Builder

1. **Type `design`** - Creates complete castle blueprint CSV
2. **Type `build`** - Builds the castle from the CSV
3. **Type `clear`** - Clears area for building

### Building Order:
- First designs and saves to CSV
- Then reads CSV and builds block by block
- Shows progress every 100 blocks

---

## Fun Challenges

1. **Custom Castle Sizes**
```python
def on_chat_small_castle():
    global castle_size, wall_height
    castle_size = 20
    wall_height = 6
    generate_full_castle()
player.on_chat("small", on_chat_small_castle)
```

2. **Different Materials**
   - Edit the CSV file in Notepad
   - Change STONE_BRICKS to GOLD_BLOCK
   - Build a golden castle!

3. **Castle Additions**
   - Add a moat (WATER blocks)
   - Create interior buildings
   - Design a drawbridge

4. **Multi-Level Towers**
   - Add floors inside towers
   - Create spiral staircases
   - Add arrow slits

---

## Pro Tips

1. **Start Small** - Test with small structures first
2. **Check CSV** - Open in Excel to verify your design
3. **Backup Designs** - Copy CSV files before editing
4. **Build in Stages** - Design walls, towers, and gates separately
5. **Use Clear** - Always clear the area before building

---

## 🎓 What You Learned

☑️ Reading and parsing CSV files  
☑️ Generating geometric shapes (circles for towers)  
☑️ Modular building design  
☑️ File I/O for large data sets  
☑️ Progress tracking for long operations  
☑️ 3D coordinate calculations  

---

## 🚀 Next Steps

* Add interior rooms and floors
* Create different castle styles (Japanese, Medieval, Fantasy)
* Build villages around your castle
* Add defensive features (moats, traps)
* Create a castle template library

Remember: Great castles start with great blueprints! 🏰📊
