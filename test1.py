import pytest

def test1():
  assert 1==1
  print("xxxxxx")
  
def main():
  test1()  

if __name__ == "__main__":
    # execute only if run as a script
    test1()
