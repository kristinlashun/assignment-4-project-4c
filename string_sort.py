def string_sort(str_list):
    for i in range(1, len(str_list)):
        current_value = str_list[i]
        j = i - 1

        # Move elements of str_list[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and str_list[j].lower() > current_value.lower():
            str_list[j + 1] = str_list[j]
            j -= 1

        str_list[j + 1] = current_value