# Have certain unsorted list with numbers
number_list_i = [564, 56, 74, 185, 3, 54, 63, 54, 67, 54, 91, 435, 4]

# Sorting Function taking as parameter an unorder list
def Bubble(ListA):
  indexing_length = len(ListA) - 1 # Calculating length of iteration
  sortedd = False
  while not sortedd:
    sortedd = True
    for i in range(0, indexing_length):
      if ListA[i] > ListA[i + 1]:
        sortedd = False
        ListA[i], ListA[i + 1] = ListA[i + 1], ListA[i] # When certain element in index i is greater than the one in index i + 1, switch them and continue iterating.
  return ListA # Finally return sorted list

# print Sorted list
print(Bubble(number_list_i))
