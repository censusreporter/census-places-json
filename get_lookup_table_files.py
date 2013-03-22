'''
Census.gov says: "The Name Look-up Tables (NLTs) are among the geographic 
products that the Census Bureau provides to states and other data users 
containing the small area census data necessary for legislative redistricting.
The NLTs contain the names and codes of every geographic area of the specific 
type within the state."

http://www.census.gov/geo/maps-data/data/nlt.html

This script will download all the lookup table zip files available at this
URL, making one request per SLEEP_SECONDS. The script can also be used to
download the file for a single state.

>> python download_lookup_table_files.py
>> python download_lookup_table_files.py -s WA
'''

import sys, optparse, os, time, traceback, urllib2, zipfile
from os.path import isdir, join, normpath, split

from __init__ import DOWNLOAD_DIR, EXTRACT_DIR

SLEEP_SECONDS = 2
URL_PREFIX = 'http://www.census.gov/geo/maps-data/data/docs/nlt/'
CENSUS_NAME_LOOKUP_TABLE_FILES = {
    'AL': 'NAMES_ST01_AL.zip',
    'AK': 'NAMES_ST02_AK.zip',
    'AZ': 'NAMES_ST04_AZ.zip',
    'AR': 'NAMES_ST05_AR.zip',
    'CA': 'NAMES_ST06_CA.zip',
    'CO': 'NAMES_ST08_CO.zip',
    'CT': 'NAMES_ST09_CT.zip',
    'DE': 'NAMES_ST10_DE.zip',
    'DC': 'NAMES_ST11_DC.zip',
    'FL': 'NAMES_ST12_FL.zip',
    'GA': 'NAMES_ST13_GA.zip',
    'HI': 'NAMES_ST15_HI.zip',
    'ID': 'NAMES_ST16_ID.zip',
    'IL': 'NAMES_ST17_IL.zip',
    'IN': 'NAMES_ST18_IN.zip',
    'IA': 'NAMES_ST19_IA.zip',
    'KS': 'NAMES_ST20_KS.zip',
    'KY': 'NAMES_ST21_KY.zip',
    'LA': 'NAMES_ST22_LA.zip',
    'ME': 'NAMES_ST23_ME.zip',
    'MD': 'NAMES_ST24_MD.zip',
    'MA': 'NAMES_ST25_MA.zip',
    'MI': 'NAMES_ST26_MI.zip',
    'MN': 'NAMES_ST27_MN.zip',
    'MS': 'NAMES_ST28_MS.zip',
    'MO': 'NAMES_ST29_MO.zip',
    'MT': 'NAMES_ST30_MT.zip',
    'NE': 'NAMES_ST31_NE.zip',
    'NV': 'NAMES_ST32_NV.zip',
    'NH': 'NAMES_ST33_NH.zip',
    'NJ': 'NAMES_ST34_NJ.zip',
    'NM': 'NAMES_ST35_NM.zip',
    'NY': 'NAMES_ST36_NY.zip',
    'NC': 'NAMES_ST37_NC.zip',
    'ND': 'NAMES_ST38_ND.zip',
    'OH': 'NAMES_ST39_OH.zip',
    'OK': 'NAMES_ST40_OK.zip',
    'OR': 'NAMES_ST41_OR.zip',
    'PA': 'NAMES_ST42_PA.zip',
    'RI': 'NAMES_ST44_RI.zip',
    'SC': 'NAMES_ST45_SC.zip',
    'SD': 'NAMES_ST46_SD.zip',
    'TN': 'NAMES_ST47_TN.zip',
    'TX': 'NAMES_ST48_TX.zip',
    'UT': 'NAMES_ST49_UT.zip',
    'VT': 'NAMES_ST50_VT.zip',
    'VA': 'NAMES_ST51_VA.zip',
    'WA': 'NAMES_ST53_WA.zip',
    'WV': 'NAMES_ST54_WV.zip',
    'WI': 'NAMES_ST55_WI.zip',
    'WY': 'NAMES_ST56_WY.zip',
}


def download_file_from_url(url):
    # yay stackoverflow: http://stackoverflow.com/a/22776
    file_name = '%s/%s' % (DOWNLOAD_DIR, url.split('/')[-1])
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()
    
    return file_name
    
    
def extract_downloaded_file(filepath):
    zipped = zipfile.ZipFile(filepath, 'r')
    
    for filename in zipped.namelist():
        print "Extracting " + os.path.basename(filename) + " ..."

        # Handle possible folders inside zipfile
        if not filename.endswith('/'): 
            root, name = split(filename)
            target_dir = normpath(join(EXTRACT_DIR, root))
            file(join(target_dir, name), 'wb').write(zipped.read(filename))

    zipped.close()


def get_one_file(state):
    target = CENSUS_NAME_LOOKUP_TABLE_FILES[state]
    target_url = ('').join([URL_PREFIX, target])
    filepath = download_file_from_url(target_url)
    extract_downloaded_file(filepath)

def get_all_files():
    for state in CENSUS_NAME_LOOKUP_TABLE_FILES:
        get_one_file(state)
        time.sleep(SLEEP_SECONDS)


def process_options(arglist=None):
    global options, args
    parser = optparse.OptionParser()
    parser.add_option(
        '-s', '--state',
        dest='state',
        help='specific state file to download')
    options, args = parser.parse_args(arglist)
    return options, args


def main(args=None):
    """
    To run:
    
    >> python download_lookup_table_files.py
    >> python download_lookup_table_files.py -s WA
    
    This will create DOWNLOAD_DIR and EXTRACT_DIR if necessary,
    fetch a zipfile or set of zipfiles from the Census website,
    then extract the contents of each file retrieved.
    """
    if args is None:
        args = sys.argv[1:]
    options, args = process_options(args)
    
    # make sure we have the expected directories
    for path in [DOWNLOAD_DIR, EXTRACT_DIR]:
        if not isdir(path):
            os.mkdir(path)
    
    # get one state or all states
    if options.state:
        get_one_file(options.state)
    else:
        get_all_files()


if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        sys.stderr.write('\n')
        traceback.print_exc(file=sys.stderr)
        sys.stderr.write('\n')
        sys.exit(1)

