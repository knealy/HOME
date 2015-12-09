class Item:
    key   = ""
    value = 0
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __repr__(self):
        # returns each item ({key:val} pair) associated with hash keys, similar to dict
        # return "{"+str(self.key)+":"+str(self.value)+"}"
        # or
        # just return values associated with the hash keys for simplicity
        return str(self.value)

class Hashtable:
    entries = 0
    hkcount = 0
    hsize = 10

    def __init__(self, dict):
        self.size = Hashtable.hsize
        self.htable=[[] for i in range(self.size)]
        for pair in dict.items():
            self.__setitem__(pair[0],pair[1])

    def __getitem__(self, key):
        prohash = hash(key)%self.size
        for n,m in enumerate(self.htable[prohash]):
            if m.key == key:
                return m.value
        return None

    def __setitem__(self, key, value):
        prohash = hash(key)%self.size
        for x,y in enumerate(self.htable[prohash]):
            if y.key == key:
                del self.htable[prohash][x]
                self.entries -= 1
        self.entries=self.entries+1      
        if self.entries>self.size:
            # print 'doubling'
            for zi in range(self.size):
                self.htable.append([])
            self.size += self.size
        self.htable[prohash].append(Item(key,value))
        self.update()

    def __delitem__(self, key):
        prohash = hash(key)%self.size
        for je,ji in enumerate(self.htable[prohash]):
            if ji.key == key:
                del self.htable[prohash][je]
                self.entries -= 1
                self.update()

    def update(self):
        nons = self.htable.count([])
        self.hkcount = self.size - nons

    def keys(self):
        retKeys = []
        for ls in self.htable:
            for it in ls:
                retKeys.append(it.key)
        return retKeys

    def __repr__(self):
        return str(self.htable)


if __name__ == "__main__":
    h1 = Hashtable({})
    print h1.size
    print h1
    h1['a'] = 3
    print h1
    h1['a']=4
    print h1
    print h1['a']
    assert h1['a'] == 4
    print h1.htable[hash('a')%h1.size][0]
    h1.__setitem__(4,5)
    print h1
    print h1.keys()
    h1['b']=10
    h1['c']=11
    print h1
    print h1.keys()
    print h1.entries
    h1.__delitem__('b')
    print h1
    del h1['a']
    print h1
    h1['z']=10
    h1['x']='yep'
    h1['y']='nope'
    print h1
    print h1
    h1['dzimla']='oen'
    h1['d;ldjdkfbvnv']='intin'
    h1['8y8,.aeljk rnc']='nopell'
    h1[';df;elvnl;d']=859400
    h1['d;ldjnkjbvv']=123456
    h1['8y8,lnlv.nc']=10101
    h1[';dfvffv;d']=45454
    h1['dziadfiubvmla']=1123
    h1['d;ldjvjfbvnv']=8758
    h1['8y8,v;jnd.nc']=293004
    h1[';del;fnvf;d']=20405
    print h1
    print h1.size
    h1['dziadfla']=112491869
    h1['d!jvjfbvnv']=870145098
    h1['8y$jnd.nc']=293300465347
    h1['dziou%42`adfiubvmla']=11230
    h1['d;ldjvjfb0962$vnv']=87589860
    h1['8y8,v;jnd41.nc']=293004079
    h1[';del;f0964nvf;d']=2040586
    h1[';del;%%fnp4981vf;d']=2051021

    # Interestingly, it seems python doesnt accept numbers beginning with 0 so this throws an error
    # h1['dzielvna']=0901

    print h1
    print h1.size
    print h1.entries
    print h1.hkcount

    h2 = Hashtable({1:2,3:4,50:60})
    print h2
    print h2.size
    print h2.entries
    print h2.hkcount
