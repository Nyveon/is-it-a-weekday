# is-it-a-weekday
Meme-module for "efficiently" checking whether a given day name is a weekday/weekend, with multi-language support.


## How does it determine the answer?
 - If it ends in 'g', 'h', or 'y' it is English or German
   - It is a weekday if the first letter is not 's'
 - If it ends in 'i', 'e' or 's' it is Spanish or French
   - It is a weekday if the third letter is not 'm' pr 'b'
 - Otherwise, it assumes it is a weekday because `statistics`


## What languages does it support?
 - English
 - Spanish
 - German
 - French
 - Other languages may or may not work. (Most likely they won't)


## Usage

`weekday()` Receives a string containing only the name of the day. Returns True if it is the name of a weekday, False if it is the name of a weekend, and an True or False if it is not a supported language or not the name of a day. 

`weekend()` Shortcut for `not weekday()`
