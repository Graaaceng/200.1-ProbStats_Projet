import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Projet probabilités et statistiques IT - Météo
    """)
    return


@app.cell
def _():
    precipitation_sum_month_key = "rre150m0"
    timestamp_key = "reference_timestamp"
    return (timestamp_key,)


@app.cell
def _(pd, timestamp_key):
    station_data = pd.read_csv("data/evo.csv", delimiter=";")
    station_data[timestamp_key] = pd.to_datetime(station_data[timestamp_key], dayfirst=True)
    station_data['month'] = station_data[timestamp_key].dt.month
    station_data['year'] = station_data[timestamp_key].dt.year

    station_data
    return


if __name__ == "__main__":
    app.run()
