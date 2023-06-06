import unittest

def fibonacci(numero):
    lista = [0,1]
    for i in range(2,numero+1):
        lista.append(lista[i-1] + lista[i-2])
    else:
        return lista[numero]


if __name__ == '__main__':
    
    class Fibonacci(unittest.TestCase):
        
        def test_1(self):
            self.assertEqual(fibonacci(0),0)
        
        def test_2(self):
            self.assertEqual(fibonacci(1),1)
        
        def test_3(self):
            self.assertEqual(fibonacci(2),1)
        
        def test_4(self):
            self.assertEqual(fibonacci(3),2)
        
        def test_5(self):
            self.assertEqual(fibonacci(4),3)
        
        def test_6(self):
            self.assertEqual(fibonacci(5),5)
        
        def test_7(self):
            self.assertEqual(fibonacci(6),8)
        
        def test_8(self):
            self.assertEqual(fibonacci(7),13)
        
        def test_9(self):
            self.assertEqual(fibonacci(8),21)
        
        def test_10(self):
            self.assertEqual(fibonacci(9),34)

    unittest.main() 





