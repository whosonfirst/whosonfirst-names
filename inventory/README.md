# inventory

Tools and data dumps for inventorying preferred name support across languages in Who's On First.

## Caveat

It's early days so I don't imagine the tools or the data do everything that people need them to do...

## Working with the data

The `inventory.py` script produces a CSV file so probably the easiest thing is converting that file in to SQLite database using [csv2sqlite](https://github.com/whosonfirst/whosonfirst-csv2sqlite), like this:

```
csv2sqlite wof-languages.db languages wof:id,wof:country,wof:placetype,wof:name,coverage,count,ara,zho,eng,spa,fre,rus,por,ben,hin,tur,ger inventory.csv
```