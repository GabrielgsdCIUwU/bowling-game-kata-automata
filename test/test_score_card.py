from src.score_card import ScoreCard
import pytest

@pytest.mark.score_card
def test_score_card():
    assert ScoreCard

@pytest.mark.get_pins
def test_get_pins():
    PINS = "12345123451234512345"
    score_card = ScoreCard(PINS)
    assert score_card.get_pins() == PINS

@pytest.mark.regular_pins
def test_hitting_pins_regular():
    pins = "12345123451234512345"
    total = 60
    score_card = ScoreCard(pins)
    assert score_card.get_score() == total

@pytest.mark.symbol_zero
def test_symbol_zero():
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    score_card = ScoreCard(pins)
    assert score_card.get_score() == total

    pins = "9-3561368153258-7181"
    total = 82
    score_card = ScoreCard(pins)
    assert score_card.get_score() == total

@pytest.mark.spare_not_extra
def test_spare_not_extra():
    pins = "9-3/613/815/-/8-7/8-"
    total = 121
    score_card = ScoreCard(pins)
    assert score_card.get_score() == total