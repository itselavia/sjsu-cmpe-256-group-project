import json
import sys
import random

def create_dataset():
    resultRows = []
    with open("/Users/akshay/Downloads/australian_users_items_cleaned.json", "r") as cleaned_file:
        for line in cleaned_file:
            try:
                json_obj = json.loads(line)
                user_id = str(json_obj['user_id'])
                items = json_obj['items']
                max_playtime = 0
                min_playtime = sys.maxsize
                for item in items:
                    playtime = item['playtime_forever']
                    if playtime > 0:
                        if playtime > max_playtime:
                            max_playtime = playtime
                        if playtime < min_playtime:
                            min_playtime = playtime
                for item in items:
                    item_id = str(item['item_id'])
                    playtime = item['playtime_forever']
                    if playtime > 0:
                        #scaled_playtime = round((playtime - min_playtime)/(max_playtime - min_playtime), 10)
                        scaled_playtime = (1-(playtime-min_playtime)/(max_playtime-min_playtime)) + 100*((playtime-min_playtime)/(max_playtime-min_playtime))
                        resultRows.append([user_id,item_id,scaled_playtime])
            except:
                pass
    random.shuffle(resultRows)
    with open("/Users/akshay/Downloads/experiment_1_dataset.csv", "w") as experiment_dataset:
        experiment_dataset.write("user_id,item_id,rating\n")
        for entry in resultRows:
            experiment_dataset.write(entry[0] + "," + entry[1] + "," + str(entry[2]) + "\n")
if __name__ == "__main__":
    create_dataset()