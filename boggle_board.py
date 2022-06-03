import random

class BoggleBoard:
  
  def __init__(self):
    self.board = ["----"] * 4

  def shake(self):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Qu','R','S','T','U','V','W','X','Y','Z']
    self.board = []
    for i in range(4):
      row = []
      for j in range(4):
        temp = random.choice(letters)
        if temp == "Qu":
          row.append([f"{temp} "])
        else:
          row.append([f'{temp}  '])
      self.board.append(row)
    print()
    
  def reset(self):
    self.board = ["----"] * 4
    


my_bog = BoggleBoard()

my_bog.shake()
for bog in my_bog.board:
  print(bog)
  
print()
print()
print(my_bog.board[0][3])
