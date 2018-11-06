import numpy as np
import pandas as pd

N_STATES = 6   # the length of the 1 dimensional world
ACTIONS = ['left', 'right']     # available actions


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table initial values
        columns=actions,    # actions's name
    )
    # print(table)    # show table
    return table


def test():
    q_table = build_q_table(N_STATES,ACTIONS)
    print(q_table)
    print('-------')
    print(q_table['left'])


def test1():
    data = [[1, 2, 3], [4, 5, 6]]
    index = ['d', 'e']
    columns = ['a', 'b', 'c']
    df = pd.DataFrame(data=data, index=index, columns=columns)
    print(df)
    print('------')
    print(df.iloc[0])
    print(df.iloc[0].idxmax())
    print('------')
    print(df.iloc[1])


def test2():
    data = [[1, 2, 3], [4, 5, 6]]
    index = ['d', 'e']
    columns = ['a', 'b', 'c']
    df = pd.DataFrame(data=data, index=index, columns=columns)
    print(df)
    print('--------')
    print(df.ix[1].max())
    print(df.ix[1,'c'])


if __name__ == "__main__":
    test2()