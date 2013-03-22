DOWNLOAD_DIR = 'downloaded_files'
EXTRACT_DIR = 'extracted_files'
JSON_DIR = 'json'

STATE_FIPS_DICT = {
    '01': {
        'abbreviation': 'AL',
        'name': 'Alabama',
        'GNISID': '01779775',
    },
    '02': {
        'abbreviation': 'AK',
        'name': 'Alaska',
        'GNISID': '01785533',
    },
    '04': {
        'abbreviation': 'AZ',
        'name': 'Arizona',
        'GNISID': '01779777',
    },
    '05': {
        'abbreviation': 'AR',
        'name': 'Arkansas',
        'GNISID': '00068085',
    },
    '06': {
        'abbreviation': 'CA',
        'name': 'California',
        'GNISID': '01779778',
    },
    '08': {
        'abbreviation': 'CO',
        'name': 'Colorado',
        'GNISID': '01779779',
    },
    '09': {
        'abbreviation': 'CT',
        'name': 'Connecticut',
        'GNISID': '01779780',
    },
    '10': {
        'abbreviation': 'DE',
        'name': 'Delaware',
        'GNISID': '01779781',
    },
    '11': {
        'abbreviation': 'DC',
        'name': 'District of Columbia',
        'GNISID': '01702382',
    },
    '12': {
        'abbreviation': 'FL',
        'name': 'Florida',
        'GNISID': '00294478',
    },
    '13': {
        'abbreviation': 'GA',
        'name': 'Georgia',
        'GNISID': '01705317',
    },
    '15': {
        'abbreviation': 'HI',
        'name': 'Hawaii',
        'GNISID': '01779782',
    },
    '16': {
        'abbreviation': 'ID',
        'name': 'Idaho',
        'GNISID': '01779783',
    },
    '17': {
        'abbreviation': 'IL',
        'name': 'Illinois',
        'GNISID': '01779784',
    },
    '18': {
        'abbreviation': 'IN',
        'name': 'Indiana',
        'GNISID': '00448508',
    },
    '19': {
        'abbreviation': 'IA',
        'name': 'Iowa',
        'GNISID': '01779785',
    },
    '20': {
        'abbreviation': 'KS',
        'name': 'Kansas',
        'GNISID': '00481813',
    },
    '21': {
        'abbreviation': 'KY',
        'name': 'Kentucky',
        'GNISID': '01779786',
    },
    '22': {
        'abbreviation': 'LA',
        'name': 'Louisiana',
        'GNISID': '01629543',
    },
    '23': {
        'abbreviation': 'ME',
        'name': 'Maine',
        'GNISID': '01779787',
    },
    '24': {
        'abbreviation': 'MD',
        'name': 'Maryland',
        'GNISID': '01714934',
    },
    '25': {
        'abbreviation': 'MA',
        'name': 'Massachusetts',
        'GNISID': '00606926',
    },
    '26': {
        'abbreviation': 'MI',
        'name': 'Michigan',
        'GNISID': '01779789',
    },
    '27': {
        'abbreviation': 'MN',
        'name': 'Minnesota',
        'GNISID': '00662849',
    },
    '28': {
        'abbreviation': 'MS',
        'name': 'Mississippi',
        'GNISID': '01779790',
    },
    '29': {
        'abbreviation': 'MO',
        'name': 'Missouri',
        'GNISID': '01779791',
    },
    '30': {
        'abbreviation': 'MT',
        'name': 'Montana',
        'GNISID': '00767982',
    },
    '31': {
        'abbreviation': 'NE',
        'name': 'Nebraska',
        'GNISID': '01779792',
    },
    '32': {
        'abbreviation': 'NV',
        'name': 'Nevada',
        'GNISID': '01779793',
    },
    '33': {
        'abbreviation': 'NH',
        'name': 'New Hampshire',
        'GNISID': '01779794',
    },
    '34': {
        'abbreviation': 'NJ',
        'name': 'New Jersey',
        'GNISID': '01779795',
    },
    '35': {
        'abbreviation': 'NM',
        'name': 'New Mexico',
        'GNISID': '00897535',
    },
    '36': {
        'abbreviation': 'NY',
        'name': 'New York',
        'GNISID': '01779796',
    },
    '37': {
        'abbreviation': 'NC',
        'name': 'North Carolina',
        'GNISID': '01027616',
    },
    '38': {
        'abbreviation': 'ND',
        'name': 'North Dakota',
        'GNISID': '01779797',
    },
    '39': {
        'abbreviation': 'OH',
        'name': 'Ohio',
        'GNISID': '01085497',
    },
    '40': {
        'abbreviation': 'OK',
        'name': 'Oklahoma',
        'GNISID': '01102857',
    },
    '41': {
        'abbreviation': 'OR',
        'name': 'Oregon',
        'GNISID': '01155107',
    },
    '42': {
        'abbreviation': 'PA',
        'name': 'Pennsylvania',
        'GNISID': '01779798',
    },
    '44': {
        'abbreviation': 'RI',
        'name': 'Rhode Island',
        'GNISID': '01219835',
    },
    '45': {
        'abbreviation': 'SC',
        'name': 'South Carolina',
        'GNISID': '01779799',
    },
    '46': {
        'abbreviation': 'SD',
        'name': 'South Dakota',
        'GNISID': '01785534',
    },
    '47': {
        'abbreviation': 'TN',
        'name': 'Tennessee',
        'GNISID': '01325873',
    },
    '48': {
        'abbreviation': 'TX',
        'name': 'Texas',
        'GNISID': '01779801',
    },
    '49': {
        'abbreviation': 'UT',
        'name': 'Utah',
        'GNISID': '01455989',
    },
    '50': {
        'abbreviation': 'VT',
        'name': 'Vermont',
        'GNISID': '01779802',
    },
    '51': {
        'abbreviation': 'VA',
        'name': 'Virginia',
        'GNISID': '01779803',
    },
    '53': {
        'abbreviation': 'WA',
        'name': 'Washington',
        'GNISID': '01779804',
    },
    '54': {
        'abbreviation': 'WV',
        'name': 'West Virginia',
        'GNISID': '01779805',
    },
    '55': {
        'abbreviation': 'WI',
        'name': 'Wisconsin',
        'GNISID': '01779806',
    },
    '56': {
        'abbreviation': 'WY',
        'name': 'Wyoming',
        'GNISID': '01779807',
    },
}