from math import cos, asin, sqrt, pi

def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))


#la1,lo1=12.97140853432287, 80.04340433922103
#la2,lo2=12.971375208818364, 80.04340232756444


la1,lo1=12.97141856018353, 80.04338795767147
la2,lo2=12.971440243375422, 80.04338930186259

print(1000*distance(la1,lo1,la2,lo2))


#11.778953610052792, 79.52935182667103
#12.971440243375422, 80.04338930186259


