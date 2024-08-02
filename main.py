def sum(numberA, numberB) -> int:
  return numberA + numberB

def isGreaterThan(numberA, numberB) -> bool:
  return numberA > numberB

def login(username, password) -> bool:
    if((username == "juan123") and (password == "1234567")):
        return True
    else:
        return False

if __name__ == "__main__":
  print(f"suma: {sum(3, 5)}")
  print(f"mayor que: {isGreaterThan(5 , 2)}")