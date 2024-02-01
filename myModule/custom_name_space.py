# my_script.py

def run_with_custom_name():
    custom_name_variable = "__my_custom_name__"

    if __name__ == custom_name_variable:
        # Code to be executed when the script is run with your custom condition
        print("This script is being run with the custom condition")
    else:
        # Code to be executed when the script is run in other scenarios
        print("This script is being run in a different context")

# Call the function to simulate running with the custom condition
run_with_custom_name()
