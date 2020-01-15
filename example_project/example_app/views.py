from django.contrib.messages import success
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _

from .forms import FileForm
from .models import File


def index(request):
    form = FileForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        success(request, _('You successfully uploaded the file!'))

        return redirect(request.path_info)

    return render(request, 'index.html', {
        'form': form,
        'last_3_files': File.objects.order_by('-id')[:3]
    })
