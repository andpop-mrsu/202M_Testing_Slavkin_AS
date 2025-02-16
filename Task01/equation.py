import math

def solve_quadratic_equation(a: float, b: float, c: float):
    """Находит корни квадратного уравнения ax^2 + bx + c = 0 и возвращает их в порядке возрастания."""
    if a == 0:
        if b == 0:
            if c == 0:
                return (float('inf'),)  # Бесконечно много решений
            else:
                return ()  # Нет решений
        return (-c / b,)  # Линейное уравнение
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return ()  # Нет действительных корней
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        sqrt_d = math.sqrt(discriminant)
        root1 = (-b - sqrt_d) / (2*a)
        root2 = (-b + sqrt_d) / (2*a)
        return (root1, root2)

    
#print(solve_quadratic_equation(0, 0, 0))
