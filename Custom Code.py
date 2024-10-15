import requests
from urllib.parse import urlparse

def main(event):
  check = 1
  try:
    domain = event.get("inputFields").get("domain")
    url = "https://" + domain
    response = requests.get(url)
    redirects = []
    if response.history:
      for resp in response.history:
        redirects.append(response.url)
    else:
        redirects.append(response.url)
    domain = ((urlparse(redirects[-1]).netloc).replace('www.','')).split(":")[0]
    check = 0
  except:
    check = 1
    domain = domain
  return {
    "outputFields": {
      "check": check,
      "Updated_Domain": domain
    }
  }