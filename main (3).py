''' implement a class player that represents a cricket player. the player class should have a
method called play() which prints "the players is playing cricket.derive a two classes, batsman and
Bowler,from the player class. override the play() method in each derived class to print"the Batsman
is batting and "the bowler is bowling", respectively.write a program to create subject or both the
Batsman and bowler class and call the play() method for each object'''


# define the base class player
class Player:
      def play(self):
          print("The player is playing cricket.")

# define the derived class Batsman 
class Batsman(Player):
      def play(self):
          print("The Batsman is batting.")

# define the derived class Bowler
class Bowler(Player):
      def play(self):
          print("the bowler is bowling.")

# create objects of Batsman and Bowler classes
batsman  =  Batsman()
bowler   =  Bowler()

# call the play() method for call object
batsman.play()
bowler.play()