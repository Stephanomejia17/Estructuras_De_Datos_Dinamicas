
class Node:
    def __init__(self, value = None, east = None, west =  None, north = None, south = None) -> None:
        self.value = value
        self.east: Node = east
        self.west: Node = west
        self.north: Node = north
        self.south: Node = south
        
    def get_value(self):
        return self.value

    def get_east(self):
        return self.east

    def get_west(self):
        return self.west

    def get_north(self):
        return self.north

    def get_south(self):
        return self.south

    def set_value(self, value):
        self.value = value

    def set_east(self, east):
        self.east = east

    def set_west(self, west):
        self.west = west

    def set_north(self, north):
        self.north = north

    def set_south(self, south):
        self.south = south
    
    
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()
n6 = Node()
n7 = Node()
n8 = Node()
n9 = Node()
n10 = Node()
n11 = Node()
n12 = Node()
n13 = Node()
n14 = Node()
n15 = Node()
n16 = Node()

n1.set_east(n2)
n1.set_south(n5)

n2.set_east(n3)
n2.set_west(n1)
n2.set_south(n6)

n3.set_east(n4)
n3.set_west(n2)
n3.set_south(n7)

n4.set_west(n3)
n4.set_south(n8)

n5.set_north(n1)
n5.set_east(n6)
n5.set_south(n9)

n6.set_east(n7)
n6.set_west(n5)
n6.set_north(n2)
n6.set_south(n10)

n7.set_east(n8)
n7.set_west(n6)
n7.set_north(n3)
n7.set_south(n11)

n8.set_west(n7)
n8.set_north(n4)
n8.set_south(n12)

n9.set_north(n5)
n9.set_east(n10)
n9.set_south(n13)

n10.set_east(n11)
n10.set_north(n6)
n10.set_south(n14)
n10.set_west(n9)

n11.set_east(n11)
n11.set_north(n7)
n11.set_south(n15)
n11.set_west(n10)

n12.set_north(n8)
n12.set_east(n16)
n12.set_south(n11)

n13.set_north(n9)
n13.set_east(n14)

n14.set_north(n10)
n14.set_east(n15)
n14.set_west(n13)

n15.set_north(n11)
n15.set_east(n16)
n15.set_west(n14)

n16.set_north(n12)
n16.set_west(n15)


