from core.calculations import calculate_sum_and_average, filter_even_numbers, is_prime, TextDataAnalyzer

def test_calculate_sum_and_average():
    assert calculate_sum_and_average([1, 2, 3]) == {"sum": 6, "average": 2.0}

def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4]) == [2, 4]

def test_is_prime():
    assert is_prime(5) is True
    assert is_prime(4) is False

def test_text_data_analyzer():
    analyzer = TextDataAnalyzer(["apple", "banana", "apple"])
    assert analyzer.calculate_stats() == {"total_items": 3, "unique_items": 2}