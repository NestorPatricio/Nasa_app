def create_html_pic(lista_dict):
    acumulador = ""
    for l in lista_dict:
        acumulador += f"""<h1>{['title']}</h1>
        <p>{['date']}</p>
        <img src="{['url']}">
        <p>{['explanation']}</p>
        """
    
    html = f"""<!DOCTYPE html>
<html lang="es" dir="ltr">

<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--Etiqueta necesaria para la responsividad.-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <!--Link para habilitar la hoja de estilos CSS de Bootstrap v5.1.3, minificado, por CDN.-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!--Link para habilitar las fuentes de Google Fonts.-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!--URL de la fuente específica que se necesita.-->
    <link href="#" rel="stylesheet">
    <!--Link para habilitar los íconos de Font Awesome v5.15.4, por CDN.-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css"
        integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <!--Link para referenciar la hoja de estilos CSS local.-->
    <link rel="stylesheet" href="#">
    <!--Etiquetas para el title de la pestaña y el favicon.-->
    <title>#</title>
    <link rel="shortcut icon" type="#" href="#">
    <!--<meta> informativos para que tu página sea fácil de encontrar por los buscadores.-->
    <meta name="author" content="#">
    <meta name="description" content="#">
    <meta name="keywords" content="#">

</head>

<body>

    <div id="#">
        {acumulador}
    </div>

    <!--Link para habilitar el script JS de JQuery v3.6.0, minificado y con Ajax y módulos effects, por CDN.-->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"
        integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <!--Link para habilitar el script JS de Bootstrap v5.1.3, minificado y con Popper, por CDN.-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
    <!--Link para referenciar el script JS local.-->
    <script src="#"></script>

</body>

</html>
    """
    return html

def create_html_planet(lista_titulos, lista_descripciones, lista_fotos):
    acumulador = ""
    for lt, ld, lf in zip(lista_titulos, lista_descripciones, lista_fotos):
        acumulador += f"""<h1>{lt}</h1>
        <img src="{lf}" widht="50%">
        <p>{ld}</p>
        """
    
    html = f"""<!DOCTYPE html>
<html lang="es" dir="ltr">

<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--Etiqueta necesaria para la responsividad.-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <!--Link para habilitar la hoja de estilos CSS de Bootstrap v5.1.3, minificado, por CDN.-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!--Link para habilitar las fuentes de Google Fonts.-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!--URL de la fuente específica que se necesita.-->
    <link href="#" rel="stylesheet">
    <!--Link para habilitar los íconos de Font Awesome v5.15.4, por CDN.-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css"
        integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <!--Link para referenciar la hoja de estilos CSS local.-->
    <link rel="stylesheet" href="#">
    <!--Etiquetas para el title de la pestaña y el favicon.-->
    <title>#</title>
    <link rel="shortcut icon" type="#" href="#">
    <!--<meta> informativos para que tu página sea fácil de encontrar por los buscadores.-->
    <meta name="author" content="#">
    <meta name="description" content="#">
    <meta name="keywords" content="#">

</head>

<body>

    <div id="#">
        {acumulador}
    </div>

    <!--Link para habilitar el script JS de JQuery v3.6.0, minificado y con Ajax y módulos effects, por CDN.-->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"
        integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <!--Link para habilitar el script JS de Bootstrap v5.1.3, minificado y con Popper, por CDN.-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
    <!--Link para referenciar el script JS local.-->
    <script src="#"></script>

</body>

</html>
    """
    return html

def create_html_earth(lista_fotos, lista_horas):
    acumulador = ""
    for lf, lh in zip(lista_fotos, lista_horas):
        acumulador += f"""<p>{lh}</p>
        <img src="{lf}" widht="50%">
        """
    
    html = f"""<!DOCTYPE html>
<html lang="es" dir="ltr">

<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!--Etiqueta necesaria para la responsividad.-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <!--Link para habilitar la hoja de estilos CSS de Bootstrap v5.1.3, minificado, por CDN.-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!--Link para habilitar las fuentes de Google Fonts.-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <!--URL de la fuente específica que se necesita.-->
    <link href="#" rel="stylesheet">
    <!--Link para habilitar los íconos de Font Awesome v5.15.4, por CDN.-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css"
        integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <!--Link para referenciar la hoja de estilos CSS local.-->
    <link rel="stylesheet" href="#">
    <!--Etiquetas para el title de la pestaña y el favicon.-->
    <title>#</title>
    <link rel="shortcut icon" type="#" href="#">
    <!--<meta> informativos para que tu página sea fácil de encontrar por los buscadores.-->
    <meta name="author" content="#">
    <meta name="description" content="#">
    <meta name="keywords" content="#">

</head>

<body>

    <div id="#">
        {acumulador}
    </div>

    <!--Link para habilitar el script JS de JQuery v3.6.0, minificado y con Ajax y módulos effects, por CDN.-->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"
        integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <!--Link para habilitar el script JS de Bootstrap v5.1.3, minificado y con Popper, por CDN.-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
    <!--Link para referenciar el script JS local.-->
    <script src="#"></script>

</body>

</html>
    """
    return html

if __name__ == '__main__':
    from show import show_pics
    from apod import pull_photos
    from planet import pull_planets
    from earth import pull_earth
    
    dict = pull_photos(2)
    html = create_html_pic(dict)
    show_pics(html, 'apod')
    
    titulos, descripciones, fotos = pull_planets(4, 5)
    html = create_html_planet(titulos, descripciones, fotos)
    show_pics(html, 'planets')
    
    fotos, horas = pull_earth()
    html = create_html_earth(fotos, horas)
    show_pics(html, 'earth')