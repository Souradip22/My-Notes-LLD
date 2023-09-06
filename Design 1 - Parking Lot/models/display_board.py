class DisplayBoard:
    def __init__(self, id, handicapped_spot, compact_spot, large_spot, motorcycle_spot) -> None:
        self.id = id
        self.handicapped_spot = handicapped_spot
        self.compact_spot = compact_spot
        self.large_spot = large_spot
        self.motorcycle_spot = motorcycle_spot

    def show_free_slot(self): # Member function
        pass