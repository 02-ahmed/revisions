import re

def decode_message(message_file):
    file = open(message_file, 'r')
    read = file.readlines()
    modified = []
    nums = []

    for line in read:
        modified.append(line.strip())

    for num in modified:
        numbers = re.findall(r'\d+', num)
        nums.extend([int(num) for num in numbers])

    nums_sorted = sorted(nums)

    pyramid = []  
    row_length = 1 

    while nums_sorted:
        row = nums_sorted[:row_length]  
        pyramid.append(row)  
        nums_sorted = nums_sorted[row_length:]  
        row_length += 1  

    last_numbers = [row[-1] for row in pyramid]

    decode_list = []

    for number in last_numbers:
       number_str = str(number)
       for string in modified:
          if string.startswith(number_str + ' ') or string == number_str:
             decode_list.append(string)

    words_list = []

    for string in decode_list:
        words = string.split()
        words_without_numbers = [word for word in words if not word.isdigit()]
        words_list.extend(words_without_numbers)

    decoded_message = ' '.join(words_list)

    return decoded_message


print(decode_message('coding_qual_input.txt'))
print(decode_message('encoded message.txt'))