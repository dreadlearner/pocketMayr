from pytube.helpers import cache
import wikipedia
from datetime import datetime
import time
import html
from bs4 import BeautifulSoup as bs
import numpy as np
import re
import pytube

# TODO: wikiresp.link

# TODO: vid, notes, and study objects

now = datetime.now()
day = str(now.day)
month = str(now.month)
year = str(now.year)
date = (f"{day}/{month}/{year}")
hour = int(now.hour)
minute = int(now.minute)
exitdoor = ("Exit", "exit", "quit", "Quit", "Cancel", "cancel")

if hour >= 17:
    time_of_day = "evening"
elif hour >= 12:
    time_of_day = "afternoon"
if hour < 12:
    time_of_day = "morning"

while True:
    print(f"\n{date} {hour}:{minute}")

    print("~"*25, f"\nGood {time_of_day}, welcome to apushTracker!\n","~"*25)

    random_message = np.random.randint(1, 4)
    if random_message == 1:
        print("\n",r"apushTracker is right 99.99% of the time!", "\n")
    if random_message == 2:
        print("\n",r"Mr.Mayr's a guide on the side!", "\n")
    if random_message == 3:
        print("\n",r"No! He's a sage on the stage!", "\n")

    query = input("Put your keyword here:")

    if query in exitdoor:
        exit()
    else:


        def unitfinder(year):
            year = int(year)
            if year < 1607:
                unit = 1
            if year > 1607 < 1754:
                unit = 2
            if year > 1754 < 1800:
                unit = 3
            if year > 1800 < 1848:
                unit = 4
            if year > 1848 < 1877:
                unit = 5
            if year > 1877 < 1898:
                unit = 6
            if year > 1898 < 1945:
                unit = 7
            if year > 1945 < 1980:
                unit = 8
            if year > 1980:
                unit = 9
            return unit


        # search wikipedia for the keyword
        class wikiresp:
            """
            wikiresp: wikiresp is an object that contains all the values to be
            displayed for a wikipedia search of the keyword. it returns:
            
            wikiresp.page: the page and all its relevant details
            
            wikiresp.err: represents an error code. if "nil", no error was returned.
            if "pageantry", PageError returned. if "disarmament", DisambiguationError
            returned. if "seriouscertificate", srsearch error returned.

            wikiresp.title: the title of the page

            wikiresp.content: the summary of the page

            wikiresp.link: a link to the full page
            """
            try:
                try:
                    page = wikipedia.search(query, results=1, suggestion=False)
                except:
                    page = wikipedia.search(query, results=1, suggestion=True)
                    pass
                if page != []:
                    err = "nil"
                    page = wikipedia.page(page)
                    link = "test"
                    title = page.title

                    wikihtml = page.html()

                    # parse the html page finding <body><div<div<table<tbody<tr<td class "infobox-data">8 May 2021</td>
                    soup = bs(wikihtml, features="lxml")
                    infodata = soup.find_all('td')

                    # split the date string into day, month, year

                    # use the year to determine what unit/time period it's part of
                    unit = unitfinder(year)
                    timeperiod = "0"

                    content = wikipedia.summary(query, sentences=3, auto_suggest=False)
                if page == []:
                    err = "seriouscertificate"
            except wikipedia.DisambiguationError as disam:
                errcontent = disam
                err = "disarmament"
                pass
            except wikipedia.PageError as page:
                errcontent = page
                err = "pageantry"
                pass


        class vid:
            unit = unitfinder(year)
            # create a list of videos for each unit
            if unit == 1: # THESE ALL NEED TO BE ACTUAL YOUTUBE LINKS, NOT THE EMBED ONES. THE EMBED ONES DON'T WORK
                videos = ["https://www.youtube.com/watch?v=2bWyFYcQQME", "https://www.youtube.com/watch?v=6pHHJqUDpDg", "https://www.youtube.com/watch?v=Zh_syCs0Pz8"]
            if unit == 2:
                videos = ["https://www.youtube.com/watch?v=LWfcXHMLaHU", "https://www.youtube.com/watch?v=CVy_9FhVfKE", "https://www.youtube.com/watch?v=kKL1UV5AiW0",
                "https://www.youtube.com/watch?v=aI-WuefcLMY", "https://www.youtube.com/watch?v=Jy0CBFnkhk4", "https://www.youtube.com/watch?v=h6jvAFpBgK4",
                "https://www.youtube.com/watch?v=e-wvspL_sk0"]
            if unit == 3:
                videos = ["https://youtu.be/5ty4aUqQXtI", "https://www.youtube.com/watch?v=eMEk3cVAy7s", "https://www.youtube.com/watch?v=4G_-6u_2A6I",
                "https://www.youtube.com/watch?v=eR1pm1IY2ns", "https://www.youtube.com/watch?v=xzryR174pdA", "https://www.youtube.com/watch?v=Z5VrogKap7Y"]
            if unit == 4:
                videos = ["https://www.youtube.com/watch?v=Xtl_f54uOEk", "https://www.youtube.com/watch?v=pgzSTdB7aTM&feature=emb_imp_woyt", "https://www.youtube.com/watch?v=Z_Af0G9_TdU",
                "https://www.youtube.com/watch?v=WZKTG_dRFG0", "https://www.youtube.com/watch?v=Wj8JuTmSwQ8", "https://www.youtube.com/watch?v=C2O00y1k31A",
                "https://www.youtube.com/watch?v=ycmUKpdBs-A", "https://www.youtube.com/watch?v=hQjpCKa2_ms"]
            if unit == 5:
                videos = ["https://www.youtube.com/watch?v=CIOgaUcd1n0", "https://www.youtube.com/watch?v=V7YwXGrF5p8", "https://www.youtube.com/watch?v=GBLuOH2_tFM",
                "https://www.youtube.com/watch?v=UaUuYbDnVUY", "https://www.youtube.com/watch?v=e6CRsl54Hg0", "https://www.youtube.com/watch?v=Z066CK0-H5E",
                "https://www.youtube.com/watch?v=SqCJ9PHMjhs", "https://www.youtube.com/watch?v=v4Jfwdoqgnw", "https://www.youtube.com/watch?v=VqKM8u1u1ZI",
                "https://www.youtube.com/watch?v=qL5ZI_t4Gy0", "https://www.youtube.com/watch?v=EyEsrpC4PUo", "https://www.youtube.com/watch?v=CfeAa3R5lfg",
                "https://www.youtube.com/watch?v=0YEJuoJDQKY", "https://www.youtube.com/watch?v=PlBbRXRzzp4", "https://www.youtube.com/watch?v=54vjFvxp0sk",
                "https://www.youtube.com/watch?v=aokrvNLUMUo&t=1s"]
            if unit == 6:
                videos = ["https://www.youtube.com/watch?v=KfGPNoOqV_U", "https://www.youtube.com/watch?v=DzEWzhPgwas", "https://www.youtube.com/watch?v=5QymghrvLiM",
                "https://www.youtube.com/watch?v=dO9MJqbCcuI", "https://www.youtube.com/watch?v=NY5Y4M6u0uU", "https://www.youtube.com/watch?v=3EbSO1vhbnc",
                "https://www.youtube.com/watch?v=LqLaQ1F0YFk", "https://www.youtube.com/watch?v=bBkfZP7T1Xk", "https://www.youtube.com/watch?v=gmbqzxHAm9k"
                "https://www.youtube.com/watch?v=F7LKIIThtPM&t", "https://www.youtube.com/watch?v=aq88f8qZbWs", "https://www.youtube.com/watch?v=csbplgLpS9I",
                "https://www.youtube.com/watch?v=0hsTpTc_T3M"]
            if unit == 7:
                videos - []
            if unit == 8:
                videos = []
            if unit == 9:
                videos = []
            # check captions for keyword. if keyword is found, return that video.
            for i in videos:
                captions = pytube.YouTube(i).captions['en'] # pull the captions
                re.findall(query, captions)
                if 

            # if keyword is not found, find the video that has dates closest to the time period. also return all videos for safety.
            if query not in result:
                content = unit.videos
            #title
            #timeperiod
            #content
            #link


        class study:
            x = 1
            unit = unitfinder(year)
            #title
            #timeperiod
            #content
            #link


        class notes:
            x = 1
            unit = unitfinder(year)
            #title
            #timeperiod
            #content
            #link


        print(f"\nYou queried: {query}\n")


        # query result page
        def wikiresult():
            print("~"*25)
            if wikiresp.err != "nil":
                if wikiresp.err == 'disarmament':
                    print(f"""\nUh-oh! We couldn't find a wikipedia page for that term!
        (Error: {wikiresp.err})
                    
        Please refine your search to match one of the following wikipedia pages:
                    
                    {wikiresp.errcontent}""")
                else:
                    print(f"""\nUh-oh! We couldn't find a wikipedia page for that term!
        (Error: {wikiresp.err})""")

            else:
                print(f"""

                Here's what I found from Wikipedia:
                APUSH Unit: {wikiresp.unit}
                Time Period: {wikiresp.timeperiod}
                Page Title: {wikiresp.title}

                Page Summary: 
                
                {wikiresp.content}

                Want to read the entire article? Type "show me the wikipedia article!"
                (This will open an external website)

                """)


        def vidresult():
            print("~"*25)
            if vid.err != "nil":
                print(f"""\nUh-oh! We couldn't find an APUSH video for that term!
                (Error: {vid.err})""")
            else:
                print(f"""
                Here's what I found from apushreview.com:
                APUSH Unit: {vid.unit}
                Time Period: {vid.timeperiod}
                Video Title: {vid.title}

                Video Summary: 
                
                {vid.description}

                Want to watch the entire video? Type "show me the video!"
                (This will open an external website)
                """)

            print("\n", "apush-apush-apush-apush"*3)


        def studyresult():
            print("~"*25)
            if study.err != "nil":
                print(f"""\nUh-oh! We couldn't find an apstudynotes page for that term!
                (Error: {study.err})""")
            else:
                print(f"""
            
                Here's what I found from apstudynotes.com:
                APUSH Unit: {study.unit}
                Time Period: {study.timeperiod}
                Page Title: {study.title}

                Page Summary: 
                
                {study.description}

                Want to read the entire page? Type "show me the study page!"
                (This will open an external website)

                """)
            print("apush-apush-apush-apush"*3)


        def notesresult():
            print("~"*25)
            if notes.err != "nil":
                print(f"""\nUh-oh! We couldn't find that in Mayr's notes!
                (Error: {notes.err})""")
            else:
                print(f"""
            
                Here's what I found from Mr. Mayr's notes:
                APUSH Unit: {notes.unit}
                Time Period: {notes.timeperiod}
                Page Title: {notes.title}

                Notes Summary: 
                
                {notes.description}

                Want to read the entire document? Type "show me Mayr's notes!"
                (This will open a Microsoft Word (.docx) document)

            """)

        wikiresult()
        #vidresult()
        #studyresult()
        #notesresult()