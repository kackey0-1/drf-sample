import celery
from celery import shared_task
from celery.utils.log import get_task_logger

from feedback.emails import send_feedback_email

logger = get_task_logger(__name__)


@shared_task(name="send_feedback_email_task")
def send_feedback_email_task(email, message):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    return send_feedback_email(email, message)


@shared_task(name="sample_task")
def sample_task():
    # https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#entries
    # @celery.app(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
    # do something
    print(f'#################  executing periodic task ##################')
