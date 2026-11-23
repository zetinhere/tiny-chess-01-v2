import json as J,os,random as R,sys,urllib.request as U,urllib.error as W
U_=os.environ.get("MAKEFUN_ENV_URL") or sys.exit(1)
MT=100000;IN=1000000
V=[0,100,320,330,500,900,0]
A=(-33,-31,-18,-14,14,18,31,33);K=(-17,-16,-15,-1,1,15,16,17);D=(-17,-15,15,17);O=(-16,-1,1,16);L={3:D,4:O,5:D+O}
MG=[[0]*128 for _ in range(13)];EG=[[0]*128 for _ in range(13)]
for s in range(128):
 if s&136:continue
 f=s&7;r=s>>4;cc=1 if f in(3,4) else 0;mf=min(f,7-f)
 for k in(0,1):
  q=r if k==0 else 7-r;w=mf+min(q,7-q)
  mg=[0,6*q+4*cc,8*w-24,6*w-12,4*w-10+(20 if q==6 else 0),4*w-10,30-10*q-8*mf]
  eg=[0,14*q+5*cc,10*w-20,8*w-16,3*w-6+(15 if q==6 else 0),6*w-12,10*w-20]
  for t in range(1,7):
   g=1 if k==0 else -1
   MG[(t if k==0 else -t)+6][s]=g*(V[t]+mg[t]);EG[(t if k==0 else -t)+6][s]=g*(V[t]+eg[t])
_R=R.Random(20261123)
Zt=[[_R.getrandbits(64) for _ in range(128)] for _ in range(12)]
Zs=_R.getrandbits(64);Zc=[_R.getrandbits(64) for _ in range(16)];Ze=[_R.getrandbits(64) for _ in range(8)]
def zi(p):return (abs(p)-1)*2+(1 if p<0 else 0)
B=[0]*128;Sd=1;Ca=0;Ep=-1;Hf=0;Wk=Bk=0;Sg=Se=Np=0;Wb=Bb=0;Hs=0;Ph=[];Un=[];Tt={};Kl=[[0,0] for _ in range(64)];Hh=[[0]*16384 for _ in range(2)];Nd=0;Bd=50000;Nl=0;Pf=[[0]*8 for _ in range(2)]
class Ab(Exception):pass
def pf(fn):
 global Sd,Ca,Ep,Hf,Wk,Bk,Sg,Se,Np,Wb,Bb,Hs,Ph,Un
 p=fn.split();Sg=Se=Np=Wb=Bb=0;Hs=0;Pf[0]=[0]*8;Pf[1]=[0]*8
 B[:]=[0]*128
 for i,rw in enumerate(p[0].split("/")):
  f=0
  for ch in rw:
   if ch.isdigit():f+=int(ch)
   else:
    s=(7-i)*16+f;q="PNBRQK".index(ch.upper())+1
    if ch.islower():q=-q
    B[s]=q;f+=1
 Sd=1 if p[1]=="w" else -1;Ca=0
 if p[2]!="-":
  for ch in p[2]:Ca|={"K":1,"Q":2,"k":4,"q":8}[ch]
 Ep=-1
 if p[3]!="-":Ep=(int(p[3][1])-1)*16+ord(p[3][0])-97
 Hf=int(p[4]) if len(p)>4 else 0
 for s in range(128):
  if s&136:continue
  q=B[s]
  if not q:continue
  if abs(q)==6:
   if q>0:Wk=s
   else:Bk=s
   continue
  Sg+=MG[q+6][s];Se+=EG[q+6][s]
  if abs(q)!=1:Np+=V[abs(q)]
  if abs(q)==1:Pf[0 if q>0 else 1][s&7]+=1
  if abs(q)==3:
   if q>0:Wb+=1
   else:Bb+=1
  Hs^=Zt[zi(q)][s]
 if Sd<0:Hs^=Zs
 Hs^=Zc[Ca]
 if Ep>=0:Hs^=Ze[Ep&7]
 Un=[];Ph=[Hs]
def ak(s,w):
 for t in(s-15,s-17) if w else(s+15,s+17):
  if 0<=t<128 and not(t&136) and B[t]==(1 if w else -1):return 1
 for o in A:
  t=s+o
  if 0<=t<128 and not(t&136) and B[t]==(2 if w else -2):return 1
 for o in K:
  t=s+o
  if 0<=t<128 and not(t&136) and B[t]==(6 if w else -6):return 1
 for o in D:
  t=s+o
  while 0<=t<128 and not(t&136):
   q=B[t]
   if q:
    if(q>0)==w and abs(q) in(3,5):return 1
    break
   t+=o
 for o in O:
  t=s+o
  while 0<=t<128 and not(t&136):
   q=B[t]
   if q:
    if(q>0)==w and abs(q) in(4,5):return 1
    break
   t+=o
 return 0
