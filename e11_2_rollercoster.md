![Minecraft Education Logo](images/education-minecraft-logo.png)

### 🎢 Lesson 11: Advanced Roller Coaster Engineering 🚀

#### 🎯 Learning Objectives:

* Master the **Roller Coaster Builder** extension in MakeCode
* Design complex roller coaster tracks using Python functions and loops
* Implement physics concepts: momentum, gravity, and centripetal force
* Create themed roller coasters with decorations and special effects
* Debug and optimize track designs for safety and excitement

---

#### 📦 Step 1: Add the Extension

If the **Roller Coaster Builder** extension isn't already added:

Create a MakeCode Project called "Epic_Rollercoaster"

<img width="529" alt="image" src="https://github.com/user-attachments/assets/7360a18f-9892-4dc5-b4c3-4b416439563f" />

<img width="675" alt="image" src="https://github.com/user-attachments/assets/c179567c-69e9-4654-b537-5daafc3fb530" />

Scroll down the MakeCode elements on the left and select "Extensions"

<img width="491" alt="image" src="https://github.com/user-attachments/assets/ded6ca7b-b856-4ad5-8021-2e0c042790cf" />

Search extensions for "Roller Coaster". Then click on it to add the extension.

<img width="673" alt="image" src="https://github.com/user-attachments/assets/e4b875f8-e51b-4d5f-8f4b-1d083ddfdd7b" />

Switch to Python Code and clear the code.

