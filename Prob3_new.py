from pgl import GWindow, GRect, GLabel, GCompound

SQUARE_SIZE = 60
GWINDOW_WIDTH = 4 * SQUARE_SIZE
GWINDOW_HEIGHT = 4 * SQUARE_SIZE
SQUARE_FILL_COLOR = "LightGray"
PUZZLE_FONT = "18px 'Sans-Serif'"


def set_up_squares():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    count = 0
    for row in range(4):
            for col in range(4):
                compound = GCompound()
                count += 1
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                square = GRect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                square.set_filled(True)
                square.set_fill_color(SQUARE_FILL_COLOR)
                if col == 3 and row == 3: 
                    gw.remove(square)
                else:
                    value = GLabel(str(count), x, y)
                    value.set_font(PUZZLE_FONT)
                    label_x = x + (SQUARE_SIZE - value.get_width()) / 2
                    label_y = y + (SQUARE_SIZE + value.get_ascent()) / 2
                    compound.add(square)
                    compound.add(value, label_x, label_y)
                    gw.add(compound)

    def check_squares(e):
        mx, my = e.get_x(), e.get_y()
        current = gw.get_element_at(mx, my)
        if current is not None:
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                cx = mx + x * SQUARE_SIZE
                cy = my + y * SQUARE_SIZE
                if ((0 < cx < GWINDOW_WIDTH) and 
                    (0 < cy < GWINDOW_HEIGHT)):
                    elem = gw.get_element_at(cx, cy)
                    if elem is None: # the empty space!
                        current.move(x * SQUARE_SIZE, 
                                    y * SQUARE_SIZE)
                        return

    gw.add_event_listener("click", check_squares)


if __name__ == "__main__":
    set_up_squares()

