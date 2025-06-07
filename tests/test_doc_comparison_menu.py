from src.cli_interface.doc_comparison_menu import *

# 1. Test take_input with valid input
def test_take_input_valid(monkeypatch):
    """
    This test simulates the user entering a valid choice ('2').
    It checks that take_input returns the correct integer.
    """
    monkeypatch.setattr("builtins.input", lambda _: "2")
    result = take_input({0, 1, 2, 3})
    assert result == 2

# 2. Test take_input with invalid input followed by valid input
def test_take_input_invalid_then_valid(monkeypatch, capfd):
    """
    This test simulates the user first entering an invalid value ('a'),
    then a valid one ('3').
    It checks that an error message is printed and the correct value is returned.
    """
    inputs = iter(["a", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = take_input({0, 1, 2, 3})
    out, _ = capfd.readouterr()
    assert "Saisie invalide" in out
    assert result == 3

# 3. Test doc_comparison_menu for each valid choice
def test_doc_comparison_menu_txt(monkeypatch, capfd):
    """
    Simulates user selecting option 1 (.txt comparison).
    Checks that the correct message is printed.
    """
    monkeypatch.setattr("builtins.input", lambda _: "1")
    doc_comparison_menu()
    out, _ = capfd.readouterr()
    assert "<< Comparaison .txt sélectionnée >>" in out

def test_doc_comparison_menu_pdf(monkeypatch, capfd):
    """
    Simulates user selecting option 2 (.pdf comparison).
    Checks that the correct message is printed.
    """
    monkeypatch.setattr("builtins.input", lambda _: "2")
    doc_comparison_menu()
    out, _ = capfd.readouterr()
    assert "<< Comparaison .pdf sélectionnée >>" in out

def test_doc_comparison_menu_mixed(monkeypatch, capfd):
    """
    Simulates user selecting option 3 (mixed comparison).
    Checks that the correct message is printed.
    """
    monkeypatch.setattr("builtins.input", lambda _: "3")
    doc_comparison_menu()
    out, _ = capfd.readouterr()
    assert "<< Comparaison mixte sélectionnée >>" in out

def test_doc_comparison_menu_return(monkeypatch, capfd):
    """
    Simulates user selecting option 0 (return to main menu).
    Checks that the correct message is printed.
    """
    monkeypatch.setattr("builtins.input", lambda _: "0")
    doc_comparison_menu()
    out, _ = capfd.readouterr()
    assert "<< Retour au menu principal >>" in out