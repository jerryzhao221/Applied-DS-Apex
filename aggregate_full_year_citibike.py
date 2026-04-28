import io
import zipfile
from pathlib import Path
from urllib.request import urlopen

import pandas as pd


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

months = [f"2025{m:02d}" for m in range(1, 13)]
url = "https://s3.amazonaws.com/tripdata/{ym}-citibike-tripdata.zip"

daily_parts = []
hourly_parts = []
total_trips = 0

for ym in months:
    print(f"Downloading and processing {ym} ...")
    with urlopen(url.format(ym=ym), timeout=120) as response:
        zip_bytes = io.BytesIO(response.read())

    with zipfile.ZipFile(zip_bytes) as zf:
        csv_names = [
            name
            for name in zf.namelist()
            if name.endswith(".csv")
            and Path(name).name.startswith(ym)
            and not Path(name).name.startswith("JC")
        ]

        for csv_name in csv_names:
            print(f"  {Path(csv_name).name}")
            with zf.open(csv_name) as f:
                for chunk in pd.read_csv(
                    f,
                    usecols=["started_at", "member_casual"],
                    parse_dates=["started_at"],
                    chunksize=1_000_000,
                ):
                    chunk = chunk.dropna(subset=["started_at", "member_casual"])
                    chunk["date"] = chunk["started_at"].dt.date
                    chunk["hour"] = chunk["started_at"].dt.hour
                    total_trips += len(chunk)

                    daily_parts.append(
                        chunk.groupby(["date", "member_casual"]).size().rename("count")
                    )
                    hourly_parts.append(
                        chunk.groupby(["date", "hour", "member_casual"])
                        .size()
                        .rename("count")
                    )

daily_usage = (
    pd.concat(daily_parts)
    .groupby(level=["date", "member_casual"])
    .sum()
    .unstack(fill_value=0)
)
hourly_usage = (
    pd.concat(hourly_parts)
    .groupby(level=["date", "hour", "member_casual"])
    .sum()
    .unstack(fill_value=0)
)

for usage in [daily_usage, hourly_usage]:
    for col in ["casual", "member"]:
        if col not in usage.columns:
            usage[col] = 0
    usage["total"] = usage["casual"] + usage["member"]

daily_usage = daily_usage[["casual", "member", "total"]]
hourly_usage = hourly_usage[["casual", "member", "total"]]

daily_usage.index = pd.to_datetime(daily_usage.index)
daily_usage.index.name = "date"

daily_usage.to_csv(DATA_DIR / "daily_usage.csv")
hourly_usage.to_csv(DATA_DIR / "hourly_usage.csv")

print("Total trips processed:", total_trips)
print("daily_usage shape:", daily_usage.shape)
print("hourly_usage shape:", hourly_usage.shape)
print("date range:", daily_usage.index.min().date(), daily_usage.index.max().date())
