def format_name(f_name, l_name):
    """Take a first and last name and format it to 
    return the title case case version of the name"""
    if f_name == "" or l_name == "":
        return  # Escapes the function
    return f_name.title() + " " + l_name.title()
    print("this isn't printed...")
print(format_name("kristian", "skreosen"))