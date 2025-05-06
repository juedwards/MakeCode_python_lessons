![Minecraft Education Logo](images/education-minecraft-logo.png)

## 🏠 Chapter 10: Build a Simple House with Code

---

### 🎯 What You’ll Learn

In this project, you’ll:

* Build a Minecraft house step by step using Python code.
* Use **loops**, **functions**, **coordinates**, and **chat commands**.
* Learn how to structure a larger project by breaking it into **sections**.

---

### 🧠 What Will We Build?

Your code will:
✅ Build a wooden **floor**
✅ Add 4 **walls**
✅ Leave a **doorway**
✅ Place a **roof**
✅ Run when you type `"house"` in the chat

---

## 🪄 Step-by-Step: Code Breakdown

### 🧱 Step 1: Define the Function

This creates a function that runs when you type the word `"house"` in Minecraft chat.

```python
def build_house():
```

We’ll fill this function with all the steps to build the house!

---

### 🪵 Step 2: Build the Floor

This loop places a 5x5 wooden floor using **oak planks**.

```python
    for x in range(5):
        for z in range(5):
            blocks.place(OAK_PLANKS, positions.create(x, 0, z))
```

💡 We’re using a **nested loop** (a loop inside a loop) to place one row at a time across the X and Z directions.

---

### 🧱 Step 3: Build the Walls

This part builds the front, back, left, and right walls using **oak logs**.

```python
    for y in range(1, 4):  # wall height = 3
        for x in range(5):
            blocks.place(OAK_LOG, positions.create(x, y, 0))      # Front wall
            blocks.place(OAK_LOG, positions.create(x, y, 4))      # Back wall
        for z in range(1, 4):
            blocks.place(OAK_LOG, positions.create(0, y, z))      # Left wall
            blocks.place(OAK_LOG, positions.create(4, y, z))      # Right wall
```

🧠 The walls are 3 blocks high (`y` goes from 1 to 3).
We build all 4 walls one row at a time.

---

### 🚪 Step 4: Add a Doorway

This clears a 2-block-tall doorway in the front wall.

```python
    blocks.place(AIR, positions.create(2, 1, 0))
    blocks.place(AIR, positions.create(2, 2, 0))
```

🔓 These two blocks remove part of the wall to make an opening you can walk through.

---

### 🧱 Step 5: Build the Roof

This adds a flat **stone roof** to cover the house.

```python
    for x in range(5):
        for z in range(5):
            blocks.place(STONE, positions.create(x, 4, z))
```

🏠 The roof goes on top at `y = 4`, one layer above the walls.

---

### 💬 Step 6: Run the Function with a Chat Command

This tells Minecraft to run `build_house()` when you type `house` in chat.

```python
player.on_chat("house", build_house)
```

✅ Now your house appears when you type:

```
house
```

---

### 🧪 Try It Out

1. Click the **green Play button** in Code Builder.
2. In Minecraft, press **T** and type:

   ```
   house
   ```
3. Hit **Enter** and watch your code build the house!

---

## 🎮 Bonus Challenges

Try upgrading your house!

✅ Add windows with `GLASS`.
✅ Place a `TORCH` inside.
✅ Replace `STONE` roof with `GLASS` roof.
✅ Use a variable like `size = 7` to make a bigger house.

---
