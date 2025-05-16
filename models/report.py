from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Report:
    """Структура для генерации отчетов."""
    title: str
    data: List[float]
    show_summary: bool = True
    include_graph: bool = False
    sort_desc: bool = False
    max_items: Optional[int] = None

    def generate(self) -> str:
        """Генерирует текстовый отчет."""
        sorted_data = sorted(self.data, reverse=self.sort_desc)
        if self.max_items is not None:
            sorted_data = sorted_data[:self.max_items]

        report = f"Report: {self.title}\n"
        if self.show_summary:
            report += f"Items: {len(sorted_data)}\n"
            report += f"Sum: {sum(sorted_data):.2f}\n"
            report += f"Average: {sum(sorted_data) / len(sorted_data):.2f}\n"
        if self.include_graph:
            report += "\n[Graph placeholder]\n"
        return report