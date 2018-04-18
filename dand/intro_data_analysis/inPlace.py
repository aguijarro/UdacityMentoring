
# Source: http://www.ritchieng.com/pandas-inplace-parameter/

# Import pandas library
import pandas as pd

def main():
    # set data source
    url = 'http://bit.ly/uforeports'
    # read data
    ufo = pd.read_csv(url)
    # describe data
    print ('Shape:', ufo.shape)
    print ('Data Head')
    print (ufo.head())

    # When you drop a column without inplace parameter
    # a copy of dataframe is created.

    ufo.drop('City', axis=1).head()
    # Because you do not make changes in the ufo data
    # when you print it, you see the same columns.
    print ('Data Ufo Head')
    print (ufo.head())

    # Here you assign you drop frame (copy) to another
    # dataframe
    ufo1 = ufo.drop('City', axis=1).head()

    # If you print ufo1, you will see the new dataframe without
    # that column
    print ('Data Ufo1 Head')
    print (ufo1.head())

    # If you use the parameter inplace, all the changes happen
    # in the same dataframe.
    ufo.drop('City', axis=1, inplace=True)
    print ('Data Ufo Head')
    print (ufo.head())

if __name__ == '__main__':
    main()