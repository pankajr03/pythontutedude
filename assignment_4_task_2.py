written_filename ='output.txt'
user_input = input('Enter text to write to the file: ')
try:
    with open(written_filename, 'w') as f:
        f.write(user_input)

    print(f'Data successfully written to {written_filename}.\n')

    user_input_append = input('Enter additional text to append: ')
    with open(written_filename, 'a') as f:
        f.write('\n' + user_input_append)

    print('Data successfully appended\n')

    print(f'Final content of {written_filename}:')
    with open(written_filename, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('File now does not exist')
except Exception as e:
    print(e)
