class ScoreCard:
    def __init__(self, score_card):
        self.pins = score_card
        
    def get_pins(self):
        return self.pins
    
    def get_score(self):
        
        
        return
    
    def __pins_to_list(self):
        all_frames = []
        frame = []
        for pin in self.pins:
            frame.append(pin)
            if len(frame) == 2:
                all_frames.append(frame)
                frame = []
        return all_frames