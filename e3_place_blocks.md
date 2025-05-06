![Minecraft Education Logo](images/education-minecraft-logo.png)

## 🧱 Exercise 3: Placing and Building with Blocks!

### 🎯 What You’ll Learn

In this activity, you'll:

* Place different kinds of blocks using code.
* Use coordinates to build in Minecraft.
* Create patterns and towers with loops!

---

### 🧠 What is a Block?

In Minecraft, everything is made of **blocks** — stone, dirt, glass, gold, and so many more! You can place them by hand… but using **code** is way faster (and cooler).

Let’s learn how to **place blocks using MakeCode Python**!

---

### 🪄 Step-by-Step Instructions

#### ✅ Step 1: Open Code Builder

1. Press the **C** key in Minecraft.
2. Pick **MakeCode** and choose **Python** editor.

---

### 📦 Step 2: Place a Block at Your Feet

Type this code to place a **stone block** where you're standing:

```python
blocks.place(STONE, player.position())
```

🧠 `player.position()` means "where I am standing."

---

### 🧭 Step 3: Place a Block Somewhere Else

You can choose **exact coordinates** using `positions.create(x, y, z)`.

Try this:

```python
blocks.place(GOLD_BLOCK, positions.create(2, 0, 2))
```

📍 This puts a gold block **2 blocks right and 2 blocks forward** from the starting point.

---

### 🔁 Step 4: Build a Row with a Loop

Let’s place 5 stone blocks in a row using a loop:

```python
for i in range(5):
    blocks.place(STONE, positions.create(i, 0, 0))
```

🧠 This builds a straight line on the **X** axis!

---

### ❌ Step 5: Remove a Block

You can remove a block by placing **AIR** on top of it:

```python
blocks.place(AIR, positions.create(2, 0, 2))
```

This removes the block at (2, 0, 2) — like a delete button!

---

### 👀 Step 6: Check What You're Standing On

Let's make your player talk if they're standing in water:

```python
if blocks.test_for_block(WATER, player.position()):
    player.say("You're standing in water!")
```

Try standing in a pond and running this code!

---

### 🧪 Practice: Build a Glass Tower

Here’s how to build a tall tower using a loop:

```python
for y in range(5):
    blocks.place(GLASS, positions.create(0, y, 0))
```

🏗️ This places 5 **glass blocks** on top of each other — building up on the **Y** axis.

---

### 🧠 What Did You Learn?

* How to **place blocks** using code.
* How to use **coordinates** to choose where.
* How to use a **loop** to repeat actions and build faster.
