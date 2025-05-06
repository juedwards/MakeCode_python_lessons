![Minecraft Education Logo](images/education-minecraft-logo.png)

## 🏰 Chapter 11: Build a Castle with Code

---

### 🎯 What You’ll Learn

In this project, you’ll:

* Build a **castle with four towers** and walls.
* Use **functions** to split the castle into parts (towers, walls, gate).
* Practice using **positioning, loops, and chat commands**.

---

### 🧠 What Is a Castle?

A simple castle has:

* Four **corner towers** 🗼
* Connecting **walls** 🧱
* A **gate** you can walk through 🚪

You’ll build it all by coding!

---

## 🪄 Step-by-Step: Castle Builder

---

### 🧱 Step 1: Start the Castle Function

We create a chat command to build the castle.

```python
def build_castle():
```

---

### 🗼 Step 2: Build a Tower

Let’s make a function to build a small tower at any corner:

```python
def build_tower(x, z):
    for y in range(5):  # height
        for dx in range(3):
            for dz in range(3):
                if dx == 0 or dx == 2 or dz == 0 or dz == 2:
                    blocks.place(STONE, positions.create(x + dx, y, z + dz))
```

🧱 This builds a 3x3 tower with hollow inside walls using `STONE`.

---

### 🧭 Step 3: Place Towers in Four Corners

Now use your `build_tower()` function four times inside `build_castle()`:

```python
    build_tower(0, 0)
    build_tower(0, 20)
    build_tower(20, 0)
    build_tower(20, 20)
```

📏 These go in a square: 20 blocks apart.

---

### 🧱 Step 4: Build the Walls Between Towers

Add these inside `build_castle()` to connect the towers:

```python
    for i in range(21):
        blocks.place(STONE, positions.create(i, 2, 0))     # front wall
        blocks.place(STONE, positions.create(i, 2, 20))    # back wall
        blocks.place(STONE, positions.create(0, 2, i))     # left wall
        blocks.place(STONE, positions.create(20, 2, i))    # right wall
```

🧱 This builds 1-block-high walls (you can stack higher if you'd like).

---

### 🚪 Step 5: Add a Gate

Clear a 2-block-wide doorway in the front wall:

```python
    blocks.place(AIR, positions.create(10, 2, 0))
    blocks.place(AIR, positions.create(11, 2, 0))
```

🔓 Now you can walk in!

---

### 💬 Step 6: Add a Chat Command

```python
player.on_chat("castle", build_castle)
```

⛏️ Type `castle` in Minecraft chat to build it!

---

### 🧪 Full Code (Copy & Paste)

```python
def build_tower(x, z):
    for y in range(5):  # tower height
        for dx in range(3):
            for dz in range(3):
                if dx == 0 or dx == 2 or dz == 0 or dz == 2:
                    blocks.place(STONE, positions.create(x + dx, y, z + dz))

def build_castle():
    # Place towers
    build_tower(0, 0)
    build_tower(0, 20)
    build_tower(20, 0)
    build_tower(20, 20)

    # Connect walls
    for i in range(21):
        blocks.place(STONE, positions.create(i, 2, 0))
        blocks.place(STONE, positions.create(i, 2, 20))
        blocks.place(STONE, positions.create(0, 2, i))
        blocks.place(STONE, positions.create(20, 2, i))

    # Add a gate
    blocks.place(AIR, positions.create(10, 2, 0))
    blocks.place(AIR, positions.create(11, 2, 0))

player.on_chat("castle", build_castle)
```

---

## 🎮 Bonus Challenges

✅ Add **flags** on top of each tower using `RED_WOOL`
✅ Place `TORCH` blocks at each corner for light
✅ Add a second layer to the walls for more height
✅ Create a **drawbridge** using `OAK_PLANKS` and a new chat command!

---
