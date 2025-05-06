![Minecraft Education Logo](images/education-minecraft-logo.png)

## Exercise 2: Magic Jump Command!

### 🎯 What You’ll Learn

In this fun activity, you’ll learn how to:

* Make a **custom command** in Minecraft using code.
* Use the chat window to make your player jump high!
* Understand what a **function** is in coding.

---

### 🤔 What’s a Command?

In Minecraft, a **command** is something you type in the chat box that makes something happen — like `/give` or `/tp`.

But with MakeCode Python, you can make your **own** command — and choose what it does!

---

### 🪄 Step-by-Step Instructions

#### ✅ Step 1: Open Code Builder

1. Press **C** on your keyboard in Minecraft to open **Code Builder**.
2. You should still be in the Python Editor, as we selected this in the previous lesson.
3. Delete all the code, so that you are starting from scratch.

![image](https://github.com/user-attachments/assets/cecc1e9a-0b70-4301-8aa2-2fbc4f254d2f)

---

#### ✅ Step 2: Type This Code

```python
def jump():
    player.teleport(pos(0, 10, 0))

player.on_chat("jump", jump)
```
![image](https://github.com/user-attachments/assets/60412458-d56a-4abe-b233-2ed45d0ece27)

🧠 What this means:

* You are **creating** a new command called `jump`.
* When you type `jump` in the Minecraft chat, it makes your player teleport 10 blocks up — like a high jump!

---

#### ✅ Step 3: Run the Code

1. Click the **green Play button** in the Code Builder.
2. In Minecraft, press **T** to open the chat.

![image](https://github.com/user-attachments/assets/96d0fb81-1ca1-4dd5-a5bf-b912ec9ddb1a)

3. Type this in the chat:

```
jump
```
![image](https://github.com/user-attachments/assets/b0513c9e-d421-414d-8087-6916efb43d29)


4. Press **Enter** — and *whoosh!* — your player jumps into the air!

![image](https://github.com/user-attachments/assets/7a030d89-7d90-470a-84ed-5fd339484945)

---

### 💡 Try This

Change the number in the code from `10` to something bigger:

```python
player.teleport(pos(0, 20, 0))
```

This will jump even higher! Just be careful — you might fall and get hurt in the game.

---

Sure! Here's a more expanded and beginner-friendly explanation of what a **function** is, tailored for young learners and included directly in your Markdown lesson:

---

### 🧠 What’s a Function?

A **function** is a special piece of code that does a job.

Think of it like a **recipe** in a cookbook:

* The **name** of the recipe is the function name (like `jump`).
* The **steps** in the recipe are the code inside the function.
* When you want to use it, you just call the name — and Minecraft follows all the steps!

In this example:

```python
def jump():
    player.teleport(pos(0, 10, 0))
```

We are:

* **Defining** a function called `jump` using `def` (short for *define*).
* Inside the function, we wrote one instruction: teleport the player up 10 blocks.

Later, we **use** the function like this:

```python
player.on_chat("jump", jump)
```

This tells Minecraft:
💬 “When the player types `jump` in the chat, run the `jump` function!”

Functions are super helpful because:

* They keep your code **organized**.
* You can **re-use** them again and again.
* You can give them **different names and purposes** (like `jump`, `build_wall`, or `plant_tree`).

We'll discover more about functions in future chapters.

---

### 🎮 Bonus Challenge

Can you make another command to teleport down low?

```python
def dive():
    player.teleport(pos(0, -5, 0))

player.on_chat("dive", dive)
```

Type `dive` in the chat to try it!

---