def en(f,t,p,l):return f|(t<<7)|(p<<14)|(l<<17)
def gn(cp=0):
 m=[];u=Sd
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or(p>0)!=(u>0):continue
  t=abs(p)
  if t==1:
   d=16 if u>0 else -16;o=s+d
   if not(o&136) and B[o]==0:
    prm=(o>>4)==(7 if u>0 else 0)
    if not cp or prm:m.append(en(s,o,5 if prm else 0,0))
    if not cp and(s>>4)==(1 if u>0 else 6):
     w=s+2*d
     if B[w]==0:m.append(en(s,w,0,2))
   for dd in(d-1,d+1):
    t2=s+dd
    if t2&136:continue
    q=B[t2]
    if q and(q>0)!=(u>0):m.append(en(s,t2,5 if(t2>>4)==(7 if u>0 else 0) else 0,1))
    elif t2==Ep:m.append(en(s,t2,0,5))
  elif t in(2,6):
   for dd in A if t==2 else K:
    t2=s+dd
    if t2&136:continue
    q=B[t2]
    if q==0:
     if not cp:m.append(en(s,t2,0,0))
    elif(q>0)!=(u>0):m.append(en(s,t2,0,1))
  else:
   for dd in L[t]:
    t2=s+dd
    while not(t2&136):
     q=B[t2]
     if q==0:
      if not cp:m.append(en(s,t2,0,0))
     else:
      if(q>0)!=(u>0):m.append(en(s,t2,0,1))
      break
     t2+=dd
 if not cp:
  if u>0 and B[4]==6:
   if Ca&1 and B[5]==0 and B[6]==0 and B[7]==4 and not any(ak(x,0)for x in(4,5,6)):m.append(en(4,6,0,8))
   if Ca&2 and B[3]==0 and B[2]==0 and B[1]==0 and B[0]==4 and not any(ak(x,0)for x in(4,3,2)):m.append(en(4,2,0,16))
  if u<0 and B[116]==-6:
   if Ca&4 and B[117]==0 and B[118]==0 and B[119]==-4 and not any(ak(x,1)for x in(116,117,118)):m.append(en(116,118,0,8))
   if Ca&8 and B[115]==0 and B[114]==0 and B[113]==0 and B[112]==-4 and not any(ak(x,1)for x in(116,115,114)):m.append(en(116,114,0,16))
 return m
def mk(m):
 global Sd,Ca,Ep,Hf,Wk,Bk,Sg,Se,Np,Wb,Bb,Hs
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;fl=m>>17;u=Sd;mv=B[f];cp=0;cs=-1;dG=dE=dN=dW=dB=0
 if fl&4:
  cs=t-16 if u>0 else t+16;cp=B[cs];B[cs]=0;dG-=MG[cp+6][cs];dE-=EG[cp+6][cs];Pf[0 if cp>0 else 1][cs&7]-=1
 elif B[t]:
  cp=B[t];cs=t;dG-=MG[cp+6][t];dE-=EG[cp+6][t]
  if abs(cp)!=1:
   dN-=V[abs(cp)]
   if abs(cp)==3:
    if cp>0:dW-=1
    else:dB-=1
  else:Pf[0 if cp>0 else 1][t&7]-=1
 np_=pr if pr else mv
 if pr:dN+=V[pr]-V[1]
 dG+=MG[np_+6][t]-MG[mv+6][f];dE+=EG[np_+6][t]-EG[mv+6][f]
 if abs(mv)==1:
  Pf[0 if u>0 else 1][f&7]-=1
  if not pr:Pf[0 if u>0 else 1][t&7]+=1
 B[t]=np_;B[f]=0;rs=rt=-1
 if fl&8:rs=7 if u>0 else 119;rt=5 if u>0 else 117
 elif fl&16:rs=0 if u>0 else 112;rt=3 if u>0 else 115
 if rs>=0:
  r=B[rs];B[rt]=r;B[rs]=0;dG+=MG[r+6][rt]-MG[r+6][rs];dE+=EG[r+6][rt]-EG[r+6][rs]
 if abs(mv)==6:
  if u>0:Wk=t
  else:Bk=t
 oc,oe,oh,oH=Ca,Ep,Hf,Hs
 if abs(mv)==6:Ca&=~(3 if u>0 else 12)
 for s,bt in((0,2),(7,1),(112,8),(119,4)):
  if f==s or t==s:Ca&=~bt
 Ep=(f+16) if(fl&2) and u>0 else((f-16) if fl&2 else -1)
 Hf=0 if abs(mv)==1 or cp else Hf+1
 Hs^=Zt[zi(mv)][f]^Zt[zi(np_)][t]
 if cp:Hs^=Zt[zi(cp)][cs]
 if rs>=0:Hs^=Zt[zi(r)][rs]^Zt[zi(r)][rt]
 Hs^=Zc[oc]^Zc[Ca]
 if oe>=0:Hs^=Ze[oe&7]
 if Ep>=0:Hs^=Ze[Ep&7]
 Hs^=Zs;Sg+=dG;Se+=dE;Np+=dN;Wb+=dW;Bb+=dB;Sd=-u;Ph.append(Hs)
 Un.append((m,cp,cs,rs,rt,oc,oe,oh,oH,dG,dE,dN,dW,dB));return u
