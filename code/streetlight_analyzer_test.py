import streetlight_analyzer as sta
import os

sta.streetlight_fc = r"..\..\..\..\data\Ottawa\Street_Lights\Street_Lights.shp"
sta.roads_cl_fc = r"..\..\..\..\data\Ottawa\Road_Centrelines\Road_Centrelines.shp"
sta.road_name_field = 'ROAD_NAME_'

def test_get_unique_values():
    expected = 8673
    actual = len(sta._get_unique_values(sta.roads_cl_fc, sta.road_name_field))
    assert expected == actual

def test_get_streetlight_count():
    expected = 849
    actual = sta.get_streetlight_count('CARLING', 0.0002)
    assert expected == actual

def test_save_streetlights():
    expected = True
    sta.save_streetlights('CARLING', 0.0002, r"..\..\..\..\data\Ottawa\outputs\Streetlight_Selected.shp")
    actual = os.path.exists(r"..\..\..\..\data\Ottawa\outputs\Streetlight_Selected.shp")
    assert expected == actual

def test_show_road_names():
    expected = 'CARLING AVE'
    pattern = 'carling'
    actual = sta.show_road_names(pattern)
    assert expected == actual