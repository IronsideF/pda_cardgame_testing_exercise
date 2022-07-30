### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
# The single = sign after card.value will throw an error, as this is an assignment expression and not a boolean as written. In order to work within the if statment, you would need to use a double equals sign, ==, to signify IS EQUAL TO, rather than an assingment. 
      return True
    else
    # No semi colon at the end of the else statement will prevent the code from running.
      return False


  dif highest_card(self, card1 card2):
  # Dif is not a word with meaning in python, which means this function is not set up correctly. Additionally, there is no comma separating card1 and card2 as parameters which will prevent this from running correctly. 
  if card1.value > card2.value:
    # The if statement is incorrectly indented, and needs to have a level of indentation added to the whole thing for it to be counted as part of the function.
    return card
    # card is not defined anywhere in the function, as the parameters were specified as card1 and card2. This should be corrected to card1.
  else:
    return card2
  


def cards_total(self, cards):
  # The indentation of this function is incorrect. It needs another level of indentation in order to be counted as a method of the CardGame class.
  total
  # Total is not assigned to anything, and so this will throw an error stating the variable is referenced before assignment. Total should be assigned to 0 on this line.
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # The return is located within the for loop, which will terminate the loop on the first iteration, preventing you from achieving an accurate total. Additionally, the code will throw an error when you attempt to concatenate a string and an integer together without first changing the integers type or making use of a formatted string.
  
```
