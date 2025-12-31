# LOADING DATA
import pandas as pd


def load_nifty(path="C:\\Users\\hp\\OneDrive\\Desktop\\QUANT GLOBAL ASSIGNMENT\\data\\Nifty50 (2000 to 2025)\\data.csv"):
    df = pd.read_csv(path)
    df.columns = [col.strip() for col in df.columns]
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[["Date", "Close"]]
    df.rename(columns={"Close": "NIFTY_Close"}, inplace=True)

    return df


def load_indiavix(path="C:\\Users\\hp\\OneDrive\\Desktop\\QUANT GLOBAL ASSIGNMENT\\data\\hist_india_vix_-01-01-2025-to-30-12-2025.csv"):
    df = pd.read_csv(path)
    df.columns = [col.strip() for col in df.columns]
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[["Date", "Close"]]

    df.rename(columns={"Close": "India_VIX"}, inplace=True)

    return df


def load_usd_inr(path="C:\\Users\\hp\\OneDrive\\Desktop\\QUANT GLOBAL ASSIGNMENT\\data\\usd_inr_2025.csv"):
    df = pd.read_csv(path)
    df.columns = [col.strip() for col in df.columns]
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[["Date", "USD_INR"]]

    return df





