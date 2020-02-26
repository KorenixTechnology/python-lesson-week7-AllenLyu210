import random

def hw_week7(secret_number):
  y=int(0)
  while True:
    y=y+1
    print('Take a guess.')
    x=int(input())
    if secret_number > x:
      print('Your guess is too low.')
    elif secret_number < x:
      print('Your guess is too high.')
    else:
      print('Good job! You guessed my number '+ str(y) +' in guesses!')
      break

if __name__ == '__main__':
  hw_week7(random.randint(1, 100))