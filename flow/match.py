# Match case (switch statements)

'''
Match case is great for checking if one value satisfies a condition out
of a long list. It's more efficient and faster than and if statement but
isn't always useable depending on the situation.
'''

mood = 'tired'

# Match case example using the value of `mood`
match mood:
  case 'hungry':
    print('Eat some food')
  case 'thirsty':
    print('Drink some water')
  case 'tired':
    print('Get some sleep')
  case _: # This is the default case when no other condition (case) is met
    print(f'Sorry, there are no recommendations for the mood: {mood}')
