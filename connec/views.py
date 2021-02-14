from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator
from .main_classes import ObjectPostgres, ObjectMySQL



# Create your views here.

class Index(View):
    template_name = 'index.html'
    def get(self, request):
        if request.session.get('result_postgres', None):
            del request.session['result_postgres']
            del request.session['result_postgres_head']



        return render(request, self.template_name)


class Subd_postgres(View):
    from .forms import FormPostgres
    template_name = 'postgres.html'
    form_class = FormPostgres

    def get(self, request, *args, **kwargs):
        form = self.form_class
        result_postgres = request.session.get('result_postgres', None)
        result_postgres_head = request.session.get('result_postgres_head', None)

        if result_postgres:
            page_number = request.GET.get('page')
            paginator = Paginator(result_postgres, 20)
            page_obj = paginator.get_page(page_number)
            return render(request, self.template_name, {'form': form,
                                                        'result_postgres_head': result_postgres_head,
                                                        'page_obj': page_obj
                                                        })

        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            db_name = form.cleaned_data['database']
            db_user = form.cleaned_data['user']
            db_password = form.cleaned_data['password']
            db_host = form.cleaned_data['host']
            db_port = form.cleaned_data['port']
            db_table = form.cleaned_data['table']

            connect = ObjectPostgres(db_name, db_user, db_password, db_host,
                                    db_port)
            if not (connect.connection):
                msg = 'Соединение не установлено! Проверьте правильность ' \
                      'введенных данных '
                return render(request, self.template_name, {'form': form,
                                                            'msg': msg})

            query = "SELECT * FROM {}".format(db_table)
            result = connect.execute_read_query(query)
            if not(result):
                msg = 'Выполнение запроса не выполнено! Проверьте правильность' \
                      ' наименования таблицы'
                return render(request, self.template_name, {'form': form,
                                                            'msg': msg})
            queryHead = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS " \
                        "WHERE TABLE_NAME= '{}'".format(db_table)
            resultHead = connect.execute_read_query(queryHead)

            request.session['result_postgres'] = result
            request.session['result_postgres_head'] = resultHead
            return HttpResponseRedirect('subd_postgresql')
        return render(request, self.template_name,
                      {'form': form})


class Subd_mysql(View):
    from .forms import FormMySQL
    template_name = 'mysql.html'
    form_class = FormMySQL

    def get(self, request, *args, **kwargs):
        form = self.form_class
        result_mysql = request.session.get('result_mysql', None)
        result_mysql_head = request.session.get('result_mysql_head', None)

        if result_mysql:
            page_number = request.GET.get('page')
            paginator = Paginator(result_mysql, 20)
            page_obj = paginator.get_page(page_number)
            return render(request, self.template_name, {'form': form,
                                                        'result_mysql_head': result_mysql_head,
                                                        'page_obj': page_obj
                                                        })

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            db_name = form.cleaned_data['database']
            db_user = form.cleaned_data['user']
            db_password = form.cleaned_data['password']
            db_host = form.cleaned_data['host']
            db_port = form.cleaned_data['port']
            db_table = form.cleaned_data['table']

            connect = ObjectMySQL(db_name, db_user, db_password, db_host,
                                    db_port)
            if not (connect.connection):
                msg = 'Соединение не установлено! Проверьте правильность ' \
                      'введенных данных '
                return render(request, self.template_name, {'form': form,
                                                            'msg': msg})

            query = "SELECT * FROM {}".format(db_table)
            result = connect.execute_read_query(query)
            if not(result):
                msg = 'Выполнение запроса не выполнено! Проверьте правильность' \
                      ' наименования таблицы'
                return render(request, self.template_name, {'form': form,
                                                            'msg': msg})
            queryHead = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS " \
                        "WHERE TABLE_SCHEMA= '{}' AND TABLE_NAME= '{}'" \
                        "".format(db_name, db_table)
            resultHead = connect.execute_read_query(queryHead)

            request.session['result_mysql'] = result
            request.session['result_mysql_head'] = resultHead
            return HttpResponseRedirect('subd_mysql')
        return render(request, self.template_name,
                      {'form': form})








