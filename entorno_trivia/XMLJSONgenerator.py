import pandas as pd
import json
import xml.etree.ElementTree as ET


#CREACIÓN DE XML
trivia = ET.Element("triviaXML")
pregunta = ET.SubElement(trivia, 'pregunta')
#pregunta1
ET.SubElement(pregunta, "Pregunta", id="1").text = "¿En qué año acabo la Segunda Guerra Mundial?"
ET.SubElement(pregunta, "Respuesta", id="1", correcta ="false").text = "1939"
ET.SubElement(pregunta, "Respuesta", id="2", correcta ="true").text = "1945"
ET.SubElement(pregunta, "Respuesta", id="3", correcta ="false").text = "1944"
ET.SubElement(pregunta, "Respuesta", id="4", correcta ="false").text = "1950"
#pregunta2
ET.SubElement(pregunta, "Pregunta", id="2").text = "¿Qué acontecimiento marcó el inicio de la Revolución Francesa en 1789?"
ET.SubElement(pregunta, "Respuesta", id="1", correcta ="false").text = "La firma del Tratado de Versalles"
ET.SubElement(pregunta, "Respuesta", id="2", correcta ="false").text = "La caída del Muro de Berlín"
ET.SubElement(pregunta, "Respuesta", id="3", correcta ="true").text = "La toma de la Bastilla"
ET.SubElement(pregunta, "Respuesta", id="4", correcta ="false").text = "La declaración de la Independencia de Estados UnidosRespuesta correcta"
#pregunta3
ET.SubElement(pregunta, "Pregunta", id="3").text = "¿Quién fue el primer emperador romano?"
ET.SubElement(pregunta, "Respuesta", id="1", correcta ="true").text = "Augusto"
ET.SubElement(pregunta, "Respuesta", id="2", correcta ="false").text = "Nerón"
ET.SubElement(pregunta, "Respuesta", id="3", correcta ="false").text = "Julio César"
ET.SubElement(pregunta, "Respuesta", id="4", correcta ="false").text = "Roberto Mancas"
#pregunta4
ET.SubElement(pregunta, "Pregunta", id="4").text = "¿Cuál es considerado el primer documento constitucional escrito del mundo?"
ET.SubElement(pregunta, "Respuesta", id="1", correcta ="true").text = "La Carta Magna"
ET.SubElement(pregunta, "Respuesta", id="2", correcta ="false").text = "La Constitución de los Estados Unidos"
ET.SubElement(pregunta, "Respuesta", id="3", correcta ="false").text = "El Código de Hammurabi"
ET.SubElement(pregunta, "Respuesta", id="4", correcta ="false").text = "Las Leyes de las Doce Tablas"
#pregunta5
ET.SubElement(pregunta, "Pregunta", id="5").text = "¿En qué año cayó el Imperio Romano de Occidente?"
ET.SubElement(pregunta, "Respuesta", id="1", correcta ="false").text = "509 d.C."
ET.SubElement(pregunta, "Respuesta", id="2", correcta ="false").text = "1453 d.C."
ET.SubElement(pregunta, "Respuesta", id="3", correcta ="false").text = "1066 d.C."
ET.SubElement(pregunta, "Respuesta", id="4", correcta ="true").text = "476 d.C"
arbol = ET.ElementTree(trivia)
arbol.write("trivia.xml", encoding="utf-8", xml_declaration=True)
print(ET.tostring(trivia))

#CREACIÓN DE JSON
trivia = {}
trivia["preguntas"] = []
trivia["preguntas"].append({
    "Numero": "1",
    "Enunciado": "¿En qué año acabo la Segunda Guerra Mundial?",
    "Respuesta1": "1939",
    "Respuesta2": "1945",
    "Respuesta3": "1944",
    "Respuesta4": "1950",
    "RespuestaCorrecta": "Respuesta2"
})
trivia["preguntas"].append({
    "Numero": "2",
    "Enunciado": "¿Qué acontecimiento marcó el inicio de la Revolución Francesa en 1789?",
    "Respuesta1": "La firma del Tratado de Versalles",
    "Respuesta2": "La caída del Muro de Berlín",
    "Respuesta3": "La toma de la Bastilla",
    "Respuesta4": "La declaración de la Independencia de Estados UnidosRespuesta correcta",
    "RespuestaCorrecta": "Respuesta3"
})
trivia["preguntas"].append({
    "Numero": "3",
    "Enunciado": "¿Quién fue el primer emperador romano?",
    "Respuesta1": "Augusto",
    "Respuesta2": "Nerón",
    "Respuesta3": "Julio César",
    "Respuesta4": "Roberto Mancas",
    "RespuestaCorrecta": "Respuesta1"
})
trivia["preguntas"].append({
    "Numero": "4",
    "Enunciado": "¿Cuál es considerado el primer documento constitucional escrito del mundo?",
    "Respuesta1": "La Carta Magna",
    "Respuesta2": "La Constitución de los Estados Unidos",
    "Respuesta3": "El Código de Hammurabi",
    "Respuesta4": "Las Leyes de las Doce Tablas",
    "RespuestaCorrecta": "Respuesta1"
})
trivia["preguntas"].append({
    "Numero": "5",
    "Enunciado": "¿En qué año cayó el Imperio Romano de Occidente?",
    "Respuesta1": "509 d.C.",
    "Respuesta2": "1453 d.C.",
    "Respuesta3": "1066 d.C.",
    "Respuesta4": "476 d.C",
    "RespuestaCorrecta": "Respuesta4"
})
with open('preguntas.json', 'w') as file:
    json.dump(trivia, file, indent=4)