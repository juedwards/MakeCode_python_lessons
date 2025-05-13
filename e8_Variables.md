## 🧠 Exercise 8: Using Variables to Store Stuff!

### 🎯 What You’ll Learn

In this activity, you’ll:

* Understand what a **variable** is.
* Use variables to **store information** like numbers and words.
* Build smarter Minecraft code that can **remember things**!

---

### 🤔 What is a Variable?

A **variable** is like a **box** with a label on it.
You can put something in the box and **use it later**.

Example:

```python
name = "Alex"
```

🧠 Now the computer remembers that `name` means `"Alex"`!

---

### 🪄 Step-by-Step Instructions

#### ✅ Step 1: Open Code Builder

1. Press **C** in Minecraft.
2. Choose **MakeCode**, then click **Python**.

---

### 🗣️ Step 2: Store a Word and Say It

```python
greeting = "Hello, Minecraft!"
player.say(greeting)
```

📦 You put the message in a variable called `greeting`.

---

### 🔢 Step 3: Store a Number and Use It

```python
height = 10
player.teleport(pos(0, height, 0))
```

💡 Instead of typing `10` in the position, you used `height`.

---

### 🔁 Step 4: Use a Variable in a Loop

```python
length = 5

for i in range(length):
    blocks.place(STONE, positions.create(i, 0, 0))
```

📏 You just built a stone path using the number **stored in a variable**!

---

### 🧪 Step 5: Use Player Info in a Variable

Let’s store your name and say hello:

```python
my_name = player.name()
player.say("Hi " + my_name + "!")
```

🎉 This tells the player’s name using a variable!

---

### 🧠 What Did You Learn?

* A **variable** stores a piece of information (text, number, etc).
* You can use the variable **again and again**.
* Variables make your code easier to **change** and **understand**.

---

### 🌟 Bonus Challenge

Make your own teleport height changer:

```python
jump_height = 15

def big_jump():
    player.teleport(pos(0, jump_height, 0))

player.on_chat("jump", big_jump)
```

Now type `jump` in chat to soar high!

---
