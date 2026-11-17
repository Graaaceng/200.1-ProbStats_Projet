import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    return mo, pd, plt, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Projet probabilités et statistiques IT - Météo
    """)
    return


@app.cell
def _():
    precipitation_sum_month_key = "rre150m0"
    temperature_2m_avg_month_key = "tre200m0"
    timestamp_key = "reference_timestamp"
    station_abbr_key = "station_abbr"
    return (
        precipitation_sum_month_key,
        station_abbr_key,
        temperature_2m_avg_month_key,
        timestamp_key,
    )


@app.cell
def _(pd, timestamp_key):
    station_data = pd.read_csv("data/evo.csv", delimiter=";")
    station_data[timestamp_key] = pd.to_datetime(station_data[timestamp_key], dayfirst=True)
    station_data['month'] = pd.DatetimeIndex(station_data[timestamp_key]).month
    station_data['year'] = pd.DatetimeIndex(station_data[timestamp_key]).year

    n_decade = 4

    station_data['decade'] = (station_data['year'] // n_decade) * n_decade

    station_data = station_data[station_data["year"] <= station_data["year"].max() - 1]

    station_data
    return n_decade, station_data


@app.cell
def _(station_data, temperature_2m_avg_month_key):
    temp_data = station_data[["decade", temperature_2m_avg_month_key]].groupby("decade").mean().reset_index()

    temp_data
    return (temp_data,)


@app.cell
def _(precipitation_sum_month_key, station_data):
    prec_data = station_data[["decade", precipitation_sum_month_key]].groupby("decade").mean().reset_index()

    prec_data
    return (prec_data,)


@app.cell
def _(prec_data, temp_data):
    prec_data["decade"] = prec_data["decade"].astype(str)
    temp_data["decade"] = temp_data["decade"].astype(str)
    return


@app.cell
def _(
    n_decade,
    plt,
    prec_data,
    precipitation_sum_month_key,
    sns,
    station_abbr_key,
    station_data,
    temp_data,
    temperature_2m_avg_month_key,
):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.set_xlabel(f"Années groupées par {n_decade} ans")

    sns.barplot(data=prec_data, x="decade", y=precipitation_sum_month_key, ax=ax1, color="#3274a1")
    ax1.set_ylabel("Moyenne des précipitations par mois [mm]", color="#3274a1")
    ax1.tick_params(axis="y", labelcolor="#3274a1")

    ax2 = ax1.twinx()
    sns.lineplot(data=temp_data, x="decade", y=temperature_2m_avg_month_key, ax=ax2, marker="o", color="orange")
    ax2.set_ylabel("Température moyenne par mois [°C]", color="orange")
    ax2.tick_params(axis="y", labelcolor="orange")

    plt.title(f"Evolution des précipitations et de la température, en moyenne, par mois, par {n_decade} ans à {station_data[station_abbr_key][0]}")
    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
