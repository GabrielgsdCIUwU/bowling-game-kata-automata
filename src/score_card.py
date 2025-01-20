class ScoreCard:
    def __init__(self, score_card):
        self.pins = score_card
        
    def get_pins(self):
        return self.pins
    
    def get_score(self):
        all_frames = self.__pins_to_list()

        total_score = 0
        for frame in all_frames:
            total_score += sum(frame)
        
        return total_score
    
    def __pins_to_list(self):
        all_frames = []
        frame = []
        for pin in self.pins:
            if pin not in ['/', '-']:
                frame.append(int(pin))
            elif pin == '-':
                frame.append(0)
            else:
                frame.append(pin)

            if len(frame) == 2:
                all_frames.append(frame)
                frame = []
        return all_frames