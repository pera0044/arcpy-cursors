import arcpy

ws = r'..\..\..\..\data\Canada'

fc = 'Can_Mjr_Cities.shp'

arcpy.env.workspace = ws

fields = ['NAME', 'PROV']

with arcpy.da.SearchCursor(fc, fields) as cursor:
    count = 0
    print(f'{fields[0].capitalize()}, {fields[1].capitalize()}')
    for row in cursor:
        count += 1
        print(f'{row[0]},{row[1]}')
    print(f'There are {count} cities in the above list')