import dbfunction
import datetime

while True:
    print('')
    print('Select table:')
    print('1. producers')
    print('2. films')
    print('e. Exit program')
    menu_input_table = raw_input()

    if menu_input_table == '1':
        while True:
            print('')
            print('Select action for table \'producers\':')
            print('1. Create')
            print('2. Update')
            print('3. Delete')
            print('4. Select')
            print('e. Go back')
            menu_input_table_producer = raw_input()

            if menu_input_table_producer == '1':
                try:
                    print('')
                    print('Enter producer name:')
                    producer_name = str(raw_input())
                    print('Enter producer Date of Birth(yyyy mm dd):')
                    yy, mm, dd = map(int, str(raw_input()).split())
                    myDateTime = datetime.date(yy, mm, dd)

                    dbfunction.create_producer(producer_name, myDateTime)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_producer == '2':
                try:
                    print('')
                    print('Enter id name that you want to update')
                    producer_id = input()

                    if (dbfunction.select_producer('id', id)) == 0:
                        raise Exception('Error: there is no producer with id \'{0}\''.format(id))

                    print('')
                    print('Enter field that you want to update (\'name\', \'date\')')
                    update_field = raw_input()

                    if (update_field != 'name') and (update_field != 'date'):
                        raise Exception('Error: invalid field')

                    if update_field == 'date':
                        print 'Enter date (yyyy mm dd h m)'
                        yy, mm, dd = map(int, str(raw_input()).split())
                        update_value = datetime.date(yy, mm, dd)
                    else:
                        print('Enter value:')
                        update_value = raw_input()

                    dbfunction.update_producer(producer_id, update_field, update_value)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_producer == '3':
                try:
                    print('')
                    print('Enter producer id that you want to delete')
                    del_id = input()

                    if(dbfunction.select_producer('id', id)) == 0:
                        raise Exception('Error: there is no producer with name \'{0}\''.format(del_id))

                    dbfunction.delete_producer(del_id)
                except Exception as e:
                    print('')
                    print(e)

            elif menu_input_table_producer == '4':
                try:
                    print('')
                    print('Enter field that you want to filter (\'name\', \'date\'), or leave blank to list all')
                    input_field = raw_input()
                    if (input_field != 'name') and (input_field != 'date') and (input_field != ''):
                        raise Exception('Error: invalid field')

                    if input_field == '':
                        print('')
                        dbfunction.print_producer(dbfunction.select_producer())
                        continue

                    print('')
                    if input_field == 'date':
                        print 'Enter date (yyyy mm dd)'
                        yy, mm, dd = map(int, str(raw_input()).split())
                        input_value = datetime.date(yy, mm, dd)
                    else:
                        print('Enter value:')
                        input_value = raw_input()
                    print('')
                    dbfunction.print_producer(dbfunction.select_producer(input_field, input_value))
                except Exception as e:
                    print('')
                    print(e)

            elif menu_input_table_producer == 'e':
                break
    elif menu_input_table == '2':
        while True:
            print('')
            print('Select action for table \'film\':')
            print('1. Create')
            print('2. Update')
            print('3. Delete')
            print('4. Select')
            print('5. Filter')
            print('e. Go back')
            menu_input_table_films = raw_input()

            if menu_input_table_films == '1':
                try:
                    print('')
                    print('Type films \'film_name\', \'producer\', \'country\' separated by spaces:')
                    input_film = raw_input().split(' ')


                    if len(input_film) < 3:
                        raise Exception('Error: you must provide three arguments')
                    dbfunction.create_film(input_film[0], input_film[1], input_film[2])
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_films == '2':
                try:
                    print('')
                    print('Enter id film that you want to update')
                    up_id = input()

                    if (dbfunction.select_film('id', id)) == 0:
                        raise Exception('Error: there is no film with id \'{0}\''.format(up_id))

                    print('')
                    print('Enter field that you want to update (\'film_name\', \'producer\', \'country\')')
                    update_field = raw_input()
                    if (update_field != 'country') and (update_field != 'film_name') and (update_field != 'producer'):
                        raise Exception('Error: invalid field')

                    print('')
                    print('Enter value:')
                    update_value = raw_input()

                    dbfunction.update_film(up_id, update_field, update_value)
                except Exception as e:
                    print('')
                    print(e)

            elif menu_input_table_films == '3':
                try:
                    print('')
                    print('Enter id film that you want to delete')
                    del_id = input()

                    if (dbfunction.select_film('id', id)) == 0:
                        raise Exception('Error: there is no film \'{0}\''.format(del_id))

                    dbfunction.delete_film(del_id)
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_films == '4':
                try:
                    print('')
                    print('Enter field that you want to filter (\'film_name\', \'producer\', \'country\'), '
                          'or leave blank to list all')
                    input_field = raw_input()
                    if (input_field != 'film_name') and (input_field != 'producer') \
                            and (input_field != 'country') and (input_field != ''):
                        raise Exception('Error: invalid field')

                    if input_field == '':
                        print('')
                        dbfunction.print_film(dbfunction.select_film())
                        continue

                    print('')
                    print('Enter value:'.format(input_field))
                    input_value = raw_input()
                    print('')

                    dbfunction.print_film(dbfunction.select_film(input_field, input_value))
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_films == '5':
                try:
                    print('')
                    print('Showing movies that were shot in Ukraine:')
                    print('')

                    print(dbfunction.filter_film())
                except Exception as e:
                    print('')
                    print(e)
            elif menu_input_table_films == 'e':
                break
    elif menu_input_table == 'e':
        exit(0)