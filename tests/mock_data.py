"""
    mock data are json strings. *_dict is the intended result. Note that every data member the parser returns is a string.
    
"""

#contains a data member within a quark (dataAge=(time=3))
site1 = '{"x":38, "y":14, "symbol":"OM", "name":"OuterMembrane", "argb":-12228727, "data_string":"(id=1182915603,setByIdentifier=true,comOut=0,dataAge=(time=3))"}'
site1_dict = {
    'argb': -12228727,
    'data_members': {'comOut': '0',
                  'dataAge': {'time': '3'},
                  'id': '1182915603',
                  'setByIdentifier': 'true'},
    'data_string_truncated': False,
    'name': 'OuterMembrane',
    'symbol': 'OM',
    'x': 38,
    'y': 14}

#truncated data_string (ends with "X")
site2 = '{"x":84, "y":15, "symbol":"ET", "name":"ETreeGeneInfo", "argb":-26317, "data_string":"(age=(time=2),geneIDInUse=[0]=false,[1]=false,[2]=false,[3]=false,[4]=false,[5]=false,[6]=false,[7]=false,[8]=false,[9]=false,[10]=false,[11]=false,[12]=false,[13]=false,[14]=false,[15]=false,[16]=false,[17]=false,[18]=false,[19]=false,[20]=false,[21]=false,[22]=false,[23]=false,[24]=false,[25]=false,[26]=false,[27]=false,[28]=false,[29]=false,[30]=false,[31]=false,[32]=false,[33]=false,[34]=false,[35]=false,[36]=false,[37]=false,[38]=false,[39]=false,[40]=false,[41]=false,[42]=false,[43]=false,[44]=false,[X"}'
site2_dict = {
    'argb': -26317,
    'data_members': {'age': {'time': '2'},
                  'geneIDInUse': ['false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false',
                                  'false']},
    'data_string_truncated': True,
    'name': 'ETreeGeneInfo',
    'symbol': 'ET',
    'x': 84,
    'y': 15}

#contains a non-truncated list
site3 = '{"x":34, "y":16, "symbol":"ER", "name":"ERootInformation", "argb":-35072, "data_string":"(age=(time=3),treeIDInUse=[0]=false,[1]=false,[2]=true,[3]=false,[4]=true,[5]=false,[6]=false,[7]=false,[8]=false,[9]=false,[10]=false,[11]=false,[12]=false,[13]=false,[14]=false,[15]=false,[16]=false,[17]=false,[18]=false,[19]=false,[20]=false,[21]=false,[22]=false,[23]=false,[24]=false,[25]=false,[26]=false,[27]=false,[28]=false,[29]=false,[30]=false)"}'
site3_dict = {
    'argb': -35072,
    'data_members': {'age': {'time': '3'},
              'treeIDInUse': ['false',
                              'false',
                              'true',
                              'false',
                              'true',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false',
                              'false']},
    'data_string_truncated': False,
    'name': 'ERootInformation',
    'symbol': 'ER',
    'x': 34,
    'y': 16}

#test 3-site grid..
testgrid = '''
{"grid_configuration":{"grid_is_staggered":true, "grid_height":64, "grid_width":130},
"tile_configuration":{"event_window_radius":4, "tile_height":40, "tile_width":60, "owned_height":32, "owned_width":52},
"non_empty_site_list": [
{"x":0, "y":0, "symbol":"E", "name":"Empty", "argb":-16777216, "data_string":""},
{"x":1, "y":0, "symbol":"E", "name":"Empty", "argb":-16777216, "data_string":""},
{"x":2, "y":0, "symbol":"E", "name":"Empty", "argb":-16777216, "data_string":""}
]}
'''

testgrid_out = {
    "grid_configuration": {"grid_is_staggered": True, "grid_height": 64, "grid_width": 130},
    "tile_configuration": {
        "event_window_radius": 4,
        "tile_height": 40,
        "tile_width": 60,
        "owned_height": 32,
        "owned_width": 52
    },
    "non_empty_site_list": [
        {'argb': -16777216,
          'data_members': None,
          'data_string_truncated': False,
          'name': 'Empty',
          'symbol': 'E',
          'x': 0,
          'y': 0},
         {'argb': -16777216,
          'data_members': None,
          'data_string_truncated': False,
          'name': 'Empty',
          'symbol': 'E',
          'x': 1,
          'y': 0},
         {'argb': -16777216,
          'data_members': None,
          'data_string_truncated': False,
          'name': 'Empty',
          'symbol': 'E',
          'x': 2,
          'y': 0}
    ]
}
