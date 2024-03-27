from datetime import datetime, timedelta

from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
import pandas as pd
from cash.models import Income, Expense
from projects.models import Status, Project
from dateutil.relativedelta import relativedelta


class IncomeExpenseChartView(views.APIView):

    def get(self, request):
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        freq = "M"
        if start_date is not None and end_date is not None:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date() + timedelta(days=1)
            end_date = end_date.strftime("%Y-%m-%d")
            date_range = pd.date_range(
                start=start_date, end=end_date, freq=freq
            ).tolist()

            list_of_income_count = list()
            list_of_expense_amount = list()
            for date in date_range:

                formatted_date = pd.Timestamp(date.year, date.month, 1)
                list_of_expense_amount.append(
                    sum(
                        [expense.amount for expense in Expense.objects.filter(
                            date__gte=formatted_date,
                            date__lt=formatted_date + relativedelta(months=1)
                        )]
                    )
                )
                list_of_income_count.append(
                    sum(
                        [income.amount for income in Income.objects.filter(
                            date__gte=formatted_date,
                            date__lt=formatted_date + relativedelta(months=1)
                        )]
                    )
                )

            return Response({
                "list_of_expense_amount": list_of_expense_amount,
                "list_of_income_count": list_of_income_count,
                "labels": date_range,
            }, status=status.HTTP_200_OK)
        return Response({
            "list_of_expense_amount": [],
            "list_of_income_count": [],
            "labels": [],
        }, status=status.HTTP_200_OK)


class ProjectChartView(views.APIView):

    def get(self, request):
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        freq = "M"
        response = list()
        date_range = list()
        if start_date is not None and end_date is not None:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date() + timedelta(days=1)
            end_date = end_date.strftime("%Y-%m-%d")
            date_range = pd.date_range(
                start=start_date, end=end_date, freq=freq
            ).tolist()
            statuses = Status.objects.all()

            for status in statuses:
                data = list()

                for date in date_range:
                    formatted_date = pd.Timestamp(date.year, date.month, 1)
                    if status.slug == 'finished':
                        projects_count = Project.objects.filter(
                                status__pk=status.pk,
                                end_at__gte=formatted_date,
                                end_at__lt=formatted_date + relativedelta(months=1)
                            ).count()
                    else:
                        projects_count = Project.objects.filter(
                            status__pk=status.pk,
                            end_at__lt=formatted_date + relativedelta(months=1)
                        ).count()
                    data.append(projects_count)

                response.append({
                    "slug": status.slug,
                    "name": status.name,
                    "color": status.color,
                    "data": data
                })
            data = list()
            for date in date_range:
                formatted_date = pd.Timestamp(date.year, date.month, 1)
                projects_count = Project.objects.filter(
                    start_at__gte=formatted_date,
                    start_at__lt=formatted_date + relativedelta(months=1)
                ).count()

                data.append(projects_count)
            response.append({
                "slug": 'new',
                "name": 'Новые проекты',
                "color": "#25D366",
                "data": data
            })
        return Response({
            "charts": response,
            "labels": date_range,
        }, status=200)

