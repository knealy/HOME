# Dynamic programming and greedy algorithms

#-----------------------------------------------------------------------------
# Coins

def makeChange (amount) :
    # for special case of quarters, dimes, nickels, and pennies
    if amount >= 25 :
        q,d,n,p = makeChange(amount-25)
        return q+1,d,n,p
    elif amount >= 10 :
        q,d,n,p = makeChange(amount-10)
        return q,d+1,n,p
    elif amount >= 5 :
        q,d,n,p = makeChange(amount-5)
        return q,d,n+1,p
    else :
        return 0,0,0,amount

##

class Coin :
    def __init__ (self,value) :
        self.value = value

class ChangeDP :
    def __init__ (self,coins) :
        self.memo = {}
        self.coins = coins

    def makeChange (self,amount) :
        return self.makeChangeInner(amount,0)

    def makeChangeInner (self,amount,i) :
        if amount in self.memo :
            return self.memo[amount]
        
        if i == len(self.coins)-1 : 
            # use last coin which must be pennies
            tot,change = amount,[0]*(i+1)
            change[i] = amount
        elif amount >= self.coins[i].value :
            # use coins[i]
            tot1,change1 = self.makeChangeInner(amount-self.coins[i].value,i)
            tot1 += 1
            change1[i] += 1
            # do not use coins[i]
            tot2,change2 = self.makeChangeInner(amount,i+1)
            # choose alternative with fewer coins
            if tot1 > tot2 : 
                tot,change = tot2,change2
            else :
                tot,change = tot1,change1
        else : 
            # skip coins[i]
            tot,change = self.makeChangeInner(amount,i+1)

        self.memo[amount] = tot,change[:] # must make copy 
        return tot,change

#-----------------------------------------------------------------------------
# Knapsack

class Item :
    def __init__ (self,name,weight,cost) :
        self.name = name
        self.weight = weight
        self.cost = cost

    def __repr__ (self) :
        return '{name}(w={w},c={c})'.\
            format(name=self.name,w=self.weight,c=self.cost)

items = [Item('watch',10,60), \
         Item('phone',20,100), \
         Item('laptop',30,120)]

# add hash table to share subproblems
def collect (items,i,max_weight) :
    print i,max_weight
    if i == len(items) :
        return (0,[])
    elif items[i].weight > max_weight :
        return collect(items,i+1,max_weight)
    else :
        value1,items1 = collect(items,i+1,max_weight)
        value2,items2 = collect(items,i+1,max_weight-items[i].weight)
        value2 += items[i].cost
        items2.append(items[i])
        if value1 > value2 :
            return value1,items1
        else :
            return value2,items2


#-----------------------------------------------------------------------------


