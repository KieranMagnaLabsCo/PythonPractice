import random
import pytest

def validate_choice(choice):
    if choice not in [0, 1, 2, 5]:
        raise ValueError

def check_should_exit(choice):
    if choice == 5:
        return True
    return False

def check_win(choice, machine_choice):
  if choice == machine_choice:
    return "tied"
  elif (choice == 0 and machine_choice == 1) or (choice == 1 and machine_choice == 2) or (choice == 2 and machine_choice == 0):
    return "lost"
  else:
    return "won"

def RPS():
  choices = ["Rock", "Paper", "Scissors"]
  while True:
    try:
      choice = int(input("Enter your choice (0: Rock, 1: Paper, 2: Scissors, 5: exit): "))
      validate_choice(choice)
      if check_should_exit(choice):
          break
    except ValueError:
      print("Invalid choice. Please enter a valid choice.")
      continue
    machine_choice = random.randint(0, 2)
    result = check_win(choice, machine_choice)
    print(f"You chose {choices[choice]}")
    print(f"The machine chose {choices[machine_choice]}")
    print(f"You {result}")

# RPS()

# begin pytest code for unit testing
def test_validate_choice():
    with pytest.raises(ValueError):
        validate_choice(-1)
    with pytest.raises(ValueError):
        validate_choice(11)
    with pytest.raises(ValueError):
        validate_choice(3)
    with pytest.raises(ValueError):
        validate_choice("rock")

def test_check_should_exit():
    assert check_should_exit(5) == True
    assert check_should_exit(2) == False

def test_check_win():
    # Test that the function returns 'tied' when choice is equal to machine_choice
    assert 'tied' == check_win(0, 0)
    assert 'tied' == check_win(1, 1)
    assert 'tied' == check_win(2, 2)

    # Test that the function returns 'lost' when choice loses to machine_choice
    assert 'lost' == check_win(0, 1)
    assert 'lost' == check_win(1,2)
    assert 'lost' == check_win(2,0)

    # Test that the function returns 'won' when choice wins against machine_choice
    assert 'won' == check_win(1, 0)
    assert 'won' == check_win(2,1)
    assert 'won' == check_win(0,2) 
