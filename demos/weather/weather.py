#!/usr/bin/env python3
"""
Simulated CLI Weather Tool.

Commands:
  current <city>          Show current weather for a city
  forecast <city>         Show 5-day forecast for a city
  compare <city1> <city2> Compare current weather between two cities

All data is deterministic fake data generated from city name hashes.
No real API calls.
"""

import argparse
import hashlib
import sys
from datetime import datetime, timedelta

CONDITIONS = [
    "Sunny",
    "Cloudy",
    "Rainy",
    "Snowy",
    "Windy",
    "Foggy",
    "Clear",
    "Overcast",
]


def _hash_digest(city: str) -> str:
    return hashlib.md5(city.lower().encode("utf-8")).hexdigest()


def _rolling_temp(city: str, day_offset: int = 0) -> float:
    """Deterministic temperature between -5 and 40 °C."""
    h = _hash_digest(f"{city}-temp-{day_offset}")
    raw = int(h[:8], 16)
    return round(-5 + (raw % 450) / 10, 1)


def _humidity(city: str, day_offset: int = 0) -> int:
    """Deterministic humidity between 20 and 100 %."""
    h = _hash_digest(f"{city}-hum-{day_offset}")
    return 20 + (int(h[:6], 16) % 81)


def _wind_speed(city: str, day_offset: int = 0) -> float:
    """Deterministic wind speed in km/h, 0–60."""
    h = _hash_digest(f"{city}-wind-{day_offset}")
    return round((int(h[:6], 16) % 600) / 10, 1)


def _condition(city: str, day_offset: int = 0) -> str:
    """Deterministic condition string."""
    h = _hash_digest(f"{city}-cond-{day_offset}")
    idx = int(h[:4], 16) % len(CONDITIONS)
    return CONDITIONS[idx]


def _wind_direction(city: str, day_offset: int = 0) -> str:
    """Deterministic cardinal wind direction."""
    h = _hash_digest(f"{city}-wdir-{day_offset}")
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return dirs[int(h[:4], 16) % len(dirs)]


def cmd_current(args: argparse.Namespace) -> None:
    city = args.city
    temp = _rolling_temp(city)
    cond = _condition(city)
    hum = _humidity(city)
    wind = _wind_speed(city)
    wdir = _wind_direction(city)

    print(f"╒══════════════════════════════════╕")
    print(f"│  Current Weather — {city:<20} │")
    print(f"╞══════════════════════════════════╡")
    print(f"│  Temperature : {temp:>5} °C          │")
    print(f"│  Conditions  : {cond:<15}      │")
    print(f"│  Humidity    : {hum:>3} %              │")
    print(f"│  Wind        : {wind:>4} km/h {wdir:<2}         │")
    print(f"╘══════════════════════════════════╛")


def cmd_forecast(args: argparse.Namespace) -> None:
    city = args.city
    days = args.days if args.days is not None else 5

    today = datetime.now()
    print(f"╒══════════════════════════════════════════════════════╕")
    print(f"│  {days}-Day Forecast — {city:<35}    │")
    print(f"╞══════════════════════════════════════════════════════╡")
    for i in range(days):
        d = today + timedelta(days=i)
        temp = _rolling_temp(city, i)
        cond = _condition(city, i)
        hum = _humidity(city, i)
        wind = _wind_speed(city, i)
        wdir = _wind_direction(city, i)
        date_str = d.strftime("%a %b %d")
        print(f"│  {date_str}  │  {temp:>5} °C  │  {cond:<10}  │  {hum:>2}%  │  {wind:>4} km/h {wdir:<2}  │")
    print(f"╘══════════════════════════════════════════════════════╛")


def cmd_compare(args: argparse.Namespace) -> None:
    c1, c2 = args.city1, args.city2

    t1, t2 = _rolling_temp(c1), _rolling_temp(c2)
    cond1, cond2 = _condition(c1), _condition(c2)
    h1, h2 = _humidity(c1), _humidity(c2)
    w1, w2 = _wind_speed(c1), _wind_speed(c2)
    wd1, wd2 = _wind_direction(c1), _wind_direction(c2)

    label_w = 20
    print(f"╒══════════════════════════════════════════════════════════╕")
    print(f"│  Weather Comparison                                    │")
    print(f"╞══════════════════════════════════════════════════════════╡")
    print(f"│  {'':<{label_w}}  │  {c1:<20}  │  {c2:<20}  │")
    print(f"│  {'─' * label_w}  │  {'─' * 20}  │  {'─' * 20}  │")
    print(f"│  {'Temperature':<{label_w}}  │  {str(t1) + ' °C':>20}  │  {str(t2) + ' °C':>20}  │")
    print(f"│  {'Conditions':<{label_w}}  │  {cond1:>20}  │  {cond2:>20}  │")
    print(f"│  {'Humidity':<{label_w}}  │  {str(h1) + ' %':>20}  │  {str(h2) + ' %':>20}  │")
    print(f"│  {'Wind':<{label_w}}  │  {f'{w1} km/h {wd1}':>20}  │  {f'{w2} km/h {wd2}':>20}  │")
    print(f"╘══════════════════════════════════════════════════════════╛")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="weather",
        description="Simulated CLI weather tool — deterministic fake data based on city name.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # current
    p_current = sub.add_parser("current", help="Show current weather for a city")
    p_current.add_argument("city", help="City name")
    p_current.set_defaults(func=cmd_current)

    # forecast
    p_forecast = sub.add_parser("forecast", help="Show multi-day forecast for a city")
    p_forecast.add_argument("city", help="City name")
    p_forecast.add_argument("-n", "--days", type=int, default=None,
                            help="Number of forecast days (default: 5)")
    p_forecast.set_defaults(func=cmd_forecast)

    # compare
    p_compare = sub.add_parser("compare", help="Compare weather between two cities")
    p_compare.add_argument("city1", help="First city")
    p_compare.add_argument("city2", help="Second city")
    p_compare.set_defaults(func=cmd_compare)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
