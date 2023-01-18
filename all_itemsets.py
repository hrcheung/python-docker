def all_itemsets(filename):
    import pandas as pd
    df=pd.read_csv(filename,sep='delimiter', header=None,engine='python')
    df=df[0].str.split(',',expand=True)
    rows=df.shape[0]
    cols=df.shape[1]
    car_set=set()
    for i in range(100):
        for j in range(4):
            if df[j][i]:
                car_set.add(df[j][i].strip())
#     print(car_set)
    res=[set()]
#     print(car_set)
    for item in car_set:
#         print("item=",item)
        for sub_s in res[:]:
            tmp=sub_s
            tmp.add(item)
            res.append(tmp)
    return res