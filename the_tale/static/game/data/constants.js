
if (!window.pgf) {
    pgf = {};
}

if (!pgf.game) {
    pgf.game = {};
}

pgf.game.constants = {

    ACTOR_TYPE: {"PERSON": 0, "PLACE": 1, "MONEY_SPENDING": 2},

    GENDER_TO_TEXT: {"0": "мужчина", "1": "женщина", "2": "оно"},
    GENDER_TO_STR: {"0": "MASCULINE", "1": "FEMININE", "2": "NEUTER"},

    PERSON_TYPE_TO_TEXT: {"0": "кузнец", "1": "рыбак", "2": "портной", "3": "плотник", "4": "охотник", "5": "стражник", "6": "торговец", "7": "трактирщик", "8": "вор", "9": "фермер", "10": "шахтёр", "11": "священник", "12": "лекарь", "13": "алхимик", "14": "палач", "15": "волшебник", "16": "мэр", "17": "бюрократ", "18": "аристократ", "19": "бард", "20": "дрессировщик", "21": "скотовод"},

    RACE_TO_TEXT: {"0": "человек", "1": "эльф", "2": "орк", "3": "гоблин", "4": "дварф"},
    RACE_TO_STR: {"0": "HUMAN", "1": "ELF", "2": "ORC", "3": "GOBLIN", "4": "DWARF"},

    GAME_STATE: {"STOPPED": 0, "WORKING": 1},
};

pgf.game.constants.ARTIFACT_TYPE = {
        "USELESS": {
        "id": 0,
        "name": "хлам"
    },    "MAIN_HAND": {
        "id": 1,
        "name": "основная рука"
    },    "OFF_HAND": {
        "id": 2,
        "name": "вторая рука"
    },    "PLATE": {
        "id": 3,
        "name": "доспех"
    },    "AMULET": {
        "id": 4,
        "name": "амулет"
    },    "HELMET": {
        "id": 5,
        "name": "шлем"
    },    "CLOAK": {
        "id": 6,
        "name": "плащ"
    },    "SHOULDERS": {
        "id": 7,
        "name": "наплечники"
    },    "GLOVES": {
        "id": 8,
        "name": "перчатки"
    },    "PANTS": {
        "id": 9,
        "name": "штаны"
    },    "BOOTS": {
        "id": 10,
        "name": "обувь"
    },    "RING": {
        "id": 11,
        "name": "кольцо"
    }};

pgf.game.constants.RARITY = {
        "NORMAL": {
        "id": 0,
        "name": "обычный артефакт"
    },    "RARE": {
        "id": 1,
        "name": "редкий артефакт"
    },    "EPIC": {
        "id": 2,
        "name": "эпический артефакт"
    }};

pgf.game.constants.NO_EFFECT_ID = 666;

