## 🔁 Exercise 5: Repeat with Loops!

### 🎯 What You’ll Learn

In this activity, you’ll:

* Use a **loop** to repeat actions in code.
* Build things faster by **repeating** instead of typing the same thing again.
* Create a path, a platform, and even a ladder!

---

### 🤔 What is a Loop?

Imagine you want to place 10 blocks in a row. You could write 10 lines of code…
**OR** you could use a loop to do it in just **3 lines!**

A **loop** tells the computer:
💬 “Do this action again and again.”

---

### 🪄 Step-by-Step Instructions

#### ✅ Step 1: Open Code Builder

1. Press **C** in Minecraft.
2. Pick **MakeCode**, then choose the **Python** editor.

---

### 🧱 Step 2: Say Something 5 Times

```python
for i in range(5):
    player.say("This is loop #" + str(i))
```

🧠 This will make your player say a message 5 times.
The number `i` starts at 0 and goes up each time.

---

### 🛤️ Step 3: Build a Path with the Agent

Let’s make the Agent place blocks as it moves forward:

```python
agent.set_slot(1)
agent.set_item(STONE, 64, 1)

for i in range(5):
    agent.place(DOWN)
    agent.move(FORWARD, 1)
```

👣 The Agent builds a **5-block-long path** under itself.

---

### 🧱 Step 4: Build a Floor with Nested Loops

This creates a **5 by 5 platform** of stone blocks:

```python
for x in range(5):
    for z in range(5):
        blocks.place(STONE, positions.create(x, 0, z))
```

📦 It places blocks across 2 directions — like a grid!

---

### 🪜 Step 5: Build a Ladder (Vertical Tower)

Use a loop to build **upward** using oak planks:

```python
for y in range(6):
    blocks.place(OAK_PLANKS, positions.create(0, y, 0))
```

📏 This builds a tall tower, one block on top of the other.

---

### 🧠 What Did You Learn?

* Loops help you **repeat** actions easily.
* You can use loops with numbers (like X, Y, Z) to build shapes.
* You can even **nest loops** to build wide areas.

---

### 💡 Bonus Challenge

Can you build a **staircase** using a loop?

Hint: Each block goes **one higher** and **one forward**.

```python
for i in range(5):
    blocks.place(STONE, positions.create(i, i, 0))
```
