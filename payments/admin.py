from django.contrib import admin

from .models import PaymentLog, Worker, Job, JobFolder


@admin.register(PaymentLog)
class PaymentLogAdmin(admin.ModelAdmin):
    list_display = (
        'invoice',
        'amount',
        'created_at',
    )
    list_filter = ('invoice__student__semester',)
    search_fields = (
        'invoice__student__user__first_name',
        'invoice__student__user__last_name',
        'invoice__student__user__username',
    )
    autocomplete_fields = ('invoice',)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'payment_preference',
        'notes',
    )
    list_display_links = (
        'pk',
        'user',
    )
    list_filter = ('payment_preference',)
    search_fields = (
        'user__first_name',
        'user__last_name',
        'paypal_username',
        'venmo_handle',
        'zelle_info',
    )
    list_filter = ('payment_preference',)
    autocomplete_fields = ('user',)


@admin.register(JobFolder)
class JobFolderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_display_links = (
        'pk',
        'name',
    )
    search_fields = ('name',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'folder',
        'name',
        'status',
        'due_date',
        'assignee',
        'spades_bounty',
        'usd_bounty',
    )
    list_display_links = (
        'pk',
        'folder',
        'name',
    )
    search_fields = (
        'name',
        'description',
    )
    list_filter = (
        'folder',
        'status',
    )
