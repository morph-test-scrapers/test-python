import scraperwiki
import time

# Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

for i in range(1, 6):
    print "%i..." % i
    time.sleep(1)
