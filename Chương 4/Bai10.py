import time
import os

shapes = [
    [
        "   *    ",
        "   **   ",
        "   ***  ",
        "******* ",
        "***     ",
        "**      ",
        "*       ",
    ],
    [
        "   *    ",
        "   **   ",
        "   * *  ",
        "******* ",
        "* *     ",
        "**      ",
        "*       ",
    ],
    [
        "   **** ",
        "   ***  ",
        "   **   ",
        "   *    ",
        "  **    ",
        " ***    ",
        "****    ",
    ],
    [
        "   **** ",
        "   * *  ",
        "   **   ",
        "   *    ",
        "  **    ",
        " * *    ",
        "****    ",
    ],
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_shapes(delay_seconds=5):
    try:
        for idx, shape in enumerate(shapes, start=1):
            clear_screen()
            print(f"Hình {idx}:\n")
            for line in shape:
                print(line)
            time.sleep(delay_seconds)
    except KeyboardInterrupt:
        print("\nĐã dừng.")

if __name__ == "__main__":
    show_shapes(5)
