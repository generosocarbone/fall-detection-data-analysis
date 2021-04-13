# python3 extract_stasis.py

import pandas
import matplotlib.pyplot as plt
import math


G = 9.81
ACCELERATION_IMPACT_COEFFICIENT = 2.5
ACCELERATION_FREE_FALL_COEFFICIENT = 0.3
ACCELERATION_IMPACT = ACCELERATION_IMPACT_COEFFICIENT * G
ACCELERATION_FREE_FALL = ACCELERATION_FREE_FALL_COEFFICIENT * G

MIN_SQM = 1.0

MAX_SPIKES = 2

MEDIANA_INTERVAL_SIZE = 17
LOWER_BOUND_MEDIANA = 0.89
UPPER_BOUND_MEDIANA = 1.13

acceleration_impact_analyzed = 0

print('_G: {}'.format(G))
print('_ACCELERATION_IMPACT: {} ({})'.format(ACCELERATION_IMPACT, ACCELERATION_IMPACT_COEFFICIENT))
print('_ACCELERATION_FREE_FALL: {} ({})'.format(ACCELERATION_FREE_FALL, ACCELERATION_FREE_FALL_COEFFICIENT))
print('_MIN_SQM: {}'.format(MIN_SQM))
print('_MAX_SPIKES: {}'.format(MAX_SPIKES))
print('_MEDIANA_INTERVAL_SIZE: {}'.format(MEDIANA_INTERVAL_SIZE))
print('_LOWER_BOUND_MEDIANA: {}'.format(LOWER_BOUND_MEDIANA))
print('_UPPER_BOUND_MEDIANA: {}'.format(UPPER_BOUND_MEDIANA))

def extract_stasis(df, csv_name, csv_path):
    global acceleration_impact_analyzed
    print('\n__dataframe: {}__'.format(csv_name))
    # df.plot.line()
    a = df['a']
    spike = a[a >= ACCELERATION_IMPACT]
    print('\n__over ACCELERATION_IMPACT {}: {}'.format(ACCELERATION_IMPACT, spike.size))

    last = 0
    count = 1
    for j in range(spike.index.size):
        i = spike.index[j]
        if last == 0:
            last = i;
        elif last + 25 < i:
            last = i
        else:
            continue

        acceleration_impact_analyzed = acceleration_impact_analyzed + 1
        subset = df[i+1 : i + 26]
        subset_csv_name = '{}/{}_stasi_{}.csv'.format(csv_path, csv_name, count)
        print(subset_csv_name)
        subset.to_csv(subset_csv_name, sep = ';', index = False)
        count = count + 1

    print('___acceleration_impact_analyzed: {}'.format(acceleration_impact_analyzed))


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
    extract_stasis(stasi, csv_name, csv_path)


csv_path='shock-2/TP'
csv_name='fall_1616171234781'
set_parameters(csv_path, csv_name, 9.81, 2.5, 0.3, 1.0, 2, 17, 0.89, 1.13)
