import wikipedia
import datetime
from bs4 import BeautifulSoup as bs
import numpy as np
import re
import pytube
from CaptionTracks import units

# TODO: wikiresp.timeperiod

# TODO: vid, notes, vocab, and study objects

# TODO: opening external links, programs, etc.

# TODO: response handling for each printed result

# TODO: steal dates and timeperiods from other functions for the end of the vidsearch

now = datetime.now()
day = int(now.day)
month = int(now.month)
year = int(now.year)
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

    print("~"*25, f"\nGood {time_of_day}, welcome to pocketMayr!\n", "~"*25)

    random_message = np.random.randint(1, 4)
    if random_message == 1:
        print("\n",r"pocketMayr is right 99.99% of the time!", "\n")
    if random_message == 2:
        print("\n",r"I'm a guide on the side!", "\n")
    if random_message == 3:
        print("\n",r"I'm a sage on the stage!", "\n")
    if random_message == 4:
        print("\n",r"Cool cool cool.", "\n")
    if random_message == 5:
        print("\n",r"Mmm. Love me some diet Coke.", "\n")
    if random_message == 6:
        print("\n",r"I've got the horses in the back...", "\n")


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
                    link = page.url
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
            # query all unit captions, return time period. then query unit.video captions, return title, and url
            units = [Units.unit1, Units.unit2, Units.unit3, Units.unit4, Units.unit5, Units.unit6, Units.unit7, Units.unit8, Units.unit9]
            for u in units:
                found = re.findall(query, u.captions)
                if len(found) != 1:
                    err = "tiebreak"
                    unit = str(u)
                elif found == None:
                    err = 'nonefound'
                    pass
                else:
                    unit = str(u)
                    err = 'nil'
            # create a list of videos for each unit
            if unit == 'Units.unit1':
                videos = ["https://www.youtube.com/watch?v=2bWyFYcQQME", "https://www.youtube.com/watch?v=6pHHJqUDpDg", "https://www.youtube.com/watch?v=Zh_syCs0Pz8"]
                subject = [Units.unit1.video1.captions, Units.unit1.video2.captions, Units.unit1.video3.captions]
                timeperiod =  '0 - 1607'
            if unit == 'Units.unit2':
                videos = ["https://www.youtube.com/watch?v=LWfcXHMLaHU", "https://www.youtube.com/watch?v=CVy_9FhVfKE", "https://www.youtube.com/watch?v=kKL1UV5AiW0",
                "https://www.youtube.com/watch?v=aI-WuefcLMY", "https://www.youtube.com/watch?v=Jy0CBFnkhk4", "https://www.youtube.com/watch?v=h6jvAFpBgK4",
                "https://www.youtube.com/watch?v=e-wvspL_sk0"]
                subject = [Units.unit2.video1.captions, Units.unit2.video2.captions, Units.unit2.video3.captions, Units.unit2.video4.captions, Units.unit2.video5.captions,
                Units.unit2.video6.captions, Units.unit2.video7.captions]
                timeperiod =  '1607 - 1754'
            if unit == 'Units.unit3':
                videos = ["https://youtu.be/5ty4aUqQXtI", "https://www.youtube.com/watch?v=eMEk3cVAy7s", "https://www.youtube.com/watch?v=4G_-6u_2A6I",
                "https://www.youtube.com/watch?v=eR1pm1IY2ns", "https://www.youtube.com/watch?v=xzryR174pdA", "https://www.youtube.com/watch?v=Z5VrogKap7Y"]
                subject = [Units.unit3.video1.captions, Units.unit3.video2.captions, Units.unit3.video3.captions, Units.unit3.video4.captions, Units.unit3.video5.captions,
                Units.unit3.video6.captions]
                timeperiod =  '1754 - 1800'
            if unit == 'Units.unit4':
                videos = ["https://www.youtube.com/watch?v=Xtl_f54uOEk", "https://www.youtube.com/watch?v=pgzSTdB7aTM&feature=emb_imp_woyt", "https://www.youtube.com/watch?v=Z_Af0G9_TdU",
                "https://www.youtube.com/watch?v=WZKTG_dRFG0", "https://www.youtube.com/watch?v=Wj8JuTmSwQ8", "https://www.youtube.com/watch?v=C2O00y1k31A",
                "https://www.youtube.com/watch?v=ycmUKpdBs-A", "https://www.youtube.com/watch?v=hQjpCKa2_ms"]
                subject = [Units.unit4.video1.captions, Units.unit4.video2.captions, Units.unit4.video3.captions, Units.unit4.video4.captions, Units.unit4.video5.captions,
                Units.unit4.video6.captions, Units.unit4.video7.captions, Units.unit4.video8.captions]
                timeperiod =  '1800 - 1848'
            if unit == 'Units.unit5':
                videos = ["https://www.youtube.com/watch?v=CIOgaUcd1n0", "https://www.youtube.com/watch?v=V7YwXGrF5p8", "https://www.youtube.com/watch?v=GBLuOH2_tFM",
                "https://www.youtube.com/watch?v=UaUuYbDnVUY", "https://www.youtube.com/watch?v=e6CRsl54Hg0", "https://www.youtube.com/watch?v=Z066CK0-H5E",
                "https://www.youtube.com/watch?v=SqCJ9PHMjhs", "https://www.youtube.com/watch?v=v4Jfwdoqgnw", "https://www.youtube.com/watch?v=VqKM8u1u1ZI",
                "https://www.youtube.com/watch?v=qL5ZI_t4Gy0", "https://www.youtube.com/watch?v=EyEsrpC4PUo", "https://www.youtube.com/watch?v=CfeAa3R5lfg",
                "https://www.youtube.com/watch?v=0YEJuoJDQKY", "https://www.youtube.com/watch?v=PlBbRXRzzp4", "https://www.youtube.com/watch?v=54vjFvxp0sk",
                "https://www.youtube.com/watch?v=aokrvNLUMUo&t=1s"]
                subject = [Units.unit5.video1.captions, Units.unit5.video2.captions, Units.unit5.video3.captions, Units.unit5.video4.captions, Units.unit5.video5.captions,
                Units.unit5.video6.captions, Units.unit5.video7.captions, Units.unit5.video8.captions, Units.unit5.video9.captions, Units.unit5.video10.captions,
                Units.unit5.video11.captions, Units.unit5.video12.captions, Units.unit5.video13.captions, Units.unit5.video14.captions, Units.unit5.video15.captions]
                timeperiod =  '1848 - 1877'
            if unit == 'Units.unit6':
                videos = ["https://www.youtube.com/watch?v=KfGPNoOqV_U", "https://www.youtube.com/watch?v=DzEWzhPgwas", "https://www.youtube.com/watch?v=5QymghrvLiM",
                "https://www.youtube.com/watch?v=dO9MJqbCcuI", "https://www.youtube.com/watch?v=NY5Y4M6u0uU", "https://www.youtube.com/watch?v=3EbSO1vhbnc",
                "https://www.youtube.com/watch?v=LqLaQ1F0YFk", "https://www.youtube.com/watch?v=bBkfZP7T1Xk", "https://www.youtube.com/watch?v=gmbqzxHAm9k"
                "https://www.youtube.com/watch?v=F7LKIIThtPM&t", "https://www.youtube.com/watch?v=aq88f8qZbWs", "https://www.youtube.com/watch?v=csbplgLpS9I",
                "https://www.youtube.com/watch?v=0hsTpTc_T3M"]
                subject = [Units.unit6.video1.captions, Units.unit6.video2.captions, Units.unit6.video3.captions, Units.unit6.video4.captions, Units.unit6.video5.captions,
                Units.unit6.video6.captions, Units.unit6.video7.captions, Units.unit6.video8.captions, Units.unit6.video9.captions, Units.unit6.video10.captions,
                Units.unit6.video11.captions, Units.unit6.video12.captions, Units.unit6.video13.captions]
                timeperiod =  '1877 - 1898'
            if unit == 'Units.unit7':
                videos = ["https://www.youtube.com/watch?v=IeGmfbRrJ5Y", "https://www.youtube.com/watch?v=0eT_B9g-ZaA", "https://www.youtube.com/watch?v=6cVgZsMczps",
                "https://www.youtube.com/watch?v=NwQrJNrRj7U", "https://www.youtube.com/watch?v=PpTNdN9MnRw"]
                subject = [Units.unit7.video1.captions, Units.unit7.video2.captions, Units.unit7.video3.captions, Units.unit7.video4.captions, Units.unit7.video5.captions]
                timeperiod = '1898 - 1945' 
            if unit == 'Units.unit8':
                videos = ["https://www.youtube.com/watch?v=IyOs5BJ3HGo", "https://www.youtube.com/watch?v=dfLmZdq6iQo", "https://www.youtube.com/watch?v=eseJiBno8Qk"]
                subject = [Units.unit8.video1.captions, Units.unit8.video2.captions, Units.unit8.video3.captions]
                timeperiod =  '1945 - 1980'
            if unit == 'Units.unit9':
                videos = ["https://www.youtube.com/watch?v=WzqeAXBwzqc", "https://www.youtube.com/watch?v=gvREnUWMKoU", "https://www.youtube.com/watch?v=LOJpTzjU7xc"]
                subject = [Units.unit9.video1.captions, Units.unit9.video2.captions, Units.unit9.video3.captions]
                timeperiod =  '1980 - Present'
            if err == 'nil':
                for i, z in subject, videos:
                    vidfound = re.findall(query, i)
                    if vidfound != None:
                        url = z
                        description = pytube.YouTube(z).description

                        content = str("\n", url, "\n", description, "\n")
                    else:
                        err == 'nonefound'
            if err == 'tiebreak':
                content = videos
            if err == 'nonefound':
                content = 'No video found! Here are some that might be relevant:'
                # take date/time period from wikisearch or sum and pass videos from that unit
                

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

        
        class vocab:
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

                Or, type "next!" to view the next result...
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
                
                {vid.content}

                Want to watch the entire video? Type "show me the video!"
                (This will open an external website)

                Or, type "next!" to view the next result...
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

                Or, type "next!" to view the next result...
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

                Or, type "next!" to view the next result...
                """)

        wikiresult()
        #vidresult()
        #studyresult()
        #notesresult()
