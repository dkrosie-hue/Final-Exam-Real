    
class Domino:
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def __str__(self):
        return f"Dominoe ({self._left},{self._right})"

    def get_left_dots(self):
        return self._left

    def get_right_dots(self):   
        return self._right

    def will_match(self, num):
        return (self._left == num or self._right == num)


if __name__ == "__main__":
    d = Domino(4,1)
    print(d)
    print(d.get_left_dots(), d.get_right_dots())
    print(d.will_match(4))
    print(d.will_match(6))