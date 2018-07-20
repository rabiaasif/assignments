import sys
import requests 
import json

def arguments():
    if len(sys.argv) == 3:
        return True
    else: 
        return False
def get_pokemon_info(name):
    url = 'http://pokeapi.co/api/v2/pokemon/' + name 
    r = requests.get(url)
    if (r.status_code == 200):
        poke_info = json.loads(r.text)  
        return get_name_and_type(poke_info)
    else:
        print("invalid pokemon name/type")
    
def get_name_and_type(poke_info):
    name_type = {poke_info['name']: poke_info['id']}
    for url in poke_info['types']:
        name_type[url['type']['name']] = ((url['type']['url']))
    return name_type

def get_type_info(url, pokemon):
    
    '''
    half_damage_from = 1
    half_damage_to = 2
    double_damage_from = 3
    no_damage_to = 4 
    double_damage_to = 5 
    
    '''
    damage = ''
    r = requests.get(url)
    poke_info = json.loads(r.text) 
    for i in (poke_info['damage_relations'].keys()):
        for j in poke_info['damage_relations'][i]:
            if (j['name']) in pokemon.keys():
                damage = i 
    return damage
        
def get_poke_name(poke_dict):
 
    for i in poke_dict.keys():
        if type(poke_dict[i]) == int: 
            return i
   
        
    
    
def winner():
    if arguments() == True:
        first_pokemon = (get_pokemon_info(sys.argv[1]))
        second_pokemon = (get_pokemon_info(sys.argv[2]))
       
        if len(first_pokemon.keys()) < len(second_pokemon.keys()):
            for i in (first_pokemon.keys()):
                if (type(first_pokemon[i])) == str and first_pokemon[i].startswith("https"):
                    damage = (get_type_info(first_pokemon[i], second_pokemon))
                    if damage.endswith("to"):
                        print(get_poke_name(second_pokemon))
                        break
                    else:
                        print(get_poke_name(first_pokemon))
                        break
        else:  
            for i in (second_pokemon.keys()):
                if (type(second_pokemon[i])) == str and second_pokemon[i].startswith("https"):
                    damage = (get_type_info(second_pokemon[i], first_pokemon))
                    if damage.endswith("to"):
                        print(get_poke_name(second_pokemon))
                        break
                    else:
                        print(get_poke_name(first_pokemon))
                        break
    else:
        print("wrong number of arguments")
    
if __name__ == "__main__":
    winner()
    
    
    
