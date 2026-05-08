from pgl import GWindow, GArc

COLORS = ["red", "green", "blue", "orange"] #colors 
GW_WIDTH = 500 #width of window 
GW_HEIGHT = 500 #height of window 
CHART_RADIUS = 150 #radius of pie chart 
HIGHLIGHT_THICKNESS = 10 # line thickness when clicked


def create_pie_chart(list_of_percents):
    def down_action(e):
        elem = gw.get_element_at(e.get_x(), e.get_y())
        if elem is not None:
            elem.set_line_width(HIGHLIGHT_THICKNESS)
    def up_action(e):
        elem = gw.get_element_at(e.get_x(), e.get_y())
        if elem is not None:
            elem.set_line_width(1)
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    start = 0
    i = 0
    for entry in list_of_percents:
        x = GW_WIDTH/2 - CHART_RADIUS
        y = GW_HEIGHT/2 - CHART_RADIUS
        stride = int(entry/100 * 360)
        arc = GArc(x, y, 2*CHART_RADIUS, 2*CHART_RADIUS, start, stride)
        arc.set_filled(True)
        arc.set_fill_color(COLORS[i % len(COLORS)])
        gw.add(arc)
        start += stride
        i += 1

    gw.add_event_listener("mousedown", down_action) 
    gw.add_event_listener("mouseup", up_action)

create_pie_chart([20,30,50])