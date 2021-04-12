import pandas
import matplotlib.pyplot as plt

print(pandas.__version__)

G = 9.81
MAX_A = 1.95 * G
MIN_A = 2.0

MIN_MEDIANA = G * 0.95
MAX_MEDIANA = G * 1.03

MIN_SQM = 2.0

MAX_SPIKES = 2

MIN_FILTERED = 20
MIN_FILTER = G * 0.94
MAX_FILTER = G * 1.05

# mediana >= MIN_MEDIANA && mediana <= MAX_MEDIANA
# sqm >= MIN_SQM
# spikes <= MAX_SPIKES
# filtered >= MIN_FILTERED

def analyze_dataframe(df, title):
    print('\n__dataframe: {}__'.format(title))
    a = df['a']
    mediana = a.median()
    std = a.std()
    print('mediana\t {}'.format(mediana))
    print(a.describe())

    print('___fall evaluation___')
    result_mediana = mediana >= MIN_MEDIANA and mediana <= MAX_MEDIANA
    print('__mediana__\nmin: {}; max: {}; current: {}; result: {}'.format(MIN_MEDIANA, MAX_MEDIANA, mediana, result_mediana))

    result_std = std >= MIN_SQM
    print('__dev standard__\nmin: {}; current: {}; result: {}'.format(MIN_SQM, std, result_std))

    spike = a[a > MAX_A]
    result_spikes = spike.size <= MAX_SPIKES
    print('__spikes__\nthreshold: {}; max: {}; current: {}; result: {}'.format(MAX_A, MAX_SPIKES, spike.size, result_spikes))

    filtered = a[a >= MIN_FILTER]
    filtered = filtered[filtered <= MAX_FILTER]
    result_filtered = filtered.size >= MIN_FILTERED
    print('__filter__\nmin: {}; max: {}; current: {}; got: {}: result: {}'.format(MIN_FILTER, MAX_FILTER, a.size, filtered.size, result_filtered))

    if result_mediana and result_spikes and result_filtered and result_std:
        print('Fall detected')
    else:
        print('No fall detected')
    df.plot.line()


csv_name='mediana-due.csv'
riposo = pandas.read_csv(csv_name, sep=';')
analyze_dataframe(riposo, csv_name)

plt.show()
