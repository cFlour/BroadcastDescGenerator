def datemonthcheck(date,month):
    if int(date)==date and int(month)==month:
        if month>=1 and month<=12:
            if date>=1 and date<=31:
                if month==2 and date>=29: #change this to 30 if year changes to a leap year (2024)
                    return False
                else:
                    t1=[1,3,5,7,8,10,12]
                    if date==31:
                        if month in t1:
                            return True
                        else:
                            return False
                    else:
                        return True
            else:
                return False
        else:
            return False
    else:
        return False
def intsuffix(n):
    if int(n)==n:
        var=n%10
        if var==1:
            return "st"
        elif var==2:
            return "nd"
        elif var==3:
            return "rd"
        else:
            return "th"
    else:
        return False
def roundday(roundhr,roundmin,date1,month1,timeadd):
    if (roundhr+(roundmin/60))+timeadd>=24:
        if datemonthcheck(date1+1,month1):
            date2=date1+1
            month2=month1
        else:
            date2=1
            month2=month1+1
    else:
        date2=date1
        month2=month1
    return date2,month2
print('Lichess broadcast description generator:\n')
print('Enter the name of the tournament:')
nam=input()
print('Enter the type of tournament [S/RR/DRR/RRE/DRE/DE/SE]. If another type, enter the name.')
print('(RR=Round Robin, DRR=Double RR, RRE=RR+Elimination, DRE=DRR+Elimination, DE=Double Elimination, SE=Single Elimination):')
t_type=input()
t_type=t_type.lower()
if t_type=='s':
    ttype='Swiss'
elif t_type=='rr':
    ttype='Round-Robin'
elif t_type=='drr':
    ttype='Double Round-Robin'
elif t_type=='rre':
    ttype='Round-Robin + Elimination'
elif t_type=='dre':
    ttype='Double Round-Robin + Elimination'
elif t_type=='de':
    ttype='Double Elimination'
elif t_type=='se':
    ttype='Single Elimination'
else:
    ttype=t_type
print('Enter the time control for the tournament [Classical/Rapid/Blitz/Bullet]')
tc=input()
tc=tc.lower()
tc=tc.capitalize()
print('Enter the number of rounds of the tournament:')
rounds=int(input())
print('Enter the month number of the start date of the tournament:')
sm=int(input())
print('Enter the day number of the start date of the tournament:')
sd=int(input())
if datemonthcheck(sd,sm):
    pass
else:
    print('Reload and try again.')
print('Enter the month number of the end date of the tournament:')
em=int(input())
print('Enter the day number of the end date of the tournament:')
ed=int(input())
if datemonthcheck(ed,em):
    pass
else:
    print('Reload and try again.')
print('Enter number of players:')
players=int(input())
print('Enter the location of the tournament:')
location=input()
print('Enter the time control in words:')
timecontrol=input()
print('Please link the official website for the tournament:')
website=input()
print('Please link the results website for the tournament (if none, enter 0):')
results=input()
print('Please enter the local time difference with GMT [2,5.5,-4,etc]:')
localtimediff=float(input())
print('Please enter the time difference for your timezone with GMT [2,5.5,-4,etc]:')
timediff=float(input())
timeadd=timediff-localtimediff
months={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
sm=months[sm]
em=months[em]
if em==sm and ed==sd:
    a=intsuffix(sd)
    s_d=f'{em} {sd}{a}'
    l_d=f'on {s_d}'
elif em==sm and ed!=sd:
    a=intsuffix(sd)
    b=intsuffix(ed)
    s_d=f'{em} {sd}{a} - {ed}{b}'
    l_d=f'from {em} {sd}{a} to the {ed}{b}'
else:
    a=intsuffix(sd)
    b=intsuffix(ed)
    s_d=f'{sm} {sd}{a} - {em} {ed}{b}'
    l_d=f'from {sm} {sd}{a} to {em} {ed}{b}'
shortdes=f'{s_d} | {players}-player {ttype} | {tc} Time Control'
longdes1=f'The {nam} is a {players}-player {ttype} tournament held at {location} {l_d}.'
if results==0: #should work, but might not. check later.
    longdes2=f'[Official Website]({website})'
else:
    longdes2=f'[Official Website]({website}) | [Results]({results})'
print('\nThe Short Broadcast Description is:')
print(shortdes)
print('\nThe Long Broadcast Description is:')
print(longdes1,'\n')
print('The Time Control is',timecontrol,end='.\n')
print(longdes2,'\n\n')
print('For each round:\n')
for i in range(1,rounds+1):
    print('Round',i,end=":")
    print('Enter date and time (local to the tournament)')
    month1=int(input('Month Number='))
    date1=int(input('Date='))
    roundhr=int(input('Number of hours complete in the day before round starts [eg: 15, if it starts at 15:30 or 15]='))
    roundmin=int(input('Number of minutes past the hour mark when the round starts='))
    if datemonthcheck(date1,month1):
        if roundhr>=0 and roundhr<=23:
            if roundmin>=0 and roundmin<=59:
                pass
            else:
                print("Reload and try again.")
        else:
            print("Reload and try again.")
    else:
        print("Reload and try again.")
    if timeadd>=0:
        addmin=(timeadd-(timeadd//1))*60
        if addmin+roundmin>=60:
            roundhr+=(1+(timeadd//1))
            roundmin=addmin+roundmin-60
            date,month=roundday(roundhr,roundmin,date1,month1,0)
        else:
            roundhr+=(timeadd//1)
            roundmin+=addmin
            date,month=roundday(roundhr,roundmin,date1,month1,0)
    else:
        submin=(timeadd+1-(timeadd//1))*60
        if roundmin-submin<0:
            roundmin=roundmin+60-submin
            roundhr-=(1-((timeadd//1)+1))
            if roundhr<0:
                date1-=1
                if date1<=0:
                    month1-=1
                else:
                    pass
            else:
                pass
        else:
            roundhr+=((timeadd//1)+1)
            roundmin-=submin
            if roundhr<0:
                date1-=1
                if date1<=0:
                    month1-=1
                else:
                    pass
            else:
                pass
        date,month=date1,month1
    print("The date and month for the round in your timezone are:")
    x=intsuffix(date)
    month=months[month]
    roundmin=roundmin//1
    rounddes=f'{date}{x} {month}, {int(roundhr)}:{int(roundmin)}'
    print(rounddes)
