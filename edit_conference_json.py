import json
import copy

JSON_FILENAME = 'conference.json'

ETHERPAD_URL = "https:\/\/pad.inf.re\/p\/" # + clé à générer
WHITEBOARD_URL = "https:\/\/wbo.ophir.dev\/boards\/" # + clé à générer
VIDEO_URL = "https://www.youtube.com/embed/" # + ID de la vidéo
POSTER_URL = "https://cdn.futura-sciences.com/buildsv6/images/largeoriginal/6/f/c/"

MSG_ETHERPAD = "Appuyer sur ESPACE pour ouvrir le document collaboratif"
MSG_WHITEBOARD = "Appuyer sur ESPACE pour ouvrir le tableau blanc"
MSG_VIDEO = "Appuyer sur ESPACE pour regarder votre vidéo"
MSG_POSTER = "Appuyer sur ESPACE pour regarder votre affiche"

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
                values.update({'values': url + key})
            if values['name'] == "openWebsiteTriggerMessage":
                values.update({'values': message})
    
    return data

def update_jitsi_properties(room):
    data = copy.deepcopy(jitsi_props)
    for values in data['properties']:
            if values['name'] == "jitsiRoom":
                values.update({'values': room})

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
        for values in json_obj['layers']:
            if values['name'] == "jitsiConfRoom" + cpt:
                values.update(props)

        props = update_website_properties(ETHERPAD_URL, "ox1LyFxabVryx_Ggndep", MSG_ETHERPAD)
        for values in json_obj['layers']:
            if values['name'] == "documentRoom" + cpt:
                values.update(props)

        props = update_website_properties(WHITEBOARD_URL, "0fl2ff9Fc4NdZXCMIJTHSZhvtOGphKrSRHOqA3ZFspQ-", MSG_WHITEBOARD)
        for values in json_obj['layers']:
            if values['name'] == "whiteboardRoom" + cpt:
                values.update(props)

        props = update_website_properties(POSTER_URL, "6fc6bc1b21_50021087_albert-einstein-langue.jpg", MSG_POSTER)
        for values in json_obj['layers']:
            if values['name'] == "posterRoom" + cpt:
                values.update(props)

        props = update_website_properties(VIDEO_URL, "dQw4w9WgXcQ", MSG_VIDEO)
        for values in json_obj['layers']:
            if values['name'] == "videoRoom" + cpt:
                values.update(props)

    props = update_jitsi_properties("RegulatoryIntakesPrintDelicately")
    for values in json_obj['layers']:
            if values['name'] == "videoRoom" + cpt:
                values.update(props)
    
    write_in_json(JSON_FILENAME, json_obj)

if __name__=="__main__":
    main()