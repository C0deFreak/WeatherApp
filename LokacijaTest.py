from geopy import geocoders
gn = geocoders.GeoNames()
gn.geocode("Cleveland, OH", exactly_one=False)[0]