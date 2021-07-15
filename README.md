# status-badge
[![Python package](https://github.com/Jsloot1986/Jochum-sloot-CD/actions/workflows/main.yml/badge.svg?branch=master&event=deployment_status)](https://github.com/Jsloot1986/Jochum-sloot-CD/actions/workflows/main.yml)

# Benoem 3 componenten van mijn oplossing
*GITHUB ACTIONS*
Github Actions is een manier om je workflow the automatiseren, customize en uittevoeren in je eigen repository.
Ik heb veel onderzoek gedaan, om te kijken wat er in een YML file moet komen.
Het handige aan Github actions is dat ze je al een vooropgezet YML file laten kiezen zodat alles wat je er in moet hebben al in is gevuld.
Nadeel, soms moet je deze updaten als je bijvoorbeeld wilt connecten met je digital ocean ubuntu server.

*SSH*
Het handige aan een SSH is dat je niet je wachtwoord hoeft toe te voegen in je github actions file.
Ik had verschillende dingen geprobeerd. Eerst op de server proberen te maken. Wat ook lukte. Daarna op je eigen pc.
Ik weet niet wat handiger is, maar toen ik dit besprak met Merijn zei hij dat je het beste de SSH-keygen op je pc kan doen en daarna kan toevoegen aan je server en github. op de server doe je de id-rga.pub en op de github de id-rga key. Je moet het wel in de SECRET plaatsen van je repository, want anders kunnen andere mensen op je server komen.

*.sh file*
Dit gedeelte vond ik interresant om te weten. Hoewel ik het niet helemaal goed werkend heb gekregen.
Ik heb een .sh file op mijn server geinstaleerd. die word aangeroepen na dat github is ingelogd op mijn server.
Mijn .sh file ziet er als volgt uit. file naam is update.sh:

cd Jochum-sloot-CD/Jochum-sloot-CD
git pull
echo 'Deployment to Digital Ocean was succesfully'

mijn repository bestaat al op mijn server dus hij gaat eerst in de map waar het staat en gaat daarna een git pull doen.
Als alles is gelukt geeft hij een commit dat het is gelukt.

# Benoem 3 problemen die je bent tegen gekomen en hoe je deze hebt opgelost
*SSH*
Ik heb heel lang steeds allemaal errors gehad met het connecten met de server via SSH.
Uiteindelijk heeft Merijn mij geholpen. ik was vergeten om de naam van het mapje SSH een . voor te zetten.

*.sh file*
Op mijn server heb ik dus een .sh file gezet die word uitgevoerd door github actions (yml file).
Ik heb het helaas niet werkend gekregen om de server te laten restarten als er iets mis gaat.
Maar op internet vond ik wel dat je daarvoor systemctl moet gebruiken.

Je moet meerdere stappen hiervoor doen omdat je dit ook op je server moet hebben. Ik ben heel lang bezig geweest met het connecten van github actions naar mijn server dat ik hier minder tijd voor had. Maar ik snap dat je een .service file moet maken op je server zodat linux automatisch steeds opnieuws opstart. dit kun je doen door in je .sh file de volgende command te zetten [sudo systemctl start my-application]

*Github Actions*
Voor de yml file had ik al een set-up via de github actions. Alleen wist ik eerst niet hoe je extra stappen kon toevoegen.
Dit heb ik uiteindelijk gevonden door veel video's and documentatie te lezen.
doormiddel van de [- name: actienaam] kun je een nieuwe actie laten lopen. Ik had eerst deze stap in een tweede run file gedaan.

*Bash*
Geleerd dat je verschillende users kan aanmaken en hun kunt toevoegen aan sudo users list. Zodat ze dingen kunnen veranderen met sudo command.
Als je wil switchen tussen user en root gebruik commando su username/of root. Ik had niet echt veel ervaring hiermee en heb gaande weg dingen geleerd. ook als je naar een mapje wil dat je bijvoorbeeld cd /etc/ en dan tab doet zodat je naar de files die er in staan kun switchen.

# Andere opmerkingen die van belang zijn
Ik heb dus heel veel tijd besteeds aan de SSH key en Server werkend te krijgen. Dit kwam dus door het mapje niet .ssh te noemen maar ssh.
Heel stom, maar als je niet zo bekend bent dat kun je lang zoeken naar het probleem.
Ik ben Merijn zeer dankbaar voor de hulp, want als hij mij niet had geholpen was ik nu nog steeds bezig te zoeken naar waar de fout lag.
Helaas door dit alles niet de systemctl gedaan. Maar de opzet zou er ongeveer zo moeten uitzien als ik de documentatie op internet las.

***document aanmaken op de server***
sudo nano /etc/systemd/system/my-application.service

***met nano opend de server het en kun je de volgende code er in kwijt***
[Unit]
Description=My flask application daemon
After=network.target
[Service]
User=jsloot1986
Group=www-data
WorkingDirectory=/home/jsloot1986/Jochum-sloot-cd/Jochum-sloot-cd
ExecStart=flask run 
[Install]
WantedBy=multi-user.target   

***met dit commando start je de server opnieuw op***
sudo systemctl start my-application

Dit zou dan in je update.sh moeten staan.

# CONCLUSIE
Ik heb heel veel geleerd van deze opdracht, maar weet nog lang niet alles er van.
Voor nu denk ik dat ik de basis weet en kan ik in de toekomst verder uitbouwen.
Nogmaals Merijn bedankt voor je goede hulp!
