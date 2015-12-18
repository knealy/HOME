class Spaces():
    def __init__(self, start, inc):
        self.depth = 4
        self.inc = inc
    def sp(self):
        return ' ' * self.depth
    def more(self):
        self.depth += self.inc
    def less(self):
        self.depth -= self.inc

sp = Spaces(4, 4)        

class sdr(object):
    def __init__(self):
        pass
    def __str__(self):
        rr = sp.sp() + "{\n"
        sp.more()
        fc = len(self.__dict__)
        for field in self.__dict__:
            rr += sp.sp() + "%s: " % field
            aa = getattr(self, field)
            if aa.__class__ == str:
                rr += '"%s"' % aa
            elif aa.__class__ == list:
                rr += '['
                for li in aa:
                    rr += str(li) + (", ", "")[li == aa[-1]]
                rr += ']'
            else:
                rr += str(aa)
            fc -= 1
            rr += (",\n", "\n")[fc == 0]
        sp.less()
        rr += sp.sp() + "}"
        return rr

class MapOptions(sdr):
    pass

class LatLng(sdr):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return "new google.maps.LatLng(%f, %f)" % (self.lat, self.lon)

class MapTypeId():
    mapTypes = ('HYBRID','ROADMAP','SATELLITE',	'TERRAIN')
    def __init__(self, typeId):
        self.typeId = typeId
    def __str__(self):
        return "google.maps.MapTypeId.%s" % self.typeId

class NavigationControlStyle():
    styles = ('SMALL', 'ZOOM_PAN', 'ANDROID', 'DEFAULT')
    def __init__(self, style):
        if style not in self.styles:
            # TODO: exception here
            sys.exit(1)
        self.style = style
    def __str__(self):
        return "google.maps.NavigationControlStyle.%s" % self.style    

class ControlPosition():
    positions = ('TOP', 'TOP_LEFT', 'TOP_RIGHT', 'BOTTOM', 'BOTTOM_LEFT', 'BOTTOM_RIGHT', 'LEFT', 'RIGHT')
    def __init__(self, position):
        if position not in self.positions:
            # TODO: exception here
            sys.exit(1)
        self.position = position
    def __str__(self):
        return "google.maps.ControlPosition.%s" % self.position

class NavigationControlOptions(sdr):
    pass

class MapTypeControlStyle():
    styles = ('HORIZONTAL_BAR', 'DROPDOWN_MENU', 'DEFAULT')
    def __init__(self, style):
        if style not in self.styles:
            # TODO: exception here
            sys.exit(1)
        self.style = style
    def __str__(self):
        return "google.maps.MapTypeControlStyle.%s" %  self.style

class ControlPosition():
    positions = ('TOP', 'TOP_LEFT', 'TOP_RIGHT', 'BOTTOM', 'BOTTOM_LEFT', 'BOTTOM_RIGHT', 'LEFT', 'RIGHT')
    def __init__(self, position):
        if position not in self.positions:
            # TODO: exception here
            sys.exit(1)
        self.position = position
    def __str__(self):
        return "google.maps.ControlPosition.%s" % self.position

class MapTypeControlOptions(sdr):
    pass

class PolylineOptions(sdr):
    pass
