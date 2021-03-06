# Generated by Django 3.1.7 on 2021-03-02 14:11
from __future__ import unicode_literals

from datetime import date

from django.db import migrations, models

TEAMS = [
    {
        "name": "Arachnobots",
        "slug": "arachnobots",
        "contact": "contact@arachnobots.com",
        "description":
            "Remote-controlled internet-enabled "
            "Spider Robots.",
        "founded_date": date(2014, 10, 31),
        "tags": ["mobile", "augmented-reality"],
        "website":
            "http://frightenyourroommate.com/",
    },
    {
        "name": "Boundless Software",
        "slug": "boundless-software",
        "contact": "hello@boundless.com",
        "description": "The sky was the limit.",
        "founded_date": date(2013, 5, 15),
        "tags": ["big-data"],
        "website": "http://boundless.com/",
    },
    {
        "name": "Game Congress",
        "slug": "game-congress",
        "contact": "vote@gamecongress.com",
        "description":
            "By gamers, for gamers, of gamers.",
        "founded_date": date(2012, 7, 4),
        "tags": ["video-games"],
        "website": "http://gamecongress.com/",
    },
    {
        "name": "JamBon Software",
        "slug": "jambon-software",
        "contact": "django@jambonsw.com",
        "description":
            "JamBon Software is a consulting "
            "company that specializes in web and "
            "mobile products. They can carry out "
            "full end-to-end development of new "
            "products, or review and advise on "
            "existing projects. They also offer "
            "hands-on training in Django.",
        "founded_date": date(2013, 1, 18),
        "tags": ["django"],
        "website": "http://jambonsw.com/",
    },
    {
        "name": "Lightning Rod Consulting",
        "slug": "lightning-rod-consulting",
        "contact": "help@lightningrod.com",
        "description":
            "Channel the storm. "
            "Trouble shoot the cloud.",
        "founded_date": date(2014, 4, 1),
        "tags":
            ["ipython", "jupyter", "big-data"],
        "website": "http://lightningrod.com/",
    },
    {
        "name": "Monkey Software",
        "slug": "monkey-software",
        "contact": "shakespeare@monkeysw.com",
        "description":
            "1000 code monkeys making software.",
        "founded_date": date(2014, 12, 10),
        "tags": ["video-games"],
        "website": "http://monkeysw.com/",
    },
    {
        "name": "Simple Robots",
        "slug": "simple-robots",
        "contact": "yoshimi@simplerobots.com",
        "description":
            "Your resource to understanding "
            "computer, robots, and technology.",
        "founded_date": date(2010, 1, 2),
        "tags": ["python", "augmented-reality"],
        "website": "http://simplerobots.com/",
    },
    {
        "name": "Thingies",
        "slug": "thingies",
        "contact": "help@lightningrod.com",
        "description":
            "A marketplace for arduino, "
            "raspberry pi, and other "
            "homemade stuff.",
        "founded_date": date(2015, 4, 7),
        "tags": ["python"],
        "website": "http://buythingies.com/",
    },
]


def add_team_data(apps, schema_editor):
    Team = apps.get_model(
        'organizer', 'Team')
    Tag = apps.get_model('organizer', 'Tag')
    for team in TEAMS:
        team_object = Team.objects.create(
            name=team['name'],
            slug=team['slug'],
            contact=team['contact'],
            description=team['description'],
            founded_date=team['founded_date'],
            website=team['website'])
        for tag_slug in team['tags']:
            team_object.tags.add(
                Tag.objects.get(
                    slug=tag_slug))


def remove_team_data(apps, schema_editor):
    Team = apps.get_model(
        'organizer', 'Team')
    for team in TEAMS:
        team_object = Team.objects.get(
            slug=team['slug'])
        team_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_tag_data'),
    ]

    operations = [
        migrations.RunPython(
            add_team_data,
            remove_team_data)
    ]