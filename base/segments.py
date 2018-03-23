
class Segment(object):
    
    def __init__( self, inptypes=int, default=None ):
        
        if type(inptypes) == type :
            inptypes = [inptypes]
        self.types = inptypes
        self.maxn = len(self.types)+1
        
        self.segs = [ ((0,None), default) ]
        
        return
        
    def __setitem__( self, key, value ):
        
        if type(key) != slice :
            raise ValueError('Segment set must use slice')
        
        start = key.start
        if start is None :
            start = (0, None)
        elif start == min :
            start = (0, None)
        else:
            try :
                n = self.types.index(type(start))+1
                start = (n, start)
            except ValueError:
                raise KeyError('Segment get can not use type %s' % type(start))
                
        stop = key.stop
        
        if stop is None :
            stop = (self.maxn, None)
        elif stop == max :
            stop = (self.maxn, None)
        else:
            try :
                n = self.types.index(type(stop))+1
                stop = (n, stop)
            except ValueError:
                raise KeyError('Segment get can not use type %s' % type(stop))
        
        v2 = self[key.stop]
        
        self.segs = [ (point, value) for point, value in self.segs if point < start or point >= stop ]
        self.segs.append( (start, value) )
        if stop != (self.maxn, None):
            self.segs.append( (stop, v2) )
            
        self.segs.sort()
        #print(self.segs)
        
        return
        
    def __getitem__( self, key ):
        
        if type(key) == slice:
            raise KeyError('Segment get can not use slice')
        
        if key is None :
            key = (0, None)
        elif key == min :
            key = (0, None)
        elif key == max :
            key = (self.maxn, None)
        else:
            try :
                n = self.types.index(type(key))+1
                key = (n, key)
            except ValueError:
                raise KeyError('Segment get can not use type %s' % type(key))
            
        v = self.segs[0][1]
        for point, value in self.segs[1:]:
            if key < point :
                break
            v = value
            
        return v
        
if __name__ == '__main__' :
    
    print( ' '.join( '%02d' % i for i in range(15) ) )
    
    s = Segment(int)
    s[:] = 'a'
    s[None:None] = 'a'
    print( ' '.join( '%2s' % s[i] for i in range(15) ) )
    print(s[None])