heart = ["♥", "♥♥♥", "♥♥♥♥♥", "♥♥♥♥♥♥♥", "♥♥♥♥♥♥♥♥♥"]
sun = ["☼", "☼☼☼", "☼☼☼☼☼", "☼☼☼☼☼☼☼", "☼☼☼☼☼☼☼☼☼"]
rhomb = ["♦", "♦♦♦", "♦♦♦♦♦", "♦♦♦♦♦♦♦", "♦♦♦♦♦♦♦♦♦"]
square = ["■", "■■■", "■■■■■", "■■■■■■■", "■■■■■■■■■"]
rectangles = ["█", "███", "█████", "███████", "█████████"]


def func_colors(color):
    if color == "black":
        return "\033[30m{}"
    elif color == "red":
        return "\033[31m{}"
    elif color == "green":
        return "\033[32m{}"
    elif color == "yellow":
        return "\033[33m{}"
    elif color == "blue":
        return "\033[34m{}"
    elif color == "purple":
        return "\033[35m{}"
    elif color == "turquoise":
        return "\033[36m{}"
    elif color == "white":
        return "\033[37m{}"


def func_symbols(symbols, color):
    for symbol in symbols:
        selected_color = func_colors(color)
        default_color = "\033[0m{}"
        print(selected_color.format(symbol), default_color.format(""))

func_symbols(heart, "red")