def get_stage_one_message():
    STAGE_ONE_MESSAGE = "Please remove inhaler cap"
    return STAGE_ONE_MESSAGE

def get_stage_two_message():
    STAGE_TWO_MESSAGE = "Cap removal detected"
    return STAGE_TWO_MESSAGE

def get_stage_three_message():
    STAGE_THREE_MESSAGE = "Inhaler in mouth detected"
    return STAGE_THREE_MESSAGE

def get_stage_four_message(seconds):
    STAGE_FOUR_MESSAGE = "Mouth closed for %1.1f seconds"
    return STAGE_FOUR_MESSAGE % round(seconds, 1)

def get_success_message():
    SUCCESS_MESSAGE = "Procedure completed!"
    return SUCCESS_MESSAGE

def get_shaking_message():
    return "Shaking detected"

def get_message(stage:int, *args):
    if stage == 1:
        return get_stage_one_message()
    elif stage == 2:
        return get_stage_two_message()
    elif stage == 3:
        return get_stage_three_message()
    elif stage == 4:
        return get_stage_four_message(*args)
    elif stage == 5:
        return get_success_message()
    else:
        return "Invalid stage"
