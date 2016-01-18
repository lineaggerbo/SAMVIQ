from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime
from django.core.urlresolvers import reverse
from .models import Image
from .models import Observer
from .models import Rating



def index(request):
	template = loader.get_template('evaluations/index.html')
	return HttpResponse(template.render(request))

def scene(request, scene_id):

	if(int(scene_id) == 1):
		o = Observer(name = "Observer", evaluation_started = datetime.now())
		o.save()
		request.session['observer_id'] = o.id

	print(scene_id)
	scene_reference_image = Image.objects.get(scene=scene_id, reference=True)
	scene_image_list = Image.objects.filter(scene=scene_id, reference=False)
	num_scenes = Image.objects.values_list('scene',flat = True).order_by('-scene')[:1][0]
	template = loader.get_template('evaluations/scene.html')

	if(int(scene_id) == num_scenes):
		last_scene = True
	else:
		last_scene = False

	context = {	'scene_reference_image': scene_reference_image,
				'scene_image_list': scene_image_list,
				'num_scenes': num_scenes, 
				'scene_id': scene_id ,
				'last_scene': last_scene,}
	return HttpResponse(template.render(context, request))

def rate(request, scene_id):
	scene_images = Image.objects.filter(scene=scene_id)
	observer_id = request.session['observer_id']
	num_scenes = Image.objects.values_list('scene',flat = True).order_by('-scene')[:1][0] 

	if(int(scene_id) == num_scenes):
		last_scene = True
	else:
		last_scene = False

	if request.method == 'POST':

		for image in scene_images:
			r = Rating(	observer_id=observer_id, 
						image_id=image.id, 
						date_rated=datetime.now(),
						score=request.POST.get('score-' + str(image.id), False))
			r.save()

		if(last_scene):
			return HttpResponseRedirect(reverse('evaluations:end'))
		else:
			return HttpResponseRedirect(reverse('evaluations:scene', args=(int(scene_id) + 1,)))


def end(request):
	observer_id = request.session['observer_id']
	o = Observer.objects.get(id=observer_id)
	o.evaluation_ended = datetime.now()
	o.save()

	template = loader.get_template('evaluations/end.html')
	return HttpResponse(template.render(request))