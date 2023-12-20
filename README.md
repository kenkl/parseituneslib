# parseitunes
### Parses Library.xml from iTunes/Music to generate a summary spreadsheet of a library.

I had the need/desire to sift through my decades-old iTunes/Music library, looking for low bitrate rips. The goal is to update (rerip) albums that I care about to the now-standard lossless format (ALAC), given that disk-space and bandwidth have gotten a lot cheaper than it was 20 years ago.

This project utilizes [Liam Kaufman's](https://github.com/liamks) excellent iTunes Library Parser, [libpytunes](https://github.com/liamks/libpytunes) to do the heavy-lifting of processing an exported Library.xml from Apple Music. It's embedded in this project, requiring no additional installation. With the parsing it provides, makexlsx.py extracts the Artist, Album, Track Name, Kind (MP3, MP4, AAC, ALAC, etc.) of encoding used, Bit Rate, Sample Rate, Date Modified, and Date Added as tracked by iTunes/Apple Music. It then creates a standard .xlsx (Excel) spreadsheet that can be used to filter, sort, and otherwise find tracks (or characteristics of tracks) of interest in the library.

[libpytunes](https://github.com/liamks/libpytunes) uses six, and makexlsx.py uses openpyxl; both are expressed in requirements.txt. In a venv (ideally), install the prereqs with 
```
pip install -r requirements.txt
```
...and then run the parsing/creation with 
```
python3 makexlsx.py Library.xml
``` 

This will generate the .xlsx in the same directory as the .xml, presenting a view of the library similar to this:
![alt text](https://github.com/kenkl/parseituneslib/blob/aff4ad9002b30c46b9e183ff82051d6bbb7a5a8a/sssample.jpg "spreadsheet sample")

If a track is known only from adding it via Apple Music, the date fields are not present, breaking my parsing of the dates, so they're simply marked as 'UNKNOWN' for these purely cloud-hosted tracks. 

Compilations are not handled specially here (unlike in iTunes/Music), so those tracks/albums will be intermingled with all the rest, depending on sorting/order used in the resulting spreadsheet.
