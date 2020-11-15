def generate_test_data():
    with open("/Users/akshay/Downloads/experiment_1_dataset_test.csv", "r") as test_file:
        with open("/Users/akshay/Downloads/experiment_1_dataset_test_with_class.csv", "w") as class_test_file:
            for line in test_file:
                splits = line.split(",")
                user_id, item_id, rating = splits[0], splits[1], splits[2]
                if float(rating) > 50:
                    class_test_file.write(user_id + "," + item_id + "," + "True\n")
                else:
                    class_test_file.write(user_id + "," + item_id + "," + "False\n")

if __name__ == "__main__":
    generate_test_data()