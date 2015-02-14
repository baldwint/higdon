#!/usr/bin/env python3

"""\
This script generates an .ics calendar file from a Hal Higdon training
plan, tailored to a race day that you specify.

"""

from datetime import datetime, timedelta
from urllib.parse import urlparse
import dateutil.parser
import icalendar
import requests
import bs4

__version__ = '0.1.0'

DAY = timedelta(1)

def get_higdon_plan(url):
    """
    Given a URL on Hal Higdon's website, scrape out the training plan
    and return in as a daily sequence.

    """
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text)

    def gen_week(row):
        for cell in row.findAll('td')[1:]:
            yield cell.text

    def gen_all(table):
        for row in table.findAll('tr')[1:]:
            yield from gen_week(row)

    table = soup.find('table', attrs={'class': 'table-training'})
    return tuple(gen_all(table))


def make_event(what, when):
    """
    Convenience function for making an all-day event.

    """
    event = icalendar.Event()
    event.add('summary', what)
    event.add('dtstart', when)
    event.add('dtend', when + DAY)
    event.add('dtstamp', datetime.utcnow())
    return event


def make_calendar(plan, race_day):
    """
    Make a calendar for a training ``plan`` so that it ends on ``race_day``.

    ``plan`` can be any sequence of consecutive daily training
    instructions, the last one of which is the race.
    Specify ``race_day`` as a date or datetime object.

    """
    cal = icalendar.Calendar()
    for i,activity in enumerate(reversed(plan)):
        today = race_day - i*DAY
        event = make_event(activity, today)
        cal.add_component(event)
    return cal


def construct_output_filename(url, date):
    """
    A good filename should contain the plan name and the target date.

    """
    slug = urlparse(url).path.split('/')[-1]
    plan_name = slug.replace('-Training-Program', '')
    return '%s.%s.ics' % (plan_name, date)


def main(url, date_string):
    """
    Given arguments as strings, do all the parsing, scraping, and writing.

    """
    race_day = dateutil.parser.parse(date_string).date()

    plan = get_higdon_plan(url)
    cal = make_calendar(plan, race_day)

    # make a sensible output filename and write the result
    fn = construct_output_filename(url, race_day)
    with open(fn, 'wb') as f:
        f.write(cal.to_ical())

def cli():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(dest='url', metavar='PLAN',
            help='URL of the Higdon training plan to use')
    parser.add_argument(dest='race_day', metavar='RACEDAY',
            help='Date the plan should end on, written in some unambiguous format')
    args = parser.parse_args()

    main(args.url, args.race_day)

if __name__ == "__main__":
    cli()
