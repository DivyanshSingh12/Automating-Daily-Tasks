Add-Type -AssemblyName System.Speech
$ATAVoiceEngine = New-Object System.Speech.Synthesis.SpeechSynthesizer
$mydata = Get-Content C:\Users\divya\OneDrive\Desktop\KnowYoutubeSubs\Subscribers.txt
$ATAVoiceEngine.Speak($mydata)