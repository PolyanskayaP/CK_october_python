class TriangleChecker:
  def __init__(self, *args):
      self.a, self.b, self.c = args
  def is_triangle(self):
    try:
      if any([x < 1 for x in (self.a, self.b, self.c)]):
        print('С отрицательными числами ничего не выйдет!')
      elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
        print('Ура, можно построить треугольник!')
      else:
        print('Жаль, но из этого треугольник не сделать')
    except TypeError:
      print('Нужно вводить только числа!')