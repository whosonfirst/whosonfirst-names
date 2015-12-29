# whosonfirst-names

What things are called in Who's On First

## Names and aliases (and languages) – aka RFC 5646

Who's On First uses a variation of [RFC 5646](http://www.rfc-editor.org/rfc/rfc5646.txt) for identifying names. The W3C's [Language tags in HTML and XML](http://www.w3.org/International/articles) page describes RFC 5646 like this:

> RFC 5646 caters for more types of subtag, and allows you to combine them in various ways. While this may appear to make life much more complicated, generally speaking choosing language tags will continue to be a simple matter - however, where you need additional power it will be available to you. In fact, for most people, RFC 5646 should actually make life simpler in a number of ways – for one thing, there is only one place you need to look now for valid subtags.

> Although it provides some additional options for identifying common language variations, RFC 5646 includes all of the tags that were previously valid. If you have been using RFC 1766, RFC 3066, or RFC 4646 you do not need to make any changes to your tags.

> The list below shows the various types of subtag that are available. We will work our way through these and how they are used in the sections that follow.

> language-extlang-script-region-variant-extension-privateuse

### RFC 5646 (BCP 47) comformance

_Sometimes RFC 5646 is referred to as BCP (Best Current Practice) 47._

* We follow the same structure outlined in RFC 5646 but use `_` (underbar) characters instead of `-` (dash) characters for delimiting individual properties of a language identifier.

* We use three-letter country codes (rather than two-letter codes) to identify the primary language.

* The use of either the "script" or "region" subtags is allowed, although neither is required.

* While not explicitly forbidden neither the "extlang" or the "variant" subtags are commonly used, and Who's On First tools for parsing name labels may not support them.

* We use private extensions, specifically a `-x-[NAME_TYPE]` label.

### RFC 5646 (BCP 47) tag conversion

1. Replace the "_" separators with "-"
2. You probably want to replace 3-letter country codes with 2-letter country codes

#### For example

```
eng_x_preferred → en-x-preferred
fre_ca_x_variant → fr-ca-x-variant
```
     
### Code-y bits (and backwards compatibility)

The [mapzen.whosonfirst.names](https://github.com/whosonfirst/py-mapzen-whosonfirst-names) Python library provides libraries and functions for converting between `Who's on First`, `Geoplanet` and `RFC 5646 subtags`.

_Note: When converting to subtags the library does convert three-letter country codes to two-letter country codes._

For example:

```
import mapzen.whosonfirst.names

lbl = mapzen.whosonfirst.names.labels()
names = ("fin_p", "eng_s", "unk_v")

for n in names:
	print n

        n2 = lbl.convert(n, 'geoplanet', 'wof')
        print n2

        n3 = lbl.convert(n2, 'wof', 'subtags')
        print n3

        n4 = lbl.convert(n3, 'subtags', 'wof')
        print n4

        n5 = lbl.convert(n4, 'wof', 'geoplanet')
        print n5
```

Would yield:

```
fin_p
fin_x_prefered
fin-x-prefered
fin_x_prefered
fin_p
eng_s
eng_x_colloquial
eng-x-colloquial
eng_x_colloquial
eng_s
unk_v
und_x_variant
und-x-variant
und_x_variant
unk_v
```

## A short history

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
	"wof:name": "Montreal",
	"wof:lang": [ "eng", "fre" ],
	"name:eng_p": "Montreal",
	"name:eng_a": "YMQ",
	"name:fre_p": "Montréal",
	"name:kor_p": "몬트리올",
}
```

But wait, there's more!

One day we met [@nyampire](https://github.com/nyampire) who told us that he had [a gazetteer of places published by the Japanese government](https://github.com/nyampire/Gazetteer_JP_2007) that contained place names in Kanji, Kana and English. Since Kanji is a script the solution described above doesn't work. So now we're using RFC 5646 and subtags.

## See also

* https://github.com/whosonfirst/whosonfirst-data
* https://github.com/whosonfirst/whosonfirst-placetypes
* https://github.com/whosonfirst/whosonfirst-dates
* https://github.com/whosonfirst/whosonfirst-sources
* https://github.com/whosonfirst/py-mapzen-whosonfirst-names
* https://github.com/whosonfirst/py-mapzen-whosonfirst-languages
