import generator
import analysis

""" Chapter 1 """

""" Problem 1 """

""" 
Generate spikes for 10s (or longer if you want better statistics) using a Poisson spike generator with a constant rate
of 100Hz, and record their times of occurrence. Compute the coefficient of variation of the interspike intervals, and
the Fano factor for spike counts obtained over counting intervals ranging from 1 to 100ms. Plot the interspike interval
histogram.
"""


def one():
    duration_in_ms = 10 * 1000
    rate_in_ms = 100 / 1000
    spikes = generator.short_way(duration_in_ms, rate_in_ms)
    coefficient_of_variation = analysis.coefficient_of_variation(spikes)
    window_widths = [x for x in range(1, 101)]
    print("Time Window\t Fano factor")
    for window in window_widths:
        fano_factor = analysis.fano_factor(window, duration_in_ms, spikes)
        print("% 8d ms \t% 11.3f" % (int(window), fano_factor))

    print(f'\nCoefficient of Variation: %1.3f' % coefficient_of_variation)


one()
