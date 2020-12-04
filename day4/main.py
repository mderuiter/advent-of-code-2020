import re

class Passport:
  def __init__(self, **entries):
      self.__dict__.update(entries)

  def isValid(self): 
    if self.validateBYR() is not True: return False
    if self.validateIYR() is not True: return False
    if self.validateEYR() is not True: return False
    if self.validateHGT() is not True: return False
    if self.validateHCL() is not True: return False
    if self.validateECL() is not True: return False
    if self.validatePID() is not True: return False
    return True

  def validateBYR(self):
    byr = getattr(self, 'byr', None)
    return byr is not None and len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002
  
  def validateIYR(self):
    iyr = getattr(self, 'iyr', None)
    return iyr is not None and len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020

  def validateEYR(self):
    eyr = getattr(self, 'eyr', None)
    return eyr is not None and len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030
  
  def validateHCL(self):
    hcl = getattr(self, 'hcl', None)
    return hcl is not None and len(hcl) == 7 and re.match(r'#[a-f0-9]{6}', hcl) is not None
    
  def validateECL(self):
    ecl = getattr(self, 'ecl', None)
    availableOptions = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl is not None and ecl in availableOptions

  def validateHGT(self):
    hgt = getattr(self, 'hgt', None)

    if hgt is not None:
      if "cm" in hgt:
        hgt = int(hgt.replace("cm", ""))
        return hgt >= 150 and hgt <= 193
      elif "in" in hgt:
        hgt = int(hgt.replace("in", ""))
        return hgt >= 59 and hgt <= 76
      else:        
        return False 
    else: 
      return False
  
  def validatePID(self):
    pid = getattr(self, 'pid', None)
    return pid is not None and len(pid) == 9
    


def download(filename):
    file = open(filename)
    return file.read().replace(" ", ",").split("\n\n")


def convert(input):
  input = input.replace("\n", ",")
  input = input.split(",")
  input = dict(s.split(':') for s in input) 
  return Passport(**input)


def only_valid_passports(passport):
	return passport.isValid()


if __name__ == "__main__":
  input = download("input.txt")
  passports = [convert(i.replace("\n", ",")) for i in input]

  valid_passport_filter = filter(only_valid_passports, passports)
  valid_passports = list(valid_passport_filter)
  print(len(valid_passports))
