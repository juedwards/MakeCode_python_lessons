![Minecraft Education Logo](images/education-minecraft-logo.png)

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

#### ✅ Step 1: Open Code Builder

1. Press **C** in Minecraft. Pick **MakeCode** if asked.

![image](https://github.com/user-attachments/assets/87b32f4f-a425-46b9-921e-bb6501344d10)

2. Create a new project called 'variable', then choose the **Python** editor. Clear the default code.

![image](https://github.com/user-attachments/assets/90cbcf5a-8804-4fc2-a013-a0434af75aa1)

3. Select Phython.

<img width="410" alt="image" src="https://github.com/user-attachments/assets/18fd0152-6387-47d5-9647-889cca4644e6" />

![image](https://github.com/user-attachments/assets/0064d882-cf4e-4d45-ac5b-ce5888b35395)

![image](https://github.com/user-attachments/assets/340958e3-25e8-470d-a896-0b34a763aacb)

Now you're ready to go!

---

### 🗣️ Step 2: Store a Word and Say It

```python
greeting = "Hello, Minecraft!"
player.say(greeting)
```
Copy and paste the code into the editor.

![image](https://github.com/user-attachments/assets/7fc7edb7-3570-4cbc-8b7e-71c9c474da15)

Run the code.

![image](https://github.com/user-attachments/assets/7b6353e9-4558-492f-b219-5f667ab72a17)

📦 You put the message in a variable called `greeting`.

---

### 🔢 Step 3: Store a Number and Use It

```python
height = 10
player.teleport(pos(0, height, 0))
```
Copy and paste the code into the editor.

![image](https://github.com/user-attachments/assets/db790696-60f3-42a6-831c-e0f808ee1902)

Run the code

![image](https://github.com/user-attachments/assets/5e16a82f-ced6-407b-9ae1-65ff7f5f1120)

💡 Instead of typing `10` in the position, you used `height`.

---

### 🔁 Step 4: Use a Variable in a Loop

```python
length = 5

for i in range(length):
    blocks.place(STONE, positions.create(i, 0, 0))
```
Copy and paste the code into the editor.

![image](https://github.com/user-attachments/assets/9c902641-2289-469b-abcc-6e2a0c6f3dc8)

Run the code

![image](https://github.com/user-attachments/assets/77fb84c5-1910-41c7-8385-07125820656a)

📏 You just built a stone path using the number **stored in a variable**!

---

### 🧪 Step 5: Use Player Info in a Variable

Let’s store your name and say hello:

```python
my_name = player.name()
player.say("Hi " + my_name + "!")
```
Copy and paste the code into the editor

![image](https://github.com/user-attachments/assets/00fde920-aae8-453d-acb5-7e0aa5773854)

Run the code.

![image](https://github.com/user-attachments/assets/8230f9be-66b4-427d-82cd-5e87fa210784)

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

Copy and paste the code into the editor. Then, run the code.

![image](https://github.com/user-attachments/assets/d9d83d03-ca82-4021-9e81-1745f50d8e2e)

Now type `jump` in chat to soar high!

![image](https://github.com/user-attachments/assets/bd74d605-a075-476e-ab52-9e90a4bc5b88)

![image](https://github.com/user-attachments/assets/11796c5b-2239-4f3f-a35d-86365e9f39a9)

---
