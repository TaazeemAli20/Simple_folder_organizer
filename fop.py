import os

conformation_checker = False

while conformation_checker == False:
    folder_address = str(input('Enter Your Folder Address Here : '))
    conformation_token = str(input('Do You Want To Continue (y\\n) : '))

    if conformation_token == 'y' or conformation_checker == 'Y':
        try:
            os.startfile(folder_address)
            content_inside_folder = os.listdir(folder_address)

            for content in content_inside_folder:
                try:
                    content_extension = content.split('.')[1]
                    print(f'{content} : Extension - {content_extension}')

                    new_folder_name = f'{content_extension}_Files'
                    new_folder_location = f'{folder_address}\\{new_folder_name}'
                    try:
                        os.mkdir(new_folder_location)

                    except FileExistsError as already_exist:
                        pass

                    try:
                        current_file_absolute_location = f'{folder_address}\\{content}'
                        os.system(f'move {current_file_absolute_location} {new_folder_location}')

                    except SyntaxError as file_not_detected:
                        current_name_of_file = content
                        changed_name = current_name_of_file.replace(" ", "_")
                        location_of_changed_name = f'{folder_address}\\{changed_name}'
                        print(location_of_changed_name)

                except IndexError as not_a_file:
                    print(f'{content} is a Folder')

            conformation_checker = True
        except FileNotFoundError as no_such_folder:
            print("There's No Such Folder. Kindly Check Your Address")

    else:
        print('\nProcess Canceled\n')