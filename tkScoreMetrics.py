import tkinter as tk
import random
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageSequence

class ScoreMetrics:
    def __init__(self):
        #Create Window
        self.HomeWindow = tk.Tk()
        self.HomeWindow.title("Speed Typing Scoring Metrics")
        self.HomeWindow.geometry(f'800x700+{(self.HomeWindow.winfo_screenwidth() - 800) // 2}+{((self.HomeWindow.winfo_screenheight() - 60) - 700) // 2}')
        self.HomeWindow.resizable(False, False)
        #Background Image/GIF
        self.BackgroundImage = PhotoImage(file="link.png")
        self.BackgroundLabel = tk.Label(self.HomeWindow, image=self.BackgroundImage)
        self.BackgroundLabel.place(relheight=1, relwidth=1)
        
        #Home Screen Title
        self.LabelTitle = tk.Label(self.HomeWindow, text="Speed Typing Scoring Metrics", anchor="center", justify="center", font=("Franklin Gothic Demi Cond", 30, "italic"), fg="#00C4D4")
        self.LabelTitle.pack(pady=30)
        
        self.Gif = Image.open('cat.gif')
        self.PixelFrame = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.Gif)]

        self.count = 0

        #Animation for GIF
        def Animation(count):
            self.GifLabel.configure(image=self.PixelFrame[count])
            self.count = (count + 1) % len(self.PixelFrame)
            self.HomeWindow.after(50, Animation, self.count)

        self.GifLabel = tk.Label(self.HomeWindow)
        self.GifLabel.pack()
        Animation(self.count)

        self.HomeScreen()
        #Main Loop
        self.HomeWindow.mainloop()

    def HomeScreen(self):
        self.HomeWindow.deiconify()

        #Checking if there's an Open Window
        if hasattr(self, 'ResultWindow') and self.ResultWindow:
            self.ResultWindow.destroy()

        if hasattr(self, 'Result') and self.Result:
            self.Result.destroy()

        if hasattr(self, 'criteriaWindow') and self.criteriaWindow:
            self.criteriaWindow.destroy()
        
        #Frame
        self.Home = tk.Frame(self.HomeWindow)
        self.Home.pack()

        #Buttons
        self.CalculateButton = tk.Button(self.Home, text="Calculate Scores", borderwidth=5, bg="cyan", font=("Exo 2 Medium", 12), width=20, height=1, command=self.CalculateScores)
        self.RankingButton = tk.Button(self.Home, text="See Rankings", borderwidth=5, bg="cyan", font=("Exo 2 Medium", 12), width=20, height=1, command=self.DisplayResult)
        self.MetricsButton = tk.Button(self.Home, text="See Scoring Metrics", borderwidth=5, bg="cyan", font=("Exo 2 Medium", 12), width=20, height=1, command=self.Criteria)

        self.CalculateButton.pack(pady=15)
        self.RankingButton.pack(pady=15)
        self.MetricsButton.pack(pady=15)


    def CalculateScores(self):
        global EntryFrame, NumberOfEntry

        self.Home.destroy()

        EntryFrame = tk.Frame(self.HomeWindow)
        EntryFrame.pack(pady=10)

        self.EntryLabel = tk.Label(EntryFrame, text="Number of Participants:", font=("Exo 2 Medium", 12))
        NumberOfEntry = tk.Entry(EntryFrame, font=("Roboto Serif 36pt Light", 12), bg="#D4F0F7", borderwidth=1)
        self.EntryLabel.grid(row=0, column=0)
        NumberOfEntry.grid(row=0, column=1, padx=7)

        self.DoneButton = tk.Button(EntryFrame,text="(Meow Meow) Done!!", borderwidth=5, bg="cyan", font=("Exo 2 Medium", 12), command=self.Participants)
        self.DoneButton.grid(row=1, column=0, columnspan=2, pady=10)

        NumberOfEntry.bind("<Return>", self.Participants)

    def Participants(self):
        global ParticipantStatistic, ParticipantEntries, TotalEntry

        self.EntryHeader = ["Name", "Accuracy", "Consistency", "T.C (s)", "W.P.M"]
        ParticipantStatistic = {}
        ParticipantEntries = {}

        TotalEntry =  int(NumberOfEntry.get())
        self.HomeWindow.withdraw()
        
        #Creating New Window
        self.InputWindow = tk.Toplevel()
        self.InputWindow.geometry(f'900x700+{(self.HomeWindow.winfo_screenwidth() - 900) // 2}+{(self.HomeWindow.winfo_screenheight() - 750) // 2}')
        self.InputWindow.title("Participants Statistics")

        #New Frame
        self.ParticipantsFrame = tk.Frame(self.InputWindow)
        self.ParticipantsFrame.pack()

        #Frame Label
        self.FrameLabel = tk.Label(self.ParticipantsFrame, text="Enter the Participants Name and their Speed Test Result", font=("Franklin Gothic Demi Cond", 20), fg="#00C4D4")
        self.FrameLabel.grid(row=0, column=0, columnspan=5)

        for col, header in enumerate(self.EntryHeader):
            header = tk.Label(self.ParticipantsFrame, text=header, background='#F6DAE4', font=("Exo 2 Medium", 10), width=10)
            header.grid(row=1, column=col)

        #Frame for Canvas
        self.CanvasFrame = tk.Frame(self.ParticipantsFrame)
        self.CanvasFrame.grid(row=2, column=0, columnspan=5, sticky='nw')
        self.CanvasFrame.grid_rowconfigure(0, weight=1)
        self.CanvasFrame.grid_columnconfigure(0, weight=1)
        self.CanvasFrame.grid_propagate(False)

        #Canva
        self.Canvas = tk.Canvas(self.CanvasFrame)
        self.Canvas.grid(row=0, column=0, sticky="news")

        #ScrollBar
        self.ScrollBar = tk.Scrollbar(self.CanvasFrame, orient='vertical', command=self.Canvas.yview)
        self.ScrollBar.grid(row=0, column=5, sticky='ns')
        self.Canvas.configure(yscrollcommand=self.ScrollBar.set)

        #Frame for Inputs
        self.InputFrame = tk.Frame(self.Canvas)
        self.Canvas.create_window((0,0), window=self.InputFrame, anchor='nw')

        for participants in range(2, TotalEntry + 2):
            status = []
            for stats in range(0, 5):
                information = tk.Entry(self.InputFrame, font=( "Roboto Serif 36pt Light", 10), bg="#D4F0F7", borderwidth=1)
                information.grid(row=participants, column=stats, pady=2, padx=15)
                status.append(information)
            participant_id = f'Participant_{participants-1}'
            ParticipantStatistic[participant_id] = []
            ParticipantEntries[participant_id] = status

        self.InputFrame.update_idletasks()
        self.Canvas.config(scrollregion=self.Canvas.bbox("all"))

        self.CanvasFrame.config(width=self.HomeWindow.winfo_width() + 90, height=500)
        self.ResultButton = tk.Button(self.ParticipantsFrame,text="Give me Meow!!",borderwidth=5, bg="cyan", font=("Exo 2 Medium", 12), command=self.ComputeResult).grid(row=participants+1, column=0,columnspan=5, pady=10, padx=20)

        EntryFrame.destroy()

    def CalculateRankings(self, entry=None):
        global rankings
        rankings = {}
        self.rank = 1
        self.ResultHeaders = ['Ranking', 'Participant ID', 'Name', 'Accuracy', 'Consistency', 'WPM', 'Time', 'Total Score']

        self.HomeWindow.deiconify()
        
        self.ResultWindow = tk.Toplevel()
        self.ResultWindow.geometry(f'1000x700+{(self.HomeWindow.winfo_screenwidth() - 1000) // 2}+{(self.HomeWindow.winfo_screenheight() - 750) // 2}')
        self.ResultWindow.title("Speed Typing Result")
        self.ResultFrame = tk.Frame(self.ResultWindow)
        self.ResultFrame.pack()

        tk.Label(self.ResultFrame, text="Result Meow!!!", font=("Franklin Gothic Demi Cond",20), fg="#00C4D4").grid(row=0, column=0, columnspan=8, pady=10)

        for participantID, stats in entry.items():
            resAccuracy = (float(stats[1]) / 100) * 45
            resConsistency = (float(stats[2]) / 100) * 35
            resWPM = (float(stats[4]) / 100) * 20
            totalScore = round(resAccuracy + resConsistency + resWPM, 2)
            rankings[f'{participantID} -> {stats[0]}'] = ["{:.2f}".format(resAccuracy), "{:.2f}".format(resConsistency), "{:.2f}".format(resWPM), stats[3], totalScore]

        rankings = sorted(rankings.items(), key=lambda score: score[1][4], reverse=True)

        self.ResultCanva = tk.Frame(self.ResultFrame)
        self.ResultCanva.grid(row=1, column=0, columnspan=8, sticky='nw')
        self.ResultCanva.grid_rowconfigure(0, weight=1)
        self.ResultCanva.grid_columnconfigure(0, weight=1)
        self.ResultCanva.grid_propagate(False)

        self.Canva = tk.Canvas(self.ResultCanva)
        self.Canva.grid(row=0, column=0, sticky='news')

        self.ResultScrollbar = tk.Scrollbar(self.ResultCanva, orient='vertical', command=self.Canva.yview)
        self.ResultScrollbar.grid(row=0, column=8, sticky='ns')
        self.Canva.configure(yscrollcommand=self.ResultScrollbar.set)

        self.FinalList = tk.Frame(self.Canva)
        self.Canva.create_window((0,0), window=self.FinalList, anchor='nw')

        for col, header in enumerate(self.ResultHeaders):
            tk.Label(self.FinalList, text=header, background='#F6DAE4', font=("Exo 2 Medium", 10), width=13).grid(row=0, column=col, padx=10)
        
        for row, (participant, values) in enumerate(rankings):
            participant_data = participant.split(' -> ')
            participant_id = random.randint(101, 999)
            name = participant_data[1]
            values = [self.rank, participant_id, name] + values 
            self.rank += 1

            for col, value in enumerate(values):
                tk.Label(self.FinalList, text=value, background='#D4F0F7', font=("Exo 2 Medium", 10), width=12).grid(row=row+1, column = col, padx=10, pady=5)

        self.FinalList.update_idletasks()
        self.Canva.config(scrollregion=self.Canva.bbox("all"))
        self.ResultCanva.config(width=self.HomeWindow.winfo_width() + 150, height = 500)

        tk.Button(self.ResultFrame, text="<- Back", borderwidth=5, bg="cyan", font=("Exo 2 Medium", 12), width=20, command=self.HomeScreen).grid(row=row + 3, column=0, columnspan=8, pady=10, padx=20)
        self.HomeWindow.withdraw()
    
    def ComputeResult(self):
        for Participants in range(2, TotalEntry + 2):
            statistic = []
            for status in range(0, 5):
                statistic.append(ParticipantEntries[f'Participant_{Participants -1}'][status].get())
            ParticipantStatistic[f'Participant_{Participants-1}'] = statistic

        self.CalculateRankings(ParticipantStatistic)
        self.InputWindow.destroy()
    
    def DisplayResult(self):
        self.Home.destroy()
        self.ranks = 1
        self.headers = ['Ranking', 'Participant ID', 'Name', 'Accuracy', 'Consistency', 'WPM', 'Time', 'Total Score']

        self.HomeWindow.deiconify()
        
        self.Result = tk.Toplevel()
        self.Result.geometry(f'1000x700+{(self.HomeWindow.winfo_screenwidth() - 1000) // 2}+{(self.HomeWindow.winfo_screenheight() - 750) // 2}')
        self.Result.title("Speed Typing Result")
        self.ResFrame = tk.Frame(self.Result)
        self.ResFrame.pack()

        tk.Label(self.ResFrame, text="Result Meow!!!", font=("Franklin Gothic Demi Cond",20), fg="#00C4D4").grid(row=0, column=0, columnspan=8, pady=10)

        self.resCanva = tk.Frame(self.ResFrame)
        self.resCanva.grid(row=1, column=0, columnspan=8, sticky='nw')
        self.resCanva.grid_rowconfigure(0, weight=1)
        self.resCanva.grid_columnconfigure(0, weight=1)
        self.resCanva.grid_propagate(False)

        self.dipCanva = tk.Canvas(self.resCanva)
        self.dipCanva.grid(row=0, column=0, sticky='news')

        self.ResScrollbar = tk.Scrollbar(self.resCanva, orient='vertical', command=self.Canva.yview)
        self.ResScrollbar.grid(row=0, column=8, sticky='ns')
        self.dipCanva.configure(yscrollcommand=self.ResScrollbar.set)

        self.FinalRes = tk.Frame(self.dipCanva)
        self.dipCanva.create_window((0,0), window=self.FinalRes, anchor='nw')

        for col, header in enumerate(self.headers):
            tk.Label(self.FinalRes, text=header, background='#F6DAE4', font=("Exo 2 Medium", 10), width=13).grid(row=0, column=col, padx=10, pady=10)
        
        for row, (participant, values) in enumerate(rankings):
            participant_data = participant.split(' -> ')
            participant_id = random.randint(101, 999)
            name = participant_data[1]
            values = [self.rank, participant_id, name] + values  # Include the name in the data
            self.ranks += 1

            for col, value in enumerate(values):
                tk.Label(self.FinalRes, text=value, background='#D4F0F7', font=("Exo 2 Medium", 10), width=12).grid(row=row+1, column = col, padx=10, pady=5)

        self.FinalRes.update_idletasks()
        self.dipCanva.config(scrollregion=self.dipCanva.bbox("all"))
        self.resCanva.config(width=self.HomeWindow.winfo_width() + 150, height = 500)

        tk.Button(self.ResFrame, text="<- Back", borderwidth=5, bg="cyan", font=("Exo 2 Medium", 12), width=20, command=self.HomeScreen).grid(row=row + 3, column=0, columnspan=8, pady=10, padx=20)
        self.HomeWindow.withdraw()

    def Criteria(self):
        self.Home.destroy()

        self.criteriaWindow = tk.Frame(self.HomeWindow)
        self.criteriaWindow.pack()
        self.CriteriaText = '''
        Accuracy:
        Score for Accuracy = (Actual Accuracy / 100) * 40

        Consistency:
        Score for Consistency = (Actual Consistency / 100) * 30

        Time of Completion:
        Score for Time = (Maximum Time / Actual Time) * 20

        Words Per Minute:
        Score for WPM = (Actual WPM / Maximum WPM) * 10   
        '''

        self.Text = tk.Text(self.criteriaWindow, wrap=tk.WORD, height=13)
        self.Text.pack(fill='both', expand=False)
        self.Text.tag_configure("center", justify="center")
        self.Text.tag_add("center", "1.0", "end")
        self.Text.insert("1.0", self.CriteriaText)
        self.Text.config(state=tk.DISABLED)
        tk.Button(self.criteriaWindow, text="<- Back",  borderwidth=5,  bg="cyan", font=("Exo 2 Medium", 12), width=15, command=self.HomeScreen).pack(side="bottom", pady=10)

screen = ScoreMetrics()
