from flask import Flask, render_template_string, request, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# General Knowledge Quiz Questions
QUIZ_DATA_GK = [
    {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Madrid"], "answer": 2},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": 1},
    {"question": "Who wrote Romeo and Juliet?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "answer": 1},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": 3},
    {"question": "In which year did World War II end?", "options": ["1943", "1944", "1945", "1946"], "answer": 2},
    {"question": "What is the smallest country in the world?", "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"], "answer": 1},
    {"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "answer": 2},
    {"question": "What is the tallest mountain in the world?", "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"], "answer": 2},
    {"question": "Which element has the chemical symbol Au?", "options": ["Silver", "Gold", "Aluminum", "Copper"], "answer": 1},
    {"question": "What is the capital of Japan?", "options": ["Osaka", "Kyoto", "Tokyo", "Hiroshima"], "answer": 2},
    {"question": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "answer": 2},
    {"question": "Who was the first person to walk on the moon?", "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"], "answer": 1},
    {"question": "What is the longest river in the world?", "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "answer": 1},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "South Korea", "Japan", "Thailand"], "answer": 2},
    {"question": "What is the largest mammal in the world?", "options": ["African Elephant", "Blue Whale", "Giraffe", "Polar Bear"], "answer": 1},
    {"question": "In which city is the Eiffel Tower located?", "options": ["London", "Rome", "Paris", "Berlin"], "answer": 2},
    {"question": "How many bones are there in the adult human body?", "options": ["186", "206", "226", "246"], "answer": 1},
    {"question": "Who invented the telephone?", "options": ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Benjamin Franklin"], "answer": 2},
    {"question": "What is the currency of the United Kingdom?", "options": ["Euro", "Dollar", "Pound Sterling", "Franc"], "answer": 2},
    {"question": "Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": 2}
]

# Science Quiz Questions
QUIZ_DATA_SCIENCE = [
    {"question": "What is the chemical formula for water?", "options": ["H2O", "CO2", "O2", "H2O2"], "answer": 0},
    {"question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "200,000 km/s"], "answer": 0},
    {"question": "What is the powerhouse of the cell?", "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"], "answer": 2},
    {"question": "What is the atomic number of carbon?", "options": ["4", "6", "8", "12"], "answer": 1},
    {"question": "What type of bond involves sharing electrons?", "options": ["Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond"], "answer": 1},
    {"question": "What is the largest organ in the human body?", "options": ["Liver", "Brain", "Skin", "Heart"], "answer": 2},
    {"question": "What process do plants use to make food?", "options": ["Respiration", "Photosynthesis", "Digestion", "Fermentation"], "answer": 1},
    {"question": "What is the unit of electrical resistance?", "options": ["Volt", "Ampere", "Ohm", "Watt"], "answer": 2},
    {"question": "Which planet has the most moons?", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"], "answer": 1},
    {"question": "What does DNA stand for?", "options": ["Deoxyribonucleic Acid", "Diribonucleic Acid", "Deoxyribose Acid", "Dioxy Nucleic Acid"], "answer": 0},
    {"question": "What is the most abundant gas in atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": 2},
    {"question": "At what temp does water boil at sea level in Celsius?", "options": ["90", "100", "110", "120"], "answer": 1},
    {"question": "What is the center of an atom called?", "options": ["Electron", "Proton", "Nucleus", "Neutron"], "answer": 2},
    {"question": "Which blood type is the universal donor?", "options": ["A+", "B+", "AB+", "O-"], "answer": 3},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "answer": 2},
    {"question": "How many chambers does the human heart have?", "options": ["2", "3", "4", "5"], "answer": 2},
    {"question": "What is the study of earthquakes called?", "options": ["Geology", "Seismology", "Meteorology", "Volcanology"], "answer": 1},
    {"question": "What is the smallest unit of life?", "options": ["Atom", "Molecule", "Cell", "Organ"], "answer": 2},
    {"question": "What force keeps planets in orbit?", "options": ["Magnetism", "Gravity", "Friction", "Centrifugal"], "answer": 1},
    {"question": "What is the pH value of pure water?", "options": ["5", "7", "9", "11"], "answer": 1}
]

# Sports Quiz Questions
QUIZ_DATA_SPORTS = [
    {"question": "How many players in a soccer team on field?", "options": ["9", "10", "11", "12"], "answer": 2},
    {"question": "In which sport would you perform a slam dunk?", "options": ["Volleyball", "Basketball", "Tennis", "Badminton"], "answer": 1},
    {"question": "How many Grand Slam tennis tournaments per year?", "options": ["2", "3", "4", "5"], "answer": 2},
    {"question": "Maximum score in a single bowling frame?", "options": ["100", "200", "300", "400"], "answer": 2},
    {"question": "Where were first modern Olympic Games held?", "options": ["France", "Greece", "Italy", "England"], "answer": 1},
    {"question": "How many players on a baseball team in field?", "options": ["8", "9", "10", "11"], "answer": 1},
    {"question": "What card for serious foul in soccer?", "options": ["Yellow", "Red", "Blue", "Green"], "answer": 1},
    {"question": "How many points is a touchdown worth?", "options": ["3", "5", "6", "7"], "answer": 2},
    {"question": "In which sport would you use a puck?", "options": ["Field Hockey", "Ice Hockey", "Lacrosse", "Cricket"], "answer": 1},
    {"question": "Length of Olympic swimming pool in meters?", "options": ["25m", "50m", "75m", "100m"], "answer": 1},
    {"question": "How many rings on the Olympic flag?", "options": ["3", "4", "5", "6"], "answer": 2},
    {"question": "In golf, one stroke under par is called?", "options": ["Eagle", "Birdie", "Bogey", "Albatross"], "answer": 1},
    {"question": "What is the national sport of Japan?", "options": ["Karate", "Judo", "Sumo Wrestling", "Kendo"], "answer": 2},
    {"question": "Points for a try in rugby union?", "options": ["3", "4", "5", "6"], "answer": 2},
    {"question": "In which sport is the Davis Cup awarded?", "options": ["Golf", "Tennis", "Cricket", "Badminton"], "answer": 1},
    {"question": "Diameter of a basketball hoop in inches?", "options": ["16", "18", "20", "22"], "answer": 1},
    {"question": "Sets needed to win men's Grand Slam match?", "options": ["2", "3", "4", "5"], "answer": 1},
    {"question": "How many players on a cricket team?", "options": ["9", "10", "11", "12"], "answer": 2},
    {"question": "Maximum break in snooker?", "options": ["100", "127", "147", "180"], "answer": 2},
    {"question": "How long is a marathon in km?", "options": ["40.2", "42.195", "44", "45"], "answer": 1}
]

# Technology Quiz Questions
QUIZ_DATA_TECHNOLOGY = [
    {"question": "Who is known as the father of computers?", "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"], "answer": 1},
    {"question": "What does CPU stand for?", "options": ["Central Processing Unit", "Computer Personal Unit", "Central Processor Union", "Computer Processing Unit"], "answer": 0},
    {"question": "In what year was the first iPhone released?", "options": ["2005", "2006", "2007", "2008"], "answer": 2},
    {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks Text Markup Language"], "answer": 0},
    {"question": "Who founded Microsoft?", "options": ["Steve Jobs", "Bill Gates and Paul Allen", "Mark Zuckerberg", "Larry Page"], "answer": 1},
    {"question": "What does RAM stand for?", "options": ["Random Access Memory", "Read Access Memory", "Rapid Action Memory", "Random Action Module"], "answer": 0},
    {"question": "Which company developed Android?", "options": ["Apple", "Microsoft", "Google", "Samsung"], "answer": 2},
    {"question": "Main programming language for AI?", "options": ["Java", "C++", "Python", "Ruby"], "answer": 2},
    {"question": "What does URL stand for?", "options": ["Universal Resource Locator", "Uniform Resource Locator", "Universal Relative Link", "Uniform Relative Locator"], "answer": 1},
    {"question": "Who is the CEO of Tesla?", "options": ["Jeff Bezos", "Elon Musk", "Tim Cook", "Sundar Pichai"], "answer": 1},
    {"question": "What does USB stand for?", "options": ["Universal Serial Bus", "United System Bus", "Universal System Board", "United Serial Board"], "answer": 0},
    {"question": "Mother of all programming languages?", "options": ["Python", "C", "Java", "Assembly"], "answer": 1},
    {"question": "Binary system is based on?", "options": ["0 and 1", "1 and 2", "0 and 2", "A and B"], "answer": 0},
    {"question": "Which company owns YouTube?", "options": ["Facebook", "Google", "Amazon", "Microsoft"], "answer": 1},
    {"question": "What does Wi-Fi stand for?", "options": ["Wireless Fidelity", "Wide Fidelity", "Wireless Fiber", "Wide Fiber"], "answer": 0},
    {"question": "Smallest unit of data in computer?", "options": ["Byte", "Bit", "Nibble", "Kilobyte"], "answer": 1},
    {"question": "Who developed Java programming language?", "options": ["Microsoft", "Apple", "Sun Microsystems", "IBM"], "answer": 2},
    {"question": "What does VPN stand for?", "options": ["Virtual Private Network", "Very Private Network", "Virtual Public Network", "Verified Private Network"], "answer": 0},
    {"question": "How many bits in a byte?", "options": ["4", "8", "16", "32"], "answer": 1},
    {"question": "Most widely used search engine?", "options": ["Bing", "Yahoo", "Google", "DuckDuckGo"], "answer": 2}
]

# Arts & Literature Quiz Questions
QUIZ_DATA_ARTS = [
    {"question": "Who wrote Pride and Prejudice?", "options": ["Charlotte Bronte", "Jane Austen", "Emily Bronte", "Mary Shelley"], "answer": 1},
    {"question": "Who painted The Starry Night?", "options": ["Claude Monet", "Vincent van Gogh", "Pablo Picasso", "Salvador Dali"], "answer": 1},
    {"question": "Who wrote 1984?", "options": ["Aldous Huxley", "Ray Bradbury", "George Orwell", "H.G. Wells"], "answer": 2},
    {"question": "Art of beautiful handwriting is called?", "options": ["Typography", "Calligraphy", "Lithography", "Stenography"], "answer": 1},
    {"question": "Who composed The Four Seasons?", "options": ["Mozart", "Bach", "Vivaldi", "Beethoven"], "answer": 2},
    {"question": "Novel that begins with Call me Ishmael?", "options": ["Moby-Dick", "Old Man and Sea", "Treasure Island", "Robinson Crusoe"], "answer": 0},
    {"question": "Who sculpted David?", "options": ["Donatello", "Michelangelo", "Bernini", "Rodin"], "answer": 1},
    {"question": "Literary device using like or as?", "options": ["Metaphor", "Simile", "Personification", "Alliteration"], "answer": 1},
    {"question": "Who wrote The Great Gatsby?", "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner"], "answer": 1},
    {"question": "Salvador Dali's art movement?", "options": ["Impressionism", "Cubism", "Surrealism", "Expressionism"], "answer": 2},
    {"question": "Who wrote To Kill a Mockingbird?", "options": ["Harper Lee", "Truman Capote", "Flannery O'Connor", "Carson McCullers"], "answer": 0},
    {"question": "What is a haiku?", "options": ["A type of painting", "A Japanese poem", "A musical instrument", "A dance form"], "answer": 1},
    {"question": "Who painted The Last Supper?", "options": ["Raphael", "Leonardo da Vinci", "Michelangelo", "Caravaggio"], "answer": 1},
    {"question": "Play with Oberon and Titania?", "options": ["The Tempest", "Midsummer Night's Dream", "As You Like It", "Twelfth Night"], "answer": 1},
    {"question": "Primary color unmixable?", "options": ["Green", "Orange", "Red", "Purple"], "answer": 2},
    {"question": "Who wrote The Catcher in the Rye?", "options": ["Jack Kerouac", "J.D. Salinger", "Allen Ginsberg", "Kurt Vonnegut"], "answer": 1},
    {"question": "Which museum houses the Mona Lisa?", "options": ["The Louvre", "The Uffizi", "The Met", "The Prado"], "answer": 0},
    {"question": "Term for story's time and place?", "options": ["Plot", "Theme", "Setting", "Conflict"], "answer": 2},
    {"question": "Who composed The Magic Flute?", "options": ["Wagner", "Verdi", "Mozart", "Puccini"], "answer": 2},
    {"question": "Art technique using small dots?", "options": ["Cubism", "Pointillism", "Fauvism", "Minimalism"], "answer": 1}
]

