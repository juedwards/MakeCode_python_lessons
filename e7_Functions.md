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

#### ✅ Step 1: Open Code Builder

1. Press **C** in Minecraft. Pick **MakeCode** if asked.

![image](https://github.com/user-attachments/assets/87b32f4f-a425-46b9-921e-bb6501344d10)

2. Create a new project called 'Function', then choose the **Python** editor. Clear the default code.

![image](https://github.com/user-attachments/assets/ef6ba8d2-eac3-41ba-907f-dcabcb1c2ff7)

3. Select Phython.

<img width="410" alt="image" src="https://github.com/user-attachments/assets/18fd0152-6387-47d5-9647-889cca4644e6" />

![image](https://github.com/user-attachments/assets/0064d882-cf4e-4d45-ac5b-ce5888b35395)

![image](https://github.com/user-attachments/assets/340958e3-25e8-470d-a896-0b34a763aacb)

Now you're ready to go!

---

### 🧱 Step 2: Write a Simple Function

Let’s make a function that places a gold block under your feet:

```python
def place_gold():
    blocks.place(GOLD_BLOCK, pos(0, -1, 0))
```
Copy and Paste this code into the editor.

![image](https://github.com/user-attachments/assets/8d06d701-edea-4b1f-a36f-2fb515ffe5c5)

🔍 What’s happening?

def place_gold(): — This defines a new function called place_gold.

blocks.place(...) — This tells Minecraft to place a gold block directly under the player (1 block down).

place_gold() — This calls the function so the block actually gets placed.

Important: If you only define the function and never call it, nothing will happen in the game!

---

### ▶️ Step 3: Call the Function

You must **call the function** to make it run:

```python
def place_gold():
    blocks.place(GOLD_BLOCK, pos(0, -1, 0))

place_gold()
```

Cope and Paste this code to update it wtih the new line.

![image](https://github.com/user-attachments/assets/3d9a7e51-bede-44c0-aeba-667b841df059)

Run the code. I places a gold block underneath you.

![image](https://github.com/user-attachments/assets/53ab6999-c950-444c-baa2-52e65e7f12c1)

---

### 🧰 Step 4: Make a Reusable Build Tool

Let’s make a function that builds a short wall:

```python
def build_wall():
    for i in range(5):
        blocks.place(STONE, positions.create(i+1, 0, 1))
```

Now type:

```python
build_wall()
```

![image](https://github.com/user-attachments/assets/ecef24f1-28e3-4ae2-8d2c-8578bee593b6)

![image](https://github.com/user-attachments/assets/0f768a46-aeac-4fe5-8d2a-cb49c9b79191)


🏗️ It places a row of 5 stone blocks.

---

### ✨ Step 5: Add a Chat Command to Run Your Function

You can trigger a function with a custom chat command:

```python
def build_bridge():
    for i in range(6):
        blocks.place(PLANKS_OAK, positions.create(i+1, -1, 1))

player.on_chat("bridge", build_bridge)
```

Copy and paste the code into the editor.

![image](https://github.com/user-attachments/assets/c4042c7c-188e-463d-9616-5ad21924e9d0)

Press **T** and enter the word 'bridge' in chat.

![image](https://github.com/user-attachments/assets/bf848cf8-123f-46c1-933e-72d5b653a8ef)

Press ENTER

![image](https://github.com/user-attachments/assets/5a286c8b-f0f8-4341-ada1-98a46415054d)

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
