import math
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

# ===== Улучшенные функции =====

def calculate_sum_and_average(numbers: List[int]) -> Dict[str, float]:
    """Вычисляет сумму и среднее значение списка чисел."""
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0.0
    return {"sum": total, "average": average}

def filter_even_numbers(numbers: List[int]) -> List[int]:
    """Фильтрует четные числа."""
    return [num for num in numbers if num % 2 == 0]

def filter_odd_numbers(numbers: List[int]) -> List[int]:
    """Фильтрует нечетные числа."""
    return [num for num in numbers if num % 2 != 0]

def is_prime(num: int) -> bool:
    """Проверяет, является ли число простым."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start: int, end: int) -> List[int]:
    """Находит все простые числа в заданном диапазоне."""
    return [num for num in range(start, end + 1) if is_prime(num)]