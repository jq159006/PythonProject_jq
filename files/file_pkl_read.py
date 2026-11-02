import os
import pickle
my_pkl_file = os.path.join('..', 'data', 'rates.pkl')

with open(my_pkl_file, mode='rb') as f: #rb - read binary读取二进制
    data = pickle.load(f) #读取pickle
    rates_dict = data[0]
    weekdays_dict = data[1]
    print(rates_dict)
    print(rates_dict['USD'])
    print(type(rates_dict['USD']))
    print(weekdays_dict)