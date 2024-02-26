class SyntaxAnalizer:
    def __init__(self) -> None:
        self.parser = {
            ('S', 'automata'): ['A', 'I', 'B', 'V'],
            ('A', 'automata'): ['automata'],
            ('I', '{'): ['{'],
            ('B', 'alfabeto'): ['AL', 'F'],
            ('V', '}'): ['}'],
            ('AL', 'alfabeto'): ['G', ':', 'SM', 'RA', ';'],
            ('G', 'alfabeto'): ['alfabeto'],
            ('SM', 'd'): ['d'],
            ('SM', 'l'): ['l'],
            ('RA', ','): [',', 'SM', 'RA'],
            ('RA', ';'): ['epsilon'],
            ('F', 'aceptacion'): ['C', ':', 'N', 'R', ';'],
            ('C', 'aceptacion'): ['aceptacion'],
            ('N', 'q'): ['Q', 'D'],
            ('D', 'd'): ['d'],
            ('R', ','): [',', 'N', 'R'],
            ('R', ';'): ['epsilon'],
            ('Q', 'q'): ['q']
        }
        self.reserved = ['automata', 'alfabeto', 'aceptacion']
        self.terminals = ['{', 'alfabeto', ',', '}', 'd', 'q', 'aceptacion', 'l', ';', 'automata', ':', '$']
        self.symbols = []
        
    
    def syntax_analyzer(self, entry):
        stack = ['$', 'S']
        result = str(stack) + '\n'
        input = entry.strip()
        input = input.strip() + ' $'
        for word in input.split():
            if word in self.reserved:
                self.symbols.append(word)
            else:
                for letter in word:
                    if letter == 'q':
                        self.symbols.append('q')
                    elif letter.isalpha():
                        self.symbols.append('l')
                    elif letter.isdigit():
                        self.symbols.append('d')
                    else:
                        self.symbols.append(letter)

        index = 0
        while True:
            X = stack.pop()
            a = self.symbols[index]
            if X in self.terminals:
                if X == a:
                    index += 1
                    result += str(stack) + '\n'
                    if X == '$':
                        return result
                else:
                    return result + 'Error de sintaxis '
            else:
                if (X, a) in self.parser:
                    productions = self.parser[(X, a)]
                    if productions != ['epsilon']:
                        for production in reversed(productions):
                            stack.append(production)
                    result += str(stack) + '\n'
                else:
                    return result + 'Error de sintaxis'