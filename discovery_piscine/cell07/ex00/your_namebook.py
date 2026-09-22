def array_of_names(name):
    fname = []
    for first_name, last_name in name.items():
        formatted_name = first_name.capitalize() + " " + last_name.capitalize()
        fname.append(formatted_name)
        
    return fname

person = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(person))