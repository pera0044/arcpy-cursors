streetlight_fc = None
roads_cl_fc = None
road_name_field = None

import arcpy 

def _get_unique_values(fc, field_name):
    road_names = []
    unique_road_names = []

    with arcpy.da.SearchCursor(fc, field_name) as cursor:
        for row in cursor:
            road_names.append(row[0])

    for element in road_names:
        if element not in unique_road_names and element != ' ' :
            unique_road_names.append(element)

    return unique_road_names

def get_streetlight_count(road_name, distance):
    selection_output = _select_streetlights(road_name,distance)
    return int(selection_output[2])

def save_streetlights(road_name, distance, out_fc):
    selection_output = _select_streetlights(road_name,distance)
    streetlights_selected = selection_output[0]
    arcpy.management.CopyFeatures(
        in_features=streetlights_selected,
        out_feature_class=out_fc,
        config_keyword="",
        spatial_grid_1=None,
        spatial_grid_2=None,
        spatial_grid_3=None
    )

def show_road_names(pattern=None):
    fc = roads_cl_fc
    field_name = road_name_field
    if pattern == None:
        valid_road_names = _get_unique_values(fc, field_name)
        return valid_road_names
    else:
        where_clause = f"{field_name} LIKE UPPER('%{pattern}%')"
        with arcpy.da.SearchCursor(fc, field_name, where_clause) as cursor:
            for row in cursor:
                return row[0]

def _select_streetlights(road_name, distance):
    ws = roads_cl_fc
    dist_filed = arcpy.AddFieldDelimiters(ws, road_name_field)
    selected_roads = arcpy.management.SelectLayerByAttribute(
    in_layer_or_view=roads_cl_fc,
    selection_type="NEW_SELECTION",
    where_clause=f"{dist_filed} LIKE '%{road_name}%'",
    invert_where_clause=None
    )
    selection_output = arcpy.management.SelectLayerByLocation(
    in_layer=streetlight_fc,
    overlap_type="INTERSECT",
    select_features=selected_roads,
    search_distance=f"{distance} DecimalDegrees",
    selection_type="NEW_SELECTION",
    invert_spatial_relationship="NOT_INVERT"
    )
    return selection_output