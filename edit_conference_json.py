import json
import copy

JSON_FILENAME = 'conference.json'

ETHERPAD_URL = "https://pad.inf.re/p/" # + clé à générer
WHITEBOARD_URL = "https://wbo.ophir.dev/boards/" # + clé à générer
VIDEO_URL = "https://www.youtube.com/embed/" # + ID de la vidéo
POSTER_URL = "https://cdn.futura-sciences.com/buildsv6/images/largeoriginal/6/f/c/"

ETHERPAD_KEY = "2Ej6zYwKybU3aXojQHvO"
WHITEBOARD_KEY = "JDBWUsyrw325eTTCTmaPINT-dGWTIxPIa3e6g2anvy4-"
VIDEO_KEY = "dQw4w9WgXcQ"
POSTER_KEY = "6fc6bc1b21_50021087_albert-einstein-langue.jpg"
JITSI_KEY = "RegulatoryIntakesPrintDelicately"

MSG_ETHERPAD = "Appuyer sur ESPACE pour ouvrir le document collaboratif"
MSG_WHITEBOARD = "Appuyer sur ESPACE pour ouvrir le tableau blanc"
MSG_VIDEO = "Appuyer sur ESPACE pour regarder votre vidéo"
MSG_POSTER = "Appuyer sur ESPACE pour regarder votre affiche"
MSG_JITSI_GRP = "Appuyer sur ESPACE pour rejoindre la visioconférence de votre groupe"
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

def update_website_properties(url, key, message):
    data = copy.deepcopy(website_props)
    for values in data['properties']:
            if values['name'] == "openWebsite":
                values.update({'value': url + key})
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


def cpt_to_str(cpt):
    if cpt < 10:
        return "0" + str(cpt)
    else :
        return str(cpt)

def main():
    json_obj = load_json(JSON_FILENAME)
    
    for i in range(1, 15):
        cpt = cpt_to_str(i)

        props = update_jitsi_properties(JITSI_KEY, MSG_JITSI_GRP)
        for values in json_obj['layers']:
            if values['name'] == "jitsiConfRoom" + cpt:
                values.update(props)

        props = update_website_properties(ETHERPAD_URL, ETHERPAD_KEY, MSG_ETHERPAD)
        for values in json_obj['layers']:
            if values['name'] == "documentRoom" + cpt:
                values.update(props)

        props = update_website_properties(WHITEBOARD_URL, WHITEBOARD_KEY, MSG_WHITEBOARD)
        for values in json_obj['layers']:
            if values['name'] == "whiteboardRoom" + cpt:
                values.update(props)

        props = update_website_properties(POSTER_URL, POSTER_KEY, MSG_POSTER)
        for values in json_obj['layers']:
            if values['name'] == "posterRoom" + cpt:
                values.update(props)

        props = update_website_properties(VIDEO_URL, VIDEO_KEY, MSG_VIDEO)
        for values in json_obj['layers']:
            if values['name'] == "videoRoom" + cpt:
                values.update(props)

    props = update_jitsi_properties(JITSI_KEY, MSG_JITSI_AMPHI)
    for values in json_obj['layers']:
            if values['name'] == "jitsiConfAmphi":
                values.update(props)
    
    write_in_json(JSON_FILENAME, json_obj)

if __name__=="__main__":
    main()