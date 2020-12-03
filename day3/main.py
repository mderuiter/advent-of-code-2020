def download(filename):
    file = open(filename)
    return file.read().split()

def calculate_trees_in_slope(input, right, down):
  postionX = 0
  numberOfTrees = 0

  for index, element in enumerate(input):

    if index % down == 0:
      numberOfPositions = len(element)
      postionX = postionX - numberOfPositions if postionX >= numberOfPositions else postionX
      if element[postionX] == "#": numberOfTrees += 1
      postionX += right

  return numberOfTrees



if __name__ == "__main__":
  input = download("input.txt")

  oneRightOneDown = calculate_trees_in_slope(input, 1, 1) 
  theeRightOneDown = calculate_trees_in_slope(input, 3, 1) 
  fiveRightOneDown = calculate_trees_in_slope(input, 5, 1) 
  sevenRightOneDown = calculate_trees_in_slope(input, 7, 1) 
  oneRightTwoDown = calculate_trees_in_slope(input, 1, 2) 
  print(oneRightOneDown * theeRightOneDown * fiveRightOneDown * sevenRightOneDown * oneRightTwoDown)

