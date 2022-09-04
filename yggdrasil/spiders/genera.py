import scrapy

# A = ['Acanthaceae', 'Achariaceae', 'Achatocarpaceae', 'Acoraceae', 'Actinidiaceae', 'Adoxaceae', 'Aextoxicaceae', 'Aizoaceae', 'Akaniaceae', 'Alismataceae', 'Alseuosmiaceae', 'Alstroemeriaceae', 'Altingiaceae', 'Amaranthaceae', 'Amaryllidaceae', 'Amborellaceae', 'Anacampserotaceae', 'Anacardiaceae', 'Anarthriaceae', 'Ancistrocladaceae', 'Anisophylleaceae', 'Annonaceae', 'Aphanopetalaceae', 'Aphloiaceae', 'Apiaceae', 'Apocynaceae', 'Apodanthaceae', 'Aponogetonaceae', 'Aquifoliaceae', 'Araceae', 'Araliaceae', 'Arecaceae', 'Argophyllaceae', 'Aristolochiaceae', 'Asparagaceae', 'Asteliaceae', 'Asteropeiaceae', 'Atherospermataceae', 'Austrobaileyaceae', 'Balanopaceae', 'Balanophoraceae', 'Balsaminaceae', 'Barbeuiaceae', 'Barbeyaceae', 'Basellaceae', 'Bataceae', 'Begoniaceae', 'Berberidaceae', 'Berberidopsidaceae', 'Betulaceae', 'Biebersteiniaceae', 'Bignoniaceae', 'Bixaceae', 'Blandfordiaceae', 'Bonnetiaceae', 'Boraginaceae', 'Boryaceae', 'Brassicaceae', 'Bromeliaceae', 'Brunelliaceae', 'Bruniaceae', 'Burmanniaceae', 'Burseraceae', 'Butomaceae', 'Buxaceae', 'Byblidaceae', 'Cabombaceae', 'Cactaceae', 'Calceolariaceae', 'Calophyllaceae', 'Calycanthaceae', 'Calyceraceae', 'Campanulaceae', 'Campynemataceae', 'Canellaceae', 'Cannabaceae', 'Cannaceae', 'Capparaceae', 'Caprifoliaceae', 'Cardiopteridaceae', 'Caricaceae', 'Carlemanniaceae', 'Caryocaraceae', 'Caryophyllaceae', 'Casuarinaceae', 'Celastraceae', 'Centrolepidaceae', 'Centroplacaceae', 'Cephalotaceae', 'Ceratophyllaceae', 'Cercidiphyllaceae', 'Chloranthaceae', 'Chrysobalanaceae', 'Circaeasteraceae', 'Cistaceae', 'Cleomaceae', 'Clethraceae', 'Clusiaceae', 'Colchicaceae', 'Columelliaceae', 'Combretaceae', 'Commelinaceae', 'Compositae', 'Connaraceae', 'Convolvulaceae', 'Coriariaceae', 'Cornaceae', 'Corsiaceae', 'Corynocarpaceae', 'Costaceae', 'Crassulaceae', 'Crossosomataceae', 'Ctenolophonaceae', 'Cucurbitaceae', 'Cunoniaceae', 'Curtisiaceae', 'Cyclanthaceae', 'Cymodoceaceae', 'Cynomoriaceae', 'Cyperaceae', 'Cyrillaceae', 'Cytinaceae', 'Daphniphyllaceae', 'Dasypogonaceae', 'Datiscaceae', 'Degeneriaceae', 'Diapensiaceae', 'Dichapetalaceae', 'Didiereaceae', 'Dilleniaceae', 'Dioncophyllaceae', 'Dioscoreaceae', 'Dipentodontaceae', 'Dipterocarpaceae', 'Dirachmaceae', 'Doryanthaceae', 'Droseraceae', 'Drosophyllaceae', 'Ebenaceae', 'Ecdeiocoleaceae', 'Elaeagnaceae', 'Elaeocarpaceae', 'Elatinaceae', 'Emblingiaceae', 'Ericaceae', 'Eriocaulaceae', 'Erythroxylaceae', 'Escalloniaceae', 'Eucommiaceae', 'Euphorbiaceae', 'Euphroniaceae', 'Eupomatiaceae', 'Eupteleaceae', 'Fagaceae', 'Flacourtiaceae', 'Flagellariaceae', 'Fouquieriaceae', 'Frankeniaceae', 'Garryaceae', 'Geissolomataceae', 'Gelsemiaceae', 'Gentianaceae', 'Geraniaceae', 'Gerrardinaceae', 'Gesneriaceae', 'Gisekiaceae', 'Gomortegaceae', 'Goodeniaceae', 'Goupiaceae', 'Grossulariaceae', 'Grubbiaceae', 'Guamatelaceae', 'Gunneraceae', 'Gyrostemonaceae', 'Haemodoraceae', 'Halophytaceae', 'Haloragaceae', 'Hamamelidaceae', 'Hanguanaceae', 'Haptanthaceae', 'Heliconiaceae', 'Helwingiaceae', 'Hernandiaceae', 'Himantandraceae', 'Huaceae', 'Humiriaceae', 'Hydatellaceae', 'Hydnoraceae', 'Hydrangeaceae', 'Hydrocharitaceae', 'Hydroleaceae', 'Hydrostachyaceae', 'Hypericaceae', 'Hypoxidaceae', 'Icacinaceae', 'Iridaceae', 'Irvingiaceae', 'Iteaceae', 'Ixioliriaceae', 'Ixonanthaceae', 'Joinvilleaceae', 'Juglandaceae', 'Juncaceae', 'Juncaginaceae',
#      'Kirkiaceae', 'Koeberliniaceae', 'Krameriaceae', 'Lacistemataceae', 'Lactoridaceae', 'Lamiaceae', 'Lanariaceae', 'Lardizabalaceae', 'Lauraceae', 'Lecythidaceae', 'Leguminosae', 'Lentibulariaceae', 'Lepidobotryaceae', 'Liliaceae', 'Limeaceae', 'Limnanthaceae', 'Linaceae', 'Linderniaceae', 'Loasaceae', 'Loganiaceae', 'Lophiocarpaceae', 'Lophopyxidaceae', 'Loranthaceae', 'Lowiaceae', 'Lythraceae', 'Magnoliaceae', 'Malpighiaceae', 'Malvaceae', 'Marantaceae', 'Marcgraviaceae', 'Martyniaceae', 'Mayacaceae', 'Melanthiaceae', 'Melastomataceae', 'Meliaceae', 'Melianthaceae', 'Menispermaceae', 'Menyanthaceae', 'Metteniusaceae', 'Misodendraceae', 'Mitrastemonaceae', 'Molluginaceae', 'Monimiaceae', 'Montiaceae', 'Montiniaceae', 'Moraceae', 'Moringaceae', 'Muntingiaceae', 'Musaceae', 'Myodocarpaceae', 'Myricaceae', 'Myristicaceae', 'Myrothamnaceae', 'Myrtaceae', 'Nartheciaceae', 'Nelumbonaceae', 'Nepenthaceae', 'Neuradaceae', 'Nitrariaceae', 'Nothofagaceae', 'Nyctaginaceae', 'Nymphaeaceae', 'Ochnaceae', 'Olacaceae', 'Oleaceae', 'Onagraceae', 'Oncothecaceae', 'Opiliaceae', 'Orchidaceae', 'Orobanchaceae', 'Oxalidaceae', 'Paeoniaceae', 'Pandaceae', 'Pandanaceae', 'Papaveraceae', 'Paracryphiaceae', 'Passifloraceae', 'Paulowniaceae', 'Pedaliaceae', 'Penaeaceae', 'Pennantiaceae', 'Pentadiplandraceae', 'Pentaphragmataceae', 'Pentaphylacaceae', 'Penthoraceae', 'Peraceae', 'Peridiscaceae', 'Petenaeaceae', 'Petermanniaceae', 'Petrosaviaceae', 'Phellinaceae', 'Philesiaceae', 'Philydraceae', 'Phrymaceae', 'Phyllanthaceae', 'Phyllonomaceae', 'Physenaceae', 'Phytolaccaceae', 'Picramniaceae', 'Picrodendraceae', 'Piperaceae', 'Pittosporaceae', 'Plantaginaceae', 'Platanaceae', 'Plocospermataceae', 'Plumbaginaceae', 'Poaceae', 'Podostemaceae', 'Polemoniaceae', 'Polygalaceae', 'Polygonaceae', 'Pontederiaceae', 'Portulacaceae', 'Posidoniaceae', 'Potamogetonaceae', 'Primulaceae', 'Proteaceae', 'Putranjivaceae', 'Quillajaceae', 'Rafflesiaceae', 'Ranunculaceae', 'Rapateaceae', 'Resedaceae', 'Restionaceae', 'Rhabdodendraceae', 'Rhamnaceae', 'Rhipogonaceae', 'Rhizophoraceae', 'Roridulaceae', 'Rosaceae', 'Rousseaceae', 'Rubiaceae', 'Ruppiaceae', 'Rutaceae', 'Sabiaceae', 'Salicaceae', 'Salvadoraceae', 'Santalaceae', 'Sapindaceae', 'Sapotaceae', 'Sarcobataceae', 'Sarcolaenaceae', 'Sarraceniaceae', 'Saururaceae', 'Saxifragaceae', 'Scheuchzeriaceae', 'Schisandraceae', 'Schlegeliaceae', 'Schoepfiaceae', 'Scrophulariaceae', 'Setchellanthaceae', 'Simaroubaceae', 'Simmondsiaceae', 'Siparunaceae', 'Sladeniaceae', 'Smilacaceae', 'Solanaceae', 'Sphaerosepalaceae', 'Sphenocleaceae', 'Stachyuraceae', 'Staphyleaceae', 'Stegnospermataceae', 'Stemonaceae', 'Stemonuraceae', 'Stilbaceae', 'Strasburgeriaceae', 'Strelitziaceae', 'Stylidiaceae', 'Styracaceae', 'Surianaceae', 'Symplocaceae', 'Talinaceae', 'Tamaricaceae', 'Tapisciaceae', 'Tecophilaeaceae', 'Tetrachondraceae', 'Tetramelaceae', 'Tetrameristaceae', 'Theaceae', 'Thomandersiaceae', 'Thurniaceae', 'Thymelaeaceae', 'Ticodendraceae', 'Tofieldiaceae', 'Torricelliaceae', 'Tovariaceae', 'Trigoniaceae', 'Trimeniaceae', 'Triuridaceae', 'Trochodendraceae', 'Tropaeolaceae', 'Typhaceae', 'Ulmaceae', 'Urticaceae', 'Vahliaceae', 'Velloziaceae', 'Verbenaceae', 'Violaceae', 'Vitaceae', 'Vivianiaceae', 'Vochysiaceae', 'Winteraceae', 'Xanthorrhoeaceae', 'Xeronemataceae', 'Xyridaceae', 'Zingiberaceae', 'Zosteraceae', 'Zygophyllaceae']

