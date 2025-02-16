class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides("Стороны треугольника должны быть положительными.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides("Сумма двух сторон должна быть больше третьей.")
        
        self.a = a
        self.b = b
        self.c = c
    
    def triangle_type(self) -> str:
        """Возвращает тип треугольника."""
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        else:
            return "nonequilateral"
    
    def perimeter(self) -> float:
        """Возвращает периметр треугольника."""
        return self.a + self.b + self.c