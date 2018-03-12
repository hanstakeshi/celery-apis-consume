from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from photos.utils import save_lastest_flickr_image

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab()),
    name="task_save_latest_flickr_image",
    ignore_result=True
)
def task_save_latest_flickr_image():
	print("Primera aplicacion GET API FLICKR")

	print("CADA MINUTO !")