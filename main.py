from core.calculations import *
from core.text_analysis import TextDataAnalyzer
from models.report import Report, ComputationCache
def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Анализ чисел
    stats = calculate_sum_and_average(numbers)
    evens = filter_even_numbers(numbers)
    odds = filter_odd_numbers(numbers)
    print("Sum & Avg:", stats)
    print("Evens:", evens)
    print("Odds:", odds)

    # Поиск простых чисел
    primes = find_primes(1, 50)
    print("Primes (1-50):", primes)

    # Анализ текста
    analyzer = TextDataAnalyzer(["apple", "banana", "apricot"])
    print("Filtered ('a'):", analyzer.filter_by_prefix("a"))

    # Кэширование вычислений
    computer = ComputationCache()
    print("Heavy(5):", computer.compute(5))

    # Отчет
    report = Report(
        title="Sales Q1",
        data=[10.5, 20.3, 15.7],
        sort_desc=True
    )
    print(report.generate())

if __name__ == "__main__":
    main()