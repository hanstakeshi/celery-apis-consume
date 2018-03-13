from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import requests
import json
from .models import Photo
logger = get_task_logger(__name__)

url_flickr = "https://api.flickr.com/services/feeds/photos_public.gne?format=json&nojsoncallback=1"


@periodic_task(
    run_every=(crontab()),
    name="task_save_latest_flickr_image",
    ignore_result=True
)
def task_save_latest_flickr_image():
	# traer la url y transformarla en json y conseguir el ultimo item
	url = url_flickr
	r = requests.get(url)
	page_content = r.text

	probably_json = page_content.replace("\\'", "'")
	feed = json.loads(probably_json)
	images = feed['items'][0]
	print(images, "<- images")
	if not Photo.objects.filter(link=images['link']).exists():
		photo = Photo(
			title=images['title'],
			link=images['link'],
			image_url=images['media']['m'],
			description=images['description']
			)
		photo.save()
	# Verificar que el link exista si no existe creas.
	print("CADA MINUTO !")