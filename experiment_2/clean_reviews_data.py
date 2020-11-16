import re
def clean_review_data():

    with open("/Users/akshay/Downloads/australian_user_reviews.json", "r") as raw_input:
        with open("/Users/akshay/Downloads/australian_user_reviews_cleaned.json", "w") as cleaned_file:
            try:
                for line in raw_input:
                    withoutSingleQuotes = line.replace('\'', '\"')
                    withoutSingleQuotes = withoutSingleQuotes.replace("True", "true")
                    withoutSingleQuotes = withoutSingleQuotes.replace("False", "false")
                    main_review_indexes = [m.start() for m in re.finditer("\"review\"", withoutSingleQuotes)]
                    for main_review_index in main_review_indexes:
                        main_review_index = main_review_index + 11
                        current_brace_index = withoutSingleQuotes[main_review_index:].find("}")
                        temp = withoutSingleQuotes[main_review_index: main_review_index + current_brace_index - 1]
                        repeatingDoubleQuotesIndexes = [m.start() for m in re.finditer("\"", temp)]
                        for i in repeatingDoubleQuotesIndexes:
                            toReplaceIndex = main_review_index + i
                            withoutSingleQuotes = withoutSingleQuotes[:toReplaceIndex] + "'" + withoutSingleQuotes[toReplaceIndex + 1:]
                    withoutSingleQuotes = withoutSingleQuotes.replace("\\", "")
                    cleaned_file.write(withoutSingleQuotes)
            except:
                pass
if __name__ == "__main__":
    clean_review_data()