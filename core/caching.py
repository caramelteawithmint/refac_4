class ComputationCache:
    """Кэширует результаты тяжелых вычислений."""
    
    def __init__(self):
        self._cache = {}

    def compute(self, x: int) -> int:
        """Вычисляет x³ + 2x² + 5x + 10 с кэшированием."""
        if x not in self._cache:
            self._cache[x] = x ** 3 + 2 * x ** 2 + 5 * x + 10
        return self._cache[x]