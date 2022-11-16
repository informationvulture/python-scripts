## Preliminary note:
The [CAF website](https://forces.ca/) as of November 15, 2022 has the following `robots.txt` file:
```txt
# www.robotstxt.org/
# www.google.com/support/webmasters/bin/answer.py?hl=en&answer=156449

User-agent: *
Disallow:
```


This indicates that the webpage allows all robots complete access. However, this project **DOES NOT** collect any personal information or any other sensitive information, but only publicly available titles of careers listed on the [CAF website](https://forces.ca/).

## What is this project?
I often visit the CAF website to look at the different careers currently in demand, as I am interested in enlisting in the near future.


This project seeks to automate the collection of the indemand career titles, helping me see what the general trend is of the jobs currently being recruited for.



## What does this project use?
This project is made using Python.


## Current issues

##### 2022-11-15 10:40 PM
The scraping file works, but can't get all the jobs (currently 22) from the page. It gets the first, and then maybe 5 but misses a bunch in between.


Various testing has led me to conclude that this is a problem with loading, as it was seen at least once to provide more titles then it currently gives.



## Resources used:

Getting Selenium setup with chromedriver:
https://www.keeganleary.com/setting-up-chrome-and-selenium-with-python-on-a-virtual-private-server-digital-ocean/


Getting Selenium setup:
https://towardsdatascience.com/using-python-and-selenium-to-automate-filling-forms-and-mouse-clicks-f87c74ed5c0f