# G = ['Araucariaceae', 'Cupressaceae', 'Cycadaceae', 'Ephedraceae', 'Ginkgoaceae', 'Gnetaceae',
#              'Pinaceae', 'Podocarpaceae', 'Sciadopityaceae', 'Taxaceae', 'Welwitschiaceae', 'Zamiaceae']

# P = ['Anemiaceae', 'Apleniaceae', 'Aspleniaceae', 'Athyriaceae', 'Blechnaceae', 'Cibotiaceae', 'Culcitaceae', 'Cyatheaceae', 'Cystodiaceae', 'Cystopteridaceae', 'Davalliaceae', 'Dennstaedtiaceae', 'Dicksoniaceae', 'Diplaziopsidaceae', 'Dipteridaceae', 'Dryopteridacae', 'Dryopteridaceae', 'Equisetaceae', 'Gleicheniaceae', 'Hymenophyllaceae', 'Hypodematiaceae', 'Isoëtaceae', 'Lindsaeaceae', 'Lomariopsidaceae', 'Lonchitidaceae', 'Loxsomataceae', 'Lycopodiaceae', 'Lygodiaceae', 'Marattiaceae', 'Marsileaceae', 'Matoniaceae', 'Metaxyaceae', 'Nephrolepidaceae', 'Oleandraceae', 'Onocleaceae', 'Ophioglossaceae', 'Osmundaceae', 'Plagiogyriaceae', 'Polypodiaceae', 'Psilotaceae', 'Pteridaceae', 'Rhachidosoraceae', 'Saccolomataceae', 'Salviniaceae', 'Schizaeaceae', 'Selaginellaceae', 'Tectariaceae', 'Thelypteridaceae', 'Thyrsopteridaceae', 'Woodsiaceae']
#

