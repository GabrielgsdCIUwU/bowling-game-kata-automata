from src.score_card import ScoreCard
def test_symbol_zero():
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    score_card = ScoreCard(pins)
    assert score_card.get_score() == total

    pins = "9-3561368153258-7181"
    total = 82
    score_card = ScoreCard(pins)
    assert score_card.get_score() == total