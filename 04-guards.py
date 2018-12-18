# dictionary with dates as keys
from datetime import datetime as dt
from collections import Counter

def processScheduleFile(filename):
    # builds schedule dict: keys are days, values are event dicts
    # event dict: keys are (hour,minute) tuples, values are text memos
    with open(filename, 'r') as f:
        schedule = dict()
        for line in f:
            logTime = dt.strptime(line[:18], "[%Y-%m-%d %H:%M]")
            key = (logTime.month, logTime.day)
            if key not in schedule:
                events = dict()
                schedule[key] = events
            time = (logTime.hour, logTime.minute)
            memo = line[19:-1]
            schedule[key][time] = memo
        return buildTimeline(schedule)

def buildTimeline(schedule):
    timeline = dict()
    guardOrder = []
    curGuard = None
    for date in sorted(schedule):
        minuteLine = ['.' for e in range(60)]
        m = 0
        guardSet = False
        awake = True
        for time in sorted(schedule[date]):
            if schedule[date][time].split()[0] == 'Guard':
                curGuard = int(schedule[date][time].split()[1][1:])
            hr,mn = time
            if hr == 0:
                if not guardSet:
                    guardOrder.append(curGuard)
                    guardSet = True
                for i in range(m, mn):
                    if not awake:
                        minuteLine[i] = '#'
                m = mn
            elif len(schedule[date]) == 1:
                guardOrder.append(curGuard)
            if schedule[date][time] == 'falls asleep':
                awake = False
            elif schedule[date][time] == 'wakes up':
                awake = True
        timeline[date] = minuteLine
    return timeline,guardOrder

def getSleepTimes(guardShiftKeys, timeline):
    guardSleepTimes = Counter()
    for guard,day in guardShiftKeys:
        minutesSlept = len([x for x in timeline[day] if x == '#'])
        guardSleepTimes[guard] += minutesSlept
    return guardSleepTimes

def getGuardMinuteSleepFreq(guardKeys, timeline):
    minuteSleepFreq = Counter()
    for key in guardKeys:
        for m,isAsleep in enumerate([x == "#" for x in timeline[key]]):
            if isAsleep:
                minuteSleepFreq[m] += 1
    return minuteSleepFreq

if __name__ == '__main__':
    timeline, guardOrder = processScheduleFile('input.txt')
    guardSleepTimes = getSleepTimes(zip(guardOrder, sorted(timeline)), timeline)

    # part 1
    maxSleeper = sorted(guardSleepTimes, key=lambda t: guardSleepTimes[t]).pop()
    maxGuardMinuteSleepFreq = getGuardMinuteSleepFreq(
        [k for g,k in zip(guardOrder, sorted(timeline)) if g == maxSleeper],
        timeline)
    maxMinuteSlept = sorted(maxGuardMinuteSleepFreq, key=lambda f: maxGuardMinuteSleepFreq[f]).pop()

    print(maxSleeper, maxMinuteSlept, maxSleeper * maxMinuteSlept)

    # part 2
    maxFreq = 0
    guardWMaxFreq = None
    minuteWMaxFreq = None
    for guard in guardOrder:
        minuteSleepFreqs = getGuardMinuteSleepFreq(
            [k for g,k in zip(guardOrder, sorted(timeline)) if g == guard], timeline)
        if minuteSleepFreqs:
            maxMinuteSlept = sorted(minuteSleepFreqs, key=lambda f: minuteSleepFreqs[f]).pop()
            freq = minuteSleepFreqs[maxMinuteSlept]
            if freq > maxFreq:
                maxFreq = freq
                guardWMaxFreq = guard
                minuteWMaxFreq = maxMinuteSlept
    print(guardWMaxFreq, minuteWMaxFreq, minuteWMaxFreq * guardWMaxFreq)
