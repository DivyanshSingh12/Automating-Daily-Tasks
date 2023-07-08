from googleapiclient.discovery import build 

youTubeApiKey = 'Put_here_your_API_Key'
youtube = build('youtube','v3',developerKey=youTubeApiKey)

channels = ['Put_Channel_ID_Of_First_Channel', 'Put_Channel_ID_Of_Second_Channel'] #You can put as many channels as you have
Names = ['Name_Of_Your_First_Channel', 'Name_Of_Your_Second_Channel'] #Put the channel names respectively
Lines = []

i = 0

while(i < 2): #Here i<n, where n is number of channels you have
    statdata = youtube.channels().list(part='statistics',id=channels[i]).execute()
    stats = statdata['items'][0]['statistics']
    subscriberCount=stats['subscriberCount']
    Lines.append(Names[i] + ' has ' + subscriberCount + ' subscribers')
    i = i + 1

TextFil = open(r"C:\Users\divya\OneDrive\Desktop\KnowYoutubeSubs\Subscribers.txt", "w") #Opening file and then writing Lines 
TextFil.writelines(Lines[0])
TextFil.writelines(" and ")
TextFil.writelines(Lines[1])
   

