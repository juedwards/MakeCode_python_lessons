## 🤖 Exercise 4: Meet Your Minecraft Agent!

### 🎯 What You’ll Learn

In this activity, you’ll:

* Get to know your **Agent** — your coding robot friend!
* Make the Agent **move**, **turn**, and **place blocks**.
* Use loops to build a path with the Agent.

---

### 🤔 What is the Agent?

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
2. Choose **MakeCode**, then select **Python** editor.

---

### 👣 Step 2: Make the Agent Move

```python
agent.move(FORWARD, 1)
```

🎮 This tells the Agent to walk **one block forward**.

Try changing the direction:

```python
agent.move(UP, 1)
```

---

### 🔄 Step 3: Turn the Agent

```python
agent.turn(LEFT_TURN)
```

This turns the Agent **left**. Use `RIGHT_TURN` to go the other way.

---

### 🧱 Step 4: Place a Block

Give your Agent a block and place it in front of them.

```python
agent.set_slot(1)
agent.set_item(STONE, 64, 1)
agent.place(FORWARD)
```

🧠 This:

1. Puts 64 stone blocks in slot 1,
2. Selects that slot,
3. Places a stone block in front of the Agent.

---

### 🧪 Practice: Build a Path

Let’s make your Agent build a 5-block-long stone path.

```python
agent.set_slot(1)
agent.set_item(STONE, 64, 1)

for i in range(5):
    agent.place(DOWN)
    agent.move(FORWARD, 1)
```

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

