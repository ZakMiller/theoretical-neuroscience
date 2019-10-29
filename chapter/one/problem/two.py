
import generator
import analysis
import plotter


def do():
    duration_in_ms = 10 * 1000
    rate_in_ms = 100 / 1000
    """
    Add a refractory period to the Poisson spike generator by allowing the
    firing rate to depend on time. Initially, set the firing rate to a constant
    value r(t) = r0. After every spike, set r(t) to 0, and then allow it to recover
    exponentially back to r0 with a time constant tauref that controls the refractory
    recovery rate.
    """
    spike_sets = [[generator.refractory(duration_in_ms, rate_in_ms, tau_ref), tau_ref] for tau_ref in range(1, 21)]

    """
    Plot the coefficient of variation as a function of tauref over the range 1 ms <= tauref <= 20 ms
    """
    data_points = [[analysis.coefficient_of_variation(spikes[0]), spikes[1]] for spikes in spike_sets]
    cvs = [point[0] for point in data_points]
    taus = [point[1] for point in data_points]
    plotter.cv_against_tau(cvs, taus)
    """
    and plot interspike interval histograms for a few different values of tau_ref in this range.
    """
    spikes = [spikes[0] for spikes in spike_sets]
    sets_to_plot = [spikes[0], spikes[5], spikes[15]]
    intervals = [analysis.interspike_intervals(s) for s in sets_to_plot]
    plotter.interspike_intervals(intervals)

    """
    Compute the Fano factor for spike counts obtained over counting intervals 
    ranging from 1 to 100 ms for the case tau_ref = 10ms.
    """
    spikes = generator.refractory(duration_in_ms, rate_in_ms, 10)
    intervals = [1, 10, 25, 100]
    for interval in intervals:
        print(f'Interval (ms)\tFano factor')
        fano = analysis.fano_factor(interval, duration_in_ms, spikes)
        print(f'%-15s %-15s' % (interval, fano))
