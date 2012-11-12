import pymongo
from operator import itemgetter

conn = pymongo.Connection('localhost')

db = conn['school']


print db.students.count()

id_scores = db.students.find({}, {'scores':True,})

print '\n'
for student in id_scores:
    sorted_scores = sorted([x for x in student['scores'] if x['type'] == 'homework'], key=itemgetter('score'))
    print sorted_scores

    print "Pulling", sorted_scores[0]['score']
    db.students.update({'_id': student['_id']}, {'$pull': {'scores': {'score': sorted_scores[0]['score']} }})

    print student['_id'], '\n'


