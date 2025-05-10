![Minecraft Education Logo](images/education-minecraft-logo.png)

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

1. Press **C** in Minecraft. Pick **MakeCode** if asked.

![image](https://github.com/user-attachments/assets/87b32f4f-a425-46b9-921e-bb6501344d10)

3. Create a new project called 'Loops', then choose the **Python** editor. Clear the default code.

![image](https://github.com/user-attachments/assets/c5af1cf9-ddaf-4b5e-8bd1-a6c4a133e779)

<img width="410" alt="image" src="https://github.com/user-attachments/assets/18fd0152-6387-47d5-9647-889cca4644e6" />

![image](https://github.com/user-attachments/assets/0064d882-cf4e-4d45-ac5b-ce5888b35395)

![image](https://github.com/user-attachments/assets/340958e3-25e8-470d-a896-0b34a763aacb)

Now you're ready to go!
---

### 🧱 Step 2: Say Something 5 Times

Copy this code into your editor and press run.

```python
for i in range(5):
    player.say("This is loop #" + str(i))
```
![image](https://github.com/user-attachments/assets/72876253-0e61-4086-bcf3-b6c0bacadc07)

![image](https://github.com/user-attachments/assets/b039695e-ddbc-46dc-b52b-4bb57d58ae81)

🧠 This will make your player say a message 5 times.
The number `i` starts at **0** and goes up by **1** each time.

---

### 🛤️ Step 3: Build a Path with the Agent

Let’s make the Agent place blocks as it moves forward:

Copy this code into the code builder, removing the previous code. Press run.

```python
agent.set_slot(1)
agent.set_item(STONE, 64, 1)

agent.move(UP, 1)

for i in range(5):
    agent.place(DOWN)
    agent.move(FORWARD, 1)
```
![image](https://github.com/user-attachments/assets/b8d56bc3-1b13-4b9b-959c-566565c62056)

![image](https://github.com/user-attachments/assets/c2ba88e8-c2e6-452b-bc17-b63d79ba3f70)

👣 The Agent moves up one block, then builds a **5-block-long path** under itself.

---

### 🧱 Step 4: Build a Floor with Nested Loops

This creates a **5 by 5 platform** of stone blocks:

```python
for x in range(5):
    for z in range(5):
        blocks.place(STONE, positions.create(x+1, 0, z))
```
![image](https://github.com/user-attachments/assets/c365b87d-7a1e-48e3-b854-d9b16ecfcbb0)

![image](https://github.com/user-attachments/assets/7d15fb67-2e7a-4430-bf5e-e31b79c83a1b)

📦 It places blocks across 2 directions — like a grid!

**What’s a Nested Loop?**

A **nested loop** is like a loop inside another loop.

First, you go across one row and place 5 blocks.

Then you move to the next row and do it again.

You keep doing that until you have 5 rows of 5 blocks — a perfect square!

---

### 🪜 Step 5: Build a Ladder (Vertical Tower)

Use a loop to build **upward** using oak planks:

```python
for y in range(6):
    blocks.place(PLANKS_OAK, positions.create(0+1, y, 0+1))
```
![image](https://github.com/user-attachments/assets/c451edd7-24f2-404d-bb99-f7711daf98a2)

![image](https://github.com/user-attachments/assets/9cb39ad3-25bf-46b8-8753-d662e16b12bd)

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
