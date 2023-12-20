from graphics import Point, Line

class Cell:
    def __init__(self, window):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2, fill_color="black"):
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        p1 = Point(min(self._x1,self._x2),min(self._y1,self._y2))
        p2 = Point(max(self._x1,self._x2),min(self._y1,self._y2))
        p3 = Point(max(self._x1,self._x2),max(self._y1,self._y2))
        p4 = Point(min(self._x1,self._x2),max(self._y1,self._y2))

        self._win.draw_line(Line(p1,p2), fill_color if self.has_top_wall else "white")
        self._win.draw_line(Line(p2,p3), fill_color if self.has_right_wall else "white")
        self._win.draw_line(Line(p3,p4), fill_color if self.has_bottom_wall else "white")
        self._win.draw_line(Line(p4,p1), fill_color if self.has_left_wall else "white")

    def draw_move(self,to_cell, undo=False):
        if self._win is None:
            return
        self_x_mid = (self._x1 + self._x2) / 2
        self_y_mid =  (self._y1 + self._y2) / 2
        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        color = "gray" if undo else "red"

#move right
        if self_x_mid < to_x_mid:
            line = Line(Point(self_x_mid, self_y_mid), Point(self._x2, self_y_mid))
            self._win.draw_line(line, color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, color)

#move left
        if self_x_mid > to_x_mid:
            line = Line(Point(self_x_mid, self_y_mid), Point(self._x1, self_y_mid))
            self._win.draw_line(line, color)
            line = Line(Point(to_cell._x2, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, color)
#move up
        if self_y_mid > to_y_mid:
            line = Line(Point(self_x_mid, self_y_mid), Point(self_x_mid, self._y1))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, color)
#move down
        if self_y_mid < to_y_mid:
            line = Line(Point(self_x_mid, self_y_mid), Point(self_x_mid, self._y2))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid, to_cell._y1), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, color)