from .messages import get_message
from .plots import colors
import time

class StageHandler:
    def __init__(self, stages_to_skip=tuple()):
        self.stages_to_skip = stages_to_skip
        self.curr_stage = 1

        self.INHALER_HAND_CLASS_NAME = "inhaler_hand"
        self.CAP_HAND_CLASS_NAME = "cap_hand"
        self.MOUTH_SEALED_ON_INHALER_CLASS_NAME = "mouth_sealed_on_inhaler"
        self.MOUTH_CLOSED_CLASS_NAME = "mouth_closed"
        self.MOUTH_OPENED_CLASS_NAME = "mouth_opened"

        self.mouth_closed_start_time = None

    def handle(self, annotator, classes_found):

        if self.curr_stage == 1:
            return self.handle_stage1(annotator, classes_found)
        elif self.curr_stage == 2:
            return self.handle_stage2(annotator, classes_found)
        elif self.curr_stage == 3:
            return self.handle_stage3(annotator, classes_found)
        elif self.curr_stage == 4:
            return self.handle_stage4(annotator, classes_found)
        elif self.curr_stage == 5:
            return self.handle_stage5(annotator, classes_found)

    def handle_stage1(self, annotator, classes_found):
        if ((self.CAP_HAND_CLASS_NAME not in classes_found) or (self.INHALER_HAND_CLASS_NAME not in classes_found)):
            message = get_message(1)
        else:
            message = get_message(2)
            self.go_to_next_stage()
            print(f"Proceeding to stage {self.curr_stage}")

        annotator.box_label([0,0,0,0], message, color=colors(0, True))

    def handle_stage2(self, annotator, classes_found):
        if ((self.MOUTH_SEALED_ON_INHALER_CLASS_NAME not in classes_found)):
            message = get_message(2)
        else:
            message = get_message(3)
            self.go_to_next_stage()
            print(f"Proceeding to stage {self.curr_stage}")

        annotator.box_label([0,0,0,0], message, color=colors(0, True))

    def handle_stage3(self, annotator, classes_found):
        if ((self.MOUTH_SEALED_ON_INHALER_CLASS_NAME in classes_found)):
            message = get_message(3)
        else:
            message = get_message(4, 0)
            self.go_to_next_stage()
            print(f"Proceeding to stage {self.curr_stage}")
        annotator.box_label([0,0,0,0], message, color=colors(0, True))

    def handle_stage4(self, annotator, classes_found):
        # Initialize timer
        if (self.mouth_closed_start_time == None) and (self.MOUTH_CLOSED_CLASS_NAME in classes_found):
            self.mouth_closed_start_time = time.time()
        
        # Update annotator
        if (self.mouth_closed_start_time != None) and (self.MOUTH_CLOSED_CLASS_NAME in classes_found):
            curr_time = time.time()
            seconds = curr_time - self.mouth_closed_start_time
            message = get_message(4, seconds)
        elif (self.mouth_closed_start_time != None) and (self.MOUTH_CLOSED_CLASS_NAME not in classes_found):
            message = get_message(5)
            self.go_to_next_stage()
            print(f"Proceeding to stage {self.curr_stage}")
        else:
            message = get_message(4, 0)
        annotator.box_label([0,0,0,0], message, color=colors(0, True))

    def handle_stage5(self, annotator, classes_found):
        message = get_message(5)
        annotator.box_label([0,0,0,0], message, color=colors(0, True))

    def go_to_next_stage(self):
        if self.curr_stage == 5:
            return
        self.curr_stage += 1
        while self.curr_stage in self.stages_to_skip and self.curr_stage < 5:
            self.curr_stage += 1