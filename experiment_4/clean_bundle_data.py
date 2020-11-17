import re
def clean_bundle_data():

    with open("/Users/akshay/Downloads/bundle_data.json", "r") as raw_input:
        with open("/Users/akshay/Downloads/bundle_data_cleaned.json", "w") as cleaned_file:
            try:
                for line in raw_input:
                    withoutSingleQuotes = line.replace('\'', '\"')
                    main_item_name_indexes = [m.start() for m in re.finditer("\"item_name\"", withoutSingleQuotes)]
                    for main_item_name_index in main_item_name_indexes:
                        main_item_name_index = main_item_name_index + 14
                        current_brace_index = withoutSingleQuotes[main_item_name_index:].find("}")
                        temp = withoutSingleQuotes[main_item_name_index: main_item_name_index + current_brace_index - 1]
                        repeatingDoubleQuotesIndexes = [m.start() for m in re.finditer("\"", temp)]
                        for i in repeatingDoubleQuotesIndexes:
                            toReplaceIndex = main_item_name_index + i
                            withoutSingleQuotes = withoutSingleQuotes[:toReplaceIndex] + "'" + withoutSingleQuotes[toReplaceIndex + 1:]


                    main_bundle_name_indexes = [m.start() for m in re.finditer("\"bundle_name\"", withoutSingleQuotes)]
                    for main_bundle_name_index in main_bundle_name_indexes:
                        main_bundle_name_index = main_bundle_name_index + 16
                        current_bid_index = withoutSingleQuotes[main_bundle_name_index:].find("bundle_id")
                        temp = withoutSingleQuotes[main_bundle_name_index: main_bundle_name_index + current_bid_index - 4]
                        repeatingDoubleQuotesIndexes = [m.start() for m in re.finditer("\"", temp)]
                        for i in repeatingDoubleQuotesIndexes:
                            toReplaceIndex = main_bundle_name_index + i
                            withoutSingleQuotes = withoutSingleQuotes[:toReplaceIndex] + "'" + withoutSingleQuotes[toReplaceIndex + 1:]
                    withoutSingleQuotes = withoutSingleQuotes.replace("\\", "")
                    cleaned_file.write(withoutSingleQuotes)
            except:
                pass
if __name__ == "__main__":
    clean_bundle_data()