# python3 plot_dataframe.py


import pandas
import matplotlib.pyplot as plt
import math

print(pandas.__version__)

G = 9.81
ACCELERATION_IMPACT_COEFFICIENT = 2.5
ACCELERATION_FREE_FALL_COEFFICIENT = 0.3
ACCELERATION_IMPACT = ACCELERATION_IMPACT_COEFFICIENT * G
ACCELERATION_FREE_FALL = 14.37

MIN_SQM = 1.0

MAX_SPIKES = 2

MEDIANA_INTERVAL_SIZE = 15
LOWER_BOUND_MEDIANA = 0.93
UPPER_BOUND_MEDIANA = 1.03

MIN_MEDIANA = G * 0.93;
MAX_MEDIANA = G * 1.05;

acceleration_impact_analyzed = 0

def plot_dataframe(df, title):
    global acceleration_impact_analyzed
    print('\n__dataframe: {}__'.format(title))
    # df.plot.line()
    a = df['a']
    spike = a[a >= ACCELERATION_IMPACT]
    print('\n__over ACCELERATION_IMPACT {}: {}'.format(ACCELERATION_IMPACT, spike.size))
    print('over ACCELERATION_IMPACT:\n{}'.format(spike.index))
    print('\n__under ACCELERATION_FREE_FALL {}: {}'.format(ACCELERATION_FREE_FALL, a[a <= ACCELERATION_FREE_FALL].size))
    print('{}'.format(a[a <= ACCELERATION_FREE_FALL]))


def analyze_dataframe(df, title):
    print('\n__dataframe: {}__'.format(title))
    a = df['a']

    a = a[2:]

    print('___fall evaluation___')
    mediana = a.median()
    result = False

    if a.size == 12:

        # Accelerazione impatto: 14.37
        # Lower bound: G * 0.93
        # Upper bound: G * 1.05
        # Mediana interval size: 6

        print('___free fall___')
        result_mediana = mediana <= G * 1.05 and mediana >= G * 0.93

        filtered = a[a >= G * 0.93]
        filtered = filtered[filtered <= G * 1.05]
        result_filtered = filtered.size >= 6

        result = result_mediana and result_filtered

        print('__mediana__\ncurrent: {}; result: {}; MAX_MEDIANA: {}; MIN_MEDIANA: {}'
            .format(mediana, result_mediana, G * 1.03, G * 0.93))
        print('__filter\nmin: {}; max: {}; current: {}; got: {}: result: {}'
            .format(G * 0.93, G * 1.05, a.size, filtered.size, result_filtered))
        print(filtered)
    else:
        std = a.std()

        # Accelerazione impatto: 2.5 * G
        # Lower bound: G * 0.93
        # Upper bound: G * 1.03
        # Mediana interval size: 15

        print('___shock___')
        result_mediana = True
        result_std = std >= MIN_SQM
        spike = a[a >= 2.5 * G]
        result_spikes = spike.size <= MAX_SPIKES

        filtered = a[a >= G * 0.93]
        filtered = filtered[filtered <= G * 1.03]
        result_filtered = filtered.size >= 15

        print(a.describe())
        print('__mediana: {}__'.format(mediana))
        print('__mediana__\ncurrent: {}; result: {}; MAX_MEDIANA: {}; MIN_MEDIANA: {}'
            .format(mediana, result_mediana, G * 1.03, G * 0.93))
        print('__dev standard__\nmin: {}; current: {}; result: {}'
            .format(MIN_SQM, std, result_std))
        print('__spikes__\nthreshold: {}; max: {}; current: {}; result: {}'
            .format(2.5 * G, MAX_SPIKES, spike.size, result_spikes))
        print('__filter__\nmin: {}; max: {}; current: {}; got: {}: result: {}'
            .format(G * 0.93, G * 1.03, a.size, filtered.size, result_filtered))
        result = result_mediana and result_spikes and result_filtered and result_std

    if result:
        print('_Fall detected')
    else:
        print('_No fall detected')

    sorted = a.sort_values()
    sorted.plot.line(title='sorted', use_index=False)


def analyze_dataframe_from_csv_name(csv_name):
    riposo = pandas.read_csv(csv_name, sep=';')
    analyze_dataframe(riposo, csv_name)


csv_name='cciv/i'
riposo = pandas.read_csv('{}.csv'.format(csv_name), sep=';')
analyze_dataframe(riposo, csv_name)

csv_name='cciv/ii'
riposo = pandas.read_csv('{}.csv'.format(csv_name), sep=';')
analyze_dataframe(riposo, csv_name)

csv_name='cciv/iii'
riposo = pandas.read_csv('{}.csv'.format(csv_name), sep=';')
analyze_dataframe(riposo, csv_name)

csv_name='cciv/iv'
riposo = pandas.read_csv('{}.csv'.format(csv_name), sep=';')
analyze_dataframe(riposo, csv_name)


plt.savefig('cciv/{}.png'.format('confronto'))
plt.show()
