from codenames.i18n.language import _Language

RUSSIAN = _Language.RUSSIAN
ENGLISH = _Language.ENGLISH


# common

AND = {
    RUSSIAN: "и",
    ENGLISH: "and"
}

NOBODY = {
    RUSSIAN: "никто",
    ENGLISH: "nobody"
}

SUCCESS = {
    RUSSIAN: "Успешно!",
    ENGLISH: "Success!"
}

CANCELLED = {
    RUSSIAN: "Ввод отменён.",
    ENGLISH: "Cancelled input."
}

DONT_UNDERSTAND = {
    RUSSIAN: "Я вас не понимаю.",
    ENGLISH: "I don't understand you."
}


# help

HELP_MESSAGE = {
    RUSSIAN: (
        "Приветствую! Я — бот, с помощью которого вы "
        "можете играть в Codenames.Duet со своими друзьями."
    ),
    ENGLISH: (
        "Hello! I am bot that will allow you to play "
        "Codenames.Duet with your friends."
    )
}


# manage game

CREATE_GAME_INLINE = {
    RUSSIAN: "создать игру",
    ENGLISH: "create a game"
}

TOKEN_COUNT_SETTING = {
    RUSSIAN: "{} ходов",
    ENGLISH: "{} turns"
}

CREATE_GAME_WITH_SETTINGS = {
    RUSSIAN: "✅ :: {token_count} ходов, {wordlist} :: ✅",
    ENGLISH: "✅ :: {token_count} turns, {wordlist} :: ✅"
}

GAME_CREATED = {
    RUSSIAN: "Игра создана.",
    ENGLISH: "Game created."
}


# join

JOIN_GAME_AUTO_TEAM = {
    RUSSIAN: "присоединиться (автовыбор стороны)",
    ENGLISH: "join (choose side automatically)"
}

JOIN_GAME_FIRST_TEAM = {
    RUSSIAN: "к первой",
    ENGLISH: "join the first"
}

JOIN_GAME_SECOND_TEAM = {
    RUSSIAN: "ко второй",
    ENGLISH: "join the second"
}

CHOOSE_NEW_GAME_SETTINGS = {
    RUSSIAN: "Задайте параметры игры:",
    ENGLISH: "Set parameters for the game:"
}

ALREADY_IN_GAME = {
    RUSSIAN: (
        "Вы уже играете. Если вы действительно хотите начать новую игру, "
        "покиньте текущую командой /leave_game."
    ),
    ENGLISH: (
        "You are already in a game. If you really want to start a new one, "
        "leave the current with /leave_game command."
    )
}

LEFT_GAME = {
    RUSSIAN: "Вы покинули игру.",
    ENGLISH: "You left the game."
}

YOU_ARE_NOT_IN_GAME = {
    RUSSIAN: "Вы не в игре.",
    ENGLISH: "You are not in game."
}

INVITATION = {
    RUSSIAN: (
        "Ваши друзья могут присоединиться, нажав на кнопку ниже. "
        "Вы можете переслать им это сообщение или отправить ссылку кнопки.\n\n"
        "На текущий момент за первым торцом стола {first_team}, а "
        "за вторым — {second_team}."
    ),
    ENGLISH: (
        "Your friends can join by tapping the button below. "
        "You can forward this message to them or just share button's link.\n\n"
        "Currently, the first table side is taken by {first_team}, while "
        "the second side is {second_team}."
    )
}


REPLAY = {
    RUSSIAN: "{} начинает игру заново.",
    ENGLISH: "{} starts the game over."
}


# play

## give clue

CLUE_ACCEPTED = {
    RUSSIAN: "Подсказка принята.",
    ENGLISH: "Clue accepted."
}

PLAYER_GIVES_CLUE = {
    RUSSIAN: "{nickname} даёт подсказку:\n{clue} {agent_count}.",
    ENGLISH: "{nickname} gives a clue:\n{clue} {agent_count}."
}


## make guess

GUESS_ACCEPTED = {
    RUSSIAN: "Догадка принята.",
    ENGLISH: "Guess accepted."
}

