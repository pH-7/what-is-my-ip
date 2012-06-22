#!/usr/bin/python

#############################################
# @title What Is My IP (Python version)
#
# @author           Pierre-Henry Soria <pierrehenrysoria@gmail.com>
# @copyright        Pierre-Henry Soria, All Rights Reserved.
# @license          Lesser General Public License (LGPL) (http://www.gnu.org/copyleft/lesser.html)
# @version          1.0
#
#############################################

from cgi import escape
from os import environ
from ConfigParser import SafeConfigParser

INDEX_FILE = "index.tpl"


# Set the HTML type to HTTP header
print("Content-type: text/html")
print("")


# Get the template file 
def tpl_file(tpl_file):
  try:
    file = open('template/' + tpl_file, 'r') 
    return file.read()
  except IOError:
    print("Can't open the tpl file: ", tpl_file)
  finally:
    file.close()


# Get configuration file
try:
  config = SafeConfigParser()
  config.read("config/conf.ini")
except IOError as e_msg:
  print("Can't open the config file: ", e_msg)
	
	
# Template Parsing
html = tpl_file(INDEX_FILE)
html = html.replace("{include_header}", tpl_file('header.inc.tpl'))
html = html.replace("{include_footer}", tpl_file('footer.inc.tpl'))
html = html.replace("{include_analytics}", tpl_file('analytics.inc.tpl'))

html = html.replace("{url}", config.get("webapp", "url"))
html = html.replace("{style_name}", config.get("webapp", "style_name"))
html = html.replace("{site_name}", config.get("general", "site_name"))
html = html.replace("{contact_email}", config.get("general", "contact_email"))
html = html.replace("{api_ip_url}", config.get("api", "ip_url"))
html = html.replace("{analytics_id}", config.get("api", "analytics_id"))
html = html.replace("{contact_email}", config.get("general", "contact_email"))
html = html.replace("{ip}", escape(environ["REMOTE_ADDR"]))


# Output
print(html)




