import unittest
def is_rightangled(a,b,c):
  a, b, c = sorted([a, b, c])
  return(b*b + c*c == a*a)

def is_triangle(a, b, c):
  a, b, c = sorted([a, b, c])
  return a > 0 and a + b > c

def classify_triangle(a,b,c):
  if is_triangle(a, b, c):
    if a == b == c:
      return('Equilateral Triangle')
    elif len(set([a, b, c])) <= 2:
      if is_rightangled(a,b,c):
        return('Right Angled Isosceles Triangle')
      else:
        return('Isosceles Traingle')
    elif is_rightangled(a,b,c):
      return('Right Angled Triangle')
    elif len(set([a, b, c])) == 3:
      return('Scalene Triangle')
  else:
    return('Not a Triangle')


class TestStringMethods(unittest.TestCase):

  def test_Equilateral(self):
    self.assertEqual(classify_triangle(3,3,3),'Equilateral Triangle')
    self.assertEqual(classify_triangle(4,3,3),'Equilateral Triangle')
    self.assertEqual(classify_triangle(2,10,3),'Equilateral Triangle')

  def test_Rightangled(self):
    self.assertEqual(classify_triangle(3,4,5),'Right Angled Triangle')
    self.assertEqual(classify_triangle(3,4,6),'Right Angled Triangle')

  def test_Isosceles(self):
    self.assertEqual(classify_triangle(5,5,10),'Isosceles Triangle')
    self.assertEqual(classify_triangle(5,5,11),'Isosceles Triangle')

  def test_Scalene(self):
    self.assertEqual(classify_triangle(7,8,13),'Scalene Triangle')
    self.assertEqual(classify_triangle(3,4,5),'Scalene Triangle')

    
if __name__ == '__main__':
    unittest.main()