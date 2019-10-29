import generator
import analysis
import plotter
import numpy as np


def do():
    duration_in_ms = 10 * 1000
    rate_in_ms = 100 / 1000
    """
    Generate spikes for 10s (or longer if you want better statistics) using a Poisson spike generator 
    with a constant rate of 100Hz, and record their times of occurrence.
    """
    spikes = generator.short_way(duration_in_ms, rate_in_ms)

    """
    Compute the coefficient of variation of the interspike intervals,
    """
    coefficient_of_variation = analysis.coefficient_of_variation(spikes)
    print(f'Coefficient of Variation: %1.3f' % coefficient_of_variation)

    """
    and the Fano factor for spike counts obtained over counting intervals ranging from 1 to 100ms.
    """
    windows = [1, 10, 25, 50, 100]
    for window in windows:
        fano_factor = analysis.fano_factor(window, duration_in_ms, spikes)
        print(f'Fano factor: %1.3f' % fano_factor)

    """
    Plot the interspike interval histogram.
    """
    window = 10
    bins = np.linspace(window, duration_in_ms, int(duration_in_ms / window))
    values, _ = np.histogram(spikes, bins)
    plotter.show(spikes, bins, f'Bucket size of {window}ms')


