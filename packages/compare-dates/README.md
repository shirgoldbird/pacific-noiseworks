# Compare Dates

A simple plugin that provides 2 utilities:

1) The ability to get the current datetime with calling `current_datetime()`

2) The ability to compare 2 datetimes with `compare_dates()`

Example:

`{% if compare_dates(child.event_date, current_datetime()) %}`

This will check if `child.event_date >= current_datetime()`.
