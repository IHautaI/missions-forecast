from django.db import models

# Create your models here.
text_default = 'None'
int_default = -1
date_default = '01/01/2000'


class TimeFrame(models.Model):
    ant_award_date = models.DateField('Anticipated Award Date', null=True)
    ant_release_date = models.DateField('Anticipated Release Date', null=True)
    #  award_length = models.CharField('Award Length')  Needs TimeDelta package
    fiscal_year = models.DateField('Year of Action', default=date_default)


    def __str__(self):
        return 'fiscal year: {}, award date: {}, release date: {}'.format(\
                self.fiscal_year, self.ant_award_date, self.ant_release_date)

class Specialist(models.Model):
    name = models.CharField(max_length=255)
    descr = models.CharField(max_length=255, blank=True)


class Details(models.Model):
    description = models.CharField('Description', max_length=255,
                                    default=text_default)

    NAICS_code = models.CharField('NAICS Code', max_length=255)

    partner = models.CharField('Implementing Partner', max_length=255,
                               default=text_default)

    small_business_SA = models.CharField('Small Business SA', max_length=255,
                                         default=text_default)

    solicitation_number = models.CharField('Solicitation Number',
                                              max_length=255)

    BF_status_change = models.CharField('BF Status Change', max_length=255,
                                        default=text_default)


class Award(models.Model):

    # necessary info to create
    MBIO_name = models.CharField('M/B/IO name', max_length=255)
    title = models.CharField('Title', max_length=255)
    award_type = models.CharField('Award Type', max_length=255)
    amt_range = models.CharField('Award Amount Range', max_length=255)

    # relations
    specialist = models.ForeignKey(Specialist, null=True)
    timeframe = models.OneToOneField(TimeFrame, null=True)
    details = models.OneToOneField(Details, null=True)

    relevant = models.BooleanField()

    def __str__(self):
        return "{}:  {}".format(self.MBIO_name, self.title)
