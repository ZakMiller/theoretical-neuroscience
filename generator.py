import numpy as np


def long_way(interval, duration, rate):
    """
    This is the long way of generating spikes.
    We're iterating over every possible time that we could have a spike, and determining whether we should or not.
    Works for firing rates that are constant and not.
    Contrast with the quick way.
    :param interval: Length of time we're testing for (to determine if it should have a spike) in ms.
    :param duration: The duration we are generating spikes for (in ms).
    :param rate: The maximum/constant rate over which we are creating spikes (in mHz).
    :return: An array of times (in ms) where a spike occurs.
    """
    window_count = duration / interval
    chance_there_is_spike = rate * interval
    all_times = [1 if np.random.random() < chance_there_is_spike else 0 for _ in range(0, int(window_count))]
    result = [index * interval for index, has_spike in enumerate(all_times) if has_spike == 1]
    return result


def short_way(duration, rate):
    """
    This is the short way of generating spikes.
    By itself, it only works for constant firing rates. Combine with spike thinning to have it work with other
    situations.
    Contrast with the long way.
    :param duration: The duration we are generating spikes for (in ms).
    :param rate: The maximum/constant rate over which we are creating spikes (in mHz).
    :return: An array of times (in ms) where a spike occurs.
    """
    t = 0
    times = []
    while t < duration:
        r = np.random.random()
        t = t - np.log(r) / rate
        times.append(t)
    times = times[:-1]
    return times
