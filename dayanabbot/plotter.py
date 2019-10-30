import matplotlib.pyplot as plt


def show(data, bins, title):
    _ = plt.hist(data, bins)
    plt.title(title)
    plt.show()


def interspike_intervals(interval_sets):
    for interval in interval_sets:
        _ = plt.hist(interval, alpha=0.6)

    plt.title('Interspike intervals')
    plt.xlabel('Interspike interval (ms)')
    plt.ylabel('Interval count')
    plt.show()


def cv_against_tau(cvs, taus):
    plt.plot(taus, cvs)
    plt.xlabel("refractory time constant (ms)")
    plt.ylabel("Coefficient of Variation")
    plt.show()


def autocorrelation(data, bins, title):
    plt.hist(data, bins)
    plt.title(title)
    plt.xlim(0, 100)
    plt.show()
