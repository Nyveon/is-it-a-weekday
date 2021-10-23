# is-it-a-weekday
Meme-module for "efficiently" checking whether a given day name is a weekday/weekend, with multi-language support.


## How does it determine the answer?
[flow chart to be inserted]

## What languages does it support?
 - English
 - Spanish
 - German
 - French
 - Other languages may or may not work. (Most likely they won't)

## Usage

`weekday()` Receives a string containing only the name of the day. Returns True if it is the name of a weekday, False if it is the name of a weekend, and an True or False if it is not a supported language or not the name of a day. 
`weekend()` Shortcut for `not weekday()`
