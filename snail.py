wellheight = 125
advancement = 30
retreat = 20
daysclimbing = 0
distanceclimbed = 0

while distanceclimbed < 125:
  daysclimbing += 1
  distanceclimbed = distanceclimbed + advancement - retreat
  print(distanceclimbed, 'climbed so far')
  if distanceclimbed >= wellheight:
    print(daysclimbing, 'days to escape')
