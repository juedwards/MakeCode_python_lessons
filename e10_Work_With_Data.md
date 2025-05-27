![Minecraft Education Logo](images/education-minecraft-logo.png)

## **Unit 10 – Read and Write Files with the Agent**

### 🔍 **Overview**

In this lesson, students will explore how to use the new file read/write features in MakeCode for Minecraft Education. They will create a `.txt` or `.csv` file that stores instructions, and then program the Agent to read those instructions and perform actions like moving, collecting, or building.

This is a great introduction to how computers store and interpret data from files, supporting foundational computer science concepts like I/O operations, parsing, and simple state machines.

---

### 🎯 **Learning Objectives**

* Understand how to write to and read from `.txt` and `.csv` files using MakeCode Python.
* Learn how to control the Minecraft Agent based on file contents.
* Practice using conditional logic and loops to perform actions based on external data.

---

### 🧰 **Required Setup**

* Minecraft Education Preview 1.22 or later
* Windows device (feature not currently supported on Chromebook)
* A known writable file path, such as:
  `C:/Users/<your name>/Desktop/agent_instructions.txt`

---

### 🧪 **Task 1 – Write Commands to a File**

Open MakeCode in Python mode in your Minecraft world and enter:

```python
def on_chat():
    file.write_file("C:/Users/<your name>/Desktop/agent_instructions.txt",
        "forward,3\nturn_left,1\nplace_block,GRASS\nbackward,2")
    player.say("Instruction file written!")

player.on_chat("write", on_chat)
```

💡 *This writes a CSV-like list of instructions for the Agent: move, turn, place, etc.*

---

### 🧭 **How to Find `<your name>` on Windows**

1. **Option A – Check your Desktop folder path**

   * Press `Windows + E` to open File Explorer.
   * Click on **"Desktop"** in the left-hand sidebar.
   * In the address bar at the top, you’ll see a path like:

     ```
     C:\Users\justin\Desktop
     ```
   * In this example, your username is `justin`.

2. **Option B – Use Command Prompt**

   * Press `Windows + R`, type `cmd`, and hit Enter.
   * In the black Command Prompt window, type:

     ```
     echo %USERNAME%
     ```
   * It will return your Windows username, e.g.:

     ```
     justin
     ```

---

### ✅ **Now Update Your Code**

Replace `<your name>` with your actual username:

```python
file.write_file("C:/Users/justin/Desktop/agent_instructions.txt", ...)
```

> ✔️ **Tip**: Avoid putting spaces in folder or file names if you’re manually typing the path in code.

Would you like the lesson to support user selection of file paths interactively with the file picker instead of hardcoding the path?


---

### 🧪 **Task 2 – Read File and Execute Instructions**

Now read the file and parse the lines:

```python
def on_chat_read():
    path = "C:/Users/<your name>/Desktop/agent_instructions.txt"
    data = file.read_file(path)
    commands = data.split("\n")

    for line in commands:
        parts = line.split(",")
        if len(parts) == 2:
            cmd = parts[0]
            value = int(parts[1])

            if cmd == "forward":
                for i in range(value):
                    agent.move(FORWARD, 1)
            elif cmd == "backward":
                for i in range(value):
                    agent.move(BACK, 1)
            elif cmd == "turn_left":
                for i in range(value):
                    agent.turn(LEFT_TURN)
            elif cmd == "place_block":
                agent.place(BLOCK_FACE_FORWARD)

    player.say("Agent followed the file!")

player.on_chat("read", on_chat_read)
```

🧠 **Challenge**: Modify the file to try different instructions, or add your own! Can you get the agent to build a staircase or dig a trench?

---

### 🛠 **Extension Ideas**

* Use `.csv` files with coordinates to build custom structures.
* Save player-collected stats (like item count) into a log file.
* Create an "agent diary" that logs actions taken during gameplay.

---

### ⚠️ **Known Limitations**

* Make sure the file path is valid and the folder exists.
* You cannot append to files — every write replaces the old data.
* This currently does **not** work on Chromebooks.
* Only folders your user has access to can be used.
