from src.score_card import ScoreCard
def test_get_pins():
    PINS = "12345123451234512345"
    score_card = ScoreCard(PINS)
    assert score_card.get_pins() == PINS