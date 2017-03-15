from fire_foo import current_week_calls, last_week_calls


def bot():
    xcalls = last_week_calls()
    ycalls = current_week_calls()

    print(len(xcalls) - len(ycalls))
