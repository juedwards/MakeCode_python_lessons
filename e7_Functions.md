![Minecraft Education Logo](images/education-minecraft-logo.png)

## Exercise 7: Writing Your Own Code Blocks (Functions!)

### 🎯 What You’ll Learn

In this activity, you’ll:

* Create your own **function** (a mini program).
* Give your function a name and run it any time you want.
* Make your code **neater** and **easier to reuse**.

---

### 🤔 What is a Function?

A **function** is like a set of instructions with a name.

You can tell Minecraft:
💬 "When I say `build_stairs()`, follow these steps!"

Instead of writing the same thing again and again, you just **call the function**.

---

### 🪄 Step-by-Step Instructions

#### ✅ Step 1: Open Code Builder

1. Press **C** in Minecraft.
2. Choose **MakeCode** and the **Python** editor.

---

### 🧱 Step 2: Write a Simple Function

Let’s make a function that places a gold block under your feet:

```python
def place_gold():
    blocks.place(GOLD_BLOCK, pos(0, -1, 0))
```

Now when you write `place_gold()`, it will do that job.

---

### ▶️ Step 3: Call the Function

You must **call the function** to make it run:

```python
place_gold()
```

🧠 Nothing happens unless you tell Minecraft to run it.

---

### 🧰 Step 4: Make a Reusable Build Tool

Let’s make a function that builds a short wall:

```python
def build_wall():
    for i in range(5):
        blocks.place(STONE, positions.create(i, 0, 0))
```

Now type:

```python
build_wall()
```

🏗️ It places a row of 5 stone blocks.

---

### ✨ Step 5: Add a Chat Command to Run Your Function

You can trigger a function with a custom chat command:

```python
def build_bridge():
    for i in range(6):
        blocks.place(PLANKS_OAK, positions.create(i, -1, 0))

player.on_chat("bridge", build_bridge)
```

Now type `bridge` in Minecraft chat and it builds for you!

---

### 🧠 What Did You Learn?

* A **function** is a named set of instructions.
* You can run (or "call") your function anytime.
* Functions make your code **organized** and **easy to reuse**.

---

### 🎮 Bonus Challenge

Can you build a staircase with a function?

```python
def staircase():
    for i in range(5):
        blocks.place(STONE, positions.create(i, i, 0))

player.on_chat("stairs", staircase)
```

Try it in-game by typing: `stairs`

---
