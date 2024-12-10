from config import PoleStatus, NUMBERS

class Cell:
    def __init__(self, val=0, free=PoleStatus.FREE):
        self.val = val
        self.free = free

    def set_val(self, v):
        if v not in NUMBERS:
            raise ValueError("This value is not possible")
        self.val = v
        self.free = PoleStatus.FILLED

    def unset_val(self):
        self.val = 0
        self.free = PoleStatus.FREE
    
    def is_free(self):
        return self.free == PoleStatus.FREE
    
    def __iadd__(self, cell):
        if not isinstance(cell, Cell):
            raise TypeError("Value is not type of Cell")
    
        self.val += cell.val
        self.free = PoleStatus.FILLED if self.val > 0 else PoleStatus.FREE
    
        return self
    

    def __eq__(self, cell):
        if not isinstance(cell, Cell):
            raise TypeError("Value is not type of Cell")
        return self.val == cell.val
    