pgf.game.constants.EFFECTS = {
        "1023": {
        "name": "живость ума",
        "description": "Задержка смены предпочтений уменьшается до 1 дня"
    },    "1024": {
        "name": "ужасный вид",
        "description": "Герой выглядит настолько ужасно, что некоторые противники в ужасе убегают, не вступая в бой"
    },    "1025": {
        "name": "точные атаки",
        "description": "Герою становится доступна способность «Критический удар» максимального уровня"
    },    "4": {
        "name": "повышение интуиции",
        "description": "Немного увеличивает получаемый героем опыт"
    },    "100001": {
        "name": "детский подарок",
        "description": "Это потерянный подарок ребёнка. Помогите герою, когда артефакт лежит в рюкзаке, и подарок вернётся к ребёнку."
    },    "5": {
        "name": "хитрость",
        "description": "Немного увеличивает влияние героя"
    },    "1028": {
        "name": "удача странника",
        "description": "Увеличивается шанс получения редких артефактов"
    },    "7": {
        "name": "скороход",
        "description": "Немного увеличивает скорость движения героя"
    },    "1029": {
        "name": "удача героя",
        "description": "Увеличивается шанс получения эпических артефактов"
    },    "1030": {
        "name": "крепость духа",
        "description": "Черты героя уменьшаются медленнее"
    },    "2": {
        "name": "хорошая реакция",
        "description": "Немного увеличивает инициативу героя в бою"
    },    "666": {
        "name": "нет эффекта",
        "description": "нет эффекта"
    },    "1000": {
        "name": "небывалая мощь",
        "description": "Сильно увеличивает физический урон"
    },    "1033": {
        "name": "ускорение",
        "description": "Герою становится доступна способность «Ускорение» максимального уровня"
    },    "1002": {
        "name": "превосходная реакция",
        "description": "Сильно увеличивает инициативу героя в бою"
    },    "8": {
        "name": "карманы",
        "description": "Немного увеличивает вместимость рюкзака героя"
    },    "1003": {
        "name": "невероятное здоровье",
        "description": "Сильно увеличивает максимальное здоровье героя"
    },    "1004": {
        "name": "сверхинтуиция",
        "description": "Сильно увеличивает получаемый героем опыт"
    },    "3": {
        "name": "здоровье",
        "description": "Немного увеличивает максимальное здоровье героя"
    },    "1005": {
        "name": "особая хитрость",
        "description": "Сильно увеличивает влияние героя"
    },    "1006": {
        "name": "большой астральный сосуд",
        "description": "Сильно увеличивает максимум энергии Хранителя"
    },    "1007": {
        "name": "неутомимый скороход",
        "description": "Сильно увеличивает скорость движения героя"
    },    "1008": {
        "name": "большие карманы",
        "description": "Сильно увеличивает вместимость рюкзака героя"
    },    "1031": {
        "name": "идейность",
        "description": "Черты героя растут быстрее"
    },    "1009": {
        "name": "выносливость",
        "description": "Герой быстрее восстанавливает здоровье во время отдыха"
    },    "1010": {
        "name": "живучесть",
        "description": "Герой быстрее воскрешается"
    },    "1026": {
        "name": "астральная преграда",
        "description": "Герою становится доступна способность «Горгулья» максимального уровня"
    },    "1011": {
        "name": "деятельность",
        "description": "Герой меньше бездельничает"
    },    "1012": {
        "name": "убеждение",
        "description": "Уменьшение всех трат"
    },    "0": {
        "name": "мощь",
        "description": "Немного увеличивает физический урон"
    },    "1013": {
        "name": "очарование",
        "description": "Увеличение цены продажи предметов"
    },    "1014": {
        "name": "духовная связь",
        "description": "Все затраты энергии уменьшаются на 1 (но не меньше 1)"
    },    "1032": {
        "name": "нерушимость",
        "description": "Экипировка героя медленнее ломается"
    },    "1015": {
        "name": "душевное равновесие",
        "description": "Хранитель иногда получает в два раза больше энергии от героя"
    },    "1016": {
        "name": "особая аура",
        "description": "Физическая и магическая сила всех артефактов, получаемых героем, увеличивается на 1"
    },    "1027": {
        "name": "затуманенный разум",
        "description": "Разум героя затуманивается и тот начинает вести себя независимо от черт"
    },    "1017": {
        "name": "регенерация",
        "description": "Герою становится доступна способность «Регенерация» максимального уровня"
    },    "1018": {
        "name": "последний шанс",
        "description": "Герою становится доступна способность «Последний шанс» максимального уровня"
    },    "1022": {
        "name": "вампиризм",
        "description": "Герою становится доступна способность «Удар вампира» максимального уровня"
    },    "1019": {
        "name": "лёд",
        "description": "Герою становится доступна способность «Заморозка» максимального уровня"
    },    "1020": {
        "name": "пламя",
        "description": "Герою становится доступна способность «Огненный шар» максимального уровня"
    },    "1001": {
        "name": "могучее колдовство",
        "description": "Сильно увеличивает магический урон"
    },    "1021": {
        "name": "яд",
        "description": "Герою становится доступна способность «Ядовитое облако» максимального уровня"
    },    "1": {
        "name": "колдовство",
        "description": "Немного увеличивает магический урон"
    },    "6": {
        "name": "астральный сосуд",
        "description": "Немного увеличивает максимум энергии Хранителя"
    }};

