All_types = ('Normal', 'Fire', 'Water', 'Grass', 'Flying', 'Fighting', 'Poison', 'Electric', 'Ground', 'Rock',
             'Psychic', 'Ice', 'Bug', 'Ghost', 'Steel', 'Dragon', 'Dark', 'Fairy')

Grass = {'name': 'Grass',
         2: ['Flying', 'Poison', 'Bug', 'Fire', 'Ice'],
         4: [],
         0.5: ['Ground', 'Water', 'Grass', 'Electric'],
         0.25: [],
         0: []
         }

Poison = {'name': 'Poison',
         2: ['Ground', 'Psychic'],
         4: [],
         0.5: ['Fighting', 'Poison', 'Grass', 'Bug', 'Fairy'],
         0.25: [],
         0: []
         }

Fire = {'name': 'Fire',
       2: ['Water', 'Rock', 'Ground'],
       4: [],
       0.5: ['Bug', 'Steel', 'Fire', 'Grass', 'Ice', 'Fairy'],
       0.25: [],
       0: []
       }

Flying = {'name': 'Flying',
         2: ['Rock', 'Electric', 'Ice'],
         4: [],
         0.5: ['Fighting', 'Bug', 'Grass'],
         0.25: [],
         0: ['Ground']
         }

Water = {'name': 'Water',
        2: ['Grass', 'Electric'],
        4: [],
        0.5: ['Steel', 'Fire', 'Water', 'Ice'],
        0.25: [],
        0: []
        }
