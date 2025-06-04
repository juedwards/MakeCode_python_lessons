![Minecraft Education Logo](images/education-minecraft-logo.png)

### 📝 Lesson 11: Build a Roller Coaster 🎢

#### 🎯 Learning Objectives:

* Utilize the **Roller Coaster Builder** extension in MakeCode.
* Construct a custom roller coaster track using Python code.
* Combine various track elements: straight lines, turns, ramps, spirals, and free falls.

---

#### 📦 Step 1: Add the Extension

If the **Roller Coaster Builder** extension isn't already added:

1. Open the Toolbox in MakeCode.
2. Click on **Extensions**.
3. Search for **Roller Coaster Builder** and add it.([github.com][1])

---

#### 🧱 Step 2: Set Up the Command

Create a chat command that will build your roller coaster when you type `build` in the chat.

```python
def on_on_chat():
    pass
player.on_chat("build", on_on_chat)
```

---

#### 🚧 Step 3: Begin the Track

Replace the `pass` line with the starting point of your roller coaster:

```python
rollerCoasterBuilder.place_track_start(pos(0, 0, 0), NORTH)
```

---

#### ➕ Step 4: Add Track Segments

Add a straight line and a left turn:

```python
rollerCoasterBuilder.add_straight_line(10)
rollerCoasterBuilder.add_turn(LEFT_TURN)
```

Then, add ramps to go up and down:

```python
rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)
rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 10)
```

---

#### 🔁 Step 5: Add a Spiral and Free Fall

Add a spiral going up and a free fall:

```python
rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, LEFT_TURN, 10, 3)
rollerCoasterBuilder.add_free_fall(10)
```

---

#### ➡️ Step 6: Finalize the Track

Add a right turn, a straight line, and end the track:

```python
rollerCoasterBuilder.add_turn(RIGHT_TURN)
rollerCoasterBuilder.add_straight_line(10)
rollerCoasterBuilder.place_track_end()
```

---

#### ✅ Full Code

Here's the complete code for your `build` command:

```python
def on_on_chat():
    rollerCoasterBuilder.place_track_start(pos(0, 0, 0), NORTH)
    rollerCoasterBuilder.add_straight_line(10)
    rollerCoasterBuilder.add_turn(LEFT_TURN)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.UP, 10)
    rollerCoasterBuilder.add_ramp(RcbVerticalDirection.DOWN, 10)
    rollerCoasterBuilder.add_spiral(RcbVerticalDirection.UP, LEFT_TURN, 10, 3)
    rollerCoasterBuilder.add_free_fall(10)
    rollerCoasterBuilder.add_turn(RIGHT_TURN)
    rollerCoasterBuilder.add_straight_line(10)
    rollerCoasterBuilder.place_track_end()
player.on_chat("build", on_on_chat)
```

---

#### 🕹️ Try It Out!

1. Click the green play ▶️ button to run the code.
2. In Minecraft, press **T**, then type `build`.
3. Locate the white and pink start wall with a minecart.
4. Right-click the cart to ride, then press the button to start!

---

#### 🧠 Challenge

* Add more elements like turns, spirals, or obstacles.
* Modify track lengths or directions.
* Decorate your roller coaster with signs, lights, or mobs!
