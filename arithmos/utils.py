import requests
from requests import RequestException
import json
try:
    from packaging.version import parse
except ImportError:
    from pip._vendor.packaging.version import parse


URL_PATTERN = 'https://pypi.python.org/pypi/{package}/json'


def req_version(package="arithmos-cipher", url_pattern=URL_PATTERN):
    """Return version of package on pypi.python.org using json."""
    try:
        req = requests.get(url_pattern.format(package=package))
        version = parse('0')
        if req.status_code == requests.codes.ok:
            j = json.loads(req.text.encode(req.encoding))
            releases = j.get('releases', [])
            for release in releases:
                ver = parse(release)
                if not ver.is_prerelease:
                    version = max(version, ver)
        return version
        
    except RequestException:
        return "offline"
        
        
def get_version():
    call = req_version
    if call == "offline":
        pass
    else:
        return call
