Create a regular expression to retrieve a subset data from the purpose column of the taxdata table in the readonly database. Write a regular expressions to retrieve that meet the following criteria:
Lines that end with with 4 or more digits

SELECT purpose FROM taxdata WHERE purpose ~ 'regex' ORDER BY purpose DESC LIMIT 3;


[0-9]{4,}$


[0-9]: Matches any digit from 0 to 9.
{4,}: Specifies that the preceding character class (digit) must appear 4 or more times.
$: Anchors the pattern to the end of the string.

