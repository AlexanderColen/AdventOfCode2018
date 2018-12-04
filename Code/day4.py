import datetime
import pandas as pd


def organizeChronologically():
    lines = open('../Input/input_day4.txt', 'r').readlines()
    df = pd.DataFrame(columns=['datetime', 'action'])
    for i, line in enumerate(lines):
        line = line.rstrip()
        # year = int(line.split('-')[0].replace('[', ''))
        # Since the actual year (1518) is out of bounds for a DateTime object, I set it to 2018 instead.
        year = 2018
        month = int(line.split('-')[1])
        day = int(line.split('-')[2].split(' ')[0])
        hour = int(line.split(' ')[1].split(':')[0])
        minutes = int(line.split(' ')[1].split(':')[1].replace(']', ''))
        x = datetime.datetime(year, month, day, hour, minutes)
        action = line.split('] ')[1]
        df.loc[i] = [x, action]

    df.sort_values(by='datetime', ascending=True, inplace=True)

    return df


def recordGuardSleepSchedule(df_chronological):
    df = pd.DataFrame(columns=['guard_id', 'time_asleep', 'fell_asleep', 'woke_up'])
    df_guards = pd.DataFrame(columns=['guard_id', 'sleepytime'])

    # Put all sleep records into DataFrame.
    guard_ID = 0
    minutes_asleep = 0
    fell_asleep_at = 0
    for index, row in df_chronological.iterrows():
        if 'Guard' in row['action']:
            # Find the new guard's ID and reset the minutes asleep to zero.
            guard_ID = row['action'].split('#')[1].split(' ')[0]
            minutes_asleep = 0
        elif 'falls asleep' in row['action']:
            fell_asleep_at = int(row['datetime'].strftime('%M'))
        elif 'wakes up' in row['action']:
            woke_up_at = int(row['datetime'].strftime('%M'))
            minutes_asleep += int(woke_up_at) - int(fell_asleep_at)
            # Submit this into the DataFrame.
            df.loc[index] = [guard_ID, minutes_asleep, fell_asleep_at, woke_up_at]
        # Add this to the other DataFrame per guard.
        if minutes_asleep != 0:
            if guard_ID in df_guards['guard_id'].values:
                df_guards['sleepytime'][df_guards['guard_id'] == guard_ID] += minutes_asleep
            else:
                df_guards.loc[index] = [guard_ID, minutes_asleep]

    return df, df_guards


def puzzle1():
    df = organizeChronologically()
    df_2, df_guards = recordGuardSleepSchedule(df_chronological=df)

    # Find the laziest guard's ID.
    df_guards.sort_values(by='sleepytime', ascending=False, inplace=True)
    sleepy_guard = df_guards['guard_id'].iloc[0]

    # Find the most slept minute by the guard.
    minute_most_slept = 0
    max_amount = 0
    for x in range(59):
        df_3 = df_2[df_2['guard_id'] == sleepy_guard]
        df_3 = df_3[(df_3['fell_asleep'] <= x) & (df_3['woke_up'] > x)]
        curr_amount = len(df_3)
        if curr_amount > max_amount:
            max_amount = curr_amount
            minute_most_slept = x

    print(f'Guard ID: {sleepy_guard} - '
          f'Time Asleep: {df_2["time_asleep"].iloc[0]} - '
          f'Minute most often asleep: {minute_most_slept}')
    return int(sleepy_guard) * int(minute_most_slept)


def puzzle2():
    df = organizeChronologically()
    df_2, df_guards = recordGuardSleepSchedule(df_chronological=df)
    df_4 = pd.DataFrame(columns=['guard_id', 'minute', 'frequency'])

    for x in range(59):
        df_3 = df_2[(df_2['fell_asleep'] <= x) & (df_2['woke_up'] > x)]
        for entry in df_3['guard_id']:
            if entry in df_4['guard_id'].values:
                # Guard exist in the DataFrame for unknown minute(s).
                if x in df_4['minute'][df_4['guard_id'] == entry].values:
                    # Guard exists with the correct minute.
                    df_4['frequency'][(df_4['guard_id'] == entry) & (df_4['minute'] == x)] += 1
                else:
                    # Guard doesn't exist with the correct minute.
                    df_4.loc[len(df_4)] = [entry, x, 1]
            else:
                # Guard doesn't exist yet in the DataFrame.
                df_4.loc[len(df_4)] = [entry, x, 1]

    # Sort by frequency.
    df_4.sort_values(by='frequency', ascending=False, inplace=True)

    sleepy_guard = int(df_4['guard_id'].iloc[0])
    minute = int(df_4['minute'].iloc[0])
    frequency = int(df_4['frequency'].iloc[0])
    print(f'Guard ID: {sleepy_guard} - '
          f'Minute most often asleep: {minute} - '
          f'Frequency: {frequency}')
    return sleepy_guard * minute


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
