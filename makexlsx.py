#!/usr/bin/env python3

from libpytunes import Library
from openpyxl import Workbook
from sys import argv
import time, datetime

def parseLibraryxml():
    l = Library(infile)
    wb=Workbook()
    ws=wb.active 
    allsongs = [['artist','album','trackname','kind','bit_rate','sample_rate','date_modified','date_added']]

    # iterate through all the songs, building the allsongs list of lists (each row is a song)
    for id,song in l.songs.items():
        if song and song.kind:
            # Let's boil the date_* fields down to something openpyxl can shove into a spreadsheet...
            date_modified = parse_datetime(song.date_modified)
            date_added = parse_datetime(song.date_added)

            thissong=[song.artist, song.album, song.name, song.kind, song.bit_rate, song.sample_rate, date_modified, date_added]
            allsongs.append(thissong)

    # take the allsongs list and dump it to XLSX
    for song in allsongs:
        ws.append(song)

    wb.save(xlfile)
    return(len(allsongs))

def parse_datetime(indate):
    try:
        outdate = datetime.datetime.fromtimestamp(time.mktime(indate))
    except:
        outdate = "UNKNOWN"
    return outdate

def main():
    count = parseLibraryxml()
    print(f"Generated {xlfile} with {count} rows from {infile}\nHave Fun!!\n")

if __name__ == "__main__":
    global infile, xlfile
    try:
        infile=argv[1]
    except:
        print('need the Library.xml filename, please.')
        print('Aborting...')
        exit(1)
    xlfile = infile[:len(infile)-4] + '.xlsx'
    main()