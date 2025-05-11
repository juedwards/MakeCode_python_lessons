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

1. Press **C** in Minecraft.
2. Pick **MakeCode**, then choose the **Python** editor.

---

### ✅ Step 2: Check for Grass

This code checks if the block **under your feet** is grass.

```python
if blocks.test_for_block(GRASS, pos(0, -1, 0)):
    player.say("You’re standing on grass!")
```

🧠 `pos(0, -1, 0)` means “1 block below the player.”

---

### 🌱 Step 3: Plant a Tree if the Ground is Right

Let’s plant an oak sapling only if the block under the player is grass.

```python
if blocks.test_for_block(GRASS, pos(0, -1, 0)):
    blocks.place(OAK_SAPLING, pos(0, 0, 0))
    player.say("Tree planted!")
else:
    player.say("This spot isn’t grassy enough.")
```

🌳 The tree gets planted only in the **right place**!

---

### 🔁 Step 4: Try More Conditions

You can also check for **water**:

```python
if blocks.test_for_block(WATER, pos(0, -1, 0)):
    player.say("You're standing in water!")
```

Or use **`elif`** (else-if) to check **more than one thing**:

```python
if blocks.test_for_block(GRASS, pos(0, -1, 0)):
    player.say("Grass!")
elif blocks.test_for_block(WATER, pos(0, -1, 0)):
    player.say("Water!")
else:
    player.say("Neither grass nor water.")
```

---

### 🧠 What Did You Learn?

* Use **`if`** to make decisions in your code.
* Use **`else`** when the condition is false.
* You can **check the blocks around you** and react.

---

### 🌟 Bonus Challenge

Build a flower pot station:

```python
if blocks.test_for_block(DIRT, pos(0, -1, 0)):
    blocks.place(FLOWER_POT, pos(0, 0, 0))
    player.say("Perfect place for a flower!")
else:
    player.say("Try standing on dirt.")
```
