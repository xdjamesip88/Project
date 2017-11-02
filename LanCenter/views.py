from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.views.generic.detail import DetailView

from django.shortcuts import render_to_response

from django.http import HttpResponse
from .forms import stockdetalleFormSet
from django.db import transaction
from .models import cuenta, stockdetalle

class Inicio(TemplateView):

    template_name = 'inicio.html'

    def get(self, request, *args, **kwargs):
        context = {"mensaje":"Holas!!!"}
        return self.render_to_response(context)


class cuentaList(ListView):
    model = cuenta

class cuentaDetail(DetailView):
    model = cuenta

    def get_context_data(self, **kwargs):
        data = super(cuentaDetail, self).get_context_data(**kwargs)
        if self.request.POST:
            data['stockdetalles'] = stockdetalleFormSet(self.request.POST,instance=self.object)
        else:
            data['stockdetalles'] = stockdetalleFormSet(instance=self.object)
        return data

class cuentaCreation(CreateView):
    model = cuenta
    success_url = reverse_lazy('cuentalist')
    def get_context_data(self, **kwargs):
        data = super(cuentaCreation, self).get_context_data(**kwargs)
        if self.request.POST:
            data['stockdetalles'] = stockdetalleFormSet(self.request.POST,instance=self.object)
        else:
            data['stockdetalles'] = stockdetalleFormSet(instance=self.object)
        return data

class cuentaUpdate(UpdateView):
    model = cuenta
    success_url = reverse_lazy('cuentalist')

class cuentaDelete(DeleteView):
    model = cuenta
    success_url = reverse_lazy('cuentalist')




#
# class stockList(ListView):
#     model = stock
#
# class stockDetail(DetailView):
#     model = stock
#
# class stockCreate(CreateView):
#     model = stock
#     success_url = reverse_lazy('inicio')
#     fields = ['usuario','fecha','bloquear']
#
#     def get_context_data(self, **kwargs):
#         data = super(stockCreate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['stockdetalles'] = stockdetalleFormSet(self.request.POST)
#         else:
#             data['stockdetalles'] = stockdetalleFormSet()
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         stockdetalles = context['stockdetalles']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if stockdetalles.is_valid():
#                 stockdetalles.instance = self.object
#                 stockdetalles.save()
#         return super(stockCreate, self).form_valid(form)
#
# class stockUpdate(UpdateView):
#     model = stock
#     success_url = reverse_lazy('inicio')
#     fields = ['usuario', 'fecha', 'bloquear']
#
#     def get_context_data(self, **kwargs):
#         data = super(stockUpdate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['stockdetalles'] = stockdetalleFormSet(self.request.POST,instance=self.object)
#         else:
#             data['stockdetalles'] = stockdetalleFormSet(instance=self.object)
#         return data
#
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         stockdetalles = context['stockdetalles']
#         with transaction.atomic():
#             self.object = form.save()
#
#             if stockdetalles.is_valid():
#                 stockdetalles.instance = self.object
#                 stockdetalles.save()
#         return super(stockUpdate, self).form_valid(form)
#
# class stockDelete(DeleteView):
#     model = stock
#     success_url = reverse_lazy('liststock')
#
#
# class stockdetalleCreate(CreateView):
#     model = stock
#     fields = ['usuario', 'fecha', 'bloquear']
#
#
#
# class stockdetalleUpdate(CreateView):
#     model = stock
#     fields = ['usuario', 'fecha', 'bloquear']