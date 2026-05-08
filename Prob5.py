class LabelGenerator:
    """Class to generate desired labels on demand"""
    def __init__ (self, prefix, start=1):
        self._prefix = prefix
        self._count = start
    
    def next_label(self):
        label = f"{self._prefix}{self._count}"
        self._count += 1
        return label

        

if __name__ == "__main__":
    figures = LabelGenerator("P ", 0) 
    print(figures.next_label()) 
    print(figures.next_label())
    print(figures.next_label())

