import logging
from typing import Any

import feedparser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from dateutil import parser
from django.conf import settings
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from podcasts.models import Episode

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(fetch_and_save_episodes,
                          trigger="interval",
                          minutes=2,
                          id="Fetch and Save Episodes",
                          max_instances=1,
                          replace_existing=True
                        )
        logger.info("Fetch and Save Episodes")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="Delete Old Job Executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: Delete Old Job Executions.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")

def fetch_and_save_episodes():
    urls = [
        "https://www.hipsters.tech/feed/",
        "https://realpython.com/podcasts/rpp/feed",
        "https://talkpython.fm/episodes/rss"
    ]

    for url in urls:
        feed = feedparser.parse(url)
        podcast_name = feed.channel.title
        image = feed.channel.image["href"]

        for item in feed.entries:
            if not Episode.objects.filter(guid=item.guid).exists():
                episode = Episode(
                    title=item.title,
                    description=item.description,
                    publication_date=parser.parse(item.published),
                    link=item.link,
                    image=image,
                    podcast_name=podcast_name,
                    guid=item.guid
                )
                episode.save()
    
def delete_old_job_executions():
    """Deletes all apscheduler job execution logs older than `max_age`."""
    one_week = 604_800
    DjangoJobExecution.objects.delete_old_job_executions(max_age=one_week)
