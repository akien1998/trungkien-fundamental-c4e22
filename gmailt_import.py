from gmail import GMail,Message
from random import choice
gmail = GMail('trungkienjm@gmail.com','vutrungkien1998')
html_content=''' 
<p>ch&agrave;o b&aacute;c sĩ <br />h&ocirc;m nay t&ocirc;i rất mệt mỏi</p>
<p>t&ocirc;i bị {{choice}};</p>
 '''
symptom=["om","dau da day "]
symptom[choice] 
html_template = html_content("{{choice}}")

msg = Message('don xin nghi',to='kienvtgch16382@fpt.edu.vn',text=html_template)
gmail.send(msg)