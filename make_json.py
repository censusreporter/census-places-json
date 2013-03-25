'''
After running `get_lookup_table_files.py`, you will probably want
to generate json from the extracted data.

>> python make_json.py
>> python make_json.py -s WA
>> python make_json.py -g CDP
>> python make_json.py -s WA -g CDP
'''

import json, optparse, os, sys, traceback
from os.path import isdir
from __init__ import EXTRACT_DIR, JSON_DIR, STATE_FIPS_DICT

# Source: http://www.census.gov/geo/maps-data/data/nlt_description.html
# Comment out field names that should not be included in data output
FIELD_DEFINITIONS = {
    'STATEFP': '2-character state FIPS code',
    'DISTRICT': 'variable length code representing the district (i.e., geographic area)',
    'PLACEFP': '5-character place FIPS code',
    #'AIANNHCE': '4-character American Indian / Alaska Native / Native Hawaiian (AIANNH) area census code',
    'COUNTYFP': '3-character county FIPS code',
    'NAME': 'variable length geographic area name (e.g., Atlanta)',
    'NAMELSAD': 'concatenated variable length geographic area name and legal/statistical area description (LSAD) (e.g., Atlanta city)',
}

# Comment out area types that should not be included in data output
GEOGRAPHIC_AREA_TYPES = {
    'CD': 'Congressional districts',
    'SLDU': 'State legislative districts - upper',
    'SLDL': 'State legislative districts - lower',
    #'VTD': 'Voting districts',
    'SDELM': 'Elementary school districts',
    'SDSEC': 'Secondary school districts',
    'SDUNI': 'Unified school districts',
    'INCPLACE': 'Incorporated places',
    'CDP': 'Census designated places',
    #'AIANNH': 'American Indian / Alaska Native / Native Hawaiian areas',
}

def get_filename_list(state=None, geo_type=None):
    start_check = "NAMES_"
    end_check = '_%s.txt' % geo_type if geo_type else '.txt'
    
    if state:
        state_check = '_%s_' % state.upper()
        filename_list = [
            filename for filename in os.listdir(EXTRACT_DIR) \
            # make sure we only get the right set of extracted files
            if filename.startswith(start_check) and filename.endswith(end_check) \
            # make sure we only get the geographic areas we want
            and filename.replace('.txt','').split('_')[-1] in GEOGRAPHIC_AREA_TYPES \
            # allow for generation of just one state
            and state_check in filename if state_check
        ]
    else:
        filename_list = [
            filename for filename in os.listdir(EXTRACT_DIR) \
            # make sure we only get the right set of extracted files
            if filename.startswith(start_check) and filename.endswith(end_check) \
            # make sure we only get the geographic areas we want
            and filename.replace('.txt','').split('_')[-1] in GEOGRAPHIC_AREA_TYPES \
        ]

    return filename_list


def read_filename_list_contents(filename_list):
    filename_list_contents = []
    for filename in filename_list:
        geo_type = filename.replace('.txt','').split('_')[-1]
        with open(os.path.join(EXTRACT_DIR, filename)) as f:
            file_contents = f.readlines()
            file_headers = file_contents.pop(0)
    
        filename_contents = convert_file_contents_to_dicts(file_headers, file_contents, geo_type)
        filename_list_contents.extend(filename_contents)
    
    return filename_list_contents


def convert_file_contents_to_dicts(file_headers, file_contents, geo_type):
    def _make_item_data(line_contents_dict):
        _item_data = {}
        _state_name = STATE_FIPS_DICT[line_contents_dict['STATEFP']]['name']
        _state_abbrev = STATE_FIPS_DICT[line_contents_dict['STATEFP']]['abbreviation']
        _item_census_name = line_contents_dict['NAME']
        _item_census_name_description = line_contents_dict['NAMELSAD']

        # create a human-friendly `name` and a `text` value
        # suitable for autocomplete matching
        if geo_type in ['CDP', 'INCPLACE']:
            _item_name = u'%s, %s' % (_item_census_name, _state_name)
            _item_text = u'%s' % (_item_census_name_description)
        elif geo_type in ['CD', 'SLDU', 'SLDL', 'VTD']:
            _item_name = u'%s %s' % (_state_name, _item_census_name_description)
            _item_text = _item_name
        elif geo_type in ['SDELM', 'SDSEC', 'SDUNI']:
            _item_name = u'%s (%s)' % (_item_census_name_description, _state_name)
            _item_text = u'%s' % (_item_census_name_description)
        else:
            _item_name = u'%s' % (_item_census_name_description)
            _item_text = _item_name
        _item_data['name'] = _item_name
        _item_data['text'] = _item_text

        # build up our key, suitable for building a query later
        _item_data['id'] = 'STATEFP:%s|GEOTYPE:%s' % (line_contents_dict['STATEFP'], geo_type)
        for field in ['DISTRICT', 'COUNTYFP', 'PLACEFP']:
            field_value = line_contents_dict.get(field)
            if field_value:
                _item_data['id'] += '|%s:%s' % (field, field_value)

        return _item_data

    headers = [header.strip() for header in file_headers.split('|')]
    contents = []
    for line in file_contents:
        line_contents = [u'%s' % line.decode('latin-1').strip() for line in line.split('|')]
        line_contents_dict = {}
        for index, header in enumerate(headers):
            if header in FIELD_DEFINITIONS:
                line_contents_dict[header] = line_contents[index]
                
        item_data = _make_item_data(line_contents_dict)
        contents.append(item_data)
    
    return contents


def write_json(contents_list, state=None, geo_type=None):
    file_name = '%s.json' % ('_').join(filter(None, (state, geo_type, 'places')))
    file_path = '%s/%s' % (JSON_DIR, file_name)
    json_dict = {'places': contents_list}
    json_data = json.dumps(json_dict,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )
    with open(file_path, 'w') as f:
        f.write(json_data)


def process_options(arglist=None):
    global options, args
    parser = optparse.OptionParser()
    parser.add_option(
        '-s', '--state',
        dest='state',
        help='specific state file to convert')
    parser.add_option(
        '-g', '--geo', '--geo_type',
        dest='geo_type',
        help='specific geographic type to convert')
    options, args = parser.parse_args(arglist)
    return options, args


def main(args=None):
    """
    """
    if args is None:
        args = sys.argv[1:]
    options, args = process_options(args)

    # make sure we have the expected directories
    for path in [JSON_DIR]:
        if not isdir(path):
            os.mkdir(path)
    
    filename_list = get_filename_list(
        state = options.state if options.state else None,
        geo_type = options.geo_type if options.geo_type else None,
    )
    
    contents_list = read_filename_list_contents(filename_list)
    write_json(
        contents_list,
        state = options.state if options.state else None,
        geo_type = options.geo_type if options.geo_type else None,
    )


if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        sys.stderr.write('\n')
        traceback.print_exc(file=sys.stderr)
        sys.stderr.write('\n')
        sys.exit(1)

