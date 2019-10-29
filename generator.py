import numpy as np
import math


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


def refractory(duration, base_rate, tau_ref):
    """
    Generates spikes with a refractory period.
    :param duration: The duration we are generating spikes for (in ms).
    :param base_rate: The starting rate we use to generate spikes. Changes over time due to a refractory period.
    :param tau_ref: The constant used to control the refractory recovery rate.
    :return: An array of times (in ms) where a spike occurs.
    """
    spikes = []
    for t in range(1, duration):
        time_since_last_spike = 1000000 if len(spikes) == 0 else t - spikes[-1]
        rate = base_rate * (1 - np.exp(- time_since_last_spike / tau_ref))
        was_spike = np.random.random() < rate
        if was_spike:
            spikes.append(t)

    return spikes


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
