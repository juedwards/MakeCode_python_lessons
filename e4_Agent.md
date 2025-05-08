![Minecraft Education Logo](images/education-minecraft-logo.png)

## 🤖 Unit 4: Meet Your Minecraft Agent!

### 🎯 What You’ll Learn

In this activity, you’ll:

* Get to know your **Agent** — your coding robot friend!
* Make the Agent **move**, **turn**, and **place blocks**.
* Use loops to build a path with the Agent.

---

### 🤔 What is the Agent?

![image](https://github.com/user-attachments/assets/47360f22-8f6d-4f7c-9368-210ea4181b7f)

The **Agent** is your helpful robot in Minecraft. You can’t see it until you run your code — but it’s always ready to follow your instructions!

Your Agent can:
✅ Walk
✅ Turn
✅ Place or break blocks
✅ Build things for you!

---

### 🪄 Step-by-Step Instructions

#### ✅ Step 1: Open Code Builder

1. Press **C** in Minecraft.

![image](https://github.com/user-attachments/assets/d86d77da-a057-47ae-a0e2-6c0db696415e)

2. Create a New Project called 'Agent'

![image](https://github.com/user-attachments/assets/f9396230-5bdd-40e3-8cfe-f2d1e9a3a964)

3. Select **Python** editor.

![image](https://github.com/user-attachments/assets/eb1b2caf-3a70-4eec-8f88-e78d9d92ce60)

4. Clear the starting code.

![image](https://github.com/user-attachments/assets/37bec060-ccdc-431f-8d87-6dbf7e86a299)

---

### 👣 Step 2: Make the Agent Move

Enter the following code...

```python
agent.move(FORWARD, 1)
```

Press the RUN button.

![image](https://github.com/user-attachments/assets/a9bc696e-6393-4271-9199-dd4b2cfb5feb)

🎮 This tells the Agent to walk **one block forward**.

Try changing the direction:

Press **C** and enter this code...

```python
agent.move(UP, 1)
```
![image](https://github.com/user-attachments/assets/05efc9a2-4e5b-44a8-953f-ae525b5c6af9)

Press the RUN button and watch the Agent rise a block.

![image](https://github.com/user-attachments/assets/4205e56e-e3f1-4ffa-8459-0491070a05a2)

---

### 🔄 Step 3: Turn the Agent

Press **C** to open the code, and replace the previous code with this line...

```python
agent.turn(LEFT_TURN)
```
![image](https://github.com/user-attachments/assets/b3c2c472-891d-4500-820e-6fd6134d2cdf)

Press the run button and watch the Agent turn.

![image](https://github.com/user-attachments/assets/af0e1a3a-98c5-4f02-89d7-298aaa852b25)

This turns the Agent **left**. Use `RIGHT_TURN` to go the other way.

---

### 🧱 Step 4: Place a Block

Give your Agent a block and place it in front of them.

Press **C** to open the code, and replace the previous code with these lines...

```python
agent.set_slot(1)
agent.set_item(STONE, 64, 1)
agent.place(FORWARD)
```
![image](https://github.com/user-attachments/assets/04867a99-f71a-44a3-9110-126ac2ac6d3c)

Then press the run button and watch the Agent lay a block in front of them.

![image](https://github.com/user-attachments/assets/0e7775a4-debc-4265-a01f-0e60d8a7b91b)

🧠 This code:

1. Puts 64 stone blocks in slot 1,
2. Selects that slot,
3. Places a stone block in front of the Agent.

---

### 🧪 Practice: Build a Path

Let’s make your Agent build a 5-block-long stone path.

Press **C** to open the code, and replace the previous code with these lines...

```python
agent.move(UP, 1)
agent.set_slot(1)
agent.set_item(STONE, 64, 1)

for i in range(5):
    agent.place(DOWN)
    agent.move(FORWARD, 1)
```

![image](https://github.com/user-attachments/assets/6a3e2a6a-9f7c-48fa-9ae6-40cfaebf335d)

Then press the run button and watch the Agent lay a road beneath them.

![image](https://github.com/user-attachments/assets/de43b1ca-8c07-46ea-b8ee-a6aa0f061178)

👷 This builds a path under the Agent as it walks!

---

### 🔍 Bonus Challenge: Check for Grass

Make the Agent talk if it sees grass ahead:

```python
if agent.inspect(FORWARD) == GRASS:
    player.say("Grass ahead!")
```

You can use this to help your Agent explore and react to the world.

---

### 🧠 What Did You Learn?

* How to move and control your Agent.
* How to give it blocks and place them.
* How to build using loops and directions.

---

