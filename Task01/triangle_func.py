class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a: float, b: float, c: float) -> str:
    """Определяет тип треугольника по длинам его сторон."""
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides("Стороны треугольника должны быть положительными.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Сумма двух сторон должна быть больше третьей.")
    
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"

print(get_triangle_type(3, 3, 3))
