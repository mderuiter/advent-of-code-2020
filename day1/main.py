def download(filename):
  path = "../inputs/{}".format(filename)
  file = open(filename)
  return file.read().split()

def convert(input):
  return int(input)

def getInput():
  puzzleInput = download("input.txt")
  return [convert(i) for i in puzzleInput]

def getProduct(input):
  for x in input:
    for y in input:
      for z in input:

        if x + y + z == 2020:
          print(x * y * z)
          exit()


if __name__ == "__main__":
    input = getInput()
    getProduct(input)

    