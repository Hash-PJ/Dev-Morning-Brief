# 🗞 Dev Morning Brief

One command. Your entire morning in the terminal.

## What you get

    python brief.py Mumbai INR

```
__________________________________________
||          DEV MORNING BRIEF           ||
||          Monday 12 May 2026          ||
||======================================||
|| ⛅ WEATHER — Mumbai                  ||
|| ☀️  32°C, feels like 36°C            ||
||======================================||
|| 💰 GOLD & SILVER (intl. spot)        ||
|| Gold    : ₹6,240.50/gram             ||
|| Silver  : ₹   72.30/gram             ||
||======================================||
|| 📰 TOP TECH NEWS                     ||
|| 1. Python 4.0 announced...           ||
||======================================||
|| 😂 DEV JOKE                          ||
|| Why do programmers prefer dark mode? ||
|| Light attracts bugs.                 ||
||======================================||
|| 🧩 DAILY RIDDLE                      ||
|| What has hands but can't clap?       ||
||======================================||
|| 🦾 YOUR TASK FOR TODAY               ||
|| Take a 10 minute walk first.         ||
——————————————————————————————————————————
```

## Features

- Live weather for any city
- Gold & Silver spot prices in INR
- Top 3 Hacker News stories
- Daily dev joke
- Daily riddle with hidden answer
- Random health task for the day

## Setup

```bash
git clone https://github.com/Hash-PJ/Dev-Morning-Brief.git
cd Dev-Morning-Brief
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Add your OpenWeatherMap API key to `.env`:
```
WEATHER_API_KEY=your_key_here
```

## Usage

```bash
python brief.py             # defaults to Mumbai
python brief.py London INR  # any city
```

## APIs Used

| Source | API | Key needed |
|--------|-----|------------|
| Weather | OpenWeatherMap | ✅ Free |
| Gold/Silver | gold-api.com | ❌ None |
| News | Hacker News | ❌ None |
| Joke | JokeAPI | ❌ None |
| Riddle | riddles-api | ❌ None |

## License
MIT
