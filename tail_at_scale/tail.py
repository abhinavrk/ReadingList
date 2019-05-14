import numpy as np
from matplotlib import pyplot as plt


def generate_data(n, min_time):
    ys = np.random.gumbel(70, 3, n) + min_time
    return ys


def hedged_requests(percentile=75):
    ys = generate_data(10000, 40)

    ptile = np.percentile(ys, percentile)

    actual_ys = []
    for y in ys:
        if y <= ptile:
            actual_ys.append(y)
        else:
            new_y = generate_data(1, 40)[0] + ptile
            actual_ys.append(min(new_y, y))

    draw_histogram(actual_ys)


def draw_histogram(data):
    ymin, ymax = min(data), max(data)
    bins = list(range(ymin, ymax, 5))
    plt.hist(data, bins=bins)
    plt.title('histogram of latencies')


if __name__ == "__main__":
    hedged_requests()
