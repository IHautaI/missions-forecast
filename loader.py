from forecast.models import Award, TimeFrame, Details, Specialist

import numpy as np
import pandas as pd


# hacked together way to load the .csv - it's a bit of a mess.

def checker(dates_list):
    final = [item if len(item) >= 2 else '0' + item for item in dates_list]
    return [final[2], final[0], final[1]]


def load_data():
    data = pd.read_csv('missionsforecast.csv', encoding='windows-1252', header=1)

    for idx in data.index:

        row = data.xs(idx)
        if not isinstance(row.loc['Anticipated_Award_Date'], float):
            row.loc['Anticipated_Award_Date'] = '20' + '-'.join(checker(row['Anticipated_Award_Date'].split('/')))
        else:
            row.loc['Anticipated_Award_Date'] = None

        if not isinstance(row.loc['Anticipated_Solicitation_Release_Date'], float):
            row.loc['Anticipated_Solicitation_Release_Date'] = '20' + '-'.join(checker(row['Anticipated_Solicitation_Release_Date'].split('/')))
        else:
            row.loc['Anticipated_Solicitation_Release_Date'] = None


        if not isinstance(row.loc['Fiscal_Year_of_Action'], float):
            row.loc['Fiscal_Year_of_Action'] = str(row['Fiscal_Year_of_Action']) + '-01-01'
        else:
            row.loc['Fiscal_Year_of_Action'] = None


        TF = {'ant_award_date': row.loc['Anticipated_Award_Date'],\
              'ant_release_date': row.loc[\
              'Anticipated_Solicitation_Release_Date'],\
              'fiscal_year': row.loc['Fiscal_Year_of_Action']}

        DTS = {'description': row.loc['Award_Description'],\
               'NAICS_code': row.loc['NAICS_Code'],\
               'partner': row.loc['Implementing_Partner'],\
               'small_business_SA': row.loc['Small_Business_SA'],\
               'solicitation_number': row.loc['Solicitation_Number'],\
               'BF_status_change': row.loc['Business_Forecast_Status_Change']}


        for item in DTS:
            if isinstance(DTS[item], float):
                if np.isnan(DTS[item]):
                    DTS[item] = None

        if DTS['NAICS_code'] is not None:
            DTS['NAICS_code'] = int(DTS['NAICS_code'])

        DTS = {item:val for item, val in DTS.items() if val is not None}

        TF = {item:val for item,val in TF.items() if val is not None}


        SP = {'name': row.loc['A&A Specialist']}

        AW = {'MBIO_name': row.loc['MBIO'], \
              'title': row.loc['Award_Title'],\
              'award_type': row.loc['Award_Type'], \
              'amt_range': row.loc['Total_Estimated_Cost']}


        time = TimeFrame.objects.get(id=TimeFrame.objects.create(**TF).id)
        deets = Details.objects.get(id=Details.objects.create(**DTS).id)

        sid = None

        if not Specialist.objects.filter(name=SP['name']).exists():
            sid = Specialist.objects.create(**SP).id
        else:
            sid = Specialist.objects.get(name=SP['name']).id

        special = Specialist.objects.get(id=sid)

        aw = Award.objects.get(id=Award.objects.create(**AW).id)
        aw.timeframe = time
        aw.details = deets
        aw.specialist = special
        aw.save()
