import arcpy


def main():
    ws = r'..\..\..\..\data\Canada\Canada.gdb'

    fc = 'MajorCities'

    arcpy.env.workspace = ws

    fields = ['NAME', 'PROV', 'UTM_MAP', 'SHAPE@X', 'SHAPE@Y']

    out_kml = r'..\..\output\Cities.kml'

    with arcpy.da.SearchCursor(fc, fields) as cursor:
        with open(out_kml, 'w') as outfile:
            #Writing header
            header_kml_file = get_kml_header()
            outfile.write(header_kml_file)

            #Writing & looping through Placemarks
            for row in cursor:
                outfile.write(f"  <Placemark>\n    <name>{row[0]},{row[1]}</name>\n    <description>\n    'http://www.canmaps.com/topo/nts50/map/{row[2]}.htm'\n    </description>\n    <Point>\n        <coordinates>{row[3]},{row[4]},0</coordinates>\n    </Point>\n  </Placemark>")

            #Writing footer
            footer_kml_file = get_kml_footer()
            outfile.write(footer_kml_file)

def get_kml_header():
    """Return the xml header including the Document start tag
    """
    return '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>'


def get_kml_footer():
    """Return the document and kml end tags
    """
    return "</Document>\n</kml>"

if __name__ == '__main__':
    main()