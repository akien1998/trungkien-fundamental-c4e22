from poll import Poll
import mlab
#1 connect
mlab.connect()
#2 read all
poll_list= Poll.objects()# lazy loading,page

for p in poll_list:
    print(p.question)
    print(p.options)
    print(p.code)