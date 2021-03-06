import wikipedia
from datetime import datetime
import numpy as np
import re
import pytube
import webbrowser
from CaptionTracks import units
from notes import notes as notesimport
from vocabnotes import vocabnotes
from rich.console import Console
console = Console()

# TODO: vocab note uploads to Google Docs

now = datetime.now()
day = int(now.day)
month = int(now.month)
year = int(now.year)
date = (f"{day}/{month}/{year}")
hour = int(now.hour)
minute = int(now.minute)

if minute < 10: 
    minute = f'0{minute}'

exitdoor = ("Exit", "exit", "quit", "Quit", "Cancel", "cancel", 'leave', 'Leave')

if hour >= 17:
    time_of_day = "evening"
elif hour >= 12:
    time_of_day = "afternoon"
if hour < 12:
    time_of_day = "morning"

while True:
    console.print(f"\n[bold cyan]{date} {hour}:{minute}[/bold cyan]", highlight=False)

    console.print("~"*25, f"\nGood {time_of_day}, welcome to [bold green]pocketMayr[/bold green]!\n", "~"*25, highlight=False)

    random_message = np.random.randint(1, 10)
    if random_message == 1:
        console.print("\n",r"pocketMayr is right 99.99% of the time!", "\n", highlight=False)
    if random_message == 2:
        console.print("\n",r"I'm a guide on the side!", "\n", highlight=False)
    if random_message == 3:
        console.print("\n",r"I'm a sage on the stage!", "\n", highlight=False)
    if random_message == 4:
        console.print("\n",r"Cool cool cool.", "\n", highlight=False)
    if random_message == 5:
        console.print("\n",r"Mmm. Love me some Diet Coke.", "\n", highlight=False)
    if random_message == 6:
        console.print("\n",r"'I've got the horses in the back...'", "\n", highlight=False)
    if random_message == 7:
        console.print("\n",r"Rohan, we know you have a microphone...", "\n", highlight=False)
    if random_message == 8:
        console.print("\n",r"Ok, then prove it.", "\n")
    if random_message == 9:
        console.print("\n", "But can you back it up? Do you have evidence?", "\n")
    if random_message == 10:
        console.print("\n", "What's up Macy? Good talk, good talk...", "\n")

    console.print("Enter [bold green]'man'[/bold green] into the keyword if you'd like to read the manual page", highlight=False)
    query = input("Put your keyword here: ")

    querylower = query.lower()

    if querylower in exitdoor:
        exit()
    if querylower == 'man':
        webbrowser.open('https://docs.google.com/document/d/1k7ts1-0yaveE-ZIPNRj7AhPiy0q680a_SDZc2lSjP6g/edit?usp=sharing')
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

        def timefinder(unit):
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

        def unitdb(unit):
            if unit == 'unit1':
                videolinks = ["https://www.youtube.com/watch?v=2bWyFYcQQME", "https://www.youtube.com/watch?v=6pHHJqUDpDg", "https://www.youtube.com/watch?v=Zh_syCs0Pz8"]
                vocab = vocabnotes.unit1.dictionary
                subjectvideo = [units.unit1.video1.captions, units.unit1.video2.captions, units.unit1.video3.captions]
                note = [notesimport.unit1.ki11, notesimport.unit1.ki12, notesimport.unit1.ki13, notesimport.unit1.ki14]
                notelinks = ['https://docs.google.com/document/d/1yJkSumMR0N5W5bXYWRzeQiqYMFlzXBUosOMBYKVJh_g/edit?usp=sharing',
                'https://docs.google.com/document/d/1574t6LyOoxUxia8QC8YQXbQCepHltuxU2SLE7RAaybI/edit?usp=sharing',
                'https://docs.google.com/document/d/1nR5iFWasmllHfrN6SQ5fKID_uInvCCD25PZs_JcMszU/edit?usp=sharing',
                'https://docs.google.com/document/d/1GQZwljULbwgpAFQZ9I-dx2VmhRZ_PRfnfokZk5M1kBI/edit?usp=sharing']
                timeperiod =  '0 - 1607'
            if unit == 'unit2':
                videolinks = ["https://www.youtube.com/watch?v=LWfcXHMLaHU", "https://www.youtube.com/watch?v=CVy_9FhVfKE", "https://www.youtube.com/watch?v=kKL1UV5AiW0",
                "https://www.youtube.com/watch?v=aI-WuefcLMY", "https://www.youtube.com/watch?v=Jy0CBFnkhk4", "https://www.youtube.com/watch?v=h6jvAFpBgK4",
                "https://www.youtube.com/watch?v=e-wvspL_sk0"]
                subjectvideo = [units.unit2.video1.captions, units.unit2.video2.captions, units.unit2.video3.captions, units.unit2.video4.captions, units.unit2.video5.captions,
                units.unit2.video6.captions, units.unit2.video7.captions]
                vocab = vocabnotes.unit2.dictionary
                note = [notesimport.unit2.ki21, notesimport.unit2.ki22, notesimport.unit2.ki23, notesimport.unit2.ki24, notesimport.unit2.ki25]
                notelinks = ['https://docs.google.com/document/d/1ptnT4Un3fbXoUw4raZTrGKS8qB5uoXmTgp-TqPaQJ38/edit?usp=sharing',
                'https://docs.google.com/document/d/10l_6ur4FxHHhBWXg6hY0kUekyyO0Eo-4m939vhGmXoA/edit?usp=sharing',
                'https://docs.google.com/document/d/1OXW-ulmLNgpVMpsdnw13hikSy2BpjkCEFo8pid7-cIc/edit?usp=sharing',
                'https://docs.google.com/document/d/1bra_wH_3vnEOolvdgMUv9FAo1L3kjGS5pRJJ8BfPR4A/edit?usp=sharing',
                'https://docs.google.com/document/d/1yF6q9eHoYZn84szdKnrj-70nE0tdqhAjGgMflGZAB4A/edit?usp=sharing']
                timeperiod =  '1607 - 1754'
            if unit == 'unit3':
                videolinks = ["https://youtu.be/5ty4aUqQXtI", "https://www.youtube.com/watch?v=eMEk3cVAy7s", "https://www.youtube.com/watch?v=4G_-6u_2A6I",
                "https://www.youtube.com/watch?v=eR1pm1IY2ns", "https://www.youtube.com/watch?v=xzryR174pdA", "https://www.youtube.com/watch?v=Z5VrogKap7Y"]
                subjectvideo = [units.unit3.video1.captions, units.unit3.video2.captions, units.unit3.video3.captions, units.unit3.video4.captions, units.unit3.video5.captions,
                units.unit3.video6.captions]
                vocab= vocabnotes.unit3.dictionary
                note = [notesimport.unit3.ki31, notesimport.unit3.ki32, notesimport.unit3.ki33, notesimport.unit3.ki34, notesimport.unit3.ki35, notesimport.unit3.ki36, notesimport.unit3.ki37]
                notelinks = ['https://docs.google.com/document/d/1so3fM3nX4sUFfuOilskk5w8SuChKx9Y_JtJ8WmwOVeY/edit?usp=sharing',
                'https://docs.google.com/document/d/1_RofzPY2EVGzz_4iC_70Gde1kWkZKnkcli8uPlBXmvM/edit?usp=sharing',
                'https://docs.google.com/document/d/14VBxfyMc8xgel80V0AxLh-DFNDA4vCImEyffonzZFA8/edit?usp=sharing',
                'https://docs.google.com/document/d/1vJLsWhIW7ZlJI7a22SZtGIvW_bjd_A2GCQmtvFiJkoA/edit?usp=sharing',
                'https://docs.google.com/document/d/15fc-wl3Ao3qX1HMbIIA13oVv4RKEY6CUULuSWdiKSgA/edit?usp=sharing',
                'https://docs.google.com/document/d/1LXO2uF0V5xEQay-8bGDFrj9gRHs2hxSR4gE6k6D2wyM/edit?usp=sharing',
                'https://docs.google.com/document/d/1ppaRIjqA7m7tMLG-vAfVVbMjXeKxE2VmDqQunamqddo/edit?usp=sharing']
                timeperiod =  '1754 - 1800'
            if unit == 'unit4':
                videolinks = ["https://www.youtube.com/watch?v=Xtl_f54uOEk", "https://www.youtube.com/watch?v=pgzSTdB7aTM&feature=emb_imp_woyt", "https://www.youtube.com/watch?v=Z_Af0G9_TdU",
                "https://www.youtube.com/watch?v=WZKTG_dRFG0", "https://www.youtube.com/watch?v=Wj8JuTmSwQ8", "https://www.youtube.com/watch?v=C2O00y1k31A",
                "https://www.youtube.com/watch?v=ycmUKpdBs-A", "https://www.youtube.com/watch?v=hQjpCKa2_ms"]
                subjectvideo = [units.unit4.video1.captions, units.unit4.video2.captions, units.unit4.video3.captions, units.unit4.video4.captions, units.unit4.video5.captions,
                units.unit4.video6.captions, units.unit4.video7.captions, units.unit4.video8.captions]
                vocab = vocabnotes.unit4.dictionary
                note = [notesimport.unit4.ki41, notesimport.unit4.ki42, notesimport.unit4.ki43, notesimport.unit4.ki44, notesimport.unit4.ki45, notesimport.unit4.ki46]
                notelinks = ["https://docs.google.com/document/d/1kbIgm7E5E_chErNSFG8FjgVJx6AdsXbbfNvKEJ4jB70/edit?usp=sharing",
                "https://docs.google.com/document/d/1XLDr2CXXjds0Fj1bM7SytN3r19adzlQ6a70g99iM7_E/edit?usp=sharing",
                "https://docs.google.com/document/d/1peFwWGRXESCH7lLoGQZmHBAfDdSzf8kb0CJQxO1GEZ8/edit?usp=sharing",
                "https://docs.google.com/document/d/1DzS-n04NOr0Ye6wN7N29pWi5n0XPdGbVECFKvpbPUgY/edit?usp=sharing",
                "https://docs.google.com/document/d/1SUotMoNGULOF80EfspdazgfIryqAqjZz9zGrrxfQFD8/edit?usp=sharing",
                "https://docs.google.com/document/d/1eCxehxuXJZ6YgkSVzP1T5tvhyCatRnPrMjojzUETwuo/edit?usp=sharing"]
                timeperiod =  '1800 - 1848'
            if unit == 'unit5':
                videolinks = ["https://www.youtube.com/watch?v=CIOgaUcd1n0", "https://www.youtube.com/watch?v=V7YwXGrF5p8", "https://www.youtube.com/watch?v=GBLuOH2_tFM",
                "https://www.youtube.com/watch?v=UaUuYbDnVUY", "https://www.youtube.com/watch?v=e6CRsl54Hg0", "https://www.youtube.com/watch?v=Z066CK0-H5E",
                "https://www.youtube.com/watch?v=SqCJ9PHMjhs", "https://www.youtube.com/watch?v=v4Jfwdoqgnw", "https://www.youtube.com/watch?v=VqKM8u1u1ZI",
                "https://www.youtube.com/watch?v=qL5ZI_t4Gy0", "https://www.youtube.com/watch?v=EyEsrpC4PUo", "https://www.youtube.com/watch?v=CfeAa3R5lfg",
                "https://www.youtube.com/watch?v=0YEJuoJDQKY", "https://www.youtube.com/watch?v=PlBbRXRzzp4", "https://www.youtube.com/watch?v=54vjFvxp0sk",
                "https://www.youtube.com/watch?v=aokrvNLUMUo&t=1s"]
                subjectvideo = [units.unit5.video1.captions, units.unit5.video2.captions, units.unit5.video3.captions, units.unit5.video4.captions, units.unit5.video5.captions,
                units.unit5.video6.captions, units.unit5.video7.captions, units.unit5.video8.captions, units.unit5.video9.captions, units.unit5.video10.captions,
                units.unit5.video11.captions, units.unit5.video12.captions, units.unit5.video13.captions, units.unit5.video14.captions, units.unit5.video15.captions]
                vocab = vocabnotes.unit5.dictionary
                note = [notesimport.unit5.ki51, notesimport.unit5.ki52, notesimport.unit5.ki53, notesimport.unit5.ki54, notesimport.unit5.ki55]
                notelinks = ["https://docs.google.com/document/d/1QVddX8w2U8fAt4B-frqIi_HLg1hl94SSsTTvh27WukU/edit?usp=sharing",
                "https://docs.google.com/document/d/13qCrsrokm-xodkJLgfdejFa_v7kADXjEdf1_O2NiIFY/edit?usp=sharing",
                "https://docs.google.com/document/d/1XI2BEdyFrZcqPuNR_DXze-iiY9lwpcRBBXxaFHUTASI/edit?usp=sharing",
                "https://docs.google.com/document/d/1G1e9U8eQCC6aES1GyxmeknBPEEj02z3gqcF4PkUq0r8/edit?usp=sharing",
                "https://docs.google.com/document/d/1tV1vwZxnRxBdeKOAPNpacIMAQzNwF4kbWed4gMRfuOk/edit?usp=sharing"]
                timeperiod =  '1848 - 1877'
            if unit == 'unit6':
                videolinks = ["https://www.youtube.com/watch?v=KfGPNoOqV_U", "https://www.youtube.com/watch?v=DzEWzhPgwas", "https://www.youtube.com/watch?v=5QymghrvLiM",
                "https://www.youtube.com/watch?v=dO9MJqbCcuI", "https://www.youtube.com/watch?v=NY5Y4M6u0uU", "https://www.youtube.com/watch?v=3EbSO1vhbnc",
                "https://www.youtube.com/watch?v=LqLaQ1F0YFk", "https://www.youtube.com/watch?v=bBkfZP7T1Xk", "https://www.youtube.com/watch?v=gmbqzxHAm9k"
                "https://www.youtube.com/watch?v=F7LKIIThtPM&t", "https://www.youtube.com/watch?v=aq88f8qZbWs", "https://www.youtube.com/watch?v=csbplgLpS9I",
                "https://www.youtube.com/watch?v=0hsTpTc_T3M"]
                subjectvideo = [units.unit6.video1.captions, units.unit6.video2.captions, units.unit6.video3.captions, units.unit6.video4.captions, units.unit6.video5.captions,
                units.unit6.video6.captions, units.unit6.video7.captions, units.unit6.video8.captions, units.unit6.video9.captions, units.unit6.video10.captions,
                units.unit6.video11.captions, units.unit6.video12.captions, units.unit6.video13.captions]
                vocab = vocabnotes.unit6.dictionary
                note = [notesimport.unit6.ki61, notesimport.unit6.ki62, notesimport.unit6.ki63, notesimport.unit6.ki64, notesimport.unit6.ki65, notesimport.unit6.ki66, notesimport.unit6.ki67]
                notelinks = ["https://docs.google.com/document/d/1aTJ-caO58SGH3zxTdxT3GcIDy1YijgjMM_Y5wItsMf4/edit?usp=sharing",
                "https://docs.google.com/document/d/1MDVXLC0xsaMwq8enzoSWhqM5Gm1pMQ2xNHA7iTsb7N8/edit?usp=sharing",
                "https://docs.google.com/document/d/13eDdsRb2Cu4QBeLMkZDoBVKzj8ep8zjsdtnlfQpukXs/edit?usp=sharing",
                "https://docs.google.com/document/d/1C3dcR-OH7wyWgnY4qGcSVTTxzhdfDnD10jsWwkPwcvQ/edit?usp=sharing",
                "https://docs.google.com/document/d/1F7YIZh4rG19KNFYCBZZQZtk2ijZfcQQ16UkyVTC2MYA/edit?usp=sharing",
                "https://docs.google.com/document/d/16cDlLFPVP55_sUqzSqrw09ZpkrdoYYUZUWNDlMEynN8/edit?usp=sharing",
                "https://docs.google.com/document/d/1azxwrZXGdkDY97Bsjy5SxlcLr3uGvOG0xI_1-mwIars/edit?usp=sharing"]
                timeperiod =  '1877 - 1898'
            if unit == 'unit7':
                videolinks = ["https://www.youtube.com/watch?v=IeGmfbRrJ5Y", "https://www.youtube.com/watch?v=0eT_B9g-ZaA", "https://www.youtube.com/watch?v=6cVgZsMczps",
                "https://www.youtube.com/watch?v=NwQrJNrRj7U", "https://www.youtube.com/watch?v=PpTNdN9MnRw"]
                subjectvideo = [units.unit7.video1.captions, units.unit7.video2.captions, units.unit7.video3.captions, units.unit7.video4.captions, units.unit7.video5.captions]
                note = [notesimport.unit7.ki71, notesimport.unit7.ki72, notesimport.unit7.ki73, notesimport.unit7.ki74, notesimport.unit7.ki75, notesimport.unit7.ki76, notesimport.unit7.ki77, notesimport.unit7.ki78]
                vocab = vocabnotes.unit7.dictionary
                notelinks = ["https://docs.google.com/document/d/1WLx-HyC9A5LjPlc4wzuB8_OfsJnTUF-FfXR9cmkQ0F4/edit?usp=sharing",
                "https://docs.google.com/document/d/1KYK8o0s50aW2-X-vsG6pw2uxgXWICLaKMb5enw89lJk/edit?usp=sharing",
                "https://docs.google.com/document/d/1PIXW8T6-TkPHLn2mYf04kjy5S2q_BAaGqjtlDnkC3MU/edit?usp=sharing",
                "https://docs.google.com/document/d/1QBr2z-qPW_UJMCBz2cil73V1UgAWQkle8-UNCegT-4o/edit?usp=sharing",
                "https://docs.google.com/document/d/1wXf4hTE-8yVoQ67zcZyFtkHVyhGixgpBnMcdfqg53CE/edit?usp=sharing",
                "https://docs.google.com/document/d/1Q0qSgEMj5zR4FsyVGPfNirDy5TtIqQ_e8TTjo55nOs4/edit?usp=sharing",
                "https://docs.google.com/document/d/1UrDf7ZKXRNwvbVAQ2qP-OA7jCu500UyJsWoLSM9ognU/edit?usp=sharing",
                "https://docs.google.com/document/d/1DKxfYhgAlaWLaz4P7sRnYaaHKM3U_3eF6g-cr5iV2D4/edit?usp=sharing"]
                timeperiod = '1898 - 1945'
            if unit == 'unit8':
                videolinks = ["https://www.youtube.com/watch?v=IyOs5BJ3HGo", "https://www.youtube.com/watch?v=dfLmZdq6iQo", "https://www.youtube.com/watch?v=eseJiBno8Qk"]
                subjectvideo = [units.unit8.video1.captions, units.unit8.video2.captions, units.unit8.video3.captions]
                vocab = vocabnotes.unit8.dictionary
                note = [notesimport.unit8.ki81, notesimport.unit8.ki82, notesimport.unit8.ki83, notesimport.unit8.ki84, notesimport.unit8.ki85, notesimport.unit8.ki86]
                notelinks = ["https://docs.google.com/document/d/1K_Je4JYVP36YCMwMKl6p8VwlDr4_TsfSwIsvQzpR74M/edit?usp=sharing",
                "https://docs.google.com/document/d/157x_QdGhUmVOdYcXPmXA_sbhn49euaT6R15HsvrZudA/edit?usp=sharing",
                "https://docs.google.com/document/d/1JdKQrEbaN9OJhlpgF1GarnBkETH8imPGEm5mgrwGI20/edit?usp=sharing",
                "https://docs.google.com/document/d/1zLGpzp_Y5A4BGXu44YW7zGl4SoTfO6m9UrMvHBY6rCU/edit?usp=sharing",
                "https://docs.google.com/document/d/1G3DQBvpatxD5gYlxN6FNN_6MqCUmRfQdcX6hLUK3FmM/edit?usp=sharing",
                "https://docs.google.com/document/d/18qvjbSUd_xPH39k6AXIjw9WUtPNDotSxdx8Li0r-cD8/edit?usp=sharing"]
                timeperiod =  '1945 - 1980'
            if unit == 'unit9':
                videolinks = ["https://www.youtube.com/watch?v=WzqeAXBwzqc", "https://www.youtube.com/watch?v=gvREnUWMKoU", "https://www.youtube.com/watch?v=LOJpTzjU7xc"]
                subjectvideo = [units.unit9.video1.captions, units.unit9.video2.captions, units.unit9.video3.captions]
                note = [notesimport.unit9.ki91, notesimport.unit9.ki92, notesimport.unit9.ki93]
                vocab = vocabnotes.unit9.dictionary
                notelinks = ["https://docs.google.com/document/d/1_Ccdsy8Zgd_P4MRR3HkLdOjKp2s7NukUJGRmfA3Xx24/edit?usp=sharing",
                "https://docs.google.com/document/d/1H4mpb_RBoElM_yGvgP3HCSOZ9eiz0yTcrJf3vBBI4F4/edit?usp=sharing",
                "https://docs.google.com/document/d/1T6nZPZlofimuo8FOrkjJBNKU6XD7a-NxAc97Bfh9DWc/edit?usp=sharing"]
                timeperiod =  '1980 - Present'
            return videolinks, subjectvideo, note, notelinks, timeperiod, vocab

        class notes:
            """
            notes: notes is an object that contains all the values to
            be returned for a search of the keyword in Mr. Mayr's notes.
            it returns the following to the user:

            notes.title: the title of the notes

            notes.err: an error code. if 'nil', no error was returned.
            if 'pageantry', the term was not found.

            notes.unit: the unit that the notes are part of

            notes.timeperiod: the time period that the notes are part of

            notes.content: the term, surrounded by 125 characters of the
            notes page

            notes.link: a link to the Google Doc containing the notes
            """
            try:
                # regex for query in each unit
                unitnotes = [notesimport.unit1, notesimport.unit2, notesimport.unit3, notesimport.unit4, notesimport.unit5, notesimport.unit6, notesimport.unit7,
                notesimport.unit8, notesimport.unit9]
                for i in unitnotes:
                    found = re.search(str(querylower), str(i.content).lower())
                    if found == None:
                        err = 'pageantry'
                        unit = None
                    else:
                        unit = str(i).split(".")
                        unit = str(unit[2]).replace("'>", "")
                        found = str(found[0])
                        err = 'nil'
                        break

                if unit == None:
                    err = 'pageantry'
                else:
                    videos, subjectvideo, notes, notelinks, daterange, vocab = unitdb(unit)

                if err == 'nil':
                    timeperiod = daterange
                    count = -1
                    for i in notes:
                        notetext = str(i.content)
                        count = int(count + 1)
                        notesfound = re.search(str(querylower), str(i.content).lower())

                        if notesfound != None:
                            title = i.title
                            
                            pos = notesfound.span()

                            querylength = pos[1] - pos[0]

                            start1 = int(pos[0] - 125)
                            end1 = pos[0]
                            start2 = pos[1]
                            end2 = int(pos[1] + 125)

                            content = f"...{notetext[start1:end1]}[bold yellow]{notetext[pos[0]:pos[1]]}[/bold yellow]{notetext[start2:end2]}..."

                            link = notelinks[count]
                            break
            except:
                err = 'u-noun'
                pass

        # search wikipedia for the keyword
        class wikiresp:
            """
            wikiresp: wikiresp is an object that contains all the values to be
            displayed for a wikipedia search of the keyword. it returns the
            following to the user:
            
            wikiresp.page: the page and all its relevant details
            
            wikiresp.err: represents an error code. if "nil", no error was returned.
            if "pageantry", PageError returned. if "disarmament", DisambiguationError
            returned. if "seriouscertificate", srsearch error returned.

            wikiresp.title: the title of the page

            wikiresp.content: the summary of the page

            wikiresp.link: a link to the full page
            """
            try:
                page = wikipedia.search(querylower, results=1, suggestion=False)
                page = wikipedia.WikipediaPage(page)
                if page != []:
                    err = "nil"
                    link = page.url
                    title = page.title
                    timeperiod = notes.timeperiod
                    unit = notes.unit

                    content = wikipedia.summary(querylower, sentences=3, auto_suggest=False)
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
            except:
                err = 'u-noun'
                pass

        class vid:
            """
            vid: vid is an object that contains all the values to be
            returned for a search of the keyword in Adam Norris'
            APUSH Videos. It returns the following to the user:

            vid.err: an error code. if "nil", no error was returned. if
            "disarmament", there were more than one videos returned. if
            "pageantry", no video was found.

            vid.unit: the unit that the video is part of

            vid.timeperiod: the time period the video is a part of

            vid.link: a link to the YouTube video itself

            vid.title: the title of the video

            vid.content: the description
            """
            try:# query all unit captions, return time period. then query unit.video captions, return title, and url
                units = [units.unit1, units.unit2, units.unit3, units.unit4, units.unit5, units.unit6, units.unit7,
                units.unit8, units.unit9]
                for u in units:
                    found = re.findall(str(querylower), str(u.captions).lower())
                    if found == [] and len(found) > 1:
                        err = "disarmament"
                        unit = str(u)
                        break
                    elif found == [] and len(found) == 0 or found == None:
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
                    videos, subjectvideo, dontuse, notelinks, daterange, vocab = unitdb(unit)

                if err == 'nil':
                    timeperiod = daterange
                    count = -1
                    for i in subjectvideo:
                        count = int(count + 1)
                        vidfound = re.findall(str(querylower), str(i).lower())
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
                if err == 'pageantry':
                    pass
            except:
                err = 'u-noun'
                pass

        class vocab:
            """
            vocab: vocab is an object that contains all the values to be
            returned for a search of the keyword in Mr. Mayr's vocab. It
            returns the following to the user:

            vocab.err: an error code.

            vocab.unit: the unit that the term is in

            vocab.timeperiod: the timeperiod that the vocab word is in

            vocab.link: a link to the vocab page

            vocab.title: the word that was queried

            vocab.content: the definition of the term
            """
            try:
                vocabunits = [vocabnotes.unit1, vocabnotes.unit2, vocabnotes.unit3, vocabnotes.unit4, vocabnotes.unit5, vocabnotes.unit6, vocabnotes.unit7, vocabnotes.unit8, vocabnotes.unit9]
                for z in vocabunits:
                    found = re.search(str(querylower), str(z.dictionary.keys()).lower())
                    if found == [] and len(found) > 1:
                        err = "disarmament"
                        unit = str(z)
                        break
                    elif found == [] and len(found) == 0 or found == None:
                        err = 'pageantry'
                        unit = None
                    else:
                        unit = str(z).split(".")
                        unit = unit[2].split("'>")
                        unit = unit[0]
                        err = 'nil'
                        dictionary = {k.lower(): v for k, v in z.dictionary.items()}
                        break
                if unit == None:
                    err = 'pageantry'
                else:
                    try:
                        content = dictionary[f'{querylower}']
                    except KeyError:
                        content = dictionary[f'{querylower} ']
                    timeperiod = timefinder(unit)
                    link = 1112223334
                    title = query
            except:
                err = 'u-noun'
                pass

        console.print(f"\nYou queried: [bold yellow]{query}[/bold yellow]", highlight=False)

        def wikiresult():
            console.print("\n", "~"*25, highlight=False)
            if wikiresp.err != "nil":
                if wikiresp.err == 'disarmament':
                    console.print(f"""\nUh-oh! We couldn't find a wikipedia page for that term!
        (Error: {wikiresp.err})
                    
        Please refine your search to match one of the following wikipedia pages:
                    
                    {wikiresp.errcontent}
                    
                    type [bold green]"next!"[/bold green] to view the next result...""", highlight=False)
                else:
                    console.print(f"""\nUh-oh! We couldn't find a wikipedia page for that term!
        (Error: {wikiresp.err})
        
        type [bold green]"next!"[/bold green] to view the next result...""", highlight=False)
            else:
                console.print(f"""

                Here's what I found from [bold magenta]Wikipedia[/bold magenta]:
                APUSH Unit: [bold pink]{wikiresp.unit}[/bold pink]
                Time Period: [bold blue]{wikiresp.timeperiod}[/bold blue]
                Page Title: [bold yellow]{wikiresp.title}[/bold yellow]

                Page Summary: 
                
                {wikiresp.content}

                Want to read the entire article? Type [bold green]"show me the wikipedia article!"[/bold green]
                (This will open a Wikipedia article [bold red](!!external website!!)[/bold red])

                Or, type [bold green]"next!"[/bold green] to view the next result...
                """, highlight=False)
            console.print("\n", "~"*25, highlight=False)

        def vidresult():
            console.print("\n", "~"*25)
            if vid.err == "pageantry":
                console.print(f"""\nUh-oh! We couldn't find an APUSH video for that term!
        (Error: {vid.err})
        
        type [bold green]"next!"[/bold green] to view the next result...""", highlight=False)

            if vid.err == 'tiebreak':
                console.print(f"""\nUh-oh! We couldn't find an APUSH video for that term!
                (Error: {vid.err})
                
                Here are some that might be relevant:
                
                {vid.relevant}
                
                type [bold green]"next!"[/bold green] to view the next result...""", highlight=False)
            elif vid.err == 'nil':
                console.print(f"""
                Here's what I found from [bold magenta]apushreview.com[/bold magenta]:
                APUSH Unit: [bold pink]{vid.unit}[/bold pink]
                Time Period: [bold blue]{vid.timeperiod}[/bold blue]
                Video Title: [bold yellow]{vid.title}[/bold yellow]

                Video Summary: 
                
                {vid.content}

                Want to watch the entire video? Type [bold green]"show me the video!"[/bold green]
                (This will open a YouTube video [bold red](!!external website!!)[/bold red])

                Or, type [bold green]"next!"[/bold green] to view the next result...
                """, highlight=False)
            console.print("\n", "~"*25, highlight=False)

        def vocabresult():
            console.print("\n", "~"*25)
            if vocab.err != "nil":
                console.print(f"""\nUh-oh! We couldn't find a Vocab entry for that term!
                (Error: {vocab.err})
                
                type [bold green]"next!"[/bold green] to enter a new keyword...""", highlight=False)
            else:
                console.print(f"""
            
                Here's what I found from [bold magenta]Mr. Mayr's Vocab[/bold magenta]:
                APUSH Unit: [bold pink]{vocab.unit}[/bold pink]
                Time Period: [bold blue]{vocab.timeperiod}[/bold blue]
                Vocab Word: [bold yellow]{vocab.title}[/bold yellow]

                Vocab Definition:
                
                {vocab.content}

                Want to read the entire page? Type [bold green]"show me Mr. Mayr's vocab![/bold green]"
                (This will open a Google Doc [bold red](!!external website!!)[/bold red])

                Or, type [bold green]"next!"[/bold green] to enter another keyword...
                """, highlight=False)
            console.print("\n", "~"*25, highlight=False)

        def notesresult():
            console.print("\n", "~"*25)
            if notes.err != "nil":
                console.print(f"""\nUh-oh! We couldn't find that in Mr. Mayr's notes!
                (Error: {notes.err})
                
                Type [bold green]"next!"[/bold green] to view the next result...""", highlight=False)
            else:
                console.print(f"""
            
                Here's the first occurence of that term in [bold magenta]Mr. Mayr's notes[/bold magenta]:
                APUSH Unit: [bold pink]{notes.unit}[/bold pink]
                Time Period: [bold blue]{notes.timeperiod}[/bold blue]
                Page Title: [bold yellow]{notes.title}[/bold yellow]

                Notes In-Context:
                
                {notes.content}

                Want to read the entire document? Type [bold green]"show me Mr. Mayr's notes!"[/bold green]
                (This will open a Google Doc [bold red](!!external website!!)[/bold red])

                Or, type [bold green]"next!"[/bold green] to view the next result...
                """, highlight=False)
            console.print("\n", "~"*25, highlight=False)

        wikiresult()
        action = input("\nWhat's next? ")
        if action == 'show me the wikipedia article!':
            # open the wikipedia article
            webbrowser.open(wikiresp.link)
            action = input("\nWhat's next? ")
        if action == 'next!' or action == 'next':
            vidresult()
            action = input("\nWhat's next? ")
        if action == 'show me the video!':
            # open the video
            webbrowser.open(vid.link)
            action = input("\nWhat's next? ")
        if action == 'next!' or action == 'next':
            notesresult()
            action = input("\nWhat's next? ")
        if action == "show me Mr. Mayr's notes!":
            # open the notes page
            webbrowser.open(notes.link)
            action = input("\nWhat's next? ")
        if action == 'next!' or action == 'next':
            vocabresult()
            action = input("\nWhat's next? ")
        if action == "show me Mr. Mayr's vocab":
            # open the vocab page
            test = "test"
            action = input("\nWhat's next? ")
        if action in exitdoor:
                exit()
