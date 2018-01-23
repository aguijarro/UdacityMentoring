import pandas as pd


def main():
    # load data
    df = pd.read_csv("data/tmdb-movies.csv")
    # display dataset
    print("*************")
    print list(df)

    # split a string as many columns as the maximum number of
    # fields included in any of your initial strings.

    # df = df.join(df['genres'].str.split('|', expand=True))

    # split a string as many columns as the maximum number of
    # fields included in any of your initial strings.

    df = df.join(df['genres'].str.split('|', expand=True)
                                        .rename(columns={0: 'genre 0',
                                                         1: 'genre 1',
                                                         2: 'genre 2',
                                                         3: 'genre 3',
                                                         4: 'genre 4'}))
    print("*************")
    print list(df)

    print(df.tail())

if __name__ == '__main__':
    main()
