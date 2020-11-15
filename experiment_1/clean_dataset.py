import ast
import json
import re
def clean_data():

    with open("/Users/akshay/Downloads/australian_users_items 2.json", "r") as raw_input:
        with open("/Users/akshay/Downloads/australian_users_items_cleaned.json", "w") as cleaned_file:
            try:
                for line in raw_input:
                    withoutSingleQuotes = line.replace('\'', '\"')
                    main_item_name_indexes = [m.start() for m in re.finditer('item_name', withoutSingleQuotes)]
                    for main_item_name_index in main_item_name_indexes:
                        main_item_name_index = main_item_name_index + 13
                        current_play_index = withoutSingleQuotes[main_item_name_index:].find("playtime_forever")
                        temp = withoutSingleQuotes[main_item_name_index: main_item_name_index + current_play_index - 4 ]
                        repeatingDoubleQuotesIndexes = [m.start() for m in re.finditer("\"", temp)]
                        for i in repeatingDoubleQuotesIndexes:
                            toReplaceIndex = main_item_name_index + i
                            withoutSingleQuotes = withoutSingleQuotes[:toReplaceIndex] + "'" + withoutSingleQuotes[toReplaceIndex + 1:]
                    cleaned_file.write(withoutSingleQuotes)
            except:
                pass
if __name__ == "__main__":
    clean_data()