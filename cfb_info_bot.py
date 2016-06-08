#!/usr/bin/env python
import urllib
import os
import praw
from prawoauth2 import PrawOAuth2Mini
import time
already_done=[]
user_agent='a tool for cfb'
r=praw.Reddit(user_agent=user_agent)
oauth_helper=PrawOAuth2Mini(r, app_key='lXiW8DtaWhRIrQ',app_secret='bOh4xyyUVnxPUlDkMwq-549Wxfc',access_token='57780469-guq3qtrnHelvsQRWOXRodj1pX-Y',refresh_token='57780469-7sJeUXRxFrOlKJjI6OMw73KNLm4',scopes=('save','submit','read','identity'))

def lookup(team,start,end):
	z=open('html.txt','w')
	url="http://cfbtrivia.com/cfbt_team_page.php?teamname=%s&teamyrfrom=%s&teamyrthru=%s"%(team,start,end)
	urlr=urllib.urlopen(url)
	z.write(urlr.read())
	z.close()
	z=open('html.txt','r')
	doc=z.readlines()
	block=doc[339]
	block=block.split('>')
	z.close
	os.system('rm html.txt')
	return block
def team_string(y):
	y=y.split('[')
	y=y[2]
	team=y.replace(']','')
	return team
def special_case(team):
	x=team
	if "Florida" in team:
		if team=="Florida":
			pass		
	        elif team=="Florida State":
			pass
		elif team =="Florida International":
			x="FIU"
		else:
			x=team.replace("Florida","Fla.")
			print team
			print x
	if 'State' in team:
		if team=="Georgia State":
			x="Georgia State"
		elif team=="NC State":
			x="N.C. State"
		elif team=="N.C. State":
			x="N.C. State"
		else:
			y=team.split(" ")
			x=y[0]
			x=(x+" St.")
	return x
def filesplit(block,index):
	record=block[index]
	record=record.split(" ")
	record=record[0]
	return record
while 0<1:
	try:
		oauth_helper.refresh()
		subreddit = r.get_subreddit('CFB')
		comments = subreddit.get_comments(limit='None')
		for x in comments:
			y=x.body
			z=x.id
			if y.startswith('[record[') and z not in already_done:
				team=team_string(y)
				team=special_case(team)
				block=lookup(team,'1869','2015')
				record=block[34]
				record=record.split(' ')
				overallrecord=record[0]
				home=block[42]
				home=home.split(" ")
				home=home[0]
				away=block[50]
				away=away.split(" ")
				away=away[0]
				already_done.append(z)
				x.reply(team+" all time record \n \n Overall-"+overallrecord+'\n'+'\n'+'Home Record-'+home+'\n'+'\n'+'Road Record-'+away)
			elif y.startswith('[record_since') and z not in already_done:
				team=team_string(y)
				team=team.split(',')[0]
				team=special_case(team)
				year=y.split(',')[1]
				year=year.split(']')[0]
				year=year.replace(' ','')
				team=team.split(',')[0]
				block=lookup(team,year,'2015')
				record=filesplit(block,34)
				home=filesplit(block,42)
				away=filesplit(block,50)
				already_done.append(z)
				x.reply(team+' record since '+year+'\n'+'\n'+'Overall-'+record+'\n'+'\n'+'Home-'+home+'\n'+'\n'+'Road-'+away)
			elif y.startswith('[record_between[') and z not in already_done:
				team=team_string(y)
				team=team.split(',')[0]
				team=special_case(team)
				year=y.split(',')[1]
				year=year.replace(' ','')
				year=year.split(']')[0]
				year1=year.split('-')[0]
				year2=year.split('-')[1]
				team=team.split(',')[0]
				block=lookup(team,year1,year2)
				record=filesplit(block,34)
				home=filesplit(block,42)
				away=filesplit(block,50)
				already_done.append(z)
				x.reply(team+' record between '+year1+' and '+year2+'\n \n Overall-'+record+'\n \n Home-'+home+'\n \n Road-'+away)
			elif y.startswith('[attendance[') and z not in already_done:
				team=team_string(y)
				team=special_case(team)
				school=(team+',')
				j=open('2015atten.txt','r')
				for xx in j.readlines():
					if school in xx:
						aa=xx.split(',')
						team=aa[0]
						games=aa[1]
						total=aa[2]
						avg=aa[3]
						already_done.append(z)
						x.reply('2015 Attendance for '+team+'\n \n  Average='+avg+'\n \n  Total='+total+'\n \n  Number of games='+games)
	except:
		pass
	try:
		del already_done[200:]
	except:
		pass
	time.sleep(15)
	
#z=open('html.txt','w')
#url="http://cfbtrivia.com/cfbt_team_page.php?teamname=Tulsa&teamyrfrom=1869&teamyrthru=2015"
#urlr=urllib.urlopen(url)
#z.write(urlr.read())
#z.close()
#z=open('html.txt','r')
#doc=z.readlines()
#block=doc[339]
#block=block.split('>')
#record=block[34]
#record=record.split(' ')
#record=record[0]
#print record

