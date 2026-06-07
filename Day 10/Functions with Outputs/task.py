def format_name(first_name, last_name):
    print(first_name.title())    # .title converts a mixture of case to first
    # letter upper case e.g fasty to Fasty or FASTY to Fasty
    print(last_name.title())

    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()

    print(f"{formatted_first_name} {formatted_last_name}")

format_name("ABDUL", "fatai")