import streamlit as st
import streamlit.components.v1 as components 
# python -m streamlit run wikipedia.py
st.sidebar.title("Wikipedia Search Engine 🔍: Top 8 Most Beautiful Places on Earth")
st.sidebar.write("Enter Your Place to Know About It")
place = st.sidebar.selectbox("Select place",["Greece🌳🏞️","New Zealand⛰️","Italy🥐🍵","Switzerland🏝️","Indonesia⛵","Thailand🌉","Norway🏙️","India🏦"])
topics = st.sidebar.radio("Select topics to know about", ["About","History", "Images", "Video", "Audio"])
if st.sidebar.button("Submit"):
    if topics == "About":
        if place == "Greece🌳🏞️":
            st.title("Welcome to Greece🌳🏞️")
            st.text("""==>        Greece is a country in southeastern Europe with thousands of islands throughout the Aegean and Ionian seas.Its capital, Athens, is home to the 5th-century BC Parthenon temple on the Acropolis hill. The country’s long,storied About includes the Golden Age of Athens, Alexander the Great’s empire and Byzantine rule.Greece is considered the cradle of Western civilisation and the birthplace of democracy, Western philosophy, Western literature, historiography, political science, major scientific and mathematical principles, theatre, and the Olympic Games. The Ancient Greeks were organised into independent city-states, or poleis (singular polis), that spanned the Mediterranean and Black seas. Philip II of Macedon united most of present-day Greece in the fourth century BC, with his son Alexander the Great conquering much of the known ancient world from the Near East to northwestern India. The subsequent Hellenistic period saw the height of Greek culture and influence in antiquity. Greece was annexed by Rome in the second century BC and became an integral part of the Roman Empire and its continuation, the Byzantine Empire, where Greek culture and language were dominant. The Greek Orthodox Church helped shape modern Greek identity and transmitted Greek traditions to the wider Orthodox world.   

                      After the Fourth Crusade in 1204, Greece and the rest of the Byzantine empire were fragmented into several Latin and Byzantine successor polities, with most Greek lands finally coming under Ottoman control by the mid-15th century. Following a protracted war of independence in 1821, Greece emerged as a modern nation state in 1830. The Kingdom of Greece pursued territorial expansion during the Balkan Wars (1912–1913) and World War I (1914–1918), until its defeat in the Greco-Turkish War in 1922. A short-lived republic was established in 1924 but faced civil strife and the challenge of resettling refugees from Turkey, culminating in a royalist dictatorship in 1936. Greece endured military occupation during World War II, the subsequent Greek Civil War, and prolonged political instability, leading to a military dictatorship in 1967. The country began transitioning to democracy in 1974, leading to the current parliamentary republic.

                      Owing to record economic growth from 1950 to 1973, Greece is a developed country with an advanced high-income economy; its high standard of living has been damaged by a decade-long debt crisis that emerged in the wake of the 2008 financial crisis. Shipping and tourism are major economic sectors, with Greece being the ninth most-visited country in the world in 2024. Greece is part of multiple international organisations and forums, being the tenth member to join what is today the European Union in 1981. The country's rich historical legacy is reflected partly by its 20 UNESCO World Heritage Sites.""")
        elif place == "New Zealand⛰️":
            st.title("Welcome to New Zealand⛰️")
            st.text("""New Zealand is an island country in the southwestern Pacific Ocean. It consists of two main landmasses—the North Islandand the South Island—and around 600 smaller islands. The capital city is Wellington, while the mostpopulous city is Auckland.""")
        elif place == "Italy🥐🍵":
            st.title("Welcome to Italy🥐🍵")
            st.text("""Italy is a European country with a long Mediterranean coastline, has left a powerful mark on Western culture and cuisine.Its capital, Rome, is home to the Vatican as well as landmark art and ancient ruins. Other major cities include Florence, with Renaissance masterpieces such as Michelangelo’s David and Brunelleschi’s Duomo; Venice, the city of canals; and Milan, Italy’s fashion capital.""")
        elif place == "Switzerland🏝️":
            st.title("Welcome to Switzerland🏝️")
            st.text("""Switzerland is a mountainous Central European country, home to numerous lakes, villages and the high peaks of the Alps.Its cities contain medieval quarters, with landmarks like capital Bern’s Zytglogge clock tower and Lucerne’s wooden chapel bridge. The country is also known for its ski resorts and hiking trails.""")
        elif place == "Indonesia⛵":
            st.title("Welcome to Indonesia⛵")
            st.text("""Indonesia is a Southeast Asian nation made up of thousands of volcanic islands.It’s home to hundreds of  ethnic groups speaking many different languages.The country has a diverse culture and is known for its beaches, volcanoes, Komodo dragonsand jungles sheltering elephants, orangutans and tigers.""")
        elif place == "Thailand🌉":
            st.title("Welcome to Thailand🌉")
            st.text("""Thailand is a Southeast Asian country known for its tropical beaches, vibrant culture, and rich About.Its capital, Bangkok, is a bustling metropolis with temples, markets, and street food. The country is also hometo ancient ruins like Ayutthaya and Sukhothai, as well as national parks and wildlife reserves.""")
        elif place == "Norway🏙️":
            st.title("Welcome to Norway🏙️")
            st.text("""Norway is a Scandinavian country with a long coastline and numerous fjords. Its capital, Oslo, is a modern city with museums, parks, and a vibrant cultural scene. The country is also known for its stunning natural landscapes, including mountains, forests, and the Northern Lights.""")
        elif place == "India🏦":
            st.title("Welcome to India🏦")
            st.text("""India is a South Asian country known for its diverse culture, About, and economy. Its capital, New Delhi,is a bustling city with historical landmarks and modern infrastructure. The country is also home to numerous temples,palaces, and natural wonders.""")
    if topics == "History":    
            if place == "Greece🌳🏞️":  
                st.title(f"History of {place}")
                st.text("""==>          Main article: History of GreecePrehistory and Aegean civilisationsMain articles: Neolithic Greece, Pelasgians, Cycladic culture, Minoan civilisation, and Mycenaean Greece

                        The entrance of the "Treasury of Atreus" (13th century BC) in Mycenae
                        The Apidima Cave in Mani, in southern Greece, has been suggested to contain the oldest remains of early modern humans outside of Africa, dated to 200,000 years ago.[13] However others suggest the remains represent archaic humans.[14] All three stages of the Stone Age are represented in Greece, for example in the Franchthi Cave.[15] Neolithic settlements in Greece, dating from the 7th millennium BC,[16] are the oldest in Europe, as Greece lies on the route by which farming spread from the Near East to Europe.[17]

                        Greece is home to the first advanced civilisations in Europe and is often considered the birthplace of Western civilisation.[18][19] The earliest of them was the Cycladic culture which flourished on the islands of the Aegean Sea, starting around 3200 BC, and produced an abundance of folded-arm and other marble figurines.[20] From c. 3100 BC to 1100 BC, Crete, a major cultural and economic centre, was home to the Minoan civilisation known for its colourful art, religious figurines, and monumental palaces.[21][22] The Minoans wrote their undeciphered language using scripts known as Linear A and Cretan hieroglyphs.[23][24] On the mainland, the Mycenaean civilisation developed around 1750 BC and lasted until c. 1100 BC.[25] The Mycenaeans possessed an advanced military and built large fortifications.[26] They worshipped many gods[27] and used Linear B to write the earliest attested form of Greek known as Mycenaean Greek.[28][29]

                        Ancient Greece
                        Main article: Ancient Greece
                        See also: Greek Dark Ages, Archaic Greece, Classical Greece, and Hellenistic Greece

                        Greek territories and colonies during the Archaic period (750–550 BC)
                        The collapse of the Mycenaean civilisation ushered in the Greek Dark Ages, from which written records are absent. The end of the Dark Ages is traditionally dated to 776 BC, the year of the first Olympic Games.[30] The Iliad and the Odyssey, the foundational texts of Western literature, are believed to have been composed by Homer in the 7th or 8th centuries BC.[31][32] Poetry shaped beliefs to the Olympian gods, but ancient Greek religion had no priestly class or systematic dogmas and encompassed other currents, such as popular cults, like that of Dionysus, mysteries and magic.[33] At this time, many kingdoms and city-states emerged across the Greek peninsula, some of which went on to establish a number of colonies in Asia Minor, the shores of the Black Sea, and southern Italy (also known as Magna Grecia). The Greek city-states reached great prosperity that resulted in an unprecedented cultural boom, that of classical Greece, expressed in architecture, drama, science, mathematics and philosophy. In 508 BC, Cleisthenes instituted the world's first democratic system of""")
            elif place == "New Zealand⛰️":
                st.title(f"History of {place}")
                st.text("""==>          The first settlers of New Zealand were the Māori, who arrived from Polynesia in several waves of canoe voyages between roughly 1320 and 1350. They developed a distinct culture with rich traditions and a strong connection to the land. European exploration began in the 17th century, with Dutch explorer Abel Tasman being the first known European to sight New Zealand in 1642. British explorer James Cook later mapped the coastline in 1769, leading to increased European interest and eventual colonization.

                        In 1840, the Treaty of Waitangi was signed between the British Crown and various Māori chiefs, establishing British sovereignty while promising to protect Māori rights and land. However, tensions over land ownership and sovereignty led to conflicts known as the New Zealand Wars in the mid-19th century. Despite these challenges, New Zealand gradually developed its own identity and institutions, becoming a self-governing colony in 1856 and gaining full independence from Britain in 1947.

                        Throughout the 20th century, New Zealand played significant roles in both World Wars and underwent social and economic changes that shaped its modern society. Today, it is known for its diverse culture, stunning landscapes, and commitment to environmental conservation.""")    
            elif place == "Italy🥐🍵":
                st.title(f"History of {place}")
                st.text("""==>          The history of Italy is a long and complex one, marked by the rise and fall of various civilizations, empires, and city-states. The earliest known inhabitants of the Italian peninsula were the Etruscans, who established a powerful civilization in central Italy around the 8th century BC. They were eventually conquered by the Romans, who went on to create one of the most influential empires in history.

                        The Roman Republic was founded in 509 BC and expanded its territory through conquest and diplomacy. It transitioned into the Roman Empire in 27 BC under Augustus Caesar, reaching its peak in the 2nd century AD. The empire's decline began in the 3rd century AD, leading to its eventual fall in 476 AD. After the fall of Rome, Italy was fragmented into various kingdoms and city-states, such as the Kingdom of Sicily, the Republic of Venice, and the Duchy of Milan.

                        The Renaissance, which began in Italy in the 14th century, was a period of great cultural and artistic flourishing that had a profound impact on Europe and the world. Italy was also a major player in the Age of Exploration, with figures like Christopher Columbus and Amerigo Vespucci making significant contributions to global navigation.

                        In the 19th century, Italy underwent a process of unification, culminating in the establishment of the Kingdom of Italy in 1861. The country faced challenges during World War I and World War II but emerged as a republic in 1946. Today, Italy is known for its rich cultural heritage, art, fashion, and cuisine.""")
            elif place == "Switzerland🏝️":
                st.title(f"History of {place}")
                st.text("""==>          Switzerland's history is characterized by its mountainous terrain and its role as a neutral country in international affairs. The region was settled by Celtic tribes in the 6th century BC, followed by Roman conquest in the 1st century BC. The Swiss Confederation was founded in 1291, initially as a defensive alliance of three cantons.

                        Over the centuries, the confederation expanded to include more cantons and became a federal state. Switzerland played a significant role in European history, particularly during the Napoleonic Wars and both World Wars. The country is known for its neutrality and has served as a haven for refugees and political dissidents.

                        Today, Switzerland is recognized for its financial sector, precision manufacturing, and high standard of living. It is also renowned for its natural beauty, including the Alps and numerous lakes.""")
            elif place == "Indonesia⛵":
                st.title(f"History of {place}")
                st.text("""==>          Indonesia's history is marked by its strategic location and rich cultural diversity. The archipelago has been inhabited for thousands of years, with evidence of early human activity dating back to 1.5 million years ago. The region was influenced by various cultures, including Indian, Chinese, and Arab traders, which contributed to the spread of Hinduism and Buddhism.

                        In the 13th century, the Majapahit Empire emerged as a powerful maritime kingdom, controlling much of Southeast Asia. The arrival of European colonizers in the 16th century, particularly the Dutch, led to centuries of colonial rule. Indonesia declared its independence in 1945, following a brief period of Japanese occupation during World War II.

                        Since gaining independence, Indonesia has faced challenges such as political instability and economic development but has emerged as a significant player in regional and global affairs. Today, it is known for its vibrant culture, diverse population, and natural beauty.""")
            elif place == "Thailand🌉":
                st.title(f"History of {place}")
                st.text("""==>          Thailand's history is a rich tapestry of kingdoms, cultures, and influences. The region was home to various ancient civilizations, including the Funan and Dvaravati kingdoms. In the 13th century, the Sukhothai Kingdom emerged as a powerful force in the area, followed by the Ayutthaya Kingdom.

                        The Thai kingdom was known for its unique blend of Buddhist and Hindu traditions, which influenced its art, architecture, and culture. The country faced challenges from European colonial powers and internal conflicts but managed to maintain its independence. Today, Thailand is recognized for its vibrant culture, beautiful landscapes, and warm hospitality.""")
            elif place == "Norway🏙️":
                st.title(f"History of {place}")
                st.text("""==>          Norway's history is deeply rooted in its Viking heritage and its struggle for independence. The region was settled by Germanic tribes in the 1st century BC, followed by the Viking Age in the 9th and 10th centuries. Norway was part of the Kalmar Union with Denmark and Sweden until 1536, when it gained its independence.

                        The country faced challenges from foreign powers, including Danish rule and later Swedish control, but managed to maintain its cultural identity. In the 19th century, Norway experienced a renaissance of its language and literature, leading to its independence from Sweden in 1905. Today, Norway is known for its stunning fjords, rich cultural heritage, and high standard of living.""")
            elif place == "India🏦":
                st.title(f"History of {place}")
                st.text("""==>          India's history is one of the world's oldest and most complex. The subcontinent has been inhabited for thousands of years, with evidence of early human activity dating back to the Paleolithic period. The region was influenced by various cultures, including the Indus Valley Civilization, which flourished around 2500 BC.

                        Over the centuries, India was ruled by numerous dynasties and empires, including the Maurya and Gupta Empires. The country faced invasions and occupations by various foreign powers, including the Mughal Empire and European colonial powers. India declared its independence in 1947, following a struggle for freedom led by figures such as Mahatma Gandhi.

                        Since gaining independence, India has experienced significant economic growth and development. Today, it is known for its diverse culture, rich history, and emerging role in the global economy.""")
    if topics == "Images":
        if place == "Greece🌳🏞️":
            st.title(f"Gallery of {place}")
            images =[["https://fs.tonkosti.ru/dk/lz/dklz1yiqed4w8c0k0ocs88kog.jpg","Greek Islands"],
                     ["https://fs.tonkosti.ru/18/bg/18bgnbqw6qassk40cg8ggc000.jpg","Greek Islands"],
                     ["https://i.pinimg.com/originals/a0/68/1a/a0681ae03013bc32851b239e9cece1e5.jpg","Greece Mobile Home"],
                     ["https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio-d2d-W3MGcrOcuG7eAop061vzwqE0OSRc9aHVo78b8foZ2vNnAfrgRUuX5_T_52wwScle-2HwSRsUW7Q9Ihzi6RDffnTnVcGPUXWNDgdkmo3UNcFxvdDQ14dmvGmnDwepOeNm4Vp-wo/s1600/DSC_1712.JPG","Parthenon in Athens"],
                     ["https://img.pac.ru/landmarks/385375/big/48BFD1B57F00010123A0A5A838EC8D8C.jpg","Acropolis of Athens"],
                     ["https://cdnp.flypgs.com/files/Sehirler-long-tail/Atina/atina-gece-hayati.jpg","Acropolis of Athens at Night"],
                     ["https://i0.wp.com/gips.ltur.com/gips/scalr/original/pics.tui.com/pics/pics1600x1200/tui/0/0e280ed0-8ebb-4ca8-b4e7-79d194f798fb.jpg","Cornelia Diamond Golf Resort"],
                     ["https://i.pinimg.com/originals/2a/3a/3f/2a3a3f701e328e772d184476bc4afd62.jpg","Soneva Jani"],
                     ["https://www.tui-reisecenter.de/wp-content/uploads/2024/06/TUI-BLUE-Tropical_Aussenansicht.jpg","TUI BLUE Tropical"],
                     ["https://assets.cntraveller.in/photos/60ba0672b1ba4c108d187543/master/w_1600%2Cc_limit/Fourseasons.jpg"," Four Seasons Resort Seychelles"]
                ]
        if place == "New Zealand⛰️":
            st.title(f"Gallery of {place}")
            images =[["https://i.insider.com/5a79d4f27101ad797500c09c","Mount Victoria in Wellington"],
                     ["https://www.travelalerts.ca/wp-content/uploads/2021/03/shutterstock_349221143hero.jpg","Mount Cook National Park"],
                     ["https://www.travelalerts.ca/wp-content/uploads/2017/02/New-Zealand.jpg","lush, green landscape of New Zealand"],
                     ["https://images.squarespace-cdn.com/content/v1/56a592da3b0be33df88bbee1/1456126924111-HWFOXVJJNG77NUAK499D/iStock_000041885702_Medium.jpg","Tauranga city"],
                     ["https://co10.nevseoboi.com.ua/posts/2011-05/1305557656_3280552-queensland-lake-wakatipu-new.jpg","Lake Wakatipu, New Zealand"],
                     ["https://avatars.mds.yandex.net/i?id=99e0a20da199f123d50230a63f11a53a_l-4401150-images-thumbs&ref=rim&n=13&w=3000&h=1875","Kelingking Beach"],
                     ["https://live.staticflickr.com/8038/8068694299_39846bba5b_b.jpg","Auckland at Night"],
                     ["https://cdn.lazytrips.com/photos/a8/98/a8984795a0e0523c9ead8ed4ef651897-mb.webp","turquoise braided river"],
                     ["https://dreamfood.ua/uploads/forum/images/1331689430.jpg","Hobbiton Movie Set"],
                     ["https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwghsm8j8JGBfvNi9lU0_CDOMWbMxBJzfGFSJPy8HiVVZvuTgAVtMTGnB0lX5jnHwBwnYgmdyllOckQWTqB8978PZ03IDXHs6Z-5jFggp3-SAfRy8fLVtHyxNvhyIjQZrezbnmme2lHqA/s1600/188256.jpg","Lake Tekapo"]
                ]
        if place == "Italy🥐🍵":
            st.title(f"Gallery of {place}")
            images =[["https://as2.ftcdn.net/v2/jpg/07/23/43/27/1000_F_723432701_ZC8gSt2toizS6M0CGtom62N8bKHkkOES.jpg","Milan Cathedral at Night"],
                     ["https://cdn.steemitimages.com/DQmcYvdeCvfTHfwQA8xfCUC6ZVCVA8RY7A7Wga6ZPa4Wg89/Colosseo-Colosseo.jpg","Colosseum in Rome"],
                     ["https://www.travelandleisure.com/thmb/fhNqzlzOy5NO6WC-xwsHD6X_ciI=/1600x1200/smart/filters:no_upscale()/aerial-view-cinque-terre-hero_CINQUETERRE0622-f99043be30454ac7ad42165f735259e3.jpg","Cinque Terre"],
                     ["https://www.travelalerts.ca/wp-content/uploads/2018/06/main-4.jpg","overlooking Florence"],
                     ["https://www.islands.com/img/gallery/the-destination-dear-to-rick-steves-where-you-can-view-every-cinque-terre-town-at-the-same-time/l-intro-1750691697.jpg","Vernazza"],
                     ["https://i.pinimg.com/736x/ba/13/34/ba13343f0f1d8c73e768caaf976fd604.jpg","Manarola"],
                     ["https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1DT9yJ.img?w=1920&h=1080&m=4&q=98","Grand Canal, Venice"],
                     ["https://ak-d.tripcdn.com/images/100h0q000000gmyp28306.jpg"," Florence Cathedral"],
                     ["https://i.insider.com/67bcd1fdc832c3638fa50ee3?width=1200&format=jpeg","Bologna"],
                     ["https://ik.imagekit.io/tvlk/blog/2024/09/shutterstock_2405201415.jpg?tr=q-70,c-at_max,w-500,h-300,dpr-2","Peter's Basilica"]
                ]
        if place == "Switzerland🏝️":
            st.title(f"Gallery of {place}")
            images =[["https://i.ytimg.com/vi/ka-7ByunLAI/maxresdefault.jpg","Swiss Alps"],
                     ["https://i.ytimg.com/vi/WsDroKTBFCs/maxresdefault.jpg","Grindelwald"],
                     ["https://i.ytimg.com/vi/uyc0RPZ8tyQ/maxresdefault.jpg","Lauterbrunnen"],
                     ["https://i.ytimg.com/vi/FB1SXEI8ZHc/maxresdefault.jpg","Lauterbrunnen Valley"],
                     ["https://www.nationsonline.org/gallery/Switzerland/Old-City-of-Bern.jpg"," Bern, the capital of Switzerland"],
                     ["https://i.ytimg.com/vi/oALw4TxqtRQ/maxresdefault.jpg","Bern, the capital of Switzerland"],
                     ["https://miro.medium.com/v2/resize:fit:1200/1*8TVC50KRem5oCjlrhrGqgg.jpeg","Meiringen in the Bernese Oberland"],
                     ["https://i.ytimg.com/vi/TalVRG79JzE/maxresdefault.jpg","Aare River flowing through Bern"],
                     ["https://i.ytimg.com/vi/-Xo7a1NY3is/maxresdefault.jpg","Bernese Alps"],
                     ["https://i.ytimg.com/vi/ry7hnkKN2f4/maxresdefault.jpg","Lauterbrunnen and Interlaken"]
                ]
        if place == "Indonesia⛵":
            st.title(f"Gallery of {place}")
            images =[["https://level.travel/media/wp-content/uploads/2019/12/shutterstock_1044182647-min.jpg"," Handara Gate"],
                     ["https://mayel.ru/wp-content/uploads/2015/03/bali2.jpg","Mount Agung"],
                     ["https://corpblog.ostrovok.ru/wp-content/uploads/2025/05/6%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F-9.jpg","Ulun Danu Beratan Temple on Lake Beratan"],
                     ["https://s.yimg.com/ny/api/res/1.2/4u1.bTMr3plqEP5_LWHjJA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD03NTA-/https://s.yimg.com/os/creatr-uploaded-images/2024-02/136a7700-cba9-11ee-9bf7-ffdabc236444","the Pura Ulun Danu Beratan temple "],
                     ["https://www.agoda.com/wp-content/uploads/2020/01/Best-time-to-visit-Bali-Tegalalang-rice-terrace.jpg","Rice Terraces in Bali"],
                     ["https://avatars.mds.yandex.net/i?id=9cace8d961495a438c9c0e775f2a33a7ecbc7ae4-5249922-images-thumbs&n=13","padar island"],
                     ["https://igotravel.vn/wwwroot/resources/upload/tumpak%20ti%E1%BB%81n%20s%E1%BB%AD.jpg"," Tumpak Sewu Waterfall"],
                     ["https://i.ytimg.com/vi/KczgN6blLKc/maxresdefault.jpg","limestone islands in Raja Ampat"],
                     ["https://group.atradius.com/.imaging/focalpoint/herocarousel/1440x800/dam/jcr:ea71705b-0d9a-4300-99bb-0dde8eeb496d/Jakarta+skyline.jpg","the Sudirman Central Business District"],
                     ["https://www.amigo-tours.ru/workdir/photos/__1200_01.jpg","Raja Ampat Islands"]
                ]
        if place == "Thailand🌉":
            st.title(f"Gallery of {place}")
            images =[["https://www.agoda.com/wp-content/uploads/2024/04/bangkok.jpg","the Grand Palace complex in Bangkok"],
                     ["https://res.klook.com/images/w_1200,h_630,c_fill,q_65/w_80,x_15,y_15,g_south_west,l_Klook_water_br_trans_yhcmh3/activities/gtjl6tmxmdwpp1ioy73k/%D0%9E%D0%B1%D0%B7%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%20%D1%8D%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D1%8F%20%D0%BF%D0%BE%20%D0%9F%D1%85%D1%83%D0%BA%D0%B5%D1%82%D1%83%3A%20%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9%20%D0%91%D1%83%D0%B4%D0%B4%D0%B0%2C%20%D0%BA%D1%83%D0%BF%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2%20%D0%B8%20%D0%BA%D0%B0%D1%82%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D0%BA%D0%B2%D0%B0%D0%B4%D1%80%D0%BE%D1%86%D0%B8%D0%BA%D0%BB%D0%B0%D1%85.jpg","the Phuket Big Buddha"],
                     ["https://s3.sravni.ru/cms/Default/KnowledgeBaseArticle/1/%D0%91%D0%B0%D0%BD%D0%B3%D0%BA%D0%BE%D0%BA.jpg"," the skyline of Bangkok"],
                     ["https://www.hilton.com/im/en/BKKHITW/3095307/wat-arun-website.jpg?impolicy=crop&cw=4500&ch=3000&gravity=NorthWest&xposition=0&yposition=0&rw=2560&rh=1708","Wat Arun"],
                     ["https://img.pac.ru/countries/213157/big/9C4439B97F00010138622FB7C6083201.jpg","Ko Ta Pu"],
                     ["https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Wat_Chaiwatthanaram_by_drone.jpg/1280px-Wat_Chaiwatthanaram_by_drone.jpg","Ayutthaya Historical Park"],
                     ["https://kidpassage.com/images/publications/tailand-noyabre-otdyh-pogoda/tailand-noyabre-otdyh-pogoda-photo-1_1042986000.jpg"," Doi Inthanon National Park"],
                     ["https://cdn.kuoni.co.uk/media/exports/KuoniUK/ImageGalleryLightboxLarge/390669_ImageGalleryLightboxLarge.jpg"," Wat Arun Ratchawararam Ratchawaramahawihan"],
                     ["https://i.pinimg.com/736x/e1/59/2a/e1592afeab99d392cffb0fea21663975.jpg","Wat Phra Si Sanphet"],
                     ["https://res.klook.com/image/upload/fl_lossy.progressive,q_85/c_fill,w_1000/v1648099462/blog/orcjxjf2lqmil8rr5pev.jpg","Narai Song Suban Royal Barge"]
                ]
        if place == "Norway🏙️" :
            st.title(f"Gallery of {place}")
            images =[["https://i.ytimg.com/vi/j59ShVTs8AM/maxresdefault.jpg","fjord in Norway"],
                     ["https://i.ytimg.com/vi/cR5DDiE7qQc/maxresdefault.jpg","norwegian fjord"],
                     ["https://www.campervannorway.com/assets/img/blog/394/fjords-norway-Romsdalsfjord.jpg","Åndalsnes, Romsdalsfjord"],
                     ["https://i.ytimg.com/vi/ZM2eK-ado4g/maxresdefault.jpg","Lofoten Islands in Norway"],
                     ["https://photos.gurushots.com/unsafe/0x0/c08804bdcf3ebcff4465cf2213daa750/3_e97fa120d0ed866ccc6654bbdf23ec15.jpg","rita holmberg"],
                     ["https://i.pinimg.com/originals/20/19/97/201997d6000e8fed40878bf2c98e2e14.png?nii=t","northern lights in Norway"],
                     ["https://arctictraveltips.com/wp-content/uploads/2023/11/Hamnoy.jpg"," Lofoten Islands"],
                     ["https://i.pinimg.com/736x/03/61/45/036145a434e6b00e078026daa3f8482a.jpg","belojusova cave"],
                     ["https://i.ytimg.com/vi/vLJ0zji0zxo/maxresdefault.jpg","senja island"],
                     ["https://i.pinimg.com/736x/06/ce/b5/06ceb51b515016d6a933dd7d2628136d.jpg","Odda"]
                ]
        if place == "India🏦":
            st.title(f"Gallery of {place}")
            images =[["https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Taj-Mahal.jpg/1280px-Taj-Mahal.jpg","Taj Mahal"],
                     ["https://res.klook.com/images/w_1200,h_630,c_fill,q_65/w_80,x_15,y_15,g_south_west,l_Klook_water_br_trans_yhcmh3/activities/iktpseyxejttdvyyesis/%D0%9F%D0%B5%D1%88%D0%B0%D1%8F%20%D0%BF%D1%80%D0%BE%D0%B3%D1%83%D0%BB%D0%BA%D0%B0%20%D0%B8%20%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE%20%D1%81%20%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%BC%20%D0%9C%D1%83%D0%BC%D0%B1%D0%B0%D0%B8%3A%20%D0%AD%D0%BA%D1%81%D0%BA%D1%83%D1%80%D1%81%D0%B8%D1%8F%20%D1%81%20%D0%BC%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D0%BC%20%D0%B3%D0%B8%D0%B4%D0%BE%D0%BC.jpg","Gateway of India"],
                     ["https://res.klook.com/images/w_1200,h_630,c_fill,q_65/w_80,x_15,y_15,g_south_west,l_Klook_water_br_trans_yhcmh3/activities/aa5grpbc1hexyxjherul/Red%20Fort%20Ticket%20with%20Optional%20Guide.jpg","Red Fort"],
                     ["https://i.pinimg.com/originals/a3/cd/b7/a3cdb7482c62698b854eec1d3d8b6897.jpg","Meenakshi Amman Temple"],
                     ["https://dynamic-media-cdn.tripadvisor.com/media/photo-o/08/46/bc/ed/hyderabad.jpg?w=1200","Hyderabad"],
                     ["https://upload.wikimedia.org/wikipedia/commons/d/d5/Rajmachi.jpg","rajmachi fort"],
                     ["https://miro.medium.com/v2/resize:fit:1200/1*56MXapI24VV8aw2jF8YfYA.jpeg","vijaya vittala temple"],
                     ["https://www.thrillophilia.com/blog/wp-content/uploads/2025/08/munnar-1024x683.jpg","munnar"],
                     ["https://akm-img-a-in.tosshub.com/indiatoday/styles/medium_crop_simple/public/2023-04/konark_gettyimages-146586312.jpg?VersionId=aRgguNsNwF_d2sQnO2sArgv6VKTbwT85","sun temple "],
                     ["https://i.pinimg.com/originals/97/6b/35/976b3561cbb302da6b48a3187d8db444.jpg","kedarnath temple"]
                ]
        cols= st.columns(2)
        for i in range(len(images)):
          with cols[i%2]:
            st.image(images[i][0],caption=images[i][1])

    if topics == "Video":
        if place == "Greece🌳🏞️":
            st.title(f"Videos of {place}")
            videos =[["https://youtu.be/Y3yJgslrsQA?si=xWYDwoKVZeCEH__o"],
                     ["https://youtu.be/pnJeM_B7O8c?si=SfsaVAmptRgLf1-1"],
                     ["https://youtu.be/gYz7qpjr4MM?si=zgZTYKZTyZKzsvPz"]
                    ]
        if place == "New Zealand⛰️":
            st.title(f"Videos of {place}")
            videos =[["https://youtu.be/q4KxOpcl-As?si=kKY58T_oK7j94MN2"],
                     ["https://youtu.be/GOrwaPG_4E8?si=H9g0YhFXOY_XYKGa"],
                     ["https://youtu.be/40Vh7oYEke4?si=yamF9RHb3fUgRUqV"]
                    ]
        if place == "Italy🥐🍵":
            st.title(f"Videos of {place}")
            videos =[["https://youtu.be/H4tyzzP33Cw?si=GWhhFSbXomxgih7P"],
                     ["https://youtu.be/9J7_NqgJSq8?si=0yu3MQ_tGlf6qswJ"],
                     ["https://youtu.be/Tovxu_sm9BA?si=138n1peEsL5cF4Qr"]
                    ]
        if place == "Switzerland🏝️":
            st.title(f"Videos of {place}")
            videos =[["https://youtu.be/1Yqt8uyprQ8?si=IIMijrIMOCkWLbAB"],
                     ["https://youtu.be/1wJlN21FAu8?si=U_TN9EBsxuxsg_yK"],
                     ["https://youtu.be/IaxvUT9kdH8?si=U_H_YfoJOfqsbM9l"]
                    ]
        if place == "Indonesia⛵":
            st.title(f"Videos of {place}")
            videos =[["https://youtu.be/3ARSuqrfZpM?si=vonbef7DMSob_O2a"],
                     ["https://youtu.be/WK3clL6eG4s?si=QXeGHNz93feVNzxi"],
                     ["https://youtu.be/V4vXAkgmw9M?si=TDNMWCGBWj3GjC7S"]
                    ]
        if place == "Thailand🌉" :  
            st.title(f"Videos of {place}")
            videos =[["https://youtu.be/ts7c6v2mKBM?si=nglurZxxH5dyf9dw"],
                     ["https://youtu.be/pwNNNm2UlJw?si=H3U29So_GmAc_qIu"],
                     ["https://youtu.be/V2lAgksvMTE?si=ajXqOaFGC0e-dp4Z"]
                    ]
        if place == "Norway🏙️" :
            st.title(f"Videos of {place}")
            videos =[["https://youtu.be/-ddk-809FHo?si=fI2ZOP0agY_j9TCI"],
                     ["https://youtu.be/KLuTLF3x9sA?si=G-5CSY7yaUqLUg9o"],
                     ["https://youtu.be/gxnS_pf2jHk?si=0NqPkahZwBgglF04"]
                    ]
        if place == "India🏦" :
            st.title(f"Videos of {place}")
            videos =[["https://youtu.be/x78fARg3yow?si=xpV72NU1Y8T9FyuL"],
                     ["https://youtu.be/KwIp2x0Kg4U?si=OpJU5-o3RY8DEMzF"],
                     ["https://youtu.be/l-5rGi8_A_4?si=LxR5gnXp8NGanhWL"]
                    ]
        for video in videos:
            st.video(video[0])
    if topics == "Audio":
        if place == "Greece🌳🏞️":
            st.title(f"Songs of {place}")
            songs = ["https://open.spotify.com/embed/track/5XNuEDeZMnPW9mBMPig8rY?si=312c275ed5974207",
                     "https://open.spotify.com/embed/track/6Y8eovMST7tkAU7bkJSA5A?si=a29306f524324bfa",
                     "https://open.spotify.com/embed/track/5z4QTxWYZkFtgZWyZAHWfG?si=37a7a01dee4f4841"
                    ]

        if place == "New Zealand⛰️":
            st.title(f"Songs of {place}")
            songs =["https://open.spotify.com/embed/track/1qbmS6ep2hbBRaEZFpn7BX?si=2f5155c793d94a78",
                    "https://open.spotify.com/embed/track/7MZHqgTVTnN6xZGYAcEEAf?si=cd3d2ea99cbb4175",
                    "https://open.spotify.com/embed/track/6gkbtMtioHgtyGjrMel6ei?si=5b0c83fa5edb4845"
                    ]   
        if place == "Italy🥐🍵":
            st.title(f"Songs of {place}")
            songs =["https://open.spotify.com/embed/track/0C2IeaV0r1F8IYWe4JjM2u?si=82e06932c3dc4e4d",
                     "https://open.spotify.com/embed/track/1GeNui6m825V8jP4uKiIaH?si=4e931d8c9f554b2d",
                     "https://open.spotify.com/embed/track/63sQFPGkKfzcK5qEZVefpu?si=bcaf783bbaff49a9"
                    ]
        if place == "Switzerland🏝️":
            st.title(f"Songs of {place}")
            songs =["https://open.spotify.com/embed/track/5vNRhkKd0yEAg8suGBpjeY?si=94651f4ec969413d",
                     "https://open.spotify.com/embed/track/55lijDD6OAjLFFUHU9tcDm?si=94ce4d4367884f79",
                     "https://open.spotify.com/embed/track/53iuhJlwXhSER5J2IYYv1W?si=d106eed429764a5f"
                    ]
        if place == "Indonesia⛵":
            st.title(f"Songs of {place}")
            songs =["https://open.spotify.com/embed/track/2aDgJHhAbABvdW9NszrAPQ?si=ecf9b263174d4ed5",
                     "https://open.spotify.com/embed/track/7zOVh5fGpEwSbZd0g9z80B?si=960663c06e754c83",
                     "https://open.spotify.com/embed/track/7F4tV8SiUy6itZTdAzdafO?si=06cc37fc352f44d2"
                    ]
        if place == "Thailand🌉" :
            st.title(f"Songs of {place}")
            songs =["https://open.spotify.com/embed/track/4QR40LqFAbMdabh4AoZJGZ?si=d6deffd2f9c74ea1",
                    "https://open.spotify.com/embed/track/6vvPecFTmWxDfEJ6cYT1wa?si=f5e8610966c24f1c",
                    "https://open.spotify.com/embed/track/3RPiQqgZbe4jFNMIZtGoaU?si=cd6ee4705c704a38"
                    ]
        if place == "Norway🏙️" :
            st.title(f"Songs of {place}")
            songs =["https://open.spotify.com/embed/track/6Azklj5eui0iZ4ikG0L47g?si=08127c7b085847c3",
                    "https://open.spotify.com/embed/playlist/5SegpORs0Z5s9NnDkUCX6Z?si=RTSDEsaHRLGPFni5nDvRBA",
                    "https://open.spotify.com/embed/track/1rIKgCH4H52lrvDcz50hS8?si=ab38e7694b4c4404"
                    ]
        if place == "India🏦" :
            st.title(f"Songs of {place}")
            songs =["https://open.spotify.com/embed/track/0RsH8g8DxdYZgdGcod5I36?si=815d9444ec40434d",
                    "https://open.spotify.com/embed/track/5gysl1k9QxPSM604I8G3uk?si=a029e628ad7e45df",
                    "https://open.spotify.com/embed/track/0Y6YW1552df031DjV8qBHv?si=b60d5205258b4e79"
                    ]
        for audio in songs:
           components.iframe(audio, height=80)