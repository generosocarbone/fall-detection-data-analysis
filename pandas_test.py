# python3 pandas_test.py
# idea:  in base a quanto e come varia il fall index possiamo stabilire se si è verificata una caduta
# Se c'è un picco che resta più o meno costante allora è possibile assumere che si sia verificata una caduta
# Se c'è un picco che non resta costante anzi tende a decrescere, allora è possibile assumere che la
# caduta non si sia verificata.
# Una cosa che ho notato è che l'accelerometro non è costantente nel fornire i valori, ma tende ad accelerare
# all'aumentare delle variazioni di accelerazione. Sembra valido per il mio samsung, non so se è un discorso
# comune a tutti i dispositivi.

# Fare un'implementazione per smartwatch in grado di fare dei run di misurazione molto lunghi e vedere come
# si comporta il Fall Index nel tempo



import pandas
import matplotlib.pyplot as plt
import math

print(pandas.__version__)

G = 9.81
ACCELERATION_IMPACT_COEFFICIENT = 2.5
ACCELERATION_FREE_FALL_COEFFICIENT = 0.3
ACCELERATION_IMPACT = ACCELERATION_IMPACT_COEFFICIENT * G
ACCELERATION_FREE_FALL = ACCELERATION_FREE_FALL_COEFFICIENT * G

MIN_SQM = 1.0

MAX_SPIKES = 2

MEDIANA_INTERVAL_SIZE = 17
LOWER_BOUND_MEDIANA = 0.93
UPPER_BOUND_MEDIANA = 1.03

acceleration_impact_analyzed = 0

print('_G: {}'.format(G))
print('_ACCELERATION_IMPACT: {} ({})'.format(ACCELERATION_IMPACT, ACCELERATION_IMPACT_COEFFICIENT))
print('_ACCELERATION_FREE_FALL: {} ({})'.format(ACCELERATION_FREE_FALL, ACCELERATION_FREE_FALL_COEFFICIENT))
print('_MIN_SQM: {}'.format(MIN_SQM))
print('_MAX_SPIKES: {}'.format(MAX_SPIKES))
print('_MEDIANA_INTERVAL_SIZE: {}'.format(MEDIANA_INTERVAL_SIZE))
print('_LOWER_BOUND_MEDIANA: {}'.format(LOWER_BOUND_MEDIANA))
print('_UPPER_BOUND_MEDIANA: {}'.format(UPPER_BOUND_MEDIANA))

def analyze_dataframe_for_fall_index(df, title):
    global acceleration_impact_analyzed
    print('\n__dataframe: {}__'.format(title))
    df.plot.line()
    a = df['a']
    spike = a[a >= ACCELERATION_IMPACT]
    print('\n__over ACCELERATION_IMPACT {}: {}'.format(ACCELERATION_IMPACT, spike.size))
    print('over ACCELERATION_IMPACT:\n{}'.format(spike.index))
    print('\n__under ACCELERATION_FREE_FALL {}: {}'.format(ACCELERATION_FREE_FALL, a[a <= ACCELERATION_FREE_FALL].size))
    print('{}'.format(a[a <= ACCELERATION_FREE_FALL]))

    last = 0
    for j in range(spike.index.size):
        i = spike.index[j]
        if last == 0:
            last = i;
        elif last + 25 < i:
            last = i
        else:
            continue

        acceleration_impact_analyzed = acceleration_impact_analyzed + 1
        subset = df[i - 10:i + 26]
        csv_name = 'davide/fall_20210413/subset_{}_index.csv'.format(i)
        subset.to_csv(csv_name, sep = ';', index = False)
        analyze_dataframe_from_csv_name('davide/fall_20210413/subset_{}_index.csv'.format(i))

    print('___acceleration_impact_analyzed: {}'.format(acceleration_impact_analyzed))


def calculate_index(df):
    if df.size <= 20:
        print('not enough samples')

    x = df['x']
    y = df['y']
    z = df['z']

    for i in range(19, x.size, 1):
        sum_x = 0
        sum_y = 0
        sum_z = 0
        for j in range(i, i-19, -1):
            sum_x = sum_x + math.pow(x[j]-x[j-1], 2)
            sum_y = sum_y + math.pow(y[j]-y[j-1], 2)
            sum_z = sum_z + math.pow(z[j]-z[j-1], 2)

        index = math.pow(sum_x + sum_y + sum_z, 1/2)
        print("index: {};{};{};{}".format(x[i], y[i], z[i], index))
        df['index'][i] = index


def analyze_dataframe(df, title):
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
        print('_Fall detected')
    else:
        print('_No fall detected')

    df.plot.line(title=title)
    plt.savefig('{}.png'.format(title))



def analyze_dataframe_from_csv_name(csv_name):
    riposo = pandas.read_csv(csv_name, sep=';')
    analyze_dataframe(riposo, csv_name)



csv_name='fall_20210413.shock'
riposo = pandas.read_csv('davide/fall_20210413/{}.csv'.format(csv_name), sep=';')
analyze_dataframe_for_fall_index(riposo, csv_name)
# analyze_dataframe(riposo, csv_name)


print("\n==================== NEW RUN ====================\n")


G = 9.81
ACCELERATION_IMPACT_COEFFICIENT = 2.5
ACCELERATION_FREE_FALL_COEFFICIENT = 0.3
ACCELERATION_IMPACT = ACCELERATION_IMPACT_COEFFICIENT * G
ACCELERATION_FREE_FALL = ACCELERATION_FREE_FALL_COEFFICIENT * G

MIN_SQM = 1.0

MAX_SPIKES = 2

MEDIANA_INTERVAL_SIZE = 17
LOWER_BOUND_MEDIANA = 0.93
UPPER_BOUND_MEDIANA = 1.03

acceleration_impact_analyzed = 0

print('_G: {}'.format(G))
print('_ACCELERATION_IMPACT: {} ({})'.format(ACCELERATION_IMPACT, ACCELERATION_IMPACT_COEFFICIENT))
print('_ACCELERATION_FREE_FALL: {} ({})'.format(ACCELERATION_FREE_FALL, ACCELERATION_FREE_FALL_COEFFICIENT))
print('_MIN_SQM: {}'.format(MIN_SQM))
print('_MAX_SPIKES: {}'.format(MAX_SPIKES))
print('_MEDIANA_INTERVAL_SIZE: {}'.format(MEDIANA_INTERVAL_SIZE))
print('_LOWER_BOUND_MEDIANA: {}'.format(LOWER_BOUND_MEDIANA))
print('_UPPER_BOUND_MEDIANA: {}'.format(UPPER_BOUND_MEDIANA))

riposo = pandas.read_csv('davide/fall_20210413/{}.csv'.format(csv_name), sep=';')
# analyze_dataframe_for_fall_index(riposo, csv_name)
analyze_dataframe(riposo, csv_name)
# plt.show()

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
