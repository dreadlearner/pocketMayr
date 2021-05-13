import time
import wikipedia
from datetime import datetime
from bs4 import BeautifulSoup as bs
import numpy as np
import re
import pytube
from CaptionTracks import units

# TODO: wikiresp.timeperiod

# TODO: notes, vocab, and study objects

# TODO: opening external links, programs, etc.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Pre-Loading Date and Time Variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

now = datetime.now()
day = int(now.day)
month = int(now.month)
year = int(now.year)
date = (f"{day}/{month}/{year}")
hour = int(now.hour)
minute = int(now.minute)
if minute > 10:
    minute = f'0{minute}'
exitdoor = ("Exit", "exit", "quit", "Quit", "Cancel", "cancel", 'leave', 'Leave')

if hour >= 17:
    time_of_day = "evening"
elif hour >= 12:
    time_of_day = "afternoon"
if hour < 12:
    time_of_day = "morning"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Printing Random Welcome Messages, accepting Queries~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
    print(f"\n{date} {hour}:{minute}")

    print("~"*25, f"\nGood {time_of_day}, welcome to pocketMayr!\n", "~"*25)

    random_message = np.random.randint(1, 7)
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


    query = input("Put your keyword here: ")

    if query in exitdoor:
        exit()
    else:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Define Unit-Finding Function based on time-period/year~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

        def timefinder(unit):
            unit = int(unit)
            if unit == 'unit1':
                year = '1607'
            if unit == 'unit2':
                year = '1607 - 1754'
            if unit == 'unit3':
                year = '1854 - 1800'
            if unit == 'unit4':
                year = '1800 - 1848'
            if unit == 'unit5':
                year = '1858 - 1877'
            if unit == 'unit6':
                year = '1877 - 1898'
            if unit == 'unit7':
                year = '1898 - 1945'
            if unit == 'unit8':
                year = '1945 - 1980'
            if unit == 'unit9':
                year = '1980 - Present'
            return year

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        class notes:
            # regex for query in each unit
            unitnotes = ['i', 'i', 'z']
            for i in unitnotes:
                found = re.findall(query, str(i))
                if found == [] and len(found) > 1:
                    err = "disarmament"
                    unit = str(i)
                    break
                elif found == [] and len(found) == 0:
                    err = 'pageantry'
                    unit = None
                else:
                    unit = str(i)
                    err = 'nil'
                    break
            if unit == None:
                err = 'pageantry'
            else:
                content = "1"

            # unit -> timeperiod
            #timeperiod = timefinder(unit)
            
            title = unit
            # take surrounding text (~ 2 lines up and down) for content
            
            #open the document

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Define a Class to search Wikipedia for the Query~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
                page = wikipedia.search(query, results=1, suggestion=False)
                page = wikipedia.WikipediaPage(page)
                if page != []:
                    err = "nil"
                    link = page.url
                    title = page.title
                    timeperiod = "0 - 1607"
                    unit = "1"

                    content = wikipedia.summary(query, sentences=3, auto_suggest=False)
                if page == []:
                    err = "disarmament"
            except wikipedia.DisambiguationError as disam:
                errcontent = disam
                err = "disarmament"
                pass
            except wikipedia.PageError as page:
                errcontent = page
                err = "pageantry"
                pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Define a Function to determine Videos from Unit~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        def unitdb(unit):
            # create a list of videos for each unit
            if unit == 'unit1':
                videos = ["https://www.youtube.com/watch?v=2bWyFYcQQME", "https://www.youtube.com/watch?v=6pHHJqUDpDg", "https://www.youtube.com/watch?v=Zh_syCs0Pz8"]
                subject = [units.unit1.video1.captions, units.unit1.video2.captions, units.unit1.video3.captions]
                timeperiod =  '0 - 1607'
            if unit == 'unit2':
                videos = ["https://www.youtube.com/watch?v=LWfcXHMLaHU", "https://www.youtube.com/watch?v=CVy_9FhVfKE", "https://www.youtube.com/watch?v=kKL1UV5AiW0",
                "https://www.youtube.com/watch?v=aI-WuefcLMY", "https://www.youtube.com/watch?v=Jy0CBFnkhk4", "https://www.youtube.com/watch?v=h6jvAFpBgK4",
                "https://www.youtube.com/watch?v=e-wvspL_sk0"]
                subject = [units.unit2.video1.captions, units.unit2.video2.captions, units.unit2.video3.captions, units.unit2.video4.captions, units.unit2.video5.captions,
                units.unit2.video6.captions, units.unit2.video7.captions]
                timeperiod =  '1607 - 1754'
            if unit == 'unit3':
                videos = ["https://youtu.be/5ty4aUqQXtI", "https://www.youtube.com/watch?v=eMEk3cVAy7s", "https://www.youtube.com/watch?v=4G_-6u_2A6I",
                "https://www.youtube.com/watch?v=eR1pm1IY2ns", "https://www.youtube.com/watch?v=xzryR174pdA", "https://www.youtube.com/watch?v=Z5VrogKap7Y"]
                subject = [units.unit3.video1.captions, units.unit3.video2.captions, units.unit3.video3.captions, units.unit3.video4.captions, units.unit3.video5.captions,
                units.unit3.video6.captions]
                timeperiod =  '1754 - 1800'
            if unit == 'unit4':
                videos = ["https://www.youtube.com/watch?v=Xtl_f54uOEk", "https://www.youtube.com/watch?v=pgzSTdB7aTM&feature=emb_imp_woyt", "https://www.youtube.com/watch?v=Z_Af0G9_TdU",
                "https://www.youtube.com/watch?v=WZKTG_dRFG0", "https://www.youtube.com/watch?v=Wj8JuTmSwQ8", "https://www.youtube.com/watch?v=C2O00y1k31A",
                "https://www.youtube.com/watch?v=ycmUKpdBs-A", "https://www.youtube.com/watch?v=hQjpCKa2_ms"]
                subject = [units.unit4.video1.captions, units.unit4.video2.captions, units.unit4.video3.captions, units.unit4.video4.captions, units.unit4.video5.captions,
                units.unit4.video6.captions, units.unit4.video7.captions, units.unit4.video8.captions]
                timeperiod =  '1800 - 1848'
            if unit == 'unit5':
                videos = ["https://www.youtube.com/watch?v=CIOgaUcd1n0", "https://www.youtube.com/watch?v=V7YwXGrF5p8", "https://www.youtube.com/watch?v=GBLuOH2_tFM",
                "https://www.youtube.com/watch?v=UaUuYbDnVUY", "https://www.youtube.com/watch?v=e6CRsl54Hg0", "https://www.youtube.com/watch?v=Z066CK0-H5E",
                "https://www.youtube.com/watch?v=SqCJ9PHMjhs", "https://www.youtube.com/watch?v=v4Jfwdoqgnw", "https://www.youtube.com/watch?v=VqKM8u1u1ZI",
                "https://www.youtube.com/watch?v=qL5ZI_t4Gy0", "https://www.youtube.com/watch?v=EyEsrpC4PUo", "https://www.youtube.com/watch?v=CfeAa3R5lfg",
                "https://www.youtube.com/watch?v=0YEJuoJDQKY", "https://www.youtube.com/watch?v=PlBbRXRzzp4", "https://www.youtube.com/watch?v=54vjFvxp0sk",
                "https://www.youtube.com/watch?v=aokrvNLUMUo&t=1s"]
                subject = [units.unit5.video1.captions, units.unit5.video2.captions, units.unit5.video3.captions, units.unit5.video4.captions, units.unit5.video5.captions,
                units.unit5.video6.captions, units.unit5.video7.captions, units.unit5.video8.captions, units.unit5.video9.captions, units.unit5.video10.captions,
                units.unit5.video11.captions, units.unit5.video12.captions, units.unit5.video13.captions, units.unit5.video14.captions, units.unit5.video15.captions]
                timeperiod =  '1848 - 1877'
            if unit == 'unit6':
                videos = ["https://www.youtube.com/watch?v=KfGPNoOqV_U", "https://www.youtube.com/watch?v=DzEWzhPgwas", "https://www.youtube.com/watch?v=5QymghrvLiM",
                "https://www.youtube.com/watch?v=dO9MJqbCcuI", "https://www.youtube.com/watch?v=NY5Y4M6u0uU", "https://www.youtube.com/watch?v=3EbSO1vhbnc",
                "https://www.youtube.com/watch?v=LqLaQ1F0YFk", "https://www.youtube.com/watch?v=bBkfZP7T1Xk", "https://www.youtube.com/watch?v=gmbqzxHAm9k"
                "https://www.youtube.com/watch?v=F7LKIIThtPM&t", "https://www.youtube.com/watch?v=aq88f8qZbWs", "https://www.youtube.com/watch?v=csbplgLpS9I",
                "https://www.youtube.com/watch?v=0hsTpTc_T3M"]
                subject = [units.unit6.video1.captions, units.unit6.video2.captions, units.unit6.video3.captions, units.unit6.video4.captions, units.unit6.video5.captions,
                units.unit6.video6.captions, units.unit6.video7.captions, units.unit6.video8.captions, units.unit6.video9.captions, units.unit6.video10.captions,
                units.unit6.video11.captions, units.unit6.video12.captions, units.unit6.video13.captions]
                timeperiod =  '1877 - 1898'
            if unit == 'unit7':
                videos = ["https://www.youtube.com/watch?v=IeGmfbRrJ5Y", "https://www.youtube.com/watch?v=0eT_B9g-ZaA", "https://www.youtube.com/watch?v=6cVgZsMczps",
                "https://www.youtube.com/watch?v=NwQrJNrRj7U", "https://www.youtube.com/watch?v=PpTNdN9MnRw"]
                subject = [units.unit7.video1.captions, units.unit7.video2.captions, units.unit7.video3.captions, units.unit7.video4.captions, units.unit7.video5.captions]
                timeperiod = '1898 - 1945' 
            if unit == 'unit8':
                videos = ["https://www.youtube.com/watch?v=IyOs5BJ3HGo", "https://www.youtube.com/watch?v=dfLmZdq6iQo", "https://www.youtube.com/watch?v=eseJiBno8Qk"]
                subject = [units.unit8.video1.captions, units.unit8.video2.captions, units.unit8.video3.captions]
                timeperiod =  '1945 - 1980'
            if unit == 'unit9':
                videos = ["https://www.youtube.com/watch?v=WzqeAXBwzqc", "https://www.youtube.com/watch?v=gvREnUWMKoU", "https://www.youtube.com/watch?v=LOJpTzjU7xc"]
                subject = [units.unit9.video1.captions, units.unit9.video2.captions, units.unit9.video3.captions]
                timeperiod =  '1980 - Present'
            return videos, subject, timeperiod

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Define a Class for regex-ing the Video Captions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        class vid:
            # query all unit captions, return time period. then query unit.video captions, return title, and url
            units = [units.unit1, units.unit2, units.unit3, units.unit4, units.unit5, units.unit6, units.unit7,
            units.unit8, units.unit9]
            for u in units:
                found = re.findall(str(query), u.captions)
                if found == [] and len(found) > 1:
                    err = "disarmament"
                    unit = str(u)
                    break
                elif found == [] and len(found) == 0:
                    err = 'pageantry'
                    unit = None
                else:
                    unit = str(u).split(".")
                    unit = unit[2].split("'>")
                    unit = unit[0]
                    err = 'nil'
                    break
            if unit == None:
                err = 'pageantry'
            else:
                videos, subject, daterange = unitdb(unit)

            # err handling
            if err == 'nil':
                timeperiod = daterange
                count = -1
                for i in subject:
                    count = int(count + 1)
                    vidfound = re.findall(str(query), str(i))
                    if vidfound != None:
                        link = str(videos[count]).replace("'", "")
                        videobj = pytube.YouTube(link)
                        description = videobj.description
                        title = videobj.title

                        content = f"\n{description}\n"
                        break
                    else:
                        err == 'pageantry'
            if err == 'disarmament':
                relevant = videos
            #if err == 'pageantry':
            #    unit = notes.unit
            #    videos, subject, timeperiod = unitdb(unit)
            #    link = str(videos[count]).replace("'", "")
            #    videobj = pytube.YouTube(link)
            #    description = videobj.description
            #    title = videobj.title
            #    timeperiod = timeperiod

            #    content = f"\n{description}\n"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       

        class study:
            x = 1
            unit = unitfinder(year)
            #title
            #timeperiod
            #content
            #link

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        class vocab:
            x = 1
            unit = unitfinder(year)
            #title
            #timeperiod
            #content
            #link

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        print(f"\nYou queried: {query}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # query result page
        def wikiresult():
            print("\n", "~"*25)
            if wikiresp.err != "nil":
                if wikiresp.err == 'disarmament':
                    print(f"""\nUh-oh! We couldn't find a wikipedia page for that term!
        (Error: {wikiresp.err})
                    
        Please refine your search to match one of the following wikipedia pages:
                    
                    {wikiresp.errcontent}""")
                else:
                    print(f"""\nUh-oh! We couldn't find a wikipedia page for that term!
        (Error: {wikiresp.err})\n""")
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        def vidresult():
            print("\n", "~"*25)
            if vid.err == "pageantry":
                print(f"""\nUh-oh! We couldn't find an APUSH video for that term!
        (Error: {vid.err})""")

            if vid.err == 'tiebreak':
                print(f"""\nUh-oh! We couldn't find an APUSH video for that term!
                (Error: {vid.err})
                
                Here are some that might be relevant:
                
                {vid.relevant}""")
            elif vid.err == 'nil':
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        def studyresult():
            print("\n", "~"*25)
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        def notesresult():
            print("\n", "~"*25)
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        wikiresult()
        action = input("What's next? ")
        if action == 'show me the wikipedia article!':
            # open the wikipedia article
            test = "test"
        if action == 'next!':
            vidresult()
        if action == 'show me the video!':
            # open the video
            test = "test"
        if action == 'next!':
            #studyresult()
            test = 'test'
        if action == 'show me the study page!':
            # open the webpage
            test = "test"
        if action == 'next!':
            #notesresult
            test = 'test'
        if action == "show me Mayr's notes!":
            # open the notes page
            test = "test"
        if action == 'next!':
            #vocabresult
            test = 'test'
        if action == "show me Mayr's vocab":
            # open the vocab page
            test = "test"
        else:
            break