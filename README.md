##  Rainbow Spiral Generator (Python Turtle Art)

This project uses **Python's Turtle graphics** library to generate a complex, mesmerizing geometric spiral that features a smooth, continuous color transition through the entire spectrum.

###  The Magic Behind the Art

The code's vibrant look comes from two key features:

1.  **Iterative Geometry:** Nested loops control the "turtle" to draw repeated curved segments, gradually rotating the entire drawing frame to create the intricate, woven pattern.
2.  **Continuous Color Cycling:** The script uses the **HSV (Hue, Saturation, Value)** color model and incrementally changes the **Hue** value by a tiny amount for every segment. This ensures a seamless flow through red, yellow, green, blue, and purple—making it look like a pure rainbow.

###  How to Run the Script

You only need a standard Python installation to run this.

1.  **Save the Code:** Save the corrected Python code as a file named `spiral_art.py` (or whatever you choose) in a folder.

2.  **Open Terminal:** Open your terminal or command prompt (or use the VS Code terminal).

3.  **Execute:** Run the script using the Python interpreter:

    ```bash
    python spiral_art.py
    ```

A new window will open, and the pattern will begin to draw itself\!

###  Experimentation

Want to create a totally different design? Try tweaking these variables in the script:

| Line of Code | What to Change | Result |
| :--- | :--- | :--- |
| `range(120)` | Change to a higher number (e.g., `200`) | Makes the pattern denser and run longer. |
| `h += 0.003` | Change the increment (e.g., `0.001` or `0.01`) | Controls how quickly the color shifts. |
| `rt(10)` | Change the rotation (e.g., `rt(11)` or `rt(5)`) | Creates different overall spiral shapes. |

-----

