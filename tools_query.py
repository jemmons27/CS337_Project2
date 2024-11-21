import regex as re
import spacy


def find_tools(task, steps, current_step, ingredients, last_query):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(steps[current_step-1]['step'])
    print(current_step)
    for token in doc:
        print(token.text, token.dep_, token.pos_, token.morph)
        
    return current_step, last_query



### (det) amod adj -> pobj/dobj/conj NOUN (punct) (cc) ||||| |||
### det compound NOUN -> dobj/pobj NOUN punct |||
### det amod VERB -> pobj PROPN |
### prep ADP pobj NOUN -> dobj NOUN |   probably outlier
### prep ADP det pobj NOUN |
### 
 

### prepared cookie sheet: amod ADJ, compound NOUN, pobj NOUN
### an ice cream scoop,: det DET, compound NOUN, compound NOUN, dobj NOUN punct
### a large bowl,: det DET, amod ADJ, pobj NOUN
### the preheated oven,: det DET, amod VERB, pobj PROPN
### from cookie sheets: prep ADP, compound NOUN, pobj NOUN
### on wire racks\b: prep ADP, pobj NOUN, dobj NOUN
### a resealable plastic bag;: det DET, amod ADJ, amod ADJ, pobj NOUN, punct
### in a Dutch oven or large pot: prep ADP, det, amod ADJ, amod ADJ, cc CCONJ, conj ADJ, pobj NOUN
### use a slotted spoon: conj VERB, det, amod ADJ, dobj NOUN
### into a blender: prep ADP, det, pobj NOUN, \b
### in a deep-fryer: prep ADP, det, amod ADJ, punct, pobj NOUN
### or large saucepan: cc amod ADJ conj NOUN
### 