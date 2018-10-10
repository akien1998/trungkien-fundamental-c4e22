from gmail import GMail,Message
import datetime
gmail = GMail('trungkienjm@gmail.com','vutrungkien1998')
msg = Message ('nắng sáng lên rồi dậy lên nương đã sáng rồi ai êi'
,to='kienvtgch16382@fpt.edu.vn',text='con gà gáy té le sáng rồi ai êi' )
my_date= datetime.time(7,0)
moment = datetime.datetime.now().time()
if moment > my_date:
    gmail.send(msg)