# Entertainment Quiz Questions
QUIZ_DATA_ENTERTAINMENT = [
    {"question": "2020 Oscar Best Picture winner?", "options": ["1917", "Joker", "Parasite", "Once Upon a Time"], "answer": 2},
    {"question": "Who played Iron Man in MCU?", "options": ["Chris Evans", "Chris Hemsworth", "Robert Downey Jr.", "Mark Ruffalo"], "answer": 2},
    {"question": "TV series with Walter White?", "options": ["The Wire", "Breaking Bad", "The Sopranos", "Mad Men"], "answer": 1},
    {"question": "Who directed Jurassic Park?", "options": ["James Cameron", "Steven Spielberg", "George Lucas", "Peter Jackson"], "answer": 1},
    {"question": "Streaming service for Stranger Things?", "options": ["Amazon Prime", "Hulu", "Netflix", "Disney+"], "answer": 2},
    {"question": "Who is the King of Pop?", "options": ["Elvis Presley", "Prince", "Michael Jackson", "Freddie Mercury"], "answer": 2},
    {"question": "Highest-grossing film of all time?", "options": ["Titanic", "Avatar", "Avengers Endgame", "Star Wars"], "answer": 1},
    {"question": "Who played Jack Dawson in Titanic?", "options": ["Brad Pitt", "Leonardo DiCaprio", "Johnny Depp", "Tom Cruise"], "answer": 1},
    {"question": "TV show set in Hawkins Indiana?", "options": ["Riverdale", "Stranger Things", "Twin Peaks", "Supernatural"], "answer": 1},
    {"question": "Who sang Bohemian Rhapsody?", "options": ["Led Zeppelin", "The Beatles", "Queen", "Pink Floyd"], "answer": 2},
    {"question": "Movie with May the Force be with you?", "options": ["Star Trek", "Star Wars", "Battlestar Galactica", "The Matrix"], "answer": 1},
    {"question": "Who directed The Dark Knight trilogy?", "options": ["Zack Snyder", "Christopher Nolan", "Tim Burton", "Sam Raimi"], "answer": 1},
    {"question": "Animated movie with Let It Go song?", "options": ["Moana", "Tangled", "Frozen", "Brave"], "answer": 2},
    {"question": "Who played Hermione in Harry Potter?", "options": ["Emma Watson", "Emma Stone", "Emily Blunt", "Emma Roberts"], "answer": 0},
    {"question": "Coffee shop name in Friends?", "options": ["Central Perk", "Coffee Bean", "Starbucks", "Java Joes"], "answer": 0},
    {"question": "Band that performed Stairway to Heaven?", "options": ["Rolling Stones", "The Who", "Led Zeppelin", "Deep Purple"], "answer": 2},
    {"question": "First American Idol winner?", "options": ["Carrie Underwood", "Kelly Clarkson", "Fantasia Barrino", "Ruben Studdard"], "answer": 1},
    {"question": "Movie with Forrest Gump character?", "options": ["Cast Away", "Philadelphia", "Forrest Gump", "The Green Mile"], "answer": 2},
    {"question": "Fictional African country in Black Panther?", "options": ["Zamunda", "Wakanda", "Genovia", "Latveria"], "answer": 1},
    {"question": "Who composed music for The Lion King?", "options": ["Hans Zimmer", "John Williams", "Alan Menken", "Elton John"], "answer": 3}
]

if __name__ == '__main__':
    print("Quiz data loaded successfully!")
    print(f"GK Questions: {len(QUIZ_DATA_GK)}")
    print(f"Science Questions: {len(QUIZ_DATA_SCIENCE)}")
    print(f"Sports Questions: {len(QUIZ_DATA_SPORTS)}")
    print(f"Technology Questions: {len(QUIZ_DATA_TECHNOLOGY)}")
    print(f"Arts Questions: {len(QUIZ_DATA_ARTS)}")
    print(f"Entertainment Questions: {len(QUIZ_DATA_ENTERTAINMENT)}")