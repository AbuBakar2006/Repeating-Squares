# 🔳 Turtle Nested Squares Pattern

A visual **Python Graphics Script** utilizing the `turtle` module. This program draws a series of concentric squares anchored at a single corner. By iteratively reducing the side length after every loop, it creates a satisfying geometric tunnel effect.



## 🚀 Features

* **Geometric Logic:** Draws squares starting from a fixed origin $(0,0)$.
* **Automated Scaling:** Starts with a large size (300px) and shrinks by 5px in every iteration.
* **Rapid Rendering:** Uses `turtle.speed(30)` for fast execution.
* **Corner Anchoring:** Unlike concentric shapes that share a center, these squares share a specific vertex, creating a perspective-like depth.

## 🛠️ Logic Explained

The script uses a `for` loop to repeat the drawing process:

| Variable | Value | Effect |
| :--- | :--- | :--- |
| **`num`** | `300` | The starting side length of the largest square. |
| **Decrement** | `num -= 5` | Reduces the square size after every completed shape. |
| **Loop Range** | `num/5` | Ensures the loop runs exactly enough times (approx. 60) until the square size reaches 0. |

**Drawing Cycle:**
1.  Turn Left (Face North).
2.  Draw Side 1.
3.  Turn Left (Face West).
4.  Draw Side 2... (and so on until the square is closed).
5.  Reduce size and repeat from the same starting point.

## 💻 How to Run

### 1. Prerequisites
Ensure you have Python installed. The `turtle` library is included by default.

### 2. Run the Script
Open your terminal or command prompt and run:

```bash
python main.py
```

### 3. Output
A window will appear and rapidly draw squares from largest to smallest, all anchored at the bottom-right corner of the pattern.

## 📝 Example Code Snippet
The core logic responsible for the pattern:
```text
for i in range(1, int(num/5)):
    # Draw one complete square
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    
    # Shrink the size for the next one
    num -= 5
```
## ⚠️ Requirements
* **Python 3.x**
* **Tkinter support** (Standard with Python installations).
