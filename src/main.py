
class A:
  num = 0

  def __init__(self):
    self.num = 10

  def hello(self):
    self.num = self.num + 1
    print('你好，世界 ' + str(self.num))

def main():
  a = A()
  a.hello()

main()
