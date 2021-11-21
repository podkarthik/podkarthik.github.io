import sys

with open(sys.argv[1]) as f:
    file = f.read()
    file = file.replace('<head>',
        '<head><script type="module" src="https://js.withorbit.com/orbit-web-component.js"></script>')

with open(sys.argv[1], 'w') as f:
    f.write(file)
