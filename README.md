# whosonfirst-names

What things are called in Who's On First

## Names and aliases (and languages)

In the beginning:

* We had names according to QuattroShapes

* We re-indexed all the names, aliases and translations from WOE (7.10) and concordances
  between WOE and the Gazetteer for many of them. Those we don't have
  concordances for will simply be imported in to the Gazetteer as new records
  complete with their names and aliases.

* We had concordances for many places in Geonames which also has many of its
  own aliases and translations, sometimes exceeding those of WOE

WOE defines two properties for a name:

1. a [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) language code
2. a name "type", which is a canned list as defined by the WOE folks:

```
The Name_Type field is a single letter code that describes the alias
as follows:

  * P is a preferred English name
  * Q is a preferred name (in other languages)
  * V is a well-known (but unofficial) variant for the place
      (e.g. "New York City" for New York)
  * S is either a synonym or a colloquial name for the place
      (e.g. "Big Apple" for New York), or a version of the name which
      is stripped of accent characters.
  * A is an abbreviation or code for the place (e.g. "NYC" for New
      York)
```

WOE also distinguishes between a `name` and an `alias` so in their world you end
up with something like:

```
Name:  Montréal 
Language: FRE
Alias (ENG_P): Montreal
Alias (KOR_Q): 몬트리올
```

WOE does not however account for the fact that [some
countries](https://www.youtube.com/watch?v=OHzMTSK1V4o) have multiple
languages.

With all that in mind, decided that:

* We should support multiple languages for a place and label placement
* We should just use `p` for a preferred name, regardless of language
* We should use a `name` namespace for names because it is explicit (likewise
  for `fullname`)
* `wof:name` is English by default and is a string (rather than a list of strings) that can be used for labels
 
For example:

```
{
	"name:name": "Montreal",
	"wof:lang": [ "eng", "fre" ],
	"name:eng_p": "Montreal",
	"name:eng_a": "YMQ",
	"name:fre_p": "Montréal",
	"name:kor_p": "몬트리올",
}
```

## See also

* https://github.com/whosonfirst/whosonfirst-data
* https://github.com/whosonfirst/whosonfirst-placetypes
* https://github.com/whosonfirst/whosonfirst-dates
* https://github.com/whosonfirst/whosonfirst-sources
