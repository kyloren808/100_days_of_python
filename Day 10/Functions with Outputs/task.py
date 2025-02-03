# def format_name(f_name, l_name):
#   return f"{f_name.title()} {l_name.title()}"
#
# my_name = format_name("nathaniel", "COLEMAn")
#
# print(my_name)


def is_leap_year(year):
  # Write your code here.
  # Don't change the function name.
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

print(is_leap_year(2400))
