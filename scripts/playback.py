def playback(instructions, rec_mode, play_mode):
    if instructions:
        print(len(instructions))
        if play_mode:
            instruction = instructions.pop(0)
            lv = instruction['lv']
            av = instruction['av']
        else:
            instruction = instructions.pop()  # 0)
            lv = -instruction['lv']
            av = -instruction['av']
    else:
        lv = 0
        av = 0
        rec_mode = True

    return lv, av, rec_mode