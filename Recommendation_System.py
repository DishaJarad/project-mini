
import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy

file_path = 'Movie_dataset_csv.csv'


df = pd.read_csv(file_path)


reader = Reader(rating_scale=(0, 11))

data = Dataset.load_from_df(df[['UserID', 'MovieID', 'Rate']], reader)


trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

model = SVD()
model.fit(trainset)

predictions = model.test(testset)


accuracy.rmse(predictions)

user_id = 1
items_to_predict = [item_id for item_id in df['MovieID'].unique() if item_id not in df[df['UserID'] == user_id]['MovieID'].unique()]

item_scores = [(item_id, model.predict(user_id, item_id).est) for item_id in items_to_predict]

item_scores.sort(key=lambda x: x[1], reverse=True)

top_n = 3
top_recommendations = item_scores[:top_n]


print(f"Top {top_n} recommendations for user {user_id}:")
for item_id, score in top_recommendations:
    print(f"Movie ID: {item_id}, Estimated rating: {score}")
    
    
    
'''
Movie_dataset_csv is given below:

UserID	MovieID	Rate
1	1001	1
2	1002	5
3	1003	2
4	1004	1
5	1005	1
6	1006	5
7	1007	3
8	1008	10
9	1009	5
10	1010	1
11	1011	10
12	1012	9
13	1013	8
14	1014	7
15	1015	4
16	1016	9
17	1017	8
18	1018	7
19	1019	4
20	1020	5


'''
