from django.contrib import admin

from .models import Award

class AwardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['MBIO_name', 'title', 'AA_specialist', 'award_type',
                            'amt_range']}),
        ('details', {'fields': ['description', 'small_business_SA',
                                'partner', 'solicitation_number',
                                'BF_status_change', 'NAICS_code'],
                                'classes':['collapse']} )
    ]

    list_display = ('MBIO_name', 'title', 'award_type',)
    list_filter = ['MBIO_name', 'award_type', 'amt_range']


admin.site.register(Award, AwardAdmin)
