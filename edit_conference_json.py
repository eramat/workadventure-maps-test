import json

JSON_FILENAME = 'conference.json'

ETHERPAD_URL = "https:\/\/pad.inf.re\/p\/" # + clé à générer
WHITEBOARD_URL = "https:\/\/wbo.ophir.dev\/boards\/" # + clé à générer

website_props = {"properties":[
		{
            "name":"openWebsite",
	     	"type":"string"
        },
	 	{
		    "name":"openWebsiteTrigger",
		    "type":"string",
		    "value":"onaction"
	 	}]
    }

jitsi_props = {"properties":[
        {
            "name":"jitsiRoom",
            "type":"string"
        },
		{
		    "name":"jitsiTrigger",
		    "type":"string",
		    "value":"onaction"
		}]
    }

# load the json file into a python object
def load_json(filename):
    with open(filename, mode='r') as fp:
        data = json.load(fp)

    return data

def write_in_json(filename, data):
    with open(filename, mode='w') as fp:
        json.dump(data, fp)

def update_website_properties(url, key):
    data = website_props
    data['properties']['name' == "openWebsite"].update({'values': url + key})
    
    return data

def update_jitsi_properties(room):
    data = jitsi_props
    data['properties']['name' == "jitsiRoom"].update({'values': room})

    return data


def cpt_to_str(cpt):
    if cpt < 10:
        return "0" + str(cpt)
    else :
        return str(cpt)

def main():
    json_obj = load_json(JSON_FILENAME)
    
    for i in range(1, 15):
        cpt = cpt_to_str(i)

        props = update_jitsi_properties("RegulatoryIntakesPrintDelicately")
        json_obj['layers']['name' == "jitsiConfRoom0" + cpt].update(props)

        props = update_website_properties(ETHERPAD_URL, "ox1LyFxabVryx_Ggndep")
        json_obj['layers']['name' == "documentRoom" + cpt].update(props)

        props = update_website_properties(WHITEBOARD_URL, "0fl2ff9Fc4NdZXCMIJTHSZhvtOGphKrSRHOqA3ZFspQ-")
        json_obj['layers']['name' == "whiteboardRoom" + cpt].update(props)

    write_in_json(JSON_FILENAME, json_obj)

if __name__=="__main__":
    main()