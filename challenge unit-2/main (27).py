class player:
  def play(self):
      print("The palyer is playing cricket.")

class Batsman(player):
  def play(self):
      print("The batsman is batting.")

class Bowler(player):
  def play(self):
      print("The bowler is bowling.")

# Create objects pf Batsman and Bowler classess
player = player()
Batsman = Batsman()
Bowler = Bowler()


#  Call the paly() mehtod for each object
player.play()
Batsman.play()
Bowler.play()
  