PLAYER_MAKES_GUESS = {
    RUSSIAN: "{nickname} называет догадку:\n{guess}.\n{result}",
    ENGLISH: "{nickname} makes a guess:\n{guess}.\n{result}"
}

BUMPED_INTO_AGENT = {
    RUSSIAN: "В яблочко! Это агент!",
    ENGLISH: "Bull's eye! It's an agent!"
}

BUMPED_INTO_BYSTANDER = {
    RUSSIAN: "Мимо! Это мирный житель.",
    ENGLISH: "Miss! It's a bystander."
}

BUMPED_INTO_ASSASSIN = {
    RUSSIAN: "Пиф-паф! Это убийца.",
    ENGLISH: "Bang bang! It's an assassin."
}

SUDDEN_DEATH = {
    RUSSIAN: "Упс! Вы исчерпали все свои ходы. Игроки вне очереди пытаются дооткрыть своих агентов.",
    ENGLISH: "Oops! You have no turns left. Now players try out of turn to reveal their agents."
}


## end turn

TURN_ENDED = {
    RUSSIAN: "Вы закончили ход.",
    ENGLISH: "You ended your turn."
}

PLAYER_ENDED_TURN = {
    RUSSIAN: "{} завершает ход.",
    ENGLISH: "{} ended their turn."
}


# settings

CURRENT_SETTINGS = {
    RUSSIAN: (
        "Текущие настройки:\n"
        "- игровое имя: {nickname} ..:: /nickname, чтобы изменить\n"
        "- язык: {language} ..:: /language, чтобы изменить"
    ),
    ENGLISH: (
        "Current settings:\n"
        "- in-game nickname: {nickname} ..:: /nickname to change\n"
        "- language: {language} ..:: /language to change"
    )
}

NICKNAME_DEFAULT_SETTING = {
    RUSSIAN: "{} [по умолчанию: ваше имя в Телеграме]",
    ENGLISH: "{} [default: your first name in Telegram]"
}

LANGUAGE_DEFAULT_SETTING = {
    RUSSIAN: "{} [по умолчанию]",
    ENGLISH: "{} [default]"
}

## language

CHOOSE_LANGUAGE = {
    RUSSIAN: "Выберите язык.",
    ENGLISH: "Choose a language."
}

LANGUAGE_NAME = {
    RUSSIAN: "🇷🇺 русский",
    ENGLISH: "🇬🇧 English"
}

LANGUAGE_CHANGED = {
    RUSSIAN: "Язык изменён на русский.",
    ENGLISH: "Language changed to English."
}

RETURN_TO_LANGUAGE_CHOICE = {
    RUSSIAN: "Отправьте /language, чтобы вернуться к выбору языка.",
    ENGLISH: "Send /language to choose again."
}


## nickname

CHANGE_NICKNAME_FROM_SET = {
    RUSSIAN: (
        "Ваше игровое имя — {}.\n"
        "Пришлите мне новое, если хотите его изменить, или /cancel, если нет.\n"
        "Отправьте /clear, чтобы очистить эту настройку."
    ),
    ENGLISH: (
        "Your in-game nickname is {}.\n"
        "Send me a new one if you want to change it or /cancel if you don't.\n"
        "You may also /clear this setting."
    )
}

CHANGE_NICKNAME_FROM_NOT_SET = {
    RUSSIAN: "Введите своё игровое имя или /cancel, чтобы оставить его вашим именем в Телеграме.",
    ENGLISH: "Enter your in-game nickname or /cancel to leave it your first name in Telegram."
}

NICKNAME_TOO_LONG = {
    RUSSIAN: "Слишком длинный ник. Пожалуйста, пришлите имя длиной не более {} символов.",
    ENGLISH: "The nickname is too long. Please provide a name that doesn't exceed {} characters."
}

NICKNAME_CLEARED = {
    RUSSIAN: "Настройка сброшена. Ваше игровое имя теперь снова ваше имя в Телеграме.",
    ENGLISH: "The setting is cleared. Your nickname is your first name in Telegram now."
}