pgf.game.constants.abilities = {

    
    "help": {
        "type": "help",
        "name": "Помочь",
        "description": "Попытаться помочь герою, чем бы тот не занимался",
        "cost": 4
    },
    "arena_pvp_1x1": {
        "type": "arena_pvp_1x1",
        "name": "Отправить на арену",
        "description": "Отправить героя на гладиаторскую арену",
        "cost": 1
    },
    "arena_pvp_1x1_leave_queue": {
        "type": "arena_pvp_1x1_leave_queue",
        "name": "Выйти из очереди",
        "description": "Выйти из очереди на арену",
        "cost": 0
    },
    "arena_pvp_1x1_accept": {
        "type": "arena_pvp_1x1_accept",
        "name": "Принять вызов",
        "description": "Принять вызов другого героя",
        "cost": 1
    },
    "building_repair": {
        "type": "building_repair",
        "name": "Вызвать рабочего",
        "description": "Вызвать рабочего для ремонта здания",
        "cost": 3
    },
    "drop_item": {
        "type": "drop_item",
        "name": "Выбросить предмет",
        "description": "Выбросить из рюкзака самый ненужный предмет",
        "cost": 3
    }
};

pgf.game.constants.sprites = {

    
    "0": {
        "x": "0",
        "y": "256"
    },

    
    "1": {
        "x": "32",
        "y": "256"
    },

    
    "2": {
        "x": "64",
        "y": "256"
    },

    
    "3": {
        "x": "96",
        "y": "256"
    },

    
    "4": {
        "x": "128",
        "y": "256"
    },

    
    "5": {
        "x": "160",
        "y": "256"
    },

    
    "6": {
        "x": "192",
        "y": "256"
    },

    
    "7": {
        "x": "224",
        "y": "256"
    },

    
    "8": {
        "x": "256",
        "y": "256"
    },

    
    "9": {
        "x": "288",
        "y": "256"
    },

    
    "10": {
        "x": "0",
        "y": "256"
    },

    
    "11": {
        "x": "64",
        "y": "256"
    },

    
    "12": {
        "x": "128",
        "y": "256"
    },

    
    "13": {
        "x": "192",
        "y": "256"
    },

    
    "14": {
        "x": "256",
        "y": "256"
    },

    
    "15": {
        "x": "128",
        "y": "64"
    },

    
    "16": {
        "x": "96",
        "y": "64"
    },

    
    "17": {
        "x": "32",
        "y": "64"
    },

    
    "18": {
        "x": "0",
        "y": "64"
    },

    
    "19": {
        "x": "32",
        "y": "0"
    },

    
    "20": {
        "x": "96",
        "y": "0"
    },

    
    "21": {
        "x": "128",
        "y": "0"
    },

    
    "22": {
        "x": "160",
        "y": "0"
    },

    
    "23": {
        "x": "0",
        "y": "0"
    },

    
    "24": {
        "x": "64",
        "y": "0"
    },

    
    "25": {
        "x": "0",
        "y": "32"
    },

    
    "26": {
        "x": "32",
        "y": "32"
    },

    
    "27": {
        "x": "64",
        "y": "32"
    },

    
    "28": {
        "x": "96",
        "y": "32"
    },

    
    "29": {
        "x": "160",
        "y": "64"
    },

    
    "30": {
        "x": "224",
        "y": "0"
    },

    
    "31": {
        "x": "352",
        "y": "0"
    },

    
    "32": {
        "x": "320",
        "y": "0"
    },

    
    "33": {
        "x": "288",
        "y": "0"
    },

    
    "34": {
        "x": "192",
        "y": "0"
    },

    
    "35": {
        "x": "256",
        "y": "0"
    },

    
    "36": {
        "x": "192",
        "y": "32"
    },

    
    "37": {
        "x": "224",
        "y": "32"
    },

    
    "38": {
        "x": "256",
        "y": "32"
    },

    
    "39": {
        "x": "288",
        "y": "32"
    },

    
    "40": {
        "x": "192",
        "y": "64"
    },

    
    "41": {
        "x": "224",
        "y": "64"
    },

    
    "42": {
        "x": "64",
        "y": "64"
    },

    
    "43": {
        "x": "352",
        "y": "32"
    },

    
    "44": {
        "x": "0",
        "y": "192"
    },

    
    "45": {
        "x": "32",
        "y": "192"
    },

    
    "46": {
        "x": "64",
        "y": "192"
    },

    
    "47": {
        "x": "96",
        "y": "192"
    },

    
    "48": {
        "x": "128",
        "y": "192"
    },

    
    "49": {
        "x": "160",
        "y": "192"
    },

    
    "50": {
        "x": "192",
        "y": "192"
    },

    
    "51": {
        "x": "224",
        "y": "192"
    },

    
    "52": {
        "x": "256",
        "y": "192"
    },

    
    "53": {
        "x": "288",
        "y": "192"
    },

    
    "54": {
        "x": "320",
        "y": "192"
    },

    
    "55": {
        "x": "352",
        "y": "192"
    },

    
    "56": {
        "x": "0",
        "y": "224"
    },

    
    "57": {
        "x": "32",
        "y": "224"
    },

    
    "58": {
        "x": "64",
        "y": "224"
    },

    
    "59": {
        "x": "96",
        "y": "224"
    },

    
    "60": {
        "x": "128",
        "y": "224"
    },

    
    "61": {
        "x": "160",
        "y": "224"
    },

    
    "62": {
        "x": "192",
        "y": "224"
    },

    
    "63": {
        "x": "224",
        "y": "224"
    },

    
    "64": {
        "x": "96",
        "y": "96"
    },

    
    "65": {
        "x": "32",
        "y": "96"
    },

    
    "66": {
        "x": "160",
        "y": "96"
    },

    
    "67": {
        "x": "64",
        "y": "96"
    },

    
    "68": {
        "x": "128",
        "y": "96"
    },

    
    "69": {
        "x": "0",
        "y": "96"
    },

    
    "70": {
        "x": "0",
        "y": "288"
    },

    
    "71": {
        "x": "32",
        "y": "288"
    },

    
    "72": {
        "x": "0",
        "y": "128"
    },

    
    "73": {
        "x": "32",
        "y": "128"
    },

    
    "74": {
        "x": "64",
        "y": "128"
    },

    
    "75": {
        "x": "96",
        "y": "128"
    },

    
    "76": {
        "x": "128",
        "y": "128"
    },

    
    "77": {
        "x": "160",
        "y": "128"
    },

    
    "78": {
        "x": "192",
        "y": "128"
    },

    
    "79": {
        "x": "224",
        "y": "128"
    },

    
    "80": {
        "x": "256",
        "y": "128"
    },

    
    "81": {
        "x": "288",
        "y": "128"
    },

    
    "82": {
        "x": "320",
        "y": "128"
    },

    
    "83": {
        "x": "352",
        "y": "128"
    },

    
    "84": {
        "x": "0",
        "y": "160"
    },

    
    "85": {
        "x": "32",
        "y": "160"
    },

    
    "86": {
        "x": "64",
        "y": "160"
    },

    
    "87": {
        "x": "96",
        "y": "160"
    },

    
    "88": {
        "x": "128",
        "y": "160"
    },

    
    "89": {
        "x": "160",
        "y": "160"
    },

    
    "90": {
        "x": "192",
        "y": "160"
    },

    
    "91": {
        "x": "224",
        "y": "160"
    },

    
    "92": {
        "x": "256",
        "y": "160"
    },

    
    "93": {
        "x": "288",
        "y": "160"
    },

    
    "CELL_HIGHLIGHTING": "71",
    "SELECT_LAND": "70"

}

