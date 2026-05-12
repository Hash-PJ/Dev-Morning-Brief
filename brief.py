from datetime import datetime
from dotenv import load_dotenv
from sources.health import HealthSource
from sources.joke import JokeSource
from sources.news import NewsSource
from sources.prices import PriceSource
from sources.riddle import RiddleSource
from sources.weather import WeatherSource
import sys

load_dotenv()

W = 78
SEP = f"||{'='*79}||"

def line(text):
    """print a padded card line"""
    print(f"|| {text:<{W}}||")


def display(health, joke, news, prices, riddle, weather):
    today = datetime.now().strftime("%A %d %b %Y")
    print(f"""{'_'*(W+5)}\n|| {'DEV MORNING BRIEF':^{W}}||\n|| {today:^{W}}||\n{SEP}""")

    if weather:
        line(f"⛅ WEATHER - {weather['city'].title()}")
        line(f"{weather["temperature"]}, feels like {weather["feels like"]}")
        line(f"{weather["description"]} • {weather["humidity"]}")
        print(SEP)

    if prices:
        line("💰 GOLD & SILVER")
        for dc in prices:
            line(f" {dc.get('name'):<8}: {dc.get('price')}")
        print(SEP)

    if news:
        line("📰 TOP TECH NEWS")
        for k, v in enumerate(news, 1):
            short = v[:W-4] + '...' if len(v) > W-4 else v
            line(f" {k}. {short}")
        print(SEP)

    if joke:
        line("😂 DEV JOKE")
        for part in joke.split('\n'):
            line(f" {part}")
        print(SEP)

    if riddle:
        line("🧩 DAILY RIDDLE")
        line(f" {riddle.get("riddle", '')}")
        input(f"|| {'Press any key to know the answer...':<{W}}||")
        line(f"> {riddle.get('answer', '')}")
        print(SEP)

    if health:
        line("🦾 YOUR TASK FOR TODAY")
        line(f"{health.get('task', '')}")
        #print(SEP)
    print(f"{'—'*(W+5)}\n")

def main():
    city = " ".join(sys.argv[1:-1]).title() if len(sys.argv) > 2 else "Mumbai"
    currency = sys.argv[-1] if len(sys.argv) > 1 else "INR"
    print(city, currency)
    hd = HealthSource().fetch()
    jd = JokeSource().fetch()
    nd = NewsSource().fetch()
    pd = PriceSource().fetch(currency)
    rd = RiddleSource().fetch()
    wd = WeatherSource().fetch(city)
    display(hd, jd, nd, pd, rd, wd)


if __name__ == "__main__":
    main()
