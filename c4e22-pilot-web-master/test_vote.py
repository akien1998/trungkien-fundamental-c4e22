import mlab
from vote import Vote
from poll import Poll
mlab.connect()
# vote  tim ra cai poll

# vote = Vote.objects().first()
# print(vote.choice)
# print(vote.voter)
# poll= vote.poll
# print(poll.question)
# print(poll.options)
poll = Poll.objects(code="MMYE123").first()
votes=Vote.objects(poll=poll)
# hom mo ra tat ca phieu
print(vote)
print(vote.poll.question)