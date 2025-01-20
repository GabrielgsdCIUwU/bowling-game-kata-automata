class ScoreCard:
    def __init__(self, score_card):
        self.pins = score_card
        
    def get_pins(self):
        return self.pins
    
    def get_score(self):
        all_frames = self.__pins_to_frames()
        total_score = 0
        for frame in all_frames:
            total_score += sum(frame)
        
        return total_score
    
    def __pins_to_frames(self):
        all_frames = []
        frame = []
        for pin in self.get_pins():
            frame.append(self.__pin_to_value(pin))
            if len(frame) == 2:
                all_frames.append(frame)
                frame = []
        return all_frames

    def __pin_to_value(self, pin):
        if pin not in ['/', '-']:
            return int(pin)
        elif pin == '-':
            return 0
        else:
            return pin