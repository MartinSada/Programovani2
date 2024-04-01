def invert_dictionary(data):
    inverted_dict = {}
    for line in data:
        if line.strip() == '---':
            break
        prop, *subjects = line.strip().split(':')
        for subject in subjects:
            subject = subject.strip()
            if subject not in inverted_dict:
                inverted_dict[subject] = []
            inverted_dict[subject].append(prop.strip())

    sorted_keys = sorted(inverted_dict.keys())
    for key in sorted_keys:
        print(f"{key}: {', '.join(sorted(inverted_dict[key]))}")
    print("---")


# Example usage
input_data = [
    "vejce: večeře",
    "špek: oběd",
    "knedlíky: snídaně, večeře",
    "zelí: oběd",
    "uzené: oběd, večeře",
    "tlačenka: snídaně, oběd, večeře",
    "---"
]

invert_dictionary(input_data)