pgf.game.constants.tilesets = {

    main: {
        TILE_SIZE: 32,
        W: 32,
        H: 32,
        SRC: "/game/images/map.png",
        sprites: jQuery.extend(true, {}, pgf.game.constants.sprites)
    },

    alternative: {
        TILE_SIZE: 32,
        W: 32,
        H: 32,
        SRC: "/game/images/map_alternative.png",
        sprites: jQuery.extend(true, {}, pgf.game.constants.sprites)
    },

    winter: {
        TILE_SIZE: 32,
        W: 32,
        H: 32,
        SRC: "/game/images/map_winter.png",
        sprites: jQuery.extend(true, {}, pgf.game.constants.sprites)
    },

    large_pixel: {
        TILE_SIZE: 32,
        W: 32,
        H: 32,
        SRC: "/game/images/map_large_pixel.png",
        sprites: jQuery.extend(true, {}, pgf.game.constants.sprites)
    }
};


for (var tilesetName in pgf.game.constants.tilesets) {
    var tileset = pgf.game.constants.tilesets[tilesetName];

    for (var spriteName in tileset.sprites) {
        var sprite = tileset.sprites[spriteName];

        if (typeof(sprite)=='string') continue;

        if (sprite.w == undefined) sprite.w = tileset.W;
        if (sprite.h == undefined) sprite.h = tileset.H;
        if (sprite.src == undefined) sprite.src = tileset.SRC;
    }
}