import solution
from io import StringIO
import sys

empty_place_inputs = StringIO('\n')
one_place_input = StringIO('London, England\n\n')
many_place_inputs = StringIO('''Shanghai, China
Beijing, China
Tel Aviv, Israel
Haifa, Israel
Madrid, Spain
Barcelona, Spain

''')


def test_no_places(monkeypatch):
    monkeypatch.setattr('sys.stdin', empty_place_inputs)
    solution.collect_places()
    assert len(solution.visits) == 1

def test_one_place(monkeypatch):
    monkeypatch.setattr('sys.stdin', one_place_input)
    solution.collect_places()
    assert len(solution.visits) == 1

def test_many_places(monkeypatch):
    monkeypatch.setattr('sys.stdin', many_place_inputs)
    solution.collect_places()
    assert len(solution.visits) == 3

def test_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('abcd\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.strip().startswith("Tell me where you went: That's not a legal city, country combination")
    assert captured_out.strip().endswith("Tell me where you went:")

def test_sorting_cities(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('Shanghai, China\nBeijing, China\nBeijing, China\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    beijing_index = captured_out.index('Beijing')
    shanghai_index = captured_out.index('Shanghai')
    assert beijing_index < shanghai_index

def test_sorting_countries(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('Haifa, Israel\nLondon, England\nNew York, USA\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    israel_index = captured_out.index('Israel')
    england_index = captured_out.index('England')
    usa_index = captured_out.index('USA')
    assert england_index < israel_index
    assert israel_index < usa_index


def test_counting(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('Shanghai, China\nBeijing, China\nBeijing, China\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()
    assert len(solution.visits['China']) == 2

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    assert 'Beijing (2)' in captured_out
    assert 'Shanghai' in captured_out