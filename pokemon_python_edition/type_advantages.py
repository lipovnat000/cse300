def type_matchups(attacking_type, defending_type):
    effective = 2
    neutral = 1
    resistant = 0.5
    ineffective = 0

    if attacking_type == "Normal":
        if defending_type in ["Rock", "Steel"]:
            return resistant
        elif defending_type in ["Ghost"]:
            return ineffective
        else:
            return neutral
        
    if attacking_type == "Fire":
        if defending_type in ["Grass", "Ice", "Bug", "Steel"]:
            return effective
        elif defending_type in ["Fire", "Water", "Rock", "Dragon"]:
            return resistant      
        else:
            return neutral
        
    if attacking_type == "Water":
        if defending_type in ["Fire", "Ground", "Rock"]:
            return effective
        elif defending_type in ["Water", "Grass", "Dragon"]:
            return resistant
        else:
            return neutral
        
    if attacking_type == "Grass":
        if defending_type in ["Water", "Ground", "Rock"]:
            return effective
        elif defending_type in ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]:
            return resistant        
        else:
            return neutral
        
    if attacking_type == "Electric":
        if defending_type in ["Water", "Flying"]:
            return effective
        elif defending_type in ["Grass", "Electric", "Dragon"]:
            return resistant
        elif defending_type in ["Ground"]:
            return ineffective        
        else:
            return neutral
        
    if attacking_type == "Ice":
        if defending_type in ["Grass", "Ground", "Flying", "Dragon"]:
            return effective
        elif defending_type in ["Fire", "Water", "Ice", "Steel"]:
            return resistant
        else:
            return neutral
    
    if attacking_type == "Fighting":
        if defending_type in ["Normal", "Rock", "Steel", "Ice", "Dark"]:
            return effective
        elif defending_type in ["Flying", "Poison", "Bug", "Psychic", "Fairy"]:
            return resistant
        elif defending_type in ["Ghost"]:
            return ineffective        
        else:
            return neutral
        
    if attacking_type == "Poison":
        if defending_type in ["Grass", "Fairy"]:
            return effective
        elif defending_type in ["Poison", "Ground", "Rock", "Ghost"]:
            return resistant
        elif defending_type in ["Steel"]:
            return ineffective        
        else:
            return neutral
        
    if attacking_type == "Ground":
        if defending_type in ["Fire", "Electric", "Poison", "Rock", "Steel"]:
            return effective
        elif defending_type in ["Grass", "Bug"]:
            return resistant
        elif defending_type in ["Flying"]:
            return ineffective        
        else:
            return neutral
        
    if attacking_type == "Flying":
        if defending_type in ["Fighting", "Bug", "Grass"]:
            return effective
        elif defending_type in ["Rock", "Steel", "Electric"]:
            return resistant
        else:
            return neutral
        
    if attacking_type == "Psychic":
        if defending_type in ["Fighting", "Poison"]:
            return effective
        elif defending_type in ["Psychic", "Steel"]:
            return resistant
        elif defending_type in ["Dark"]:
            return ineffective        
        else:
            return neutral