from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import TemplateView, UpdateView
from . import forms
from django.views.generic.base import View
from .models import Despesas
from django.urls import include, path, reverse

class DespesasListView(View):

    def get(self, request, *args, **kwargs):
        user_id = request.user.pk
        despesas = Despesas.objects.filter(user_id =user_id)
        return render(request, 'despesas/despesas.html', {'despesas': despesas})


class CreaterDespesasView(View):
    form_class =forms.DespesasForm()

    def get(self, request, *args, **kwargs):
        form = forms.DespesasForm()
        Despesas.user = self.request.user.pk
        return render(request, 'despesas/creater.html', {'form': form})

    def post(self,request):
        despesas = Despesas()
        despesas.user_id =   request.user.id
        despesas.descricao = request.POST['descricao']
        despesas.categoria = int(request.POST['categoria'])
        despesas.created_date =request.POST['created_date']
        despesas.valor = request.POST['valor']
        despesas.tipo =  request.POST.get('tipo', False)
        despesas.save()
        return HttpResponseRedirect(reverse('home'))


class HomePageView(TemplateView):


    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = forms.DespesasForm()
        user_id = request.user.pk
        despesas = Despesas.objects.filter(user_id =user_id)
        cout = despesas.count()
        return render(request, 'home.html',
                      {'despesas': despesas, 'form': form, 'total': Despesas.total(self=self, despesas=despesas),
                       'cout': cout, 'total_cartao': Despesas.total_cartao(self=self, despesas=despesas),
                       'total_dinheiro': Despesas.total_dinheiro(self=self, despesas=despesas), 'mes': 13})



class DeleteDespesasView(TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):

        try:
            mes = Despesas.objects.get(pk=self.kwargs['pk']).created_date.month
            Despesas.objects.get(pk=self.kwargs['pk']).delete()
        except:
            mes =13
        form = forms.DespesasForm()
        user_id = request.user.pk
        despesas = Despesas.objects.filter(user_id=user_id, created_date__month=mes)
        cout = despesas.count()
        return render(request, 'home.html',
                      {'despesas': despesas, 'form': form, 'total': Despesas.total(self=self, despesas=despesas),
                       'cout': cout, 'total_cartao': Despesas.total_cartao(self=self, despesas=despesas),
                       'total_dinheiro': Despesas.total_dinheiro(self=self, despesas=despesas), 'mes':mes})


class filtroDespesasView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = forms.DespesasForm()
        user_id = request.user.pk
        mes = self.request.GET.get('date', '')

        try:
            if (mes == '13'):
                despesas = Despesas.objects.filter(user_id=user_id)
            else:
                despesas = Despesas.objects.filter(user_id=user_id, created_date__month=mes)
        except:
            pass
        cout = despesas.count()
        return render(request, 'home.html',
                      {'despesas': despesas, 'form': form, 'total': Despesas.total(self=self, despesas=despesas),
                       'cout': cout, 'total_cartao': Despesas.total_cartao(self=self, despesas=despesas),
                       'total_dinheiro': Despesas.total_dinheiro(self=self, despesas=despesas), 'mes': mes})



class EditerDespesasView(TemplateView):


    def get(self, request, *args, **kwargs):
        data=dict()
        despesa = Despesas.objects.get(id=self.kwargs['pk'])
        form = forms.DespesasForm(instance=despesa)
        context = {'form': form}
        data['html_form'] = render_to_string('signup.html', context, request=self.request)
        return JsonResponse(data)


    def post(self, request, *args, **kwargs):
        despesas = Despesas.objects.get(id=self.kwargs['pk'])
        despesas.user_id =   request.user.id
        despesas.descricao = request.POST['descricao']
        despesas.categoria = int(request.POST['categoria'])
        despesas.created_date =request.POST['created_date']
        despesas.valor = request.POST['valor']
        despesas.tipo =  request.POST.get('tipo', False)
        despesas.save()
        return HttpResponseRedirect(reverse('home'))



class MaisDespesasView(TemplateView):


    def get(self, request, *args, **kwargs):
        data=dict()
        keys =[]
        x = request.GET
        for key in x.keys():
            ke = key[1:len(key)-1].split(',')
            for i in ke:
                keys.append(i[1:3].replace('"',''))
        despesa = Despesas.objects.get(id=self.kwargs['pk'])
        for mes in keys:
            print('mes',mes==despesa.created_date.month)
            if int(mes) != int(despesa.created_date.month):

                data = str(despesa.created_date.year) + '-' + mes + '-' + str(despesa.created_date.day)
                despesas = Despesas()
                despesas.user_id = request.user.id
                despesas.descricao =  despesa.descricao
                despesas.categoria =   despesa.categoria
                despesas.created_date= data
                despesas.valor = despesa.valor
                despesas.tipo = despesa.tipo
                despesas.save()



        return JsonResponse(data)