![Minecraft Education Logo](images/education-minecraft-logo.png)

## Exercise 6: Making Decisions with Code!

### 🎯 What You’ll Learn

In this activity, you’ll:

* Learn how to make your code **decide** what to do.
* Use **`if`** statements to check conditions in Minecraft.
* Plant a tree **only if the ground is right**.

---

### 🤔 What is a Conditional?

Sometimes we want code to **only do something if a condition is true**.

For example:
💬 "If it's raining, go indoors."
💬 "If there’s grass, plant a tree."

In coding, we use:

```python
if something_is_true:
    do_this()
```
Notice that the second line is **indented** or moved inwards from the left margin. That means it happens if something is true. 
---

### 🪄 Step-by-Step Instructions

#### ✅ Step 1: Open Code Builder

1. Press **C** in Minecraft. Pick **MakeCode** if asked.

![image](https://github.com/user-attachments/assets/87b32f4f-a425-46b9-921e-bb6501344d10)

2. Create a new project called 'Decisions', then choose the **Python** editor. Clear the default code.

![image](https://github.com/user-attachments/assets/f45ba8e8-20e4-4f7c-a5ad-a49d679155d0)

3. Select Phython.

<img width="410" alt="image" src="https://github.com/user-attachments/assets/18fd0152-6387-47d5-9647-889cca4644e6" />

![image](https://github.com/user-attachments/assets/0064d882-cf4e-4d45-ac5b-ce5888b35395)

![image](https://github.com/user-attachments/assets/340958e3-25e8-470d-a896-0b34a763aacb)

Now you're ready to go!

---

### ✅ Step 2: Check for Grass

This code checks if the block **under the Agent's feet** is grass.

```python
if agent.inspect(AgentInspection.BLOCK, DOWN) == GRASS:
    player.say("Agent standing on grass!")
```
Copy and Paste it to the editor.

![image](https://github.com/user-attachments/assets/8288f277-9d97-4fd7-a89e-1356917cef26)

Run the code.

![image](https://github.com/user-attachments/assets/33611d43-3665-40af-8c63-c3487d735057)

---

### 🌱 Step 3: Plant a Tree if the Ground is Right

Let’s plant an oak sapling only if the block under the player is grass.

```python
if agent.inspect(AgentInspection.BLOCK, DOWN) == GRASS:
    agent.set_slot(1)
    agent.set_item(OAK_SAPLING, 1, 1)
    agent.move(FORWARD, 1)
    agent.place(BACK)
    player.say("Tree Planted!")
else:
    player.say("Not enough grass to plant a tree!")

```
Copy and Paste this code to the editor.

![image](https://github.com/user-attachments/assets/0a62faab-c3a9-4fbe-b996-ea0a88ed9351)

Run the code.

![image](https://github.com/user-attachments/assets/8bb56c49-3f16-4063-abae-ed71b9a72193)

🌳 The tree gets planted only in the **right place**!

This code uses a **conditional statement** (`if...else`) in MakeCode Python to make a decision based on the block under the player's Agent. Let’s break it down step-by-step:

### 🌱 **What it does:**

The Agent checks if the block directly beneath it is **grass**.

* If **yes**, it plants an **oak sapling** behind it.
* If **no**, it says a message explaining why it didn’t plant.

### 🔍 **Line-by-line explanation:**

```python
if agent.inspect(AgentInspection.BLOCK, DOWN) == GRASS:
```

* This checks the block **underneath the Agent**.
* If it’s **GRASS**, the code inside the `if` block will run.

```python
    agent.set_slot(1)
```

* Selects inventory **slot 1** for placing an item.

```python
    agent.set_item(OAK_SAPLING, 1, 1)
```

* Places **1 oak sapling** into slot 1 (ready to be planted).

```python
    agent.move(FORWARD, 1)
```

* The Agent moves **forward by 1 block**.

```python
    agent.place(BACK)
```

* The Agent places the oak sapling **behind itself** (where it just came from).

```python
    player.say("Tree Planted!")
```

* Displays a message in the chat: **"Tree Planted!"**

```python
else:
    player.say("Not enough grass to plant a tree!")
```

* If the block **is not grass**, it skips the planting and instead tells the player why.

---

### 🔁 Step 4: Try More Conditions

You can also check for **water**:

```python
if agent.inspect(AgentInspection.BLOCK, DOWN) == WATER:
    player.say("Agent standing on water!")
```

Or use **`elif`** (else-if) to check **more than one thing**:

```python
if agent.inspect(AgentInspection.BLOCK, DOWN) == GRASS:
    player.say("Agent standing on grass!")
elif agent.inspect(AgentInspection.BLOCK, DOWN) == WATER:
    player.say("Agent standing on water!")
else:
    player.say("Neither grass nor water.")
```
Copy and paste the code into the editor.

![image](https://github.com/user-attachments/assets/581dd490-f522-4a39-b011-98d635f0a5c4)

Run the code.

![image](https://github.com/user-attachments/assets/ee86d4a5-17b4-4742-b504-a098c33d4b8a)

---

### 🧠 What Did You Learn?

* Use **`if`** to make decisions in your code.
* Use **`else`** when the condition is false.
* You can **check the blocks below the agent** and react.

---
