# Hong Kong Jockey Club Football API documentation

## Overview
Recently, [HKJC Football](https://bet.hkjc.com/football/index.aspx?lang=EN) changed from XML to JSON to present data and it is now easier to fetch betting data for analysis.

## Disclaimer
This is an **unofficial** documentation and I do not own the API.

## Endpoints Example

### Match Schedule
https://bet.hkjc.com/football/getJSON.aspx?jsontype=schedule.aspx&pageno=1

### All Odds
https://bet.hkjc.com/football/getJSON.aspx?jsontype=odds_allodds.aspx&pageno=1

### Results
> Maximum search period length is 31 days.

https://bet.hkjc.com/football/getJSON.aspx?jsontype=search_result.aspx&startdate=20210701&enddate=20210731&pageno=1

## Variables
| Variable Name | Description | Example |
| ----------- | ----------- | ----------- |
| matchID | ID of the match | dbe4edea-923d-4272-b960-290d8f321729 |
| matchIDinofficial | Inofficial ID of the match | 20210711SUN1 |
| matchNum | Match Number | 1 |
| matchDate | Date of the match | 2021-07-11+08:00 |
| matchDay | Weekday of the match | SUN |
| coupon > couponID | ID of the coupon | 2 |
| coupon > couponShortName | Short name of the coupon | SUN |
| coupon > couponNameCH | Chinese name of the coupon | 周日賽事 |
| coupon > couponNameEN | English name of the coupon | Sunday Matches |
| league > leagueID | ID of the league | 12 |
| league > leagueShortName | Short name of the league | EUC |
| league > leagueNameCH | Chinese name of the league | 歐洲國家盃 |
| league > leagueNameEN | English name of the league | Euro Championship |
| homeTeam > teamID | ID of the home team | 113 |
| homeTeam > teamNameCH | Chinese name of the home team | 英格蘭 |
| homeTeam > teamNameEN | English name of the home team | England |
| awayTeam > teamID | ID of the away team | 125 |
| awayTeam > teamNameCH | Chinese name of the away team | 意大利 |
| awayTeam > teamNameEN | English name of the away team | Italy |
| matchStatus | Status of the match | ResultIn |
| matchTime | Date and time of the match | 2021-07-12T03:00:00+08:00 |
| statuslastupdated | Last update time | 2021-07-12T06:01:04+08:00 |
| inplaydelay |  | true |
| liveEvent > ilcLiveDisplay |  | true |
| liveEvent > hasLiveInfo | Set to true id there is live information | true |
| liveEvent > isIncomplete |  | true |
| liveEvent > matchIDbetradar |  | 21514521 |
| liveEvent > matchstate | State of the match | EndedAfterPK |
| liveEvent > stateTS | Timestamp of the state | 2021-07-12T05:54:27+08:00 |
| liveEvent > liveevent > order | Order of the event | 1 |
| liveEvent > liveevent > minutesElasped | Timing of the event | 2 |
| liveEvent > liveevent > actionType | Type of the event | Regular |
| liveEvent > liveevent > playerNameCH | Chinese player name of the event | 勞基梳爾 |
| liveEvent > liveevent > playerNameEN | English player name of the event | Luke Shaw |
| liveEvent > liveevent > homeaway | Team of the player of the event | home |
| accumulatedscore > periodvalue | Period of the score | FirstHalf |
| accumulatedscore > periodstatus | Status of the period | ResultFinal |
| accumulatedscore > periodhome | Home team score at the end of the period | 1 |
| accumulatedscore > periodaway | Away team score at the end of the period | 0 |
| livescore > home | Livescore of home team | 3 |
| livescore > away | Livescore of away team | 4 |
| cornerresult | Number of corners | 6 |
| cornerresultfinal | Set to true if the corner result is final | true |
| Cur |  | 1 |
| hasWebTV |  | false |
| hasOdds | Set to true if odds information is available | true |
| hadodds > H | Home odd of home / away / draw | 100@21.00 |
| hadodds > A | Away odd of home / away / draw | 100@23.00 |
| hadodds > D | Draw odd of home / away / draw | 100@1.02 |
| hadodds > ID | ID of odds | 7af73ca1-c3d1-45cc-8e41-1c992a70848f |
| hadodds > POOLSTATUS | Status of odds | Payout |
| hadodds > ET |  | 0 |
| hadodds > INPLAY | Set to true if the odd is inplay | true |
| hadodds > ALLUP |  | true |
| hadodds > Cur |  | 1 |
| fhaodds > H | Home odd of first half home / away / draw | 100@3.20 |
| fhaodds > A | Away odd of first half home / away / draw | 100@3.85 |
| fhaodds > D | Draw odd of first half home / away / draw | 100@1.80 |
| fhaodds > ID | ID of odds | 53d9b8d4-9f4a-4038-b5ca-db9a9f90026f |
| fhaodds > POOLSTATUS | Status of odds | Payout |
| fhaodds > ET |  | 0 |
| fhaodds > INPLAY | Set to true if the odd is inplay | false |
| hadodds > ALLUP |  | true |
| hadodds > Cur |  | 1 |
| crsodds > S0000, S0100, ..., SM1MD, SM1MA | Odds of correct score of 0:0 draw, home win 1:0, ..., draw others, away others | 101@5.70, 101@2.06, ..., 100@900.0, 100@1000
| crsodds > ID | ID of odds | 2b5fd8b9-57fe-4c85-b7c0-3235f1f8ab10 |
| crsodds > POOLSTATUS | Status of odds | Payout |
| crsodds > ET |  | 0 |
| crsodds > INPLAY | Set to true if the odd is inplay | true |
| crsodds > ALLUP |  | true |
| crsodds > Cur |  | 1 |
| fcsodds > S0000, S0100, ..., SM1MD, SM1MA | Odds of correct first half score of 0:0 draw, home win 1:0, ..., draw others, away others | 101@2.00, 100@4.20, ..., 100@4000, 100@2000
| fcsodds > ID | ID of odds | 890fb775-4860-47c0-93ee-2060d043d782 |
| fcsodds > POOLSTATUS | Status of odds | Payout |
| fcsodds > ET |  | 0 |
| fcsodds > INPLAY | Set to true if the odd is inplay | true |
| fcsodds > ALLUP |  | true |
| fcsodds > Cur |  | 1 |
| ftsodds > H | Home odd of first team score | 100@1.93 |
| ftsodds > A | Away odd of first team score | 100@2.28 |
| ftsodds > N | No goal odd of first team score | 100@5.80 |
| ftsodds > ID | ID of odds | cc2ed5bb-9b51-4162-847d-58e20eb64ecf |
| ftsodds > POOLSTATUS | Status of odds | Payout |
| ftsodds > ET |  | 0 |
| ftsodds > INPLAY | Set to true if the odd is inplay | false |
| ftsodds > ALLUP |  | true |
| ftsodds > Cur |  | 1 |
| ooeodds > O | Odd odd of odd / even | 100@1.90 |
| ooeodds > E | Even odd of odd / even | 100@1.80 |
| ooeodds > ID | ID of odds | e11a0919-7247-4160-9179-ffb26da52942 |
| ooeodds > POOLSTATUS | Status of odds | Payout |
| ooeodds > ET |  | 0 |
| ooeodds > INPLAY | Set to true if the odd is inplay | false |
| ooeodds > ALLUP |  | true |
| ooeodds > Cur |  | 1 |
| ttgodds > P0, P1, ..., M7 | Odds of total goals of 0, 1, ..., more than 7 | 100@5.80, 100@3.60, ..., 100@50.00
| ttgodds > ID | ID of odds | 243555c6-6c12-4035-b660-54bb096e6405 |
| ttgodds > POOLSTATUS | Status of odds | Payout |
| ttgodds > ET |  | 0 |
| ttgodds > INPLAY | Set to true if the odd is inplay | false |
| ttgodds > ALLUP |  | true |
| ttgodds > Cur |  | 1 |
| hftodds > HH, HD, ..., AA | Odds of HaFu of H-H, H-D, ..., A-A | 100@3.80, 100@13.00, ..., 100@5.00
| hftodds > ID | ID of odds | cae1c625-b389-486a-81c1-135f70947266 |
| hftodds > POOLSTATUS | Status of odds | Payout |
| hftodds > ET |  | 0 |
| hftodds > INPLAY | Set to true if the odd is inplay | false |
| hftodds > ALLUP |  | true |
| hftodds > Cur |  | 1 |
| fgsodds > SELLLIST > CONTENTCH | Chinese Name of first scorer | 哈利卡尼
| fgsodds > SELLLIST > CONTENTEN | English Name of first scorer | Harry KANE
| fgsodds > SELLLIST > SEL |  | 101
| fgsodds > SELLLIST > ODDS | Odd of first scorer | 100@3.50
| fgsodds > ID | ID of odds | def18aa0-80e3-478e-a357-7d9d41dfc5cd |
| fgsodds > POOLSTATUS | Status of odds | Payout |
| fgsodds > ET |  | 0 |
| fgsodds > INPLAY | Set to true if the odd is inplay | false |
| fgsodds > ALLUP |  | true |
| fgsodds > Cur |  | 1 |
| hasExtraTimePools | Set to true if extra time pools are available | false
| results > HAD | Result of home / away / draw | D
| results > FHA | Result of first half home / away / draw | H
| results > CRS | Result of correct score | 01:01
| results > FCS | Result of first half correct score | 01:00
| results > FTS | Result of first team score | H
| results > NTS1, NTS2, NTS3 |  | H, A, N
| results > 00E | Result of odd / even | E
| results > TTG | Result of total score | +2
| results > HFT | Result of HaFu | H:D
| results > FGS > CONTENTCH | Chinese Name of first scorer result | 勞基梳爾
| results > FGS > CONTENTEN | Chinese Name of first scorer result | Luke SHAW
| results > FGS > SEL |  | 118
| results > FGS > ODDS | Odd of first scorer result | 100@50.00
| results > SPC1, ... > ITEMEN | English description of special event | Which event will happen to Harry KANE (England) first?
| results > SPC1, ... > ITEMCH | Chinese description of special event | 那一件事會首先發生在 哈利卡尼 (英格蘭) 身上?
| results > SPC1, ... > RFDList |  | 
| results > SPC1, ... > WINLIST > CONTENTCH | Chinese description of special event result | 上述事件沒有發生
| results > SPC1, ... > WINLIST > CONTENTEN | English description of special event result | None of the above
| results > SPC1, ... > WINLIST > SEL |  | 05
| results > SPC1, ... > WINLIST > SELSTATUS |  | StartSell
| results > SPC1, ... > WINLIST > ODDS | Odd of special event result | 100@1.81
