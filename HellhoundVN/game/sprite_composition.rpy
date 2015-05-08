init -1 python:
    import renpy.exports as renpy # Needed so Ren'Py properly handles rollback with classes
    from operator import attrgetter # Needed for sorting items
    
    class Actor(renpy.store.object):
        def __init__(self):
            self.wearing=[]
            
        def remove(self,clothes):
            if clothes in self.wearing:
                self.wearing.remove(clothes)
            return
        
        def wear(self,clothes):
            self.wearing.append(clothes)
            return
        
        def remove_all(self):
            list = [item for item in self.wearing if item.can_strip]
            if list!=[]:
                for item in list:
                    self.wearing.remove(item)
            return

    class Clothing(renpy.store.object):
            def __init__(self, name, priority=10, wettable=False, barbie=False, can_strip=True):
                self.name = name
                self.priority = priority
                self.wettable = wettable
                self.can_strip = can_strip
                self.barbie = barbie
            
    # Composites the sprite with expression and clothes
    def draw_clothing(st, at, character, art_path="", eyes="neutral", brows="neutral", mouth="neutral", ears="up", tail="down", blush="", flames=False):
        
        list=sorted(character.wearing, key=attrgetter('priority')) # Drawing order depends on priority
        
        base = "base_nude_"
        
        # Switch to base with no nipples if barbie is True for any item
        # This prevents nipples from clipping through clothes
        for item in list:
            if item.barbie and state is "dry":
               base = "base_barbie_"
                
        command_line="LiveComposite((766,1024),(0,0),\""+art_path+"tail_"+tail+"_"+state+".png\""
        command_line=command_line+",(0,0),\""+art_path+base+state+".png\""

        if flames:
            command_line=command_line+",(0,0),\""+art_path+"flames.png\""

        command_line=command_line+",(0,0),\""+art_path+"brows_"+brows+".png\""
        command_line=command_line+",(0,0),\""+art_path+"eyes_"+eyes+".png\""
        command_line=command_line+",(0,0),\""+art_path+"mouth_"+mouth+".png\""
        command_line=command_line+",(0,0),\""+art_path+"ears_"+ears+"_"+state+".png\""

        if blush<>"":
             command_line=command_line+",(0,0),\""+art_path+"blush_"+blush+".png\""
        
        for item in list:
            if item.wettable:
                command_line=command_line+",(0,0),\""+art_path+item.name+"_"+state+".png\""
            else:
                command_line=command_line+",(0,0),\""+art_path+item.name+".png\""

        command_line=command_line+")"
        
        return eval(command_line),None # Refresh rate is None