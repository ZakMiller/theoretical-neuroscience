import numpy as np
import itertools as it
from typing import List


def interspike_intervals(spike_times):
    """
    Calculates the interspike intervals for a series of spikes.
    :param spike_times: A list of times (in ms) where a spike occurs.
    :return: A list of interspike intervals.
    """
    return [j - i for i, j in zip(spike_times[:-1], spike_times[1:])]


def edges(n: int):
    """Returns the number of possible undirected edges given a number of n nodes.
    Arguments:
        n {int} -- The number of nodes.
    Returns:
        int -- The number of edges.
    """
    return n * (n - 1) / 2


# This isn't giving me the value I expect
def ac_for_bin(pairings: int, duration: int, bin_length: int, spikes: int):
    """Returns the autocorrelation value for a particular bin.
    T is total length of time.
    delta_t is bin length.
    n is total spike count.
    Nm is count of pairings in bin.
    Hm = Nm/T - n**2 * delta_t/T**2
    Arguments:
        pairings {int} -- (Nm) The pair count (including self pairs).
        duration {int} -- (T) The trial duration (in ms).
        bin_length {int} -- (delta_t) The length of the bin (in ms).
        spikes {int} -- (n) The spike count.

    Returns:
        {float} -- (Hm) The autocorrelation value.
    """
    result = (pairings / duration) - spikes**2 * (bin_length / duration ** 2)
    return result


def autocorrelation(spikes: List[int], duration: int, bin_length: int):
    """Returns a list of autocorrelations for each bin.
    :param spikes: A list of times (in ms) where a spike occurs.
    :param duration: The duration of the trial in ms.
    :param bin_length: The length of each bin.
    :return: A list of autocorrelation values for each bin.
    """

    distances = [y - x for x, y in it.combinations(spikes, 2)]

    bins = np.linspace(bin_length, duration, np.floor(duration / bin_length))
    values, _ = np.histogram(distances, bins)

    return [ac_for_bin(distance, duration, bin_length, len(spikes))
            for distance in values], bins


def coefficient_of_variation(spike_times: List[int]):
    """
    Computes the coefficient of variation for a series of spikes time.
    :param spike_times: A list of times (in ms) where a spike occurs.
    :return: The coefficient of variation.
    """
    intervals = interspike_intervals(spike_times)
    return np.std(intervals) / np.mean(intervals)


def fano_factor(interval, duration, spikes):
    """
    Computes the fano factor for a list of spikes.
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
