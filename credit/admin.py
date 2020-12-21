from django.contrib import admin
from .models import Program, Borrower, Bid, Blacklist


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('min_credits_sum', 'max_credits_sum', 'age_min', 'age_max')


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('iin', 'birthday')
    search_fields = ('iin',)


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('program', 'data', 'sum', 'status')
    list_filter = ('status',)


@admin.register(Blacklist)
class BlacklistAdmin(admin.ModelAdmin):
    list_display = ('iin',)