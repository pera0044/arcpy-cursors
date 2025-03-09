import sys

def main():
    global arcpy

    if len(sys.argv) !=2:
        print('Usage: cursor02.py <valid province abbreviation>')
        sys.exit()

    list_provinces = ['NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']
    
    province = sys.argv[1]

    if province.upper() not in list_provinces:
        print(f'{province} is not a valid province abbreviation')
        sys.exit()

    import arcpy
    
    show_name_province(province)

def show_name_province(province):
    ws = r'..\..\..\..\data\Canada'

    fc = 'Can_Mjr_Cities.shp'

    arcpy.env.workspace = ws

    fields = ['NAME', 'PROV']

    field = arcpy.AddFieldDelimiters(ws, fields[1])

    where_clause = f"{field} LIKE '{province.upper()}'"

    with arcpy.da.SearchCursor(fc, fields, where_clause) as cursor:
        count = 0
        print(f'{fields[0].capitalize()}, {fields[1].capitalize()}')
        for row in cursor:
            count += 1
            print(f'{row[0]},{row[1]}')
        print(f'There are {count} cities in the above list')

if __name__ == '__main__':
    main()