B = ['Acrobolbaceae', 'Adelanthaceae', 'Allisoniaceae', 'Amblystegiaceae', 'Anastrophyllaceae', 'Andreaeaceae', 'Andreaeobryaceae', 'Aneuraceae', 'Antheliaceae', 'Anthocerotaceae', 'Archidiaceae', 'Arnelliaceae', 'Aulacomniaceae', 'Aytoniaceae', 'Balantiopsaceae', 'Bartramiaceae', 'Blasiaceae', 'Brachytheciaceae', 'Brevianthaceae', 'Bruchiaceae', 'Bryaceae', 'Bryobartramiaceae', 'Bryoxiphiaceae', 'Buxbaumiaceae', 'Calomniaceae', 'Calymperaceae', 'Calypogeiaceae', 'Catagoniaceae', 'Catoscopiaceae', 'Cephaloziaceae', 'Cephaloziellaceae', 'Chaetophyllopsaceae', 'Chonecoleaceae', 'Cinclidotaceae', 'Cleveaceae', 'Climaciaceae', 'Conocephalaceae', 'Corsiniaceae', 'Cryphaeaceae', 'Cyrtopodaceae', 'Daltoniaceae', 'Dendrocerotaceae', 'Dicnemonaceae', 'Dicranaceae', 'Diphysciaceae', 'Disceliaceae', 'Ditrichaceae', 'Echinodiaceae', 'Encalyptaceae', 'Entodontaceae', 'Ephemeraceae', 'Erpodiaceae', 'Eustichiaceae', 'Exormothecaceae', 'Fabroniaceae', 'Fissidentaceae', 'Fontinalaceae', 'Fossombroniaceae', 'Funariaceae', 'Geocalycaceae', 'Gigaspermaceae', 'Goebeliellaceae', 'Grimmiaceae', 'Gymnomitriaceae', 'Gyrothyraceae', 'Haplomitriaceae', 'Hedwigiaceae', 'Helicophyllaceae', 'Herbertaceae', 'Hookeriaceae', 'Hylocomiaceae', 'Hymenophytaceae', 'Hypnaceae', 'Hypnodendraceae', 'Hypopterygiaceae', 'Jackiellaceae', 'Jubulaceae', 'Jubulopsaceae', 'Jungermanniaceae', 'Lejeuneaceae', 'Lembophyllaceae', 'Lepicoleaceae', 'Lepidolaenaceae', 'Lepidoziaceae', 'Leptodontaceae', 'Lepyrodontaceae', 'Leskeaceae', 'Leucodontaceae', 'Leucomiaceae', 'Lophocoleaceae', 'Lophoziaceae', 'Lunulariaceae', 'Makinoaceae', 'Marchantiaceae', 'Mastigophoraceae', 'Meesiaceae', 'Mesoptychiaceae', 'Meteoriaceae', 'Metzgeriaceae', 'Microtheciellaceae', 'Mitteniaceae', 'Mizutaniaceae', 'Mniaceae', 'Monocarpaceae', 'Monocleaceae', 'Monosoleniaceae', 'Myriniaceae', 'Myuriaceae', 'Neckeraceae', 'Neotrichocoleaceae', 'Notothyladaceae', 'Octoblepharaceae', 'Oedipodiaceae', 'Orthorrhynchiaceae', 'Orthotrichaceae', 'Oxymitraceae', 'Pallaviciniaceae', 'Pelliaceae', 'Phyllodrepaniaceae', 'Phyllogoniaceae', 'Pilotrichaceae', 'Plagiochilaceae', 'Plagiotheciaceae', 'Pleurophascaceae', 'Pleuroziaceae', 'Pleuroziopsaceae', 'Polytrichaceae', 'Porellaceae', 'Pottiaceae', 'Prionodontaceae', 'Pseudoditrichaceae', 'Pseudolepicoleaceae', 'Pterigynandraceae', 'Pterobryaceae', 'Ptilidiaceae', 'Ptychomitriaceae', 'Ptychomniaceae', 'Racopilaceae', 'Radulaceae', 'Regmatodontaceae', 'Rhabdoweisiaceae', 'Rhachitheciaceae', 'Rhacocarpaceae', 'Rhizogoniaceae', 'Ricciaceae', 'Riellaceae', 'Rigodiaceae', 'Rutenbergiaceae', 'Scapaniaceae', 'Schistochilaceae', 'Schistostegaceae', 'Scorpidiaceae', 'Seligeriaceae', 'Sematophyllaceae', 'Serpotortellaceae', 'Sorapillaceae', 'Sphaerocarpaceae', 'Sphagnaceae', 'Spiridentaceae', 'Splachnaceae', 'Splachnobryaceae', 'Stereophyllaceae', 'Takakiaceae', 'Targioniaceae', 'Tetraphidaceae', 'Thamnobryaceae', 'Theliaceae', 'Thuidiaceae', 'Timmiaceae', 'Trachypodaceae', 'Treubiaceae', 'Trichocoleaceae', 'Trichotemnomataceae', 'Vandiemeniaceae', 'Vetaformaceae', 'Viridivelleraceae', 'Wardiaceae', 'Wiesnerellaceae']

TIPO = 'B'
ARRAYZAO = B


class GeneraSpider(scrapy.Spider):
    name = 'genera'
    increment = 1
    start_urls = [
        'http://www.theplantlist.org/1.1/browse/'+TIPO+'/'+ARRAYZAO[0]+'/']

    def parse(self, response):
        families = response.css('ul#nametree li i')

        for family in families:

            yield {'name': family.css('::text').get(), 'family_id': self.increment + 474}

        self.increment += 1

        yield scrapy.Request('http://www.theplantlist.org/1.1/browse/'+TIPO+'/'+ARRAYZAO[self.increment-1])
