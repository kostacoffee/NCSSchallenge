def mountains(line, layers=[], currentLayer=-1, brackets=[]):
    if (len(line) == 0):
        if (len(brackets) == 0):
            return layers
        else:
            raise Exception
    else:
        c = line[0]
        if c == '(' or c == '{':
            brackets.append(c)
            currentLayer += 1
            for i in range(len(layers)):
                if (i != currentLayer):
                    layers[i] += ' '
            if currentLayer >= len(layers):
                layers.append('')
            layers[currentLayer] += c
        elif (c == ')' or c == '}'):
            if (c == ')' and brackets[-1] == '(') or (c == '}' and brackets[-1] == '{'):
                brackets.pop()
                layers[currentLayer] += c
                for i in range(len(layers)):
                    if (i != currentLayer):
                        layers[i] += ' '
                currentLayer -= 1
        return mountains(line[1:], layers, currentLayer, brackets)

try:
    lines = mountains(input())
    for i in range(len(lines)-1, -1, -1):
        print(' '*(i) + lines[i].strip())
except Exception:
    print('Invalid input!')
