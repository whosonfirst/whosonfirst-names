#!/usr/bin/env python

import mapzen.whosonfirst.utils
import sys
import os
import csv

import cooperhewitt.csvtools	# because unicode... https://github.com/cooperhewitt/py-cooperhewitt-csvtools

if __name__ == '__main__':
    
    # https://en.wikipedia.org/wiki/Official_languages_of_the_United_Nations

    langs = (
        "ara",
        "zho",
        "eng",
        "spa",
        "fre",
        "rus",
        "por",	# proposed UN
        "ben",	# proposed UN
        "hin",	# proposed UN
        "tur",	# proposed UN
        "ger",	# because tilezen
        "jap",	# because tilezen
        "kor",	# because tilezen
        "ita",	# because tilezen
        "gre",	# because tilezen
        "vie",	# because tilezen
    )
    
    crawl = mapzen.whosonfirst.utils.crawl("/usr/local/data/whosonfirst-data/data", inflate=True)

    fieldnames = [ "wof:id", "wof:country", "wof:placetype", "wof:name", "coverage", "count" ] 
    fieldnames.extend(langs)

    fh = open("inventory.csv", "w")
    writer = cooperhewitt.csvtools.UnicodeWriter(fh, fieldnames=fieldnames)

    for feature in crawl:

        props = feature['properties']

        wofid = props['wof:id']
        placetype = props['wof:placetype']
        country = props['wof:country']
        name = props.get('wof:name', 'MISSING wof:name')

        out = {
            "wof:id": unicode(wofid),
            "wof:placetype": unicode(placetype),
            "wof:country": unicode(country),
            "wof:name": name,
        }
        
        coverage = 1
        total = 0

        for l in langs:

            preferred = "name:%s_x_preferred" % l
            count = len(props.get(preferred, []))

            out[ l ] = unicode(count)

            if count == 0:
                coverage = 0
            else:
                total += 1

        out['coverage'] = unicode(coverage)
        out['count'] = unicode(total)
        writer.writerow(out)
