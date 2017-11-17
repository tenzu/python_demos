import random
i,j = 0,0
tmp_list = []
tmp_CSYS = []
f = open('tmp_CSYS.txt','w')
while i <= 2:
	while j <= 5:
		if j <= 2:
			tmp_list.append(random.uniform(-100,100))
		else:
			tmp_list.append(random.uniform(0,360))
		j+=1
	tmp_CSYS.append(tmp_list)
	for k in tmp_list:
		f.write('%3.3f' % k + '\t')
	f.write('\n')
	tmp_list = []
	j=0
	i+=1
