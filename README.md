census-places-json
==================

Simple scripts for fetching Census places data and generating json representations.

### get_lookup_table_files.py ###

Census.gov says: "The Name Look-up Tables (NLTs) are among the geographic 
products that the Census Bureau provides to states and other data users 
containing the small area census data necessary for legislative redistricting.
The NLTs contain the names and codes of every geographic area of the specific 
type within the state."

http://www.census.gov/geo/maps-data/data/nlt.html

This script will download all the lookup table zip files available at this
URL, or can be used to download the file for a single state.


    >> python download_lookup_table_files.py
    >> python download_lookup_table_files.py -s WA


### make_json.py ###

After running `get_lookup_table_files.py`, you will probably want
to generate JSON from the extracted data.

    >> python make_json.py
    >> python make_json.py -s WA
    >> python make_json.py -g CDP
    >> python make_json.py -s WA -g CDP

Each record in the JSON will have two attributes:

- `census_key`: a generated key with all the bits necessary for making a query against this place, e.g. "STATEFP:53|GEOTYPE:INCPLACE|PLACEFP:67000"
- `name`: a human-friendly title for the Census place, e.g. "Spokane, Washington"
