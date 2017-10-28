import os,sys
print "*" * 50
#Header
def hr():
    for i in range (10):
        ll=(30-i)
        print " " *ll + "*" * (i*2) 
    for i in range(10):
        ll=(i+20)
        print " " *ll + "*" * (10-i) *2
hr()
hr()

raw_input('Press Enter to Start Building Output File....')

for i in range (10):
    ll=(30-i)
    print " " *ll + "*" * (i*2) 
for i in range(10):
    ll=(i+20)
    print " " *ll + "*" * (10-i) *2







users=open("User.txt",'r')
md=open("mdaemon_users.csv",'w')
md.writelines('"Mailbox","FullName","MailDir","AllowAccess","Password","ApplyQuotas","MaxDiskSpace"')
hh=[]
for i in users:
    hh.append(i.split(', '))

f=[]
tt=0
ts=open('text.txt','w')
for i in hh:
    try:
        tt +=1
        #ts.writelines(i)
        op=i[0] + "_" + i[1][0]
        print '\n"'+i[0] + "_" + i[1][0] +'","'+ i[0] + " " + i[1][:-1] + '","' + "D:\\MdaemonMail\\" +'\\'  + i[0] + "_" + i[1][0] + '\\",Y,"12345678",Y,300000\n ___________________________\n'
        md.writelines('\n"'+i[0] + "_" + i[1][0] +'","'+ i[0] + " " + i[1][:-1] + '","' + "D:\\MdaemonMail" +'\\'  + i[0] + "_" + i[1][0] + '\\",Y,"12345678",Y,"300000"')
    except:
        print "\nError Occored."
        #raw_input('')
ts.close()
md.close()
print '\n\n\n\n\n' + str(tt)
raw_input('Press Enter to Exit....')

#    print '\n"'+i[0] + "_" + i[1][0] +'","'+ i[0] + " " + i[1] + '","C:\MDaemon\Users\PH1516.local\'+ i[0] + "_" + i[1][0] + r'\",Y,"Passw0rd"'
##'\n"'+i[0] + "_" + i[1][0] +'","'+ i[0] + " " + i[1] + '","' + "C:\\MDaemon\\Users\\PH1516.local" +'\\'  + i[0] + "_" + i[1][0] + '\\",Y,"Passw0rd"'

