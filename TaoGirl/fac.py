

file = open('C:\\Users\\i067382\\Documents\\DS\\HANA CalView\\table_names.sql', 'r')
target = open('C:\\Users\\i067382\\Documents\\DS\\HANA CalView\\convert.sql', 'a')
tableNames = file.readlines()
for tableName in tableNames:
    #target.write('select * from ' + tableName + ' into ' + tableName + '_T;\n')
    #target.write('drop table ' + tableName + ';\n')
    #target.write('rename table ' + tableName + '_T to ' + tableName + ';\n\n')
    target.write('drop table ' + tableName + '_T;\n')