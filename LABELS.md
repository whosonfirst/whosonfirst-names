# LABELS

## What?

The back-story is that one day I said:

```
It's not so much a "mailing address" as it different types of labels / names for a place

short name (Montreal) versus long name (Montreal, Quebec, Canada) versus in-between-name
(Montreal, QC, Canada)

versus names that no one uses (Montreal, Montreal (county), Quebec, Canada) versus the part
where the English have two towns with the same name in the same region so you have to
disambiguate on county

versus names with neighbourhoods which would be a hilarious trend to start with the postal
service

as of this writing there are only short names but there should be others, yes

also versus things with postal codes that sometimes make no sense, like a display label for
a geotagged photo

so, I think what would be useful / helpful is to start identifying the kinds of labels we
need to pre-calculate

and from there we can start to write an opencagedata style spec for actually generating them
based on country / locale / etc.
```

So this is that document.

See also: [whosonfirst-names](https://github.com/whosonfirst/whosonfirst-names).

## Use Cases

### {lang}_x_colloquial

The colloquial, informal label for a place (inclusive of hierarchy).

_Example: eng_x_colloquial_

```
"label:eng_x_colloquial": "Fairfax, Virginia, USA"
```


### {lang}_x_colloquial_abbreviation

The colloquial, informal abbreviation for a place (inclusive of hierarchy).

_Example: eng_x_colloquial_abbreviation_

```
"label:eng_x_colloquial_abbreviation": "SFO, California, USA"
```


### {lang}_x_historical

The historical label for a place (inclusive of hierarchy).

_Example: zho_x_historical_

```
"label:eng_x_historical": "Yerba Buena, California, USA"
```

### {lang}_x_preferred

The fully qualified "preferred" label for a place (inclusive of hierarchy), in practice a single element list. Used in Pelias and to generate language-specific map labels. The `label:{lang}_x_preferred` property takes precedence over `wof:label`.

_Example: kor_x_preferred_

```
"label:eng_x_preferred": "Fairfax city, Virginia, USA"
```

### {lang}_x_preferred_abbreviation

The "preferred" label for a place name (exclusive of hierarchy), in practice a single element list. Used in Pelias and to generate language-specific map labels.

_Example: kor_x_preferred_abbreviation_

```
"label:eng_x_preferred_abbreviation": ["U.S.A."]
"label:eng_x_preferred_abbreviation": ["Calif."]
"label:eng_x_preferred_abbreviation": ["Va."]
"label:eng_x_preferred_abbreviation": ["Maine"]
"label:eng_x_preferred_abbreviation": ["Ore."]
"label:eng_x_preferred_abbreviation": ["S.F. Int'l Airport"]
```

### {lang}_x_preferred_disambiguation

The "preferred" disambiguation label for a place (exclusive of hierarchy), in practice a single element list. Either append the feature's placetype or append the parent's name in parenthesis.

_Example: kor_x_preferred_disambiguation_

```
"label:eng_x_variant_disambiguation": ["Fairfax city"]
"label:eng_x_variant_disambiguation": ["Fairfax county"]
"label:eng_x_variant_disambiguation": ["Portland (Maine)"]
"label:eng_x_variant_disambiguation": ["Portland (Oregon)"]
```

### {lang}_x_preferred_placetype

A feature's "preferred" placetype label (exclusive of place name and hierarchy), in practice a single element list. While `wof:placetype` is an enumerated value, this localized value is a string.

_Example: kor_x_preferred_placetype_

```
"label:eng_x_preferred_placetype": ["parish"]
"label:eng_x_preferred_placetype": ["local government area"]
```

### {lang}_x_preferred_shortcode

A feature's "preferred" localized shortcode that takes precedence over `wof:shortcode` (exclusive of place name and hierarchy), in practice a single element list. 

A short alphabetic code, preferring 3-characters for `country` (e.g. **USA**), 2-characters for `region` (e.g. **CA**), and either 3-characer or 2-character for `county` (e.g. **HUM** or **HU**) placetypes. Other placetypes like `venue` can also have shortcodes but their length is not standardized, and they may contain alphanumeric values.

_Example: eng_x_preferred_shortcode_ 

```
"label:eng_x_preferred_shortcode": ["US"]
"label:eng_x_preferred_shortcode": ["CA"]
"label:eng_x_preferred_shortcode": ["ME"]
"label:eng_x_preferred_shortcode": ["OR"]
"label:eng_x_preferred_shortcode": ["VA"]
"label:eng_x_preferred_shortcode": ["SFO"]
"label:eng_x_preferred_shortcode": ["SF"]
"label:eng_x_variant_shortcode": ["HUM"]
```

_WARNING: do not confuse `{lang}_x_preferred_shortcode` and `wof:shortcode` properties with the deprecated `wof:abbreviation` or `wof:country_alpha3` properties._

### {lang}_x_unknown

Uncommon "unclassified" labels used for a place (inclusive of hierarchy).

_Example: nep_x_unknown_

### {lang}_x_variant

Uncommon "variant" labels used for a place (inclusive of hierarchy). Used in mapping and geocoding software and to generate language-specific map labels.

_Example: deu_x_variant_

### {lang}_x_variant_abbreviation

Uncommon "variant" abbreviations used for a place (exclusive of hierarchy).

_Example: deu_x_variant_abbreviation_

```
"label:eng_x_variant_abbreviation": ["S.F.O. Int'l Airport"]
"label:eng_x_variant_abbreviation": ["S.F."]
"label:eng_x_variant_abbreviation": ["USA", "U.S."]
"label:eng_x_variant_abbreviation": ["Cali."]
```

### {lang}_x_variant_disambiguation


Uncommon "variant" disambiguation labels for a place (exclusive of hierarchy). Either append the feature's placetype or append the parent's name in parenthesis.

_Example: deu_x_variant_disambiguation_

```
"label:eng_x_variant_disambiguation": ["Portland (ME)"]
"label:eng_x_variant_disambiguation": ["Portland (OR)", "Portland (Ore.)"]
```

### {lang}_x_variant_placetype

Uncommon "variant" placetype labels (exclusive of hierarchy). While `wof:placetype` is an enumerated value, this value is a string value.

_Example: deu_x_variant_placetype_

```
"label:eng_x_preferred_placetype": ["Parish"]
"label:eng_x_variant_placetype": ["LGA", "lga", "L.G.A.", "l.g.a.", "local gov't area"]
```

### {lang}_x_variant_shortcode

Uncommon localized shortcodes (exclusive of hierarchy).

A short alphabetic code, preferring 3-characters for `country` (e.g. **USA**), 2-characters for `region` (e.g. **CA**), and either 3-characer or 2-character for `county` (e.g. **HUM** or **HU**) placetypes. Other placetypes like `venue` can also have shortcodes but their length is not standardized, and they may contain alphanumeric values.

_Example: label:deu_x_variant_shortcode_

```
"label:eng_x_variant_shortcode": ["KSFO"]
"label:eng_x_variant_shortcode": ["HU"]
```
