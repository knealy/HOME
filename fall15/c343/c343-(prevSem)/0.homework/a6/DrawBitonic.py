from gmapsrappa import *

headerText = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<style type="text/css">
  html { height: 100% }
  body { height: 100%; margin: 0px; padding: 0px }
  #map_canvas { height: 100% }
</style>
<title>Google Maps JavaScript API v3 Example: Map Simple</title>
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
<script type="text/javascript">
function initialize() {
"""

tailerText = """}
</script>
</head>
<body onload="initialize()">
  <div id="map_canvas"></div>
</body>
</html>
"""

def createMap(center,path,fileName=None):
    if not fileName :
        fileName = 'BitonicMap.html'
    try:
        fpo = open(fileName, mode = 'w')
    except IOError:
        sys.stderr.write("IOError on filename: %s\n" % fileName)
        sys.exit(1)

    fpo.write(headerText)
    mapOpts = MapOptions()
    mapOpts.zoom = 6
    mapOpts.center = LatLng(center.lat,center.lon)
    mapOpts.mapTypeId = MapTypeId('HYBRID')

    navCtlOpt = NavigationControlOptions()
    navCtlOpt.style = NavigationControlStyle('ZOOM_PAN')
    navCtlOpt.position = ControlPosition('TOP_LEFT')
    mapOpts.navigationControlOptions = navCtlOpt

    mapTypeOpt = MapTypeControlOptions()
    mapTypeOpt.style = MapTypeControlStyle('HORIZONTAL_BAR')
    mapTypeOpt.position = ControlPosition('TOP_RIGHT')
    mapOpts.mapTypeControlOptions = mapTypeOpt
    fpo.write("var myOptions = " + str(mapOpts) + ";\n")
    fpo.write('var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);\n')
    plOpts = PolylineOptions()

    newPath = []

    for pt in path.points:
        newPath.append(LatLng(pt.lat,pt.lon))

    plOpts.path = newPath
    plOpts.StrokeColor = "#FF0000"
    plOpts.StrokeOpacity = 10.0
    plOpts.strokeWeight = 3
    fpo.write('fpath = new google.maps.Polyline(' + str(plOpts) + ');\n')
    fpo.write('fpath.setMap(map);\n')

    fpo.write(tailerText)
