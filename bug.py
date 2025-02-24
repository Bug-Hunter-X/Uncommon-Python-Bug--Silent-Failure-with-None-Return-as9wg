def function_with_uncommon_bug(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Division by zero!")
        return None

# Uncommon bug: The function returns None on error, which might not be handled properly
# In some cases a different error handling approach like raising exception is preferred
result = function_with_uncommon_bug(10, 0)
if result is None:
    print("An error occured!")