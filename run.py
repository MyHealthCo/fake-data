import fake_data.controllers


def main(number_of_records):
    result = {}

    result["patients"] = fake_data.controllers.patients(number_of_records)

    print(result)


if __name__ == "__main__":
    main(10)
