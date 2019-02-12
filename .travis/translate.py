import json, os, sys
#
# This script is intended to search for keywords in english and translate to other languages.
# Please be very careful when using certain keywords in the dicctionary, because this script
# can search-replace code which will cause the form to break.
#


#   The envisioned use would be something like this:
#       $ python .travis/translate.py  "./public/js/app.bundle.js"   "./local/es.json"
#       

translation_file = "app.bundle.js"
json_file = "local/complaintDict.json"
directory = os.path.dirname(os.path.abspath(__file__))



#
# A sample json file looks like this, but notice they are stored in the local directory
#

sample_dict = {
    "language": "ru",   # The language code (it can be anything...)
    "urlpath": "fiscalizacion-de-policia/queja",
    "translations": {
            # Translate routes
            "police-oversight/complaint": "fiscalizacion-de-policia/queja",
            "introduction":"introduccion",
            "what-happened": "que-sucedio",
            "share-evidence": "compartir-evidencia",
            "officer-details": "detalles-oficial",
            "witness-details": "detalles-testigos",
            "about-you": "acerca-de-usted",
            "review-and-submit": "revisar-y-enviar",
            
            # Translate SAFE Phrases (long phrases that can be easily differentiated from code)
            # Long phrases should be translated first, short or single-word translations should be done last.

            "Office of Police Oversight": "Oficina de la Fiscalizacion de la Policia",
            "File a Complaint": "Envie una queja",

            # Translate UNSAFE Phrases (words or keywords that could replace javascript code)
            # For this cases, it is important to use the percentage character: '%' which stands for a double quote symbol in javascript
            "%Remove%": "%Remover%",
            "%Time %": "%Tiempo%",
            "%True%": "%Si%",

            # Patch Code (notice the use of '%' and commas)
            # This will specifically find the code which specifies an array of strings
            # which is contained in quotes and separated by a comma.
            "%Sunday%,%Monday%,%Tuesday%,%Wednesday%,%Thursday%,%Friday%,%Saturday%":
					"%Domingo%,%Lunes%,%Martes%,%Miercoles%,%Jueves%,%Viernes%,%Sabado%",

            "<button>Edit</button>": "<button>Editar</button>",

            # Short translations last please, and within '%' symbols to avoid code conflicts.
            "%Abort%": "%Abortar%",
            "%Retry%": "%Re-Intentar%",
            "%Cancel%": "%Cancelar%",
            "%Undo%": "%Deshacer%",
            "%Upload%": "%Enviar%",
            "%Edit%": "%Editar%"

    }
}





def filter_string(inputstr):
	return inputstr.replace("%", "\"")



with open(json_file) as json_file:
	data = json.load(json_file)

	for item in data:
        language =  item['language']
        urlpath =  item['urlpath']
        translations = item['translations']
        translation_public_dir = "public_" + language

        try:
            os.system("cp -r public " + translation_public_dir)
        except Exception as e:
            print("Could not copy 'public' directory." + str(e))
            sys.exit(1) # Helpful to indicate Travis there has been a problem with the deployment

        translation_file_lang =  translation_public_dir + "/js/" + translation_file
        fullAppString = ""

		print("language: " + language)
		print("urlpath: " + urlpath)
		print("translation_file_lang: " + translation_file_lang)

		with open(translation_file_lang) as f:
				fullAppString=f.read()


		for phrase, translation in translations.items():
			p = filter_string(phrase)
			t = filter_string(translation)

			print("{0} | Phrase: '{1}' = '{2}'".format(translation_file_lang, p, t))
			fullAppString = fullAppString.replace(p, t)
			
			 
		with open(translation_file_lang, "w") as f:
			f.write(fullAppString)