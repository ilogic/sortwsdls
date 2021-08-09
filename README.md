## SORTWSDLS

Ordena ficheros de extensión WSDL en la carpeta actual y en todas las subcarpetas, creando ficheros con el mismo
nombre (incluyendo .wsdl) y añadiendoles la extensión .sorted  (p.ej: GET_VALUES.wsdl => GET_VALUES.wsdl.sorted)

### Actualización

Se ha mejorado el proceso incluyendo la librería lxml de etree que mejora mucho el resultado

[Fuente en StackOverflow (respuesta del usuario "zesk")](https://stackoverflow.com/questions/25338817/sorting-xml-in-python-etree)

Para instalarla se puede hacer mediante pip:

`pip install lxml`
