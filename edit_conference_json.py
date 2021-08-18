import json
import copy

JSON_MAP_FILENAME = 'conference.json'
JSON_INTERACTIONS_FILENAME = 'groups.json'

MSG_DOCUMENT = "Appuyer sur ESPACE pour ouvrir le document collaboratif"
MSG_WHITEBOARD = "Appuyer sur ESPACE pour ouvrir le tableau blanc"
MSG_VIDEO = "Appuyer sur ESPACE pour regarder votre vidéo"
MSG_POSTER = "Appuyer sur ESPACE pour regarder votre affiche"
MSG_JITSI_GRP = "Appuyer sur ESPACE pour rejoindre votre groupe en visioconférence"
MSG_JITSI_AMPHI = "Appuyer sur ESPACE pour rejoindre la classe virtuel"

website_props = {"properties":[
		{
            "name":"openWebsite",
	     	"type":"string"
        },
	 	{
		    "name":"openWebsiteTrigger",
		    "type":"string",
		    "value":"onaction"
	 	},
        {
            "name": "openWebsiteTriggerMessage",
            "type": "string"
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
		},
        {
            "name": "jitsiTriggerMessage",
            "type": "string"
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

def update_website_properties(url, message):
    data = copy.deepcopy(website_props)
    for values in data['properties']:
            if values['name'] == "openWebsite":
                values.update({'value': url})
            if values['name'] == "openWebsiteTriggerMessage":
                values.update({'value': message})
    
    return data

def update_jitsi_properties(room, message):
    data = copy.deepcopy(jitsi_props)
    for values in data['properties']:
            if values['name'] == "jitsiRoom":
                values.update({'value': room})
            if values['name'] == "jitsiTriggerMessage":
                values.update({'value': message})

    return data

def insert_in_dictionnary(json_obj, name, url, message, jitsi=False):
    if jitsi:
        props = update_jitsi_properties(url, message)
    else:
        props = update_website_properties(url, message)
    
    for values in json_obj['layers']:
            if values['name'] == name:
                values.update(props)


def main():
    json_map = load_json(JSON_MAP_FILENAME)
    json_interactions = load_json(JSON_INTERACTIONS_FILENAME)

    for values in json_interactions["groups"]:
        group = values["group"]

        insert_in_dictionnary(json_map, "jitsiConfRoom" + group, values["jitsi"], MSG_JITSI_GRP, True)
        insert_in_dictionnary(json_map, "documentRoom" + group, values["document"], MSG_DOCUMENT)
        insert_in_dictionnary(json_map, "whiteboardRoom" + group, values["whiteboard"], MSG_WHITEBOARD)
        insert_in_dictionnary(json_map, "posterRoom" + group, values["poster"], MSG_POSTER)
        insert_in_dictionnary(json_map, "videoRoom" + group, values["video"], MSG_VIDEO)

    insert_in_dictionnary(json_map, "jitsiConfAmphi" + group, json_interactions["amphi"]["jitsi"], MSG_JITSI_AMPHI, True)

    write_in_json(JSON_MAP_FILENAME, json_map)

if __name__=="__main__":
    main()