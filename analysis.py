import functools
import numpy as np


def interspike_intervals(spike_times):
    """
    Calculates the interspike intervals for a series of spikes.
    :param spike_times: An array of times (in ms) where a spike occurs.
    :return: A list of interspike intervals.
    """
    return [j - i for i, j in zip(spike_times[:-1], spike_times[1:])]


def coefficient_of_variation(spike_times):
    """
    Computes the coefficient of variation for a series of spikes time.
    :param spike_times: An array of times (in ms) where a spike occurs.
    :return: The coefficient of variation.
    """
    intervals = interspike_intervals(spike_times)
    return np.std(intervals) / np.mean(intervals)


def fano_factor(interval, duration, spikes):
    """
    Computes the fano factor for a list of Trials.
    :param interval: Length of the bucket we're evaluating (in ms).
    :param duration: The duration of the trial (in ms).
    :param spikes: The times at which each spike occurs (in ms).
    :return: The fano factor.
    """
    bins = np.linspace(interval, duration, int(duration / interval))
    values, _ = np.histogram(spikes, bins)
    return np.var(values) / np.mean(values)


def spike_count_variance(duration, rate):
    """
    Computes the spike count variance.
    :param duration: The duration we are generating spikes for (in ms).
    :param rate: The maximum/constant rate over which we are creating spikes (in hz).
    :return: The spike count variance.
    """
    return duration * rate
