from arcutils import will_be_deleted_with
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from hotline.perms import permissions
from hotline.species.models import Category, Severity, Species


class SpeciesList(ListView):
    model = Species


class SpeciesCreateView(SuccessMessageMixin, CreateView):
    model = Species
    fields = ['name', 'scientific_name', 'remedy', 'resources', 'is_confidential', 'category', 'severity']
    success_message = "Species created successfully."
    template_name_suffix = '_detail_form'

    def get_success_url(self):
        return reverse("species-list")


class SpeciesDetailView(SuccessMessageMixin, UpdateView):
    model = Species
    fields = ['name', 'scientific_name', 'remedy', 'resources', 'is_confidential', 'category', 'severity']
    success_message = "Species updated successfully."
    template_name_suffix = '_detail_form'

    def get_success_url(self):
        success_url = self.request.get_full_path()
        return success_url


class SpeciesDeleteView(SuccessMessageMixin, DeleteView):
    model = Species
    success_message = "Species deleted successfully."
    success_url = reverse_lazy('species_list')

    template_name = "delete.html"
    template_name_suffix = ""

    def get_context_data(self, **kwargs):
        obj = super(DeleteView, self).get_object()
        context = super(SpeciesDeleteView, self).get_context_data(**kwargs)
        context['will_be_deleted_with'] = will_be_deleted_with(obj)

        return context


class CategoryList(ListView):
    model = Category


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    fields = ['name', 'icon']
    template_name_suffix = '_detail_form'
    success_message = "Category created successfully."

    def get_success_url(self):
        return reverse("categories-list")


class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Category
    success_message = "Category deleted successfully."
    success_url = reverse_lazy('category_list')

    template_name = "delete.html"
    template_name_suffix = ""

    def get_context_data(self, **kwargs):
        obj = super(DeleteView, self).get_object()
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['will_be_deleted_with'] = will_be_deleted_with(obj)

        return context


class CategoryDetailView(SuccessMessageMixin, UpdateView):
    model = Category
    fields = ['name', 'icon']
    success_message = "Category updated successfully."
    template_name_suffix = '_detail_form'

    def get_success_url(self):
        return reverse("categories-list")


class SeverityList(ListView):
    model = Severity


class SeverityCreateView(SuccessMessageMixin, CreateView):
    model = Severity
    fields = ['name', 'color']
    success_message = "Severity created successfully."
    template_name_suffix = '_detail_form'

    def get_success_url(self):
        return reverse("severities-list")


class SeverityDeleteView(SuccessMessageMixin, DeleteView):
    model = Severity
    success_url = reverse_lazy('severities-list')
    success_message = "Severity deleted successfully."

    template_name = "delete.html"
    template_name_suffix = ""

    def get_context_data(self, **kwargs):
        obj = super(DeleteView, self).get_object()
        context = super(SeverityDeleteView, self).get_context_data(**kwargs)
        context['will_be_deleted_with'] = will_be_deleted_with(obj)

        return context


class SeverityDetailView(SuccessMessageMixin, UpdateView):
    model = Severity
    fields = ['name', 'color']
    success_message = "Severity updated successfully."
    template_name_suffix = '_detail_form'

    def get_success_url(self):
        return reverse("severities-list")


@permissions.is_staff
def admin_panel(request):
    return render(request, 'species/admin_panel.html')