def um():
 global Sd,Ca,Ep,Hf,Wk,Bk,Sg,Se,Np,Wb,Bb,Hs
 m,cp,cs,rs,rt,oc,oe,oh,oH,dG,dE,dN,dW,dB=Un.pop();Ph.pop();Sd=-Sd;u=Sd
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;fl=m>>17
 mv=B[t] if not pr else(1 if u>0 else -1)
 if rs>=0:
  r=B[rt];B[rs]=r;B[rt]=0
 B[f]=mv;B[t]=0
 if cp:B[cs]=cp
 if abs(mv)==6:
  if u>0:Wk=f
  else:Bk=f
 if abs(mv)==1:
  Pf[0 if u>0 else 1][f&7]+=1
  if not pr:Pf[0 if u>0 else 1][t&7]-=1
 if cp and abs(cp)==1:Pf[0 if cp>0 else 1][cs&7]+=1
 Ca,Ep,Hf,Hs=oc,oe,oh,oH;Sg-=dG;Se-=dE;Np-=dN;Wb-=dW;Bb-=dB
def ev():
 p=min(Np,6400)
 e=(Sg*p+Se*(6400-p))//6400+(25 if Wb>=2 else 0)-(25 if Bb>=2 else 0)
 for k in(0,1):e+=sum(c-1 for c in Pf[k] if c>1)*(10 if k else -10)
 return e if Sd>0 else -e
def od(ms,tm,pl):
 def sc(m):
  if m==tm:return 10000000
  t=(m>>7)&127;f=m&127;pr=(m>>14)&7;v=0;fl=m>>17
  if fl&1 or fl&4:
   vc=B[t]
   if fl&4:vc=1 if Sd>0 else -1
   v=1000000+10*V[abs(vc)]-V[abs(B[f])]//16
  if pr:v+=900000+V[pr]
  if m==Kl[pl][0]:v+=80000
  elif m==Kl[pl][1]:v+=70000
  else:v+=Hh[0 if Sd>0 else 1][f*128+t]
  return v
 return sorted(ms,key=sc,reverse=True)
def qc(al,be,pl):
 global Nd
 Nd+=1
 if Nd>Bd:raise Ab
 if Hf>=100 or Hs in Ph[:-1] or pl>48:return 0 if pl<=48 else ev()
 ks=Wk if Sd>0 else Bk;ic=ak(ks,Sd<0)
 if ic:
  ms=[]
  for m in gn():
   u=mk(m)
   if not ak(Wk if u>0 else Bk,u<0):ms.append(m)
   um()
  if not ms:return -MT+pl
  bs=-IN
  for m in od(ms,0,pl):
   mk(m);s=-qc(-be,-al,pl+1);um()
   if s>bs:bs=s
   if bs>al:al=bs
   if al>=be:break
  return bs
 st=ev()
 if st>=be:return be
 if st>al:al=st
 bs=al;ms=[]
 for m in gn(1):
  u=mk(m)
  if not ak(Wk if u>0 else Bk,u<0):ms.append(m)
  um()
 for m in od(ms,0,pl):
  if not((m>>14)&7):
   vc=B[(m>>7)&127]
   if(m>>17)&4:vc=1 if Sd>0 else -1
   if st+V[abs(vc)]+200<al:continue
  mk(m);s=-qc(-be,-al,pl+1);um()
  if s>bs:bs=s
  if bs>al:al=bs
  if al>=be:break
 return bs
