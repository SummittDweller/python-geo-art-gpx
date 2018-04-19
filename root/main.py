import glob
import codecs
import csv

# -------------------------------------------------

if __name__ == '__main__':
  print("python-geo-art-gpx starting...")
  count = 0

  for numbers in glob.iglob('/tmp/inputs/*.csv'):

    if numbers.rsplit(".")[-1] != "csv":
      print("ERROR - File must have a .csv extension!  {} found.".format(numbers))
      exit(1)

    print("Processing CSV file {}...".format(numbers))

    # Open a new /tmp/output/IrishEyes.gpx for output and seed it.

    with open('/tmp/output/IrishEyes.gpx', 'w+') as f:
      f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
      f.write('<gpx version="1.0" xmlns="http://www.topografix.com/GPX/1/0">\n')

      with codecs.open(numbers, "rU", encoding='utf-8', errors='ignore') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
          url = row['GC Code']

          if url:
            gc = url[-7:]
            fn = url[-5:]

            pid = row['Point ID']
            posted = row['Posted']
            final = row['Final']
            lat = row['Latitude']
            lon = row['Longitude']
            f_lat = row['Final Latitude']
            f_lon = row['Final Longitude']

            # Write the geocache (posted coordinates)

            f.write('  <wpt lat="{0}" lon="{1}">\n'.format(lat, lon))
            f.write('    <name>{}</name>\n'.format(gc))
            f.write('    <sym>Geocache</sym>\n')
            f.write('  </wpt>\n')

            # Write the final coordinates

            f.write('  <wpt lat="{0}" lon="{1}">\n'.format(f_lat, f_lon))
            f.write('    <name>FN{}</name>\n'.format(fn))
            f.write('    <sym>Geocache</sym>\n')
            f.write('  </wpt>\n')

            count += 1
            print("{0}. Point ID: {3}, GC: {4}, Latitude: {1}, Longitude: {2}".format(count, lat, lon, pid, gc))

        f.write('</gpx>\n')
        f.close()
