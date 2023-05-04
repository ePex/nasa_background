# nasa_background

Downloads the Astronomy Picture of the Day from the nasa api and set's it as background image on you macOS

I use this in combination with a crontab entry to automate this every day at 9:00 am.
To do this just run ``` crontab -e ``` and add the following line: ``` 0 9 * * * /path/to/python/ /path/to/script/nasa_background.py ```

## Requirements

* macOS
* python
* requests module
