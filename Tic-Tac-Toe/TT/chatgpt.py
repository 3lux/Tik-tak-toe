from dataclasses import dataclass

@dataclass
class Tube:
  id: int
  contents: str

class TubeStorage:
  def __init__(self, rows: int, cols: int):
    self.rows = rows
    self.cols = cols
    self.tubes = [[None for _ in range(cols)] for _ in range(rows)]
  
  def add_tube(self, tube: Tube, row: int, col: int):
    self.tubes[row][col] = tube
  
  def remove_tube(self, row: int, col: int):
    self.tubes[row][col] = None
  
  def get_tube(self, row: int, col: int) -> Tube:
    return self.tubes[row][col]

# Create a new tube storage unit with 2 rows and 8 columns
tube_storage = TubeStorage(2, 8)

# Add a tube to the storage unit
tube_storage.add_tube(Tube(1, "Compound X"), 0, 0)

# Remove a tube from the storage unit
tube_storage.remove_tube(0, 0)

# Get a tube from the storage unit
tube = tube_storage.get_tube(0, 0)