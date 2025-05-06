## 🚀 Exercise 2: Magic Jump Command!

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
2. Choose **MakeCode** and select the **Python** editor.

---

#### ✅ Step 2: Type This Code

```python
def jump():
    player.teleport(pos(0, 10, 0))

player.on_chat("jump", jump)
```

🧠 What this means:

* You are **creating** a new command called `jump`.
* When you type `jump` in the Minecraft chat, it makes your player teleport 10 blocks up — like a high jump!

---

#### ✅ Step 3: Run the Code

1. Click the **green Play button** in the Code Builder.
2. In Minecraft, press **T** to open the chat.
3. Type this in the chat:

```
jump
```

4. Press **Enter** — and *whoosh!* — your player jumps into the air!

---

### 💡 Try This

Change the number in the code from `10` to something bigger:

```python
player.teleport(pos(0, 20, 0))
```

This will jump even higher! Just be careful — you might fall and get hurt in the game.

---

### 🧠 What’s a Function?

A **function** is like a mini-program inside your code. You give it a name (like `jump`) and it does a job when you call it. This makes your code tidy and reusable.

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
