mot = "Fvezs Zsyw ezid viywwm e gewwiv pi xsyx tviqmiv gshi h'yri psrkyi wévmi. Tsyv pe wymxi, syzvid pi jmglmiv dmt gm-nsmrx ezig pi qsx hi tewwi TvskveqqexmsrSvmirxiiSfnix. E ey jemx, n'ezemw syfpmé hi hmvi uyi dw xauzawj ugflwfm vsfk dw rah wkl mfw aesyw talesh 24talk. Jwfvwr-dma ks néjalstdw wplwfkagf !"

mot = mot.lower()
d = {}

for k in range(26):
    sol =""
    for i in range(ord('a'), ord('z')+1):
        if i + k > ord('z'):
            reste = ord('a') + (i+k)%ord('z') -1
        else:
            reste = (i+k)
        d[chr(i)] = chr(reste) 

    for k in mot:
        
        if ord(k) > ord('z') or ord(k)< ord('a'):
            sol = sol + k
        else:
            k.lower()
            sol = sol + d[k]
    print(sol)
    print(k)




