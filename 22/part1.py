# a=[(0,0,0) for i in range(-50,50)]
# import numpy

with open("input22.txt") as f:
  data = f.read()
print(data)


state = []
st=0;

def parse(data):
  data = data.splitlines()
  global state;
  for i in data:
    j,k=i.split(' ')
    # state[st]=j
    # state.append(j)
    # st+=1
    a,b,c=k.split(',')
    _,a=a.split('=')
    _,b=b.split('=')
    _,c=c.split('=')
    la,ra = a.split('..')
    lb,rb = b.split('..')
    lc,rc = c.split('..')
    state.append((j,int(la),int(ra),int(lb),int(rb),int(lc),int(rc)));
    # x=
    # y=

parse(data); 
print(state);

# threeD = [];
# threeD = numpy.zeros((i,j,k))
threeD = [[[0 for i in range(-50,50+1)] for j in range(-50,50+1)] for k in range(-50,50+1)]
#       threeD[i,j,k]=0;
#       threeD.append(0);

count = 0
st_ct = 0
for j,la,ra,lb,rb,lc,rc in state:
  print(len(state)-st_ct,"states left")
  st_ct+=1
  la=max(la,-50)
  ra=min(ra,50)
  lb=max(lb,-50)
  rb=min(rb,50)
  lc=max(lc,-50)
  rc=min(rc,50)

  if(j=='on'):
    for a in range(la,ra+1):
      for b in range(lb,rb+1):
        for c in range(lc,rc+1):
          # a=int(a)
          # b=int(b)
          # c=int(c)
          if(a<=50 and a>=-50):
            if(b<=50 and b>=-50):
              if(c<=50 and c>=-50):
                if(threeD[a][b][c]==0):
                  threeD[a][b][c]=1
                  count+=1
  elif(j=='off'):
    for a in range(la,ra+1):
      for b in range(lb,rb+1):
        for c in range(lc,rc+1):
          # a=int(a)
          # b=int(b)
          # c=int(c)
          if(a<=50 and a>=-50):
            if(b<=50 and b>=-50):
              if(c<=50 and c>=-50):
                if(threeD[a][b][c]==1):
                  threeD[a][b][c]=0
                  count-=1
    

# count = 0
# for i in range(-50,50+1):
#   for j in range(-50,50+1):
#     for k in range(-50,50+1):
#       if(threeD[i][j][k]==1):
#         count+=1

     
print(count)
