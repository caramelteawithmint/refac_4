from typing import List, Dict
class TextDataAnalyzer:
    """Анализирует текстовые данные (уникальность, фильтрация)."""
    
    def __init__(self, data: List[str]):
        self.data = data

    def calculate_stats(self) -> Dict[str, int]:
        """Возвращает статистику по данным."""
        return {
            "total_items": len(self.data),
            "unique_items": len(set(self.data))
        }

    def filter_by_prefix(self, prefix: str) -> List[str]:
        """Фильтрует строки по префиксу."""
        return [item for item in self.data if item.startswith(prefix)]