![image](https://github.com/user-attachments/assets/35e7e530-6b71-4ba2-95db-7f31b95f1faf)

---

#### 🧱 Step 2: Create Multiple Commands

Let's create different commands for different roller coaster designs:

```python
# Basic roller coaster
def on_basic_coaster():
    pass
player.on_chat("basic", on_basic_coaster)

# Advanced roller coaster
def on_advanced_coaster():
    pass
player.on_chat("advanced", on_advanced_coaster)

# Mega roller coaster
def on_mega_coaster():
    pass
player.on_chat("mega", on_mega_coaster)
```

---

#### 🎨 Step 3: Build a Themed Basic Coaster

Replace the `pass` in `on_basic_coaster` with a space-themed design:

```python
def on_basic_coaster():
    # Clear the area first
    blocks.fill(AIR, pos(-20, -1, -20), pos(50, 30, 50))
    
    # Create a launch pad with glowstone
    blocks.fill(GLOWSTONE, pos(-2, -1, -2), pos(2, -1, 2))
    
    # Start the track
    rollerCoasterBuilder.place_track_start(pos(0, 0, 0), NORTH)
    
    # Launch sequence - straight acceleration
    rollerCoasterBuilder.add_straight_line(15)
    
    # First hill - the anticipation builder
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 12)
    
    # The big drop!
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 15)
    
    # Recovery turn
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    
    # Speed section
    rollerCoasterBuilder.add_straight_line(10)
    
    # End safely
    rollerCoasterBuilder.place_track_end()
    
    # Add decorations
    blocks.place(SEA_LANTERN, pos(0, 5, 0))
    player.say("Basic Space Coaster Ready! 🚀")
```

---

#### 🔧 Step 4: Create Helper Functions

Add these helper functions before your chat commands to make building easier:

```python
# Helper function to create a loop-de-loop pattern
def create_loop():
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 5)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 3)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 3)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 5)
    rollerCoasterBuilder.add_turn(LEFT_TURN)

# Helper function to create a corkscrew
def create_corkscrew(direction, height):
    for i in range(3):
        rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, direction, height, 1)
        rollerCoasterBuilder.add_spiral(RcbVerticalDirection.DOWN, direction, height, 1)

# Helper function to add track lighting
def add_lights(start_pos, length):
    for i in range(length):
        blocks.place(GLOWSTONE, start_pos.add(pos(i * 2, -2, 0)))
```

---

#### 🎢 Step 5: Build the Advanced Coaster

Replace the `pass` in `on_advanced_coaster` with a more complex design:

```python
def on_advanced_coaster():
    # Clear and prepare the area
    blocks.fill(AIR, pos(-30, -1, -30), pos(60, 40, 60))
    
    # Create a themed platform
    blocks.fill(STONE_BRICKS, pos(-5, -2, -5), pos(5, -1, 5))
    
    # Start the coaster
    rollerCoasterBuilder.place_track_start(pos(0, 0, 0), NORTH)
    
    # Chain lift hill
    player.say("Going up... 🎢")
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 20)
    
    # The terrifying drop
    rollerCoasterBuilder.add_free_fall(15)
    
    # High-speed chicane
    rollerCoasterBuilder.add_turn(RIGHT_TURN)
    rollerCoasterBuilder.add_straight_line(5)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_straight_line(5)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    
    # Create a loop using our helper
    create_loop()
    
    # Spiral madness
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, RIGHT_TURN, 8, 2)
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.DOWN, LEFT_TURN, 8, 2)
    
    # Brake run
    rollerCoasterBuilder.add_straight_line(10)
    
    # Station return
    rollerCoasterBuilder.add_turn(RIGHT_TURN)
    rollerCoasterBuilder.add_straight_line(8)
    rollerCoasterBuilder.place_track_end()
    
    # Add special effects
    add_lights(pos(0, 0, 0), 10)
    player.say("Advanced Thrill Coaster Complete! 🎉")
```

---

#### 🚀 Step 6: Create the Mega Coaster

Replace the `pass` in `on_mega_coaster` with the ultimate design:

```python
def on_mega_coaster():
    # Massive clear
    blocks.fill(AIR, pos(-50, -1, -50), pos(100, 60, 100))
    
    # Create multiple platforms
    blocks.fill(QUARTZ_BLOCK, pos(-10, -2, -10), pos(10, -1, 10))
    blocks.fill(QUARTZ_BLOCK, pos(40, 18, -10), pos(50, 19, 10))
    
    # Start position
    rollerCoasterBuilder.place_track_start(pos(0, 0, 0), NORTH)
    
    # SECTION 1: The Launcher
    player.say("MEGA COASTER ACTIVATING! 🚀🎢🔥")
    rollerCoasterBuilder.add_straight_line(20)
    
    # SECTION 2: The Mountain Climb
    for i in range(3):
        rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)
        rollerCoasterBuilder.add_turn(RIGHT_TURN if i % 2 == 0 else LEFT_TURN)
    
    # SECTION 3: The Mega Drop
    rollerCoasterBuilder.add_free_fall(25)
    
    # SECTION 4: Underground Tunnel
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 5)
    rollerCoasterBuilder.add_straight_line(15)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 5)
    
    # SECTION 5: Double Corkscrew
    create_corkscrew(LEFT_TURN, 5)
    create_corkscrew(RIGHT_TURN, 5)
    
    # SECTION 6: The Pretzel Loop
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 8)
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, LEFT_TURN, 10, 3)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.DOWN, RIGHT_TURN, 10, 3)
    
    # SECTION 7: Speed Hills
    for i in range(5):
        rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 3)
        rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 3)
    
    # SECTION 8: Final Helix
    for i in range(4):
        rollerCoasterBuilder.add_turn(RIGHT_TURN)
        rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 2)
    
    # End sequence
    rollerCoasterBuilder.add_straight_line(15)
    rollerCoasterBuilder.place_track_end()
    
    # Epic decorations
    add_lights(pos(0, 0, 0), 20)
    blocks.place(BEACON, pos(0, 30, 0))
    
    # Fireworks!
    mobs.spawn(FIREWORKS_ROCKET, pos(0, 5, 0))
    mobs.spawn(FIREWORKS_ROCKET, pos(5, 5, 5))
    mobs.spawn(FIREWORKS_ROCKET, pos(-5, 5, -5))
    
    player.say("MEGA COASTER COMPLETE! 🎆🎢🎆")
```

---

#### 🛠️ Step 7: Add a Safety Test Function

Create a function to test your coaster:

```python
def on_test_coaster():
    player.say("Testing coaster safety... 🔍")
    
    # Teleport player to a good viewing position
    player.teleport(pos(10, 20, 10))
    
    # Spawn a test dummy (armor stand)
    mobs.spawn(ARMOR_STAND, pos(0, 1, 0))
    
    player.say("Test complete! Ready for riders! ✅")

player.on_chat("test", on_test_coaster)
```

---

#### ✅ Full Enhanced Code

Here's the complete code with all features:

```python
# Helper function to create a loop-de-loop pattern
def create_loop():
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 5)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 3)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 3)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 5)
    rollerCoasterBuilder.add_turn(LEFT_TURN)

# Helper function to create a corkscrew
def create_corkscrew(direction, height):
    for i in range(3):
        rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, direction, height, 1)
        rollerCoasterBuilder.add_spiral(RcbVerticalDirection.DOWN, direction, height, 1)

# Helper function to add track lighting
def add_lights(start_pos, length):
    for i in range(length):
        blocks.place(GLOWSTONE, start_pos.add(pos(i * 2, -2, 0)))

# Basic roller coaster
def on_basic_coaster():
    # Clear the area first
    blocks.fill(AIR, pos(-20, -1, -20), pos(50, 30, 50))
    
    # Create a launch pad with glowstone
    blocks.fill(GLOWSTONE, pos(-2, -1, -2), pos(2, -1, 2))
    
    # Start the track
    rollerCoasterBuilder.place_track_start(pos(0, 0, 0), NORTH)
    
    # Launch sequence - straight acceleration
    rollerCoasterBuilder.add_straight_line(15)
    
    # First hill - the anticipation builder
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 12)
    
    # The big drop!
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 15)
    
    # Recovery turn
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    
    # Speed section
    rollerCoasterBuilder.add_straight_line(10)
    
    # End safely
    rollerCoasterBuilder.place_track_end()
    
    # Add decorations
    blocks.place(SEA_LANTERN, pos(0, 5, 0))
    player.say("Basic Space Coaster Ready! 🚀")

player.on_chat("basic", on_basic_coaster)

# Advanced roller coaster
def on_advanced_coaster():
    # Clear and prepare the area
    blocks.fill(AIR, pos(-30, -1, -30), pos(60, 40, 60))
    
    # Create a themed platform
    blocks.fill(STONE_BRICKS, pos(-5, -2, -5), pos(5, -1, 5))
    
    # Start the coaster
    rollerCoasterBuilder.place_track_start(pos(0, 0, 0), NORTH)
    
    # Chain lift hill
    player.say("Going up... 🎢")
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 20)
    
    # The terrifying drop
    rollerCoasterBuilder.add_free_fall(15)
    
    # High-speed chicane
    rollerCoasterBuilder.add_turn(RIGHT_TURN)
    rollerCoasterBuilder.add_straight_line(5)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_straight_line(5)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    
    # Create a loop using our helper
    create_loop()
    
    # Spiral madness
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, RIGHT_TURN, 8, 2)
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.DOWN, LEFT_TURN, 8, 2)
    
    # Brake run
    rollerCoasterBuilder.add_straight_line(10)
    
    # Station return
    rollerCoasterBuilder.add_turn(RIGHT_TURN)
    rollerCoasterBuilder.add_straight_line(8)
    rollerCoasterBuilder.place_track_end()
    
    # Add special effects
    add_lights(pos(0, 0, 0), 10)
    player.say("Advanced Thrill Coaster Complete! 🎉")

player.on_chat("advanced", on_advanced_coaster)

# Mega roller coaster
def on_mega_coaster():
    # Massive clear
    blocks.fill(AIR, pos(-50, -1, -50), pos(100, 60, 100))
    
    # Create multiple platforms
    blocks.fill(QUARTZ_BLOCK, pos(-10, -2, -10), pos(10, -1, 10))
    blocks.fill(QUARTZ_BLOCK, pos(40, 18, -10), pos(50, 19, 10))
    
    # Start position
    rollerCoasterBuilder.place_track_start(pos(0, 0, 0), NORTH)
    
    # SECTION 1: The Launcher
    player.say("MEGA COASTER ACTIVATING! 🚀🎢🔥")
    rollerCoasterBuilder.add_straight_line(20)
    
    # SECTION 2: The Mountain Climb
    for i in range(3):
        rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)
        rollerCoasterBuilder.add_turn(RIGHT_TURN if i % 2 == 0 else LEFT_TURN)
    
    # SECTION 3: The Mega Drop
    rollerCoasterBuilder.add_free_fall(25)
    
    # SECTION 4: Underground Tunnel
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 5)
    rollerCoasterBuilder.add_straight_line(15)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 5)
    
    # SECTION 5: Double Corkscrew
    create_corkscrew(LEFT_TURN, 5)
    create_corkscrew(RIGHT_TURN, 5)
    
    # SECTION 6: The Pretzel Loop
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 8)
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, LEFT_TURN, 10, 3)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.DOWN, RIGHT_TURN, 10, 3)
    
    # SECTION 7: Speed Hills
    for i in range(5):
        rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 3)
        rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 3)
    
    # SECTION 8: Final Helix
    for i in range(4):
        rollerCoasterBuilder.add_turn(RIGHT_TURN)
        rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 2)
    
    # End sequence
    rollerCoasterBuilder.add_straight_line(15)
    rollerCoasterBuilder.place_track_end()
    
    # Epic decorations
    add_lights(pos(0, 0, 0), 20)
    blocks.place(BEACON, pos(0, 30, 0))
    
    # Fireworks!
    mobs.spawn(FIREWORKS_ROCKET, pos(0, 5, 0))
    mobs.spawn(FIREWORKS_ROCKET, pos(5, 5, 5))
    mobs.spawn(FIREWORKS_ROCKET, pos(-5, 5, -5))
    
    player.say("MEGA COASTER COMPLETE! 🎆🎢🎆")

player.on_chat("mega", on_mega_coaster)

# Test function
def on_test_coaster():
    player.say("Testing coaster safety... 🔍")
    
    # Teleport player to a good viewing position
    player.teleport(pos(10, 20, 10))
    
    # Spawn a test dummy (armor stand)
    mobs.spawn(ARMOR_STAND, pos(0, 1, 0))
    
    player.say("Test complete! Ready for riders! ✅")

player.on_chat("test", on_test_coaster)
```

---

#### 🕹️ How to Use Your Coasters

1. Click the green play ▶️ button to run the code
2. In Minecraft, press **T** to open chat
3. Type one of these commands:
   - `basic` - Build the Space Coaster
   - `advanced` - Build the Thrill Coaster  
   - `mega` - Build the Ultimate Mega Coaster
   - `test` - Test your coaster with safety checks
4. Find the white and pink start wall with a minecart
5. Right-click the cart to enter, then press the button to launch!

---

#### 🧠 Advanced Challenges

1. **Physics Challenge**: Create a coaster that demonstrates conservation of energy
2. **Theme Challenge**: Build a coaster themed around:
   - 🏰 Medieval Castle
   - 🌊 Underwater Adventure
   - 🌋 Volcano Escape
   - 👽 Alien Invasion

3. **Code Challenge**: 
   - Add a timer to track ride duration
   - Create a function that counts total track pieces
   - Build a coaster that spells out letters when viewed from above

4. **Engineering Challenge**:
   - Design a dueling coaster (two tracks that interact)
   - Create a coaster with multiple paths using switches
   - Build a coaster that goes through different biomes

---

#### 💡 Tips for Success

- **Start Small**: Test each section before adding more
- **Height Matters**: Higher starts = more speed = more fun!
- **Banking Turns**: Use spirals before sharp turns to prevent crashes
- **Theme Everything**: Add blocks, mobs, and particles for atmosphere
- **Safety First**: Always test with the `test` command before riding

---

#### 🎓 What You've Learned

- ✅ Using functions to organize complex code
- ✅ Creating reusable helper functions
- ✅ Implementing loops for repetitive patterns
- ✅ Combining multiple programming concepts
- ✅ Testing and debugging techniques
