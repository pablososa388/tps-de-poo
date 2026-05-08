from continente import Continente
from pais import Pais
from provincia import Provincia


def inicializarDatos():

    # -------------------------
    # CONTINENTES
    # -------------------------
    america = Continente("América")
    europa = Continente("Europa")

    # =========================================================
    # AMÉRICA DEL SUR
    # =========================================================

    # ARGENTINA
    argentina = Pais("Argentina", "Buenos Aires", 2780400, america)
    for prov in ["Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "Tucumán",
                 "Entre Ríos", "Salta", "Misiones", "Chaco", "Corrientes",
                 "Santiago del Estero", "San Juan", "Jujuy", "Río Negro",
                 "Neuquén", "Formosa", "Chubut", "San Luis", "Catamarca",
                 "La Rioja", "La Pampa", "Santa Cruz", "Tierra del Fuego"]:
        argentina.agregarProvincia(Provincia(prov))

    # BRASIL
    brasil = Pais("Brasil", "Brasilia", 8515767, america)
    for est in ["São Paulo", "Minas Gerais", "Rio de Janeiro", "Bahia", "Paraná",
                "Rio Grande do Sul", "Pernambuco", "Ceará", "Pará", "Maranhão",
                "Goiás", "Amazonas", "Mato Grosso", "Santa Catarina", "Mato Grosso do Sul"]:
        brasil.agregarProvincia(Provincia(est))

    # CHILE
    chile = Pais("Chile", "Santiago", 756102, america)
    for reg in ["Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama",
                "Coquimbo", "Valparaíso", "Metropolitana", "O'Higgins",
                "Maule", "Ñuble", "Biobío", "La Araucanía", "Los Ríos",
                "Los Lagos", "Aysén", "Magallanes"]:
        chile.agregarProvincia(Provincia(reg))

    # URUGUAY
    uruguay = Pais("Uruguay", "Montevideo", 176215, america)
    for dep in ["Montevideo", "Canelones", "Maldonado", "Colonia", "San José",
                "Salto", "Paysandú", "Rivera", "Tacuarembó", "Rocha"]:
        uruguay.agregarProvincia(Provincia(dep))

    # PARAGUAY
    paraguay = Pais("Paraguay", "Asunción", 406752, america)
    for dep in ["Asunción", "Central", "Alto Paraná", "Itapúa", "Cordillera",
                "Guairá", "Caaguazú", "Misiones", "Paraguarí", "Amambay"]:
        paraguay.agregarProvincia(Provincia(dep))

    # BOLIVIA
    bolivia = Pais("Bolivia", "Sucre", 1098581, america)
    for dep in ["La Paz", "Santa Cruz", "Cochabamba", "Potosí", "Oruro",
                "Chuquisaca", "Tarija", "Beni", "Pando"]:
        bolivia.agregarProvincia(Provincia(dep))

    # PERÚ
    peru = Pais("Perú", "Lima", 1285216, america)
    for dep in ["Lima", "Arequipa", "La Libertad", "Piura", "Cajamarca",
                "Puno", "Junín", "Cusco", "Lambayeque", "Áncash"]:
        peru.agregarProvincia(Provincia(dep))

    # COLOMBIA
    colombia = Pais("Colombia", "Bogotá", 1141748, america)
    for dep in ["Bogotá", "Antioquia", "Valle del Cauca", "Cundinamarca",
                "Atlántico", "Santander", "Bolívar", "Nariño", "Córdoba", "Tolima"]:
        colombia.agregarProvincia(Provincia(dep))

    # VENEZUELA
    venezuela = Pais("Venezuela", "Caracas", 916445, america)
    for est in ["Zulia", "Miranda", "Carabobo", "Bolívar", "Anzoátegui",
                "Táchira", "Mérida", "Lara", "Aragua", "Monagas"]:
        venezuela.agregarProvincia(Provincia(est))

    # ECUADOR
    ecuador = Pais("Ecuador", "Quito", 283561, america)
    for prov in ["Pichincha", "Guayas", "Manabí", "El Oro", "Los Ríos",
                 "Azuay", "Esmeraldas", "Loja", "Tungurahua", "Chimborazo"]:
        ecuador.agregarProvincia(Provincia(prov))

    # GUYANA
    guyana = Pais("Guyana", "Georgetown", 214969, america)
    for reg in ["Demerara-Mahaica", "East Berbice-Corentyne", "Essequibo Islands"]:
        guyana.agregarProvincia(Provincia(reg))

    # SURINAM
    surinam = Pais("Surinam", "Paramaribo", 163820, america)
    for dist in ["Paramaribo", "Wanica", "Nickerie", "Commewijne"]:
        surinam.agregarProvincia(Provincia(dist))

    # =========================================================
    # AMÉRICA CENTRAL Y CARIBE
    # =========================================================

    # MÉXICO
    mexico = Pais("México", "Ciudad de México", 1964375, america)
    for est in ["Ciudad de México", "Jalisco", "Nuevo León", "Veracruz",
                "Puebla", "Guanajuato", "Chiapas", "Michoacán", "Oaxaca", "Estado de México"]:
        mexico.agregarProvincia(Provincia(est))

    # CUBA
    cuba = Pais("Cuba", "La Habana", 109884, america)
    for prov in ["La Habana", "Santiago de Cuba", "Holguín", "Villa Clara", "Camagüey"]:
        cuba.agregarProvincia(Provincia(prov))

    # GUATEMALA
    guatemala = Pais("Guatemala", "Ciudad de Guatemala", 108889, america)
    for dep in ["Guatemala", "Quetzaltenango", "Huehuetenango", "Alta Verapaz", "San Marcos"]:
        guatemala.agregarProvincia(Provincia(dep))

    # HONDURAS
    honduras = Pais("Honduras", "Tegucigalpa", 112492, america)
    for dep in ["Francisco Morazán", "Cortés", "Olancho", "Choluteca", "Santa Bárbara"]:
        honduras.agregarProvincia(Provincia(dep))

    # EL SALVADOR
    el_salvador = Pais("El Salvador", "San Salvador", 21041, america)
    for dep in ["San Salvador", "Santa Ana", "San Miguel", "La Libertad", "Sonsonate"]:
        el_salvador.agregarProvincia(Provincia(dep))

    # NICARAGUA
    nicaragua = Pais("Nicaragua", "Managua", 130373, america)
    for dep in ["Managua", "Matagalpa", "Chinandega", "León", "Granada"]:
        nicaragua.agregarProvincia(Provincia(dep))

    # COSTA RICA
    costa_rica = Pais("Costa Rica", "San José", 51100, america)
    for prov in ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste"]:
        costa_rica.agregarProvincia(Provincia(prov))

    # PANAMÁ
    panama = Pais("Panamá", "Ciudad de Panamá", 75417, america)
    for prov in ["Panamá", "Colón", "Chiriquí", "Bocas del Toro", "Veraguas"]:
        panama.agregarProvincia(Provincia(prov))

    # =========================================================
    # AMÉRICA DEL NORTE
    # =========================================================

    # ESTADOS UNIDOS
    eeuu = Pais("Estados Unidos", "Washington D.C.", 9833517, america)
    for est in ["California", "Texas", "Florida", "Nueva York", "Illinois",
                "Pensilvania", "Ohio", "Georgia", "Carolina del Norte", "Michigan"]:
        eeuu.agregarProvincia(Provincia(est))

    # CANADÁ
    canada = Pais("Canadá", "Ottawa", 9984670, america)
    for prov in ["Ontario", "Quebec", "Columbia Británica", "Alberta", "Manitoba",
                 "Saskatchewan", "Nueva Escocia", "Nuevo Brunswick"]:
        canada.agregarProvincia(Provincia(prov))

    # =========================================================
    # EUROPA
    # =========================================================

    # ESPAÑA
    espana = Pais("España", "Madrid", 505990, europa)
    for ccaa in ["Madrid", "Cataluña", "Andalucía", "Valencia", "Galicia",
                 "País Vasco", "Castilla y León", "Castilla-La Mancha", "Aragón", "Murcia"]:
        espana.agregarProvincia(Provincia(ccaa))

    # FRANCIA
    francia = Pais("Francia", "París", 551695, europa)
    for reg in ["Île-de-France", "Provenza", "Occitania", "Nueva Aquitania",
                "Auvernia-Ródano-Alpes", "Bretaña", "Normandía", "Borgoña"]:
        francia.agregarProvincia(Provincia(reg))

    # ALEMANIA
    alemania = Pais("Alemania", "Berlín", 357114, europa)
    for land in ["Baviera", "Renania del Norte-Westfalia", "Baden-Württemberg",
                 "Baja Sajonia", "Hesse", "Sajonia", "Berlín", "Hamburgo"]:
        alemania.agregarProvincia(Provincia(land))

    # ITALIA
    italia = Pais("Italia", "Roma", 301340, europa)
    for reg in ["Lombardía", "Lacio", "Campania", "Sicilia", "Véneto",
                "Piamonte", "Puglia", "Toscana", "Emilia-Romaña", "Cerdeña"]:
        italia.agregarProvincia(Provincia(reg))

    # PORTUGAL
    portugal = Pais("Portugal", "Lisboa", 92212, europa)
    for dist in ["Lisboa", "Oporto", "Braga", "Setúbal", "Aveiro", "Coimbra"]:
        portugal.agregarProvincia(Provincia(dist))

    # REINO UNIDO
    reino_unido = Pais("Reino Unido", "Londres", 243610, europa)
    for reg in ["Inglaterra", "Escocia", "Gales", "Irlanda del Norte"]:
        reino_unido.agregarProvincia(Provincia(reg))

    # PAÍSES BAJOS
    paises_bajos = Pais("Países Bajos", "Ámsterdam", 41543, europa)
    for prov in ["Holanda del Norte", "Holanda del Sur", "Utrecht", "Gelderland", "Brabante del Norte"]:
        paises_bajos.agregarProvincia(Provincia(prov))

    # BÉLGICA
    belgica = Pais("Bélgica", "Bruselas", 30528, europa)
    for reg in ["Bruselas", "Flandes", "Valonia"]:
        belgica.agregarProvincia(Provincia(reg))

    # SUIZA
    suiza = Pais("Suiza", "Berna", 41285, europa)
    for cant in ["Zúrich", "Berna", "Vaud", "Aargau", "Ginebra"]:
        suiza.agregarProvincia(Provincia(cant))

    # AUSTRIA
    austria = Pais("Austria", "Viena", 83871, europa)
    for land in ["Viena", "Baja Austria", "Alta Austria", "Estiria", "Tirol"]:
        austria.agregarProvincia(Provincia(land))

    # POLONIA
    polonia = Pais("Polonia", "Varsovia", 312696, europa)
    for voi in ["Mazovia", "Silesia", "Gran Polonia", "Pomerania", "Małopolska"]:
        polonia.agregarProvincia(Provincia(voi))

    # REPÚBLICA CHECA
    rep_checa = Pais("República Checa", "Praga", 78866, europa)
    for reg in ["Praga", "Bohemia Central", "Moravia del Sur", "Moravia-Silesia"]:
        rep_checa.agregarProvincia(Provincia(reg))

    # HUNGRÍA
    hungria = Pais("Hungría", "Budapest", 93028, europa)
    for reg in ["Budapest", "Pest", "Győr-Moson-Sopron", "Hajdú-Bihar", "Borsod"]:
        hungria.agregarProvincia(Provincia(reg))

    # RUMANIA
    rumania = Pais("Rumania", "Bucarest", 238397, europa)
    for reg in ["Bucarest", "Cluj", "Timișoara", "Iași", "Constanța"]:
        rumania.agregarProvincia(Provincia(reg))

    # GRECIA
    grecia = Pais("Grecia", "Atenas", 131957, europa)
    for reg in ["Ática", "Macedonia Central", "Tesalia", "Macedonia Oriental", "Peloponeso"]:
        grecia.agregarProvincia(Provincia(reg))

    # SUECIA
    suecia = Pais("Suecia", "Estocolmo", 450295, europa)
    for lan in ["Estocolmo", "Västra Götaland", "Skåne", "Östergötland", "Uppsala"]:
        suecia.agregarProvincia(Provincia(lan))

    # NORUEGA
    noruega = Pais("Noruega", "Oslo", 385207, europa)
    for reg in ["Oslo", "Viken", "Vestland", "Innlandet", "Trøndelag"]:
        noruega.agregarProvincia(Provincia(reg))

    # DINAMARCA
    dinamarca = Pais("Dinamarca", "Copenhague", 43094, europa)
    for reg in ["Capital", "Selandia", "Jutlandia del Sur", "Jutlandia Central", "Nordjylland"]:
        dinamarca.agregarProvincia(Provincia(reg))

    # FINLANDIA
    finlandia = Pais("Finlandia", "Helsinki", 338455, europa)
    for reg in ["Finlandia Meridional", "Finlandia Occidental", "Finlandia Oriental", "Oulu", "Laponia"]:
        finlandia.agregarProvincia(Provincia(reg))

    # RUSIA (parte europea)
    rusia = Pais("Rusia", "Moscú", 17098242, europa)
    for reg in ["Moscú", "San Petersburgo", "Krasnodar", "Sverdlovsk", "Tartaristán"]:
        rusia.agregarProvincia(Provincia(reg))

    # UCRANIA
    ucrania = Pais("Ucrania", "Kiev", 603550, europa)
    for obl in ["Kiev", "Járkov", "Dnipró", "Donetsk", "Odesa"]:
        ucrania.agregarProvincia(Provincia(obl))

    # =========================================================
    # LÍMITES - AMÉRICA DEL SUR
    # =========================================================
    argentina.agregarLimitrofe(chile)
    argentina.agregarLimitrofe(bolivia)
    argentina.agregarLimitrofe(paraguay)
    argentina.agregarLimitrofe(brasil)
    argentina.agregarLimitrofe(uruguay)

    brasil.agregarLimitrofe(argentina)
    brasil.agregarLimitrofe(uruguay)
    brasil.agregarLimitrofe(paraguay)
    brasil.agregarLimitrofe(bolivia)
    brasil.agregarLimitrofe(peru)
    brasil.agregarLimitrofe(colombia)
    brasil.agregarLimitrofe(venezuela)
    brasil.agregarLimitrofe(guyana)
    brasil.agregarLimitrofe(surinam)

    chile.agregarLimitrofe(argentina)
    chile.agregarLimitrofe(peru)
    chile.agregarLimitrofe(bolivia)

    uruguay.agregarLimitrofe(argentina)
    uruguay.agregarLimitrofe(brasil)

    paraguay.agregarLimitrofe(argentina)
    paraguay.agregarLimitrofe(brasil)
    paraguay.agregarLimitrofe(bolivia)

    bolivia.agregarLimitrofe(argentina)
    bolivia.agregarLimitrofe(chile)
    bolivia.agregarLimitrofe(peru)
    bolivia.agregarLimitrofe(brasil)
    bolivia.agregarLimitrofe(paraguay)

    peru.agregarLimitrofe(ecuador)
    peru.agregarLimitrofe(colombia)
    peru.agregarLimitrofe(brasil)
    peru.agregarLimitrofe(bolivia)
    peru.agregarLimitrofe(chile)

    colombia.agregarLimitrofe(venezuela)
    colombia.agregarLimitrofe(brasil)
    colombia.agregarLimitrofe(peru)
    colombia.agregarLimitrofe(ecuador)
    colombia.agregarLimitrofe(panama)

    venezuela.agregarLimitrofe(colombia)
    venezuela.agregarLimitrofe(brasil)
    venezuela.agregarLimitrofe(guyana)

    ecuador.agregarLimitrofe(colombia)
    ecuador.agregarLimitrofe(peru)

    guyana.agregarLimitrofe(venezuela)
    guyana.agregarLimitrofe(brasil)
    guyana.agregarLimitrofe(surinam)

    surinam.agregarLimitrofe(guyana)
    surinam.agregarLimitrofe(brasil)

    # =========================================================
    # LÍMITES - AMÉRICA CENTRAL Y NORTE
    # =========================================================
    mexico.agregarLimitrofe(eeuu)
    mexico.agregarLimitrofe(guatemala)
    mexico.agregarLimitrofe(belize := Pais("Belice", "Belmopán", 22966, america))

    guatemala.agregarLimitrofe(mexico)
    guatemala.agregarLimitrofe(honduras)
    guatemala.agregarLimitrofe(el_salvador)

    honduras.agregarLimitrofe(guatemala)
    honduras.agregarLimitrofe(el_salvador)
    honduras.agregarLimitrofe(nicaragua)

    el_salvador.agregarLimitrofe(guatemala)
    el_salvador.agregarLimitrofe(honduras)

    nicaragua.agregarLimitrofe(honduras)
    nicaragua.agregarLimitrofe(costa_rica)

    costa_rica.agregarLimitrofe(nicaragua)
    costa_rica.agregarLimitrofe(panama)

    panama.agregarLimitrofe(costa_rica)
    panama.agregarLimitrofe(colombia)

    eeuu.agregarLimitrofe(canada)
    eeuu.agregarLimitrofe(mexico)

    canada.agregarLimitrofe(eeuu)

    # =========================================================
    # LÍMITES - EUROPA
    # =========================================================
    espana.agregarLimitrofe(portugal)
    espana.agregarLimitrofe(francia)
    espana.agregarLimitrofe(andorra := Pais("Andorra", "Andorra la Vella", 468, europa))

    francia.agregarLimitrofe(espana)
    francia.agregarLimitrofe(belgica)
    francia.agregarLimitrofe(alemania)
    francia.agregarLimitrofe(suiza)
    francia.agregarLimitrofe(italia)

    alemania.agregarLimitrofe(francia)
    alemania.agregarLimitrofe(belgica)
    alemania.agregarLimitrofe(paises_bajos)
    alemania.agregarLimitrofe(austria)
    alemania.agregarLimitrofe(suiza)
    alemania.agregarLimitrofe(polonia)
    alemania.agregarLimitrofe(rep_checa)

    italia.agregarLimitrofe(francia)
    italia.agregarLimitrofe(suiza)
    italia.agregarLimitrofe(austria)
    italia.agregarLimitrofe(eslovenia := Pais("Eslovenia", "Liubliana", 20273, europa))

    austria.agregarLimitrofe(alemania)
    austria.agregarLimitrofe(suiza)
    austria.agregarLimitrofe(italia)
    austria.agregarLimitrofe(hungria)
    austria.agregarLimitrofe(rep_checa)

    suiza.agregarLimitrofe(francia)
    suiza.agregarLimitrofe(alemania)
    suiza.agregarLimitrofe(austria)
    suiza.agregarLimitrofe(italia)

    belgica.agregarLimitrofe(francia)
    belgica.agregarLimitrofe(alemania)
    belgica.agregarLimitrofe(paises_bajos)

    paises_bajos.agregarLimitrofe(belgica)
    paises_bajos.agregarLimitrofe(alemania)

    polonia.agregarLimitrofe(alemania)
    polonia.agregarLimitrofe(rep_checa)
    polonia.agregarLimitrofe(hungria)
    polonia.agregarLimitrofe(ucrania)
    polonia.agregarLimitrofe(rusia)

    portugal.agregarLimitrofe(espana)

    grecia.agregarLimitrofe(bulgaria := Pais("Bulgaria", "Sofía", 110879, europa))
    grecia.agregarLimitrofe(rumania)

    rumania.agregarLimitrofe(hungria)
    rumania.agregarLimitrofe(ucrania)
    rumania.agregarLimitrofe(grecia)

    ucrania.agregarLimitrofe(polonia)
    ucrania.agregarLimitrofe(rumania)
    ucrania.agregarLimitrofe(rusia)

    # =========================================================
    # VINCULAR PAÍSES A CONTINENTES
    # =========================================================
    for pais in [argentina, brasil, chile, uruguay, paraguay, bolivia, peru,
                 colombia, venezuela, ecuador, guyana, surinam,
                 mexico, cuba, guatemala, honduras, el_salvador,
                 nicaragua, costa_rica, panama, eeuu, canada]:
        america.agregarPais(pais)

    for pais in [espana, francia, alemania, italia, portugal, reino_unido,
                 paises_bajos, belgica, suiza, austria, polonia, rep_checa,
                 hungria, rumania, grecia, suecia, noruega, dinamarca,
                 finlandia, rusia, ucrania]:
        europa.agregarPais(pais)

    return america, europa
