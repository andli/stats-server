import requests


def geolocate_ip(ip_addr):
    try:
        r = requests.get(
            f"http://api.ipstack.com/{ip_addr}?access_key=33071ba576a6328a4ed81cf28123f088"
        )
        return r.json()
    except Exception as e:
        print(e.args)
        return None


if __name__ == "__main__":
    """ This is executed when run from the command line """
    stuff = geolocate_ip("98.128.228.189")["latitude"]
    print(stuff)
