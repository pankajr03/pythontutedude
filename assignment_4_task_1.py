file_name = 'sample.txt'
try:
    with open(file_name, 'r') as file_read:
        file_content = file_read.readlines()
        line_count = 1
        txt_file_content = ''
        print('Reading the file content:')
        for content in file_content:
            print(f'Line {line_count}: {content.strip()}')
            line_count += 1

except FileNotFoundError:
    print(f'The file \'{file_name}\' was not found')
