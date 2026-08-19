import matplotlib.pyplot as plt
from pathlib import Path


def save_plot(fig, filepath):
    """
    Save a matplotlib figure to the specified path.
    """

    filepath = Path(filepath)

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fig.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)


def plot_time_series(
    df,
    date_column,
    value_column,
    title,
    output_path
):
    """
    Create and save a time-series plot.
    """

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    ax.plot(
        df[date_column],
        df[value_column]
    )

    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel(value_column)

    ax.grid(
        True,
        alpha=0.3
    )

    save_plot(
        fig,
        output_path
    )