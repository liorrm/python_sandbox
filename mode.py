# input: an array of numbers
# output: the mode of that array

def mode(array):
  tallies = {}
  for elem in array:
    tallies[elem] = 0
  for elem in array:
    tallies[elem] += 1
  values = tallies.values()
  keys = tallies.keys()
  return keys[values.index(max(values))]

print mode([1, 2, 3, 1, 1, 3]) == 1
print mode([1, 2, 3, 1]) == 1
print mode([1, 5, 2, 3, 5, 5]) == 5
print mode([2, 2, 2, 3]) == 2
print mode([3, 2, 3, 2, 3, 1, 1, 3]) == 3