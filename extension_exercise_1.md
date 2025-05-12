## 🧱 Extension: Build a 5x5 Agent Wall House

**What you will make:**
In this challenge, you will program the Agent to build **four tall walls** in a square shape — like the walls of a small stone house!

### 🎯 What you will learn:

* How to use **loops** inside loops
* How to make the Agent **build upwards**
* How to build a **square wall structure** using code

---

### 🔧 Step-by-step Instructions

#### 1. Start with this code:

Paste the code below into MakeCode and run the `wall` command in the chat.

```python
# Chat command to build a 5x5 square enclosure
def build_walls():
    agent.teleport_to_player()
    agent.set_assist(DESTROY_OBSTACLES, True)
    agent.set_item(STONE, 64, 1)
    agent.set_slot(1)
    agent.move(FORWARD, 1)
    agent.move(LEFT, 1)

    agent.set_assist(PLACE_ON_MOVE, True)

    for layer in range(5):  # This makes the walls 5 blocks high
        for side in range(4):  # This makes the Agent go around the square
            agent.move(FORWARD, 5)
            agent.turn_right()
        agent.move(UP, 1)  # After each square, go up 1 block

player.on_chat("wall", build_walls)
```
![image](https://github.com/user-attachments/assets/31da7cc5-e709-48c4-b271-99467b1c5c3d)

---

### 🧠 What is happening?

Let’s break it down:

* `agent.teleport_to_player()`: The Agent comes to you.
* `agent.set_item(STONE, 64, 1)`: The Agent gets 64 stone blocks.
* `for layer in range(5)`: This builds the wall **five blocks high**.
* `for side in range(4)`: This tells the Agent to build **all four sides** of the square.
* `agent.move(UP, 1)`: After each layer, the Agent moves up to build the next level!

---

### 💡 Challenge: Make it your own!

Try one or more of these ideas:

✅ Add a **roof** using another `for` loop.

```python
# Chat command to build a 5x5 square enclosure with a roof
def build_walls():
    agent.teleport_to_player()
    agent.set_assist(DESTROY_OBSTACLES, True)
    agent.set_item(STONE, 64, 1)
    agent.set_slot(1)
    agent.move(FORWARD, 1)
    agent.move(LEFT, 1)

    agent.set_assist(PLACE_ON_MOVE, True)

    # Build 5x5 walls, 5 blocks high
    for layer in range(5):
        for side in range(4):
            agent.move(FORWARD, 5)
            agent.turn_right()
        agent.move(UP, 1)

    # Move agent to top-left corner of roof
    agent.set_assist(PLACE_ON_MOVE, False)
    agent.move(RIGHT, 1)
    agent.move(BACK, 5)
    agent.turn_left()

    agent.set_assist(PLACE_ON_MOVE, True)

    # Build flat 5x5 roof using zigzag pattern
    for row in range(5):
        for col in range(4):  # Move forward 4 times (5 blocks total with starting position)
            agent.move(FORWARD, 1)
        if row < 4:  # Turn and go to next row
            if row % 2 == 0:
                agent.turn_right()
                agent.move(FORWARD, 1)
                agent.turn_right()
            else:
                agent.turn_left()
                agent.move(FORWARD, 1)
                agent.turn_left()

player.on_chat("wall", build_walls)
```

### 🔍 What’s New?

* The **roof** is built using two nested loops:

  * `row` loop moves across each row.
  * `col` loop places 5 blocks in each row.
  * At the end of each row, the Agent **zig-zags** to the next row.
* The Agent **ends up on top** of the wall before building the roof.

---

### 📝 Reflection

* What happens if you remove the `agent.move(UP, 1)` line?
* How would you make the walls **longer** or **taller**?

---

Would you like me to write this up as a Markdown `.md` file for the repo with headings and formatting?
