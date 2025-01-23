class ScoreCard:
    def __init__(self, score_card):
        self.pins = score_card
        
    def get_pins(self):
        return self.pins
    
    def get_score(self):
        all_frames = self.__pins_to_frames()
        all_frames = self.__spare_to_value(all_frames)
        all_frames = self.__strike_to_value(all_frames[::-1])
        total_score = 0
        for frame in all_frames:
            total_score += sum(frame)
        
        return total_score
    
    def __pins_to_frames(self):
        all_frames = []
        frame = []
        for pin in self.get_pins():
            if pin == 'X':
                if len(all_frames) == 10:
                    all_frames.append(all_frames.pop() + ['X'])
                else:
                    all_frames.append(['X'])
            else:
                frame.append(self.__pin_to_value(pin))
            if len(frame) == 2:
                all_frames.append(frame)
                frame = []
        if frame:
            all_frames.append(all_frames.pop(-1) + frame)
        return all_frames

    def __pin_to_value(self, pin):
        if pin not in ['/', '-']:
            return int(pin)
        elif pin == '-':
            return 0
        else:
            return pin
        
    def __spare_to_value(self, all_frames):
        for i, frame in enumerate(all_frames):
            try:
                if '/' in frame:
                    if all_frames[i+1][0] == 'X':
                        all_frames[i] = [10]
                    else:
                        all_frames[i] = [10, all_frames[i+1][0]]
            except IndexError:
                if len(all_frames[i]) == 2:
                    all_frames[i] = [10]
                else:
                    all_frames[i] = [10, frame[2]] 
        return all_frames
    
    def __strike_to_value(self, all_frames):
        for i, frame in enumerate(all_frames):
            try:
                if 'X' in frame:
                    if i in [0, 1, 2]:
                        all_frames[i] = [10]
                    else:
                        all_frames[i] = [10, all_frames[i-1][0], all_frames[i-1][1]]
            except IndexError:
                all_frames[i] = [10, all_frames[i-1][0]]
        return all_frames
    

if __name__ == '__main__':
    pins = "XXX9-9-9-9-9-9-9-"
    total = 141
    score_card = ScoreCard(pins)
    assert score_card.get_score() == total