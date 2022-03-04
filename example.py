import json
import math
import pandas as pd
import requests
from datetime import date

start_date = "2003-08-02"
end_date = date.today()

month_starts = pd.date_range(start=start_date, end=end_date, freq="MS")
month_ends = pd.date_range(start=start_date, end=end_date, freq="M")

session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

for month_end, month_start in zip(month_ends, month_starts):
    matches = []
    response = session.post(
        "https://bet.hkjc.com/football/getJSON.aspx",
        headers=headers,
        params={
            "jsontype": "search_result.aspx",
            "startdate": month_start.strftime("%Y%m%d"),
            "enddate": month_end.strftime("%Y%m%d"),
            "pageno": 1,
        },
    )
    data = json.loads(response.text)[0]

    matchescount = data["matchescount"]

    for page in range(1, math.ceil(int(matchescount) / 20) + 1):
        response = session.post(
            "https://bet.hkjc.com/football/getJSON.aspx",
            headers=headers,
            params={
                "jsontype": "search_result.aspx",
                "startdate": month_start.strftime("%Y%m%d"),
                "enddate": month_end.strftime("%Y%m%d"),
                "pageno": page,
            },
        )
        if text := json.loads(response.text):
            data = text[0]

        matches.append(data["matches"])

    df = pd.DataFrame(matches)
    df.to_csv("matches.csv", index=False)
