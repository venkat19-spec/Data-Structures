
n = int(input("Number of songs: "))

songs = [0] * n

for i in range(0,n):

    songs[i] = i+1

m = int(input("Number of minutes(for each CD): "))


# create a cd array
cds = [m]

for song in songs:
  
  #get maximum index
  max_cd = cds.index(max(cds))

  #if capacity of cd >= song length
  if cds[max_cd] >= song:
    cds[max_cd] -= song
  
  #otherwise create a new cd
  else:
    cds.append(m - song)


print("Minimum number of cds: ",len(cds))
