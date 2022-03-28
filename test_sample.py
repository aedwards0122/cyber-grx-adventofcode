from main import StringParser

def test_load_data():
    test = StringParser("data/source_test.txt")
    assert len(test.data) == 10

def test_score_p1():
    test = StringParser("data/source_test.txt")
    assert test.total_score == 26397

def test_score_count():
    test = StringParser("data/source_test.txt")
    assert len(test.total_scores_p2) % 2 != 0

def test_score_p2():
    test = StringParser("data/source_test.txt")
    assert test.middle_score == 288957

