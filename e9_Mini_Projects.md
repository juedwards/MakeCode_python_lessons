![Minecraft Education Logo](images/education-minecraft-logo.png)

## 🎮 Exercise 9: Mini Projects and Code Challenges!

### 🎯 What You’ll Learn

In this activity, you’ll:

* Build **your own projects** using everything you’ve learned.
* Combine loops, functions, variables, and conditionals.
* Be creative and make your Minecraft world interactive!

---

### 🤖 Project 1: The Auto Bridge Builder

**Goal**: Type a chat command and build a bridge of planks ahead of the player.

```python
def build_bridge():
    length = 10
    for i in range(length):
        blocks.place(PLANKS_OAK, positions.create(i, -1, 0))

player.on_chat("bridge", build_bridge)
```

🪵 Walk forward and see your bridge appear!

---

### 💥 Project 2: The TNT Warning System

**Goal**: If the player steps on TNT, show a warning message.

```python
if blocks.test_for_block(TNT, pos(0, -1, 0)):
    player.say("Whoa! You're on TNT! Move away!")
```

🚨 You can turn this into a safety game!

---

### 🌳 Project 3: Random Tree Garden

**Goal**: Plant 5 oak saplings in random places near the player.

```python
for i in range(5):
    blocks.place(OAK_SAPLING, randpos(pos(-3, 0, -3), pos(3, 0, 3)))
```

🌱 This grows a fun, messy garden!

---

### 🧱 Project 4: Block Detector Maze

**Goal**: Say something when the player steps on a special block (like gold).

```python
if blocks.test_for_block(GOLD_BLOCK, pos(0, -1, 0)):
    player.say("You found the golden path!")
```

Use this in a maze challenge or puzzle room!

---

### 💬 Project 5: Chat-Powered Builder

**Goal**: Use different chat commands to build structures.

```python
def tower():
    for y in range(5):
        blocks.place(STONE, positions.create(0, y, 0))

def floor():
    for x in range(5):
        for z in range(5):
            blocks.place(OAK_PLANKS, positions.create(x, 0, z))

player.on_chat("tower", tower)
player.on_chat("floor", floor)
```

Now you have a **command-based builder tool**!

---

### 🏁 Bonus Challenge: Secret Code Room

**Goal**: Only open the door if the player types the correct password in chat.

```python
def unlock():
    code = "1234"
    if player.name() == "YourNameHere":
        blocks.place(AIR, positions.create(1, 0, 0))  # Removes the door

player.on_chat("1234", unlock)
```

🔒 Replace `"YourNameHere"` with your Minecraft name!

---

### 🧠 What Did You Learn?

* You can **combine everything**: loops, variables, functions, and conditions.
* Chat commands make your projects fun and interactive.
* Coding makes your Minecraft world do **whatever you imagine**!
