from celery import shared_task
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from .models import AlertRule

@shared_task
def evaluate_alerts():
    alert_rules = AlertRule.objects.all()
    for rule in alert_rules:
        rule.evaluate_condition()

def setup_periodic_tasks(sender, **kwargs):
    schedule, created = CrontabSchedule.objects.get_or_create(
        minute='*/5',
        hour='*',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
    )
    PeriodicTask.objects.get_or_create(
        crontab=schedule,
        name='Evaluate Alerts Every 5 Minutes',
        task='backend.apps.alerts.tasks.evaluate_alerts',
    )
