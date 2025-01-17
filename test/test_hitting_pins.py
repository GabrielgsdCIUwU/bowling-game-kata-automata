from src.score_card import ScoreCard

def test_hitting_pins_regular():
    pins = "12345123451234512345"
    total = 60
    score_card = ScoreCard(pins)
    assert score_card.get_score() == total