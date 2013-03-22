census-places-json
==================

Simple scripts for fetching Census places data and generating json 
representations.

### get_lookup_table_files.py ###

[Census.gov says](http://www.census.gov/geo/maps-data/data/nlt.html): "The Name Look-up Tables (NLTs) are among the geographic 
products that the Census Bureau provides to states and other data users 
containing the small area census data necessary for legislative redistricting.
The NLTs contain the names and codes of every geographic area of the specific 
type within the state."


This script will download all the lookup table zip files available at this
URL. An optional `-s` argument will limit the download to a single state.


    >> python download_lookup_table_files.py
    >> python download_lookup_table_files.py -s WA


### make_json.py ###

After running `get_lookup_table_files.py`, you will probably want
to generate JSON from the extracted data. An optional `-s` argument will limit 
the export to a single state, and an optional `-g` argument will limit the 
export to a single geographic type.

    >> python make_json.py
    >> python make_json.py -s WA
    >> python make_json.py -g CDP
    >> python make_json.py -s WA -g CDP

Each record in the JSON will have three attributes:

- `id`: a generated key with the bits necessary for making a query 
against this place, e.g. "STATEFP:53|GEOTYPE:INCPLACE|PLACEFP:67000"
- `name`: a human-friendly title for the Census place, e.g. "Spokane, Washington"
- `text`: a machine-friendly field suitable for autocomplete matching


### examples ###

Two example pages are included, which use the [Select2 widget](http://ivaynberg.github.com/select2/) for autocomplete matching.

- `simple.html`: Open this in your browser, and search for any city in Illinois.
- `all-places.html`: To try this example, you'll need to run the python scripts in this project to download Census data and generate a `places.json` file, then copy it to the `examples/json` directory.
