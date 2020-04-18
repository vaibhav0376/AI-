import ml_metrics as metrics
import numpy as np


with open('kaggle_visible_evaluation_triplets.txt', 'r') as f:
    song_to_count = dict() 
    for line in f:
        _, song, _ = line.strip().split('\t') 
        if song in song_to_count: 
            song_to_count[song] += 1 
        else: 
            song_to_count[song] = 1 
            pass
        pass
    pass



songs_ordered = sorted( song_to_count.keys(), 
                        key=lambda s: song_to_count[s],
                        reverse=True)



with open('year1_valid_triplets_visible.txt', 'r') as f:
    user_to_songs = dict() 
    for line in f:
        user, song, _ = line.strip().split('\t') 
        if user in user_to_songs: 
            user_to_songs[user].add(song) 
        else: 
            user_to_songs[user] = set([song])
            pass
        pass
    pass



with open('user_valid.txt', 'r') as f:
    canonical_users = map(lambda line: line.strip(), f.readlines()) 
    pass


with open('kaggle_songs.txt', 'r') as f:
    song_to_index = dict(map(lambda line: line.strip().split(' '), f.readlines())) 
    pass


with open('year1_valid_triplets_hidden.txt','r') as f:
    uts=dict()
    for line in f:
        user,song,_=line.strip().split('\t')
        if user in uts:
            uts[user].add(song_to_index[song])
        else:
            uts[user]=set([song_to_index[song]])
            pass
	pass
    pass
    
with open('submission_valid.txt', 'w') as f:
    myDic = {}
    for user in canonical_users:
        songs_to_recommend  = [] 

        for song in songs_ordered: 
            if len(songs_to_recommend) >= 500: 
                break 
            if not song in user_to_songs[user]: 
                songs_to_recommend.append(song_to_index[song]) 
                pass
        
        myDic[user] = songs_to_recommend
        print user
        print myDic[1]
        pass
    pass

c = 0
for i, user in enumerate(canonical_users):
    c = c+metrics.apk(uts[user],myDic[user])
    pass 

t = c/i
print t








//2nd file starts from here

with open ("song_unsort.txt", "w") as f2:
	with open('year1_valid_triplets_visible.txt', 'r') as f:
	    song_to_count = dict()
	    for line in f:
        	_, song, _ = line.strip().split('\t')
        	if song in song_to_count:
        	    song_to_count[song] += 1
        	else:
        	    song_to_count[song] = 1
    		    f2.write(song+'\n')        
        	    pass
        	pass
	    pass

