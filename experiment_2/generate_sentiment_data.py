import json
def generate_test_data():
    resultRows = []
    with open("/Users/akshay/Downloads/australian_user_reviews_cleaned.json", "r") as cleaned_file:
        for line in cleaned_file:
            try:
                json_obj = json.loads(line)
                reviews = json_obj["reviews"]
                for review in reviews:
                    review_text = review["review"]
                    sentiment = review["recommend"]
                    resultRows.append([review_text, sentiment])
            except Exception as e:
                pass
                    
    with open("/Users/akshay/Downloads/experiment_2_sentiment_dataset.tsv", "w") as sentiment_dataset:
        for entry in resultRows:
            sentiment_dataset.write(entry[0] + "\t" + str(int(entry[1])) + "\n")
                

if __name__ == "__main__":
    generate_test_data()