def nm(de,al,be,pl):
 global Nd,Nl,Sd,Ep,Hf,Hs
 Nd+=1
 if Nd>Bd:raise Ab
 if Hf>=100 or Hs in Ph[:-1]:return 0
 if pl>0:
  al=max(al,-MT+pl);be=min(be,MT-pl)
  if al>=be:return al
 if de<=0:return qc(al,be,pl)
 e=Tt.get(Hs);tm=0
 if e and e[0]>=de:
  _,fl,s,mv=e
  if s>MT-1000:s-=pl
  elif s<-MT+1000:s+=pl
  if fl==0:return s
  if fl==1 and s<=al:return s
  if fl==2 and s>=be:return s
  tm=mv
 ks=Wk if Sd>0 else Bk;ic=ak(ks,Sd<0)
 if ic:de+=1
 if not Nl and not ic and de>=3 and Np>0:
  _s,_e,_h,_H=Sd,Ep,Hf,Hs;Sd=-Sd;Ep=-1;Hf+=1;Hs^=Zs
  if _e>=0:Hs^=Ze[_e&7]
  Ph.append(Hs);Nl=1;R=2+(1 if de>=6 else 0)
  try:s=-nm(de-1-R,-be,-be+1,pl+1)
  finally:Nl=0;Sd,Ep,Hf,Hs=_s,_e,_h,_H;Ph.pop()
  if s>=be:return be
 bs=-IN;bm=0;lg=0;oa=al
 ms=od(gn(),tm,pl)
 for ix,m in enumerate(ms):
  u=mk(m)
  if ak(Wk if u>0 else Bk,u<0):um();continue
  lg+=1
  if lg==1:s=-nm(de-1,-be,-al,pl+1)
  else:
   rd=0
   if de>=3 and ix>=3 and not((m>>17)&1) and not((m>>14)&7):rd=1+(1 if de>=6 and ix>=8 else 0)
   if rd:
    s=-nm(de-1-rd,-al-1,-al,pl+1)
    if s>al:s=-nm(de-1,-be,-al,pl+1)
   else:
    s=-nm(de-1,-al-1,-al,pl+1)
    if al<s<be:s=-nm(de-1,-be,-al,pl+1)
  um()
  if s>bs:bs=s;bm=m
  if s>al:al=s
  if al>=be:
   if not((m>>17)&1):
    Kl[pl][1]=Kl[pl][0];Kl[pl][0]=m;Hh[0 if u>0 else 1][(m&127)*128+((m>>7)&127)]+=de*de
   break
 if lg==0:return -MT+pl if ic else 0
 fl=1 if bs<=oa else(2 if bs>=be else 0)
 ss=bs+pl if bs>MT-1000 else(bs-pl if bs<-MT+1000 else bs)
 Tt[Hs]=(de,fl,ss,bm);return bs
def lm():
 ms=[]
 for m in gn():
  u=mk(m)
  if not ak(Wk if u>0 else Bk,u<0):ms.append(m)
  um()
 return ms
def sr(pl):
 global Bd,Nd
 ms=lm()
 if len(ms)==1:return ms[0]
 Bd=75000 if pl<60 else(50000 if pl<120 else 25000)
 if len(Tt)>300000:Tt.clear()
 bs=ms[0];sc={m:0 for m in ms};Nd=0
 for d in range(1,11):
  try:
   ms.sort(key=sc.get,reverse=True);al=-IN;cb=bs;cs={}
   for i,m in enumerate(ms):
    mk(m)
    if i==0:s=-nm(d-1,-IN,-al,1)
    else:
     s=-nm(d-1,-al-1,-al,1)
     if al<s:s=-nm(d-1,-IN,-al,1)
    um();cs[m]=s
    if s>al:al=s;cb=m
   bs=cb;sc=cs
  except Ab:break
 return bs
def uc(m):
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;a="abcdefgh"
 s=a[f&7]+str((f>>4)+1)+a[t&7]+str((t>>4)+1)
 return s+("qrbn"[5-pr] if pr else "")
def po(pa,bd):
 q=U.Request(U_+pa,data=J.dumps(bd).encode(),headers={"content-type":"application/json"})
 try:
  with U.urlopen(q) as r:return J.load(r)
 except W.HTTPError:raise RuntimeError(pa)
while True:
 g=po("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  pf(g["fen"]);mv=sr(g["plies"]);u=uc(mv)
  if u not in g["legal_moves"]:
   u=max(g["legal_moves"],key=lambda x:V[abs(B[(ord(x[2])-97)+(int(x[3])-1)*16])])
  try:g=po("/move",{"game":g["game"],"move":u})
  except RuntimeError:
   g=po("/game",{})
   if g["status"]=="your_move":g=po("/move",{"game":g["game"],"move":g["legal_moves"][0]})
print("done",g['wins'],g['draws'],g['losses'],file=sys.stderr)
