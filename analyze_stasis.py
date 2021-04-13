20210402# python3 analyze_stasis.py

import pandas
import matplotlib.pyplot as plt
import math


def analyze_dataframe(df, title, G, ACCELERATION_IMPACT, ACCELERATION_FREE_FALL, MIN_SQM, MAX_SPIKES, MEDIANA_INTERVAL_SIZE, LOWER_BOUND_MEDIANA, UPPER_BOUND_MEDIANA):
    print('\n__dataframe: {}__'.format(title))
    a = df['a']
    print('___a: {}__'.format(a.size))
    if a.size == 36:
        a = a[11:]
    mediana = a.median()
    std = a.std()

    print('___fall evaluation___')
    result_mediana = True
    result_std = std >= MIN_SQM
    spike = a[a > ACCELERATION_IMPACT]
    result_spikes = spike.size <= MAX_SPIKES

    filtered = a[a >= LOWER_BOUND_MEDIANA * mediana]
    filtered = filtered[filtered <= UPPER_BOUND_MEDIANA * mediana]
    result_filtered = filtered.size >= MEDIANA_INTERVAL_SIZE

    if result_mediana and result_spikes and result_filtered and result_std:
        print(a.describe())
        print('__mediana: {}__'.format(mediana))
        print('__mediana__\ncurrent: {}; result: {}'.format(mediana, result_mediana))
        print('__dev standard__\nmin: {}; current: {}; result: {}'.format(MIN_SQM, std, result_std))
        print('__spikes__\nthreshold: {}; max: {}; current: {}; result: {}'.format(ACCELERATION_IMPACT, MAX_SPIKES, spike.size, result_spikes))
        print('__filter__\nmin: {}; max: {}; current: {}; got: {}: result: {}'.format(LOWER_BOUND_MEDIANA * mediana, UPPER_BOUND_MEDIANA * mediana, a.size, filtered.size, result_filtered))
        print('__Fall detected')
    else:
        print('__No fall detected')


def set_parameters(csv_path, csv_name, G, ACCELERATION_IMPACT_COEFFICIENT, ACCELERATION_FREE_FALL_COEFFICIENT, MIN_SQM, MAX_SPIKES, MEDIANA_INTERVAL_SIZE, LOWER_BOUND_MEDIANA, UPPER_BOUND_MEDIANA):
    ACCELERATION_IMPACT = ACCELERATION_IMPACT_COEFFICIENT * G
    ACCELERATION_FREE_FALL = ACCELERATION_FREE_FALL_COEFFICIENT * G

    acceleration_impact_analyzed = 0

    print('_G: {}'.format(G))
    print('_ACCELERATION_IMPACT: {} ({})'.format(ACCELERATION_IMPACT, ACCELERATION_IMPACT_COEFFICIENT))
    print('_ACCELERATION_FREE_FALL: {} ({})'.format(ACCELERATION_FREE_FALL, ACCELERATION_FREE_FALL_COEFFICIENT))
    print('_MIN_SQM: {}'.format(MIN_SQM))
    print('_MAX_SPIKES: {}'.format(MAX_SPIKES))
    print('_MEDIANA_INTERVAL_SIZE: {}'.format(MEDIANA_INTERVAL_SIZE))
    print('_LOWER_BOUND_MEDIANA: {}'.format(LOWER_BOUND_MEDIANA))
    print('_UPPER_BOUND_MEDIANA: {}'.format(UPPER_BOUND_MEDIANA))
    stasi = pandas.read_csv('{}/{}.csv'.format(csv_path, csv_name), sep=';')
    analyze_dataframe(stasi, csv_name, G, ACCELERATION_IMPACT, ACCELERATION_FREE_FALL, MIN_SQM, MAX_SPIKES, MEDIANA_INTERVAL_SIZE, LOWER_BOUND_MEDIANA, UPPER_BOUND_MEDIANA)


for i in range(1):
    csv_path='ato-2/fall_20210406/3G'
    csv_name='fall_20210406_stasi_{}'.format(i+1)

    print("\n==================== NEW RUN (1) ====================\n")
    set_parameters(csv_path, csv_name, 9.81, 3, 0.3, 1.0, 2, 17, 0.89, 1.13)
    print("\n==================== NEW RUN (2) ====================\n")
    set_parameters(csv_path, csv_name, 9.81, 3, 0.3, 1.0, 2, 20, 0.89, 1.13)
    print("\n==================== NEW RUN (3) ====================\n")
    set_parameters(csv_path, csv_name, 9.81, 3, 0.3, 1.0, 2, 17, 0.93, 1.03)
    print("\n==================== NEW RUN (4) ====================\n")
    set_parameters(csv_path, csv_name, 9.81, 3, 0.3, 1.0, 2, 20, 0.93, 1.03)
    print("\n==================== NEW RUN (5) ====================\n")
    set_parameters(csv_path, csv_name, 9.81, 2.5, 0.3, 1.0, 2, 17, 0.89, 1.13)
    print("\n==================== NEW RUN (6) ====================\n")
    set_parameters(csv_path, csv_name, 9.81, 2.5, 0.3, 1.0, 2, 20, 0.89, 1.13)
    print("\n==================== NEW RUN (7) ====================\n")
    set_parameters(csv_path, csv_name, 9.81, 2.5, 0.3, 1.0, 2, 17, 0.93, 1.03)
    print("\n==================== NEW RUN (8) ====================\n")
    set_parameters(csv_path, csv_name, 9.81, 2.5, 0.3, 1.0, 2, 20, 0.93, 1.03)
    print("\n==================== END RUN ====================\n")



# size: 158075
#
# __over ACCELERATION_IMPACT 24.525000000000002: 7
# over ACCELERATION_IMPACT:
# 4533     29.790
# 5030     25.707
# 13125    35.622
# 17126    45.129
# 17127    43.841
# 18955    26.265
# 30054    25.899
# Name: a, dtype: float64
#
# __under ACCELERATION_FREE_FALL 2.943: 3
# 16140    2.923
# 18921    1.805
# 30055    2.118
