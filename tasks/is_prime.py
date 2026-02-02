__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    if number <= 1:
        return False
    
    # Проверяем делители от 2 до sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True