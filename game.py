import random
import time

#creates a dataset list of the words to be used in the game
words=["staple", "beauty", "master", "desert", "result", "danger", "spirit", "marvel", "dreams", "camera", "minute","toggle", "outlet"]

       
#creates a list of other 6 letter words that can be used
additional_words = ["pastel", "pleats", "petals", "stream", "maters", "tamers", "resets", "rested", "treads", "meters", "rustle", "garden", "rustle", "ranged", "sprint"]


#this is a function that scrambled the word
def scramble_word(word):
  word_list=list(word)
  random.shuffle(word_list) 
  return ''.join(word_list)


#function to generate all possible words from a scrambled word
def generate_words(scrambled_word):
  possible_words=[]
  for w in words:
    if len(w)==len(words) and sorted(w)==sorted(words) and w!= words:
      possible_words.append(w)
      return possible_words


#function to calculate the points
def calculate_points(word):
  points=0
  if len(word)==6:
    points= len(word)*100
    return points
  else:
    return 0


#function to play the gamе
def play_game():
  score =0
  start_time = time.time()
  while True:
    if time.time() - start_time >=60:
      print("Your time is up!")
      print("Your final score is, ", score, "points")
      exit()
    word = random.choice(words)
    scrambled_word = scramble_word(word)
    print("Scrambled word:", scrambled_word)
    answer_input = input("UNSCRAMBLE!: ").lower().strip()
    possible_words = generate_words(scrambled_word)
    
    if answer_input in additional_words or answer_input in words or (possible_words and answer_input in possible_words):
      points= calculate_points (answer_input)
      score += points
      print("That is the correct response, you have earned, ", points, "points")
    else:
      print("That is incorrect! Try again")
      


#This executes the whole game
if __name__ == "__main__":
  play_game()
