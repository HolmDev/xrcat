from Xlib import display
from Xlib.Xatom import RESOURCE_MANAGER, STRING
import fnmatch

resources = {}

def _getRawResources() -> str:
    xdisplay = display.Display()
    screen = xdisplay.screen()
    resource_man = screen.root.get_full_property(RESOURCE_MANAGER, STRING)
    return resource_man.value.decode()

def _parseResources(raw: str) -> dict:
    mush = raw.splitlines()
    resource_dict = {}
    for line in mush:
        index, value = line.split(":\t")
        resource_dict[index] = value
    return resource_dict

def updateResources() -> None:
    global resources
    resources = _parseResources(_getRawResources())

def getResource(name: str) -> str:
    try:
        return resources[name]
    except KeyError:
        possible_resources = []

        for resource in resources:
           if fnmatch.fnmatch(name, resource):
               possible_resources.append(resource)
        possible_resources.sort(key=len, reverse=True)
        if len(possible_resources) == 0:
            raise Exception(f"No resources found for {name}")
        else:
            return resources[possible_resources[0]]
