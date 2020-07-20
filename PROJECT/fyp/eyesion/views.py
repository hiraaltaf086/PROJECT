from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from eyesion.forms import ImageUploadForm
from eyesion.models import ImageModel
from django.db.models import Q
from eyesion.predict import predict_class


class HomeView(generic.TemplateView):
    template_name = 'eyesion/homepage.html'


class ImageUploadView(generic.CreateView):
    """Creating malfunction reports: User Method"""
    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=False)
            form.instance.uploaded_by = self.request.user
            form.instance.prediction = 0
            form.save()
            obj=ImageModel.objects.get(Image=form.instance.Image)
            return HttpResponseRedirect(reverse_lazy('eyesion:details',
                                                     kwargs={ 'id': obj.id}))

    def get(self, request, *args, **kwargs):
        return render(request, 'eyesion/upload.html' )


class ImageDetailView(generic.TemplateView):
    template_name = 'eyesion/details.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        image = get_object_or_404(ImageModel, id=self.kwargs['id'])
        context['image']= image
        return context


class ImageListView(generic.ListView):
    context_object_name = 'images'
    template_name = 'eyesion/list.html'
    paginate_by = 7

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return ImageModel.sorted_images.all()
        return ImageModel.sorted_images.filter(uploaded_by=self.request.user)


class SearchResultsView(generic.ListView):
    template_name = 'eyesion/list.html'
    model = ImageModel
    context_object_name = 'images'

    def get_queryset(self):
        query = self.request.GET.get('q')
        images = ImageModel.objects.filter(
            Q(Image__icontains=query)
        )
        return images


class PredictView(generic.TemplateView):
    template_name = 'eyesion/details.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        image = get_object_or_404(ImageModel, id=self.kwargs['id'])
        img_url=image.Image.url
        url = img_url.replace('/', '', 1)
        res = predict_class(url)
        image.prediction = res
        image.save()
        context['image']= image
        return context
