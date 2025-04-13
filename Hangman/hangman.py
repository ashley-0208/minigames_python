import PySimpleGUI as sg
from string import ascii_uppercase
from random import choice

MAX_WRONG_GUESSES = 6


def select_word():
    with open('word.txt', mode='r', encoding='utf-8') as words:
        word_list = words.readlines()
    return choice(word_list).strip().upper()


def build_canvas_frame():
    return sg.Frame('Hangman', [
        [sg.Graph(key='-CANVAS-', canvas_size=(300, 300), graph_bottom_left=(0, 0), graph_top_right=(200, 400))]
    ], font='Any 20')


def build_letters_frame():
    letter_groups = [
        ascii_uppercase[i: i + 4]  # چینش حروف به صورت 4 ستونی (هر ردیف 4 حرف)
        for i in range(0, len(ascii_uppercase), 4)
    ]
    letter_buttons = [
        [
            sg.Button(
                button_text=f'{letter}',
                font='Courier 20',
                border_width=0,
                button_color=(None, sg.theme_background_color()),
                key=f'-letter-{letter}-',
                enable_events=True,
            )
            for letter in letter_group
        ]
        for letter_group in letter_groups
    ]
    return sg.Column([  # قرار دادن دکمه‌ها در یک ستون با قاب
        [
            sg.Frame(
                'Letters',
                letter_buttons,
                font='Any 20'
            ),
            sg.Sizer()
        ]
    ])


def build_guessed_word_frame():
    return sg.Frame(
        '',
        [
            [
                sg.Text(
                    key='-DISPLAY-WORD-',
                    font='Courier 20',
                )
            ]
        ],
        element_justification='center'
    )


def build_action_buttons_frame():
    return sg.Frame(
        '',
        [
            [
                sg.Sizer(h_pixels=90),  # The Sizer objects allow you to add some padding in between the buttons
                sg.Button(
                    button_text='New',
                    key='-NEW-',  # Using this key, you can reference the element and know which element
                    # initiated an event.
                    font='Any 20'
                ),
                sg.Sizer(h_pixels=60),
                sg.Button(
                    button_text='Restart',
                    key='-RESTART-',
                    font='Any 20'
                ),
                sg.Sizer(h_pixels=60),
                sg.Button(
                    button_text='Quit',
                    key='-QUIT-',
                    font='Any 20'
                ),
                sg.Sizer(h_pixels=90)
            ]
        ],
        font='Any 20'
    )


class Hangman:
    def __init__(self):
        self.window = sg.Window(
            title='hangman',
            layout=[  # Each sublist represents a row and can contain multiple controls.
                [build_canvas_frame(),build_letters_frame()],
                [build_guessed_word_frame()],
                [build_action_buttons_frame()]
            ],
            finalize=True,  # to specify whether the window’s layout should be frozen
            margins=(100, 100)
        )
        self.canvas = self.window['-CANVAS-']  # holds a reference to the drawing area

        self.target_word = select_word()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.guessed_word = self.build_guessed_word()
        self.quit = False

        self.draw_scaffold()

    def draw_scaffold(self):
        # هر نقطه یه تاپل با مختصات دو نقطه ست / عدد آخر مشخص کننده ی پهناست
        lines = [
            ((40, 55), (180, 55), 10),
            ((165, 60), (165, 365), 10),
            ((160, 360), (100, 360), 10),
            ((100, 365), (100, 330), 10),
        ]
        for *points, width in lines:
            self.canvas.draw_line(*points, color='black', width=width)

    def draw_hanged_man(self):
        head = (100, 290)
        torso = [((100, 250), (100, 190))]  # two points to draw one vertical line

        left_arm = [
            ((100, 250), (80, 250)),
            ((80, 250), (60, 210)),
            ((60, 210), (60, 190)),
        ]  # three lines as shoulder, arm and forearm
        right_arm = [
            ((100, 250), (120, 250)),
            ((120, 250), (140, 210)),
            ((140, 210), (140, 190)),
        ]

        left_leg = [
            ((100, 170), (80, 170)),
            ((80, 170), (70, 140)),
            ((70, 140), (70, 80)),
            ((70, 80), (60, 80)),
        ]  # four points as the hip, thigh, calf and foot
        right_leg = [
            ((100, 170), (120, 170)),
            ((120, 170), (130, 140)),
            ((130, 140), (130, 80)),
            ((130, 80), (140, 80)),
        ]

        body = [torso, left_arm, right_arm, left_leg, right_leg]

        if self.wrong_guesses == 1:
            self.canvas.draw_circle(head, radius=20, line_color='red', line_width=2)
        elif self.wrong_guesses > 1:
            for part in body[self.wrong_guesses - 2]:
                self.canvas.draw_line(*part, color='red', width=2)

    def build_guessed_word(self):
        current_letters = []
        for letter in self.target_word:
            if letter in self.guessed_letters:
                current_letters.append(letter)
            else:
                current_letters.append('_')
        return ' '.join(current_letters)  # adds ' ' in between current_l strings!

    def new_game(self):
        self.target_word = select_word()
        self.restart_game()

    def restart_game(self):
        self.guessed_letters = set()  # to choose a new word every time
        self.wrong_guesses = 0
        self.guessed_word = self.build_guessed_word()
        # Restart GUI
        self.canvas.erase()  # resets the hanged man drawing
        self.draw_scaffold()
        for letter in ascii_uppercase:
            self.window[f'-letter-{letter}-'].update(disabled=False)
            # you’ll keep track of the guessed letters by disabling the letter once the player has clicked the
            # corresponding button.
        self.window['-DISPLAY-WORD-'].update(self.guessed_word)

    def read_event(self):
        #   allow you to read all the user events on the app’s GUI/ events like: clicking, passing
        event = self.window.read()
        if event is not None:
            event_id = event[0]
        else:
            event_id = None
        return event_id

    def process_event(self, event):
        # use to handle all the relevant user interactions or events
        if event[:8] == '-letter-':
            self.play(letter=event[8])  # if event is one of letter buttons/ not restart or new
        elif event == '-RESTART-':
            self.restart_game()
        elif event == '-NEW-':
            self.new_game()

    def play(self, letter):
        if letter not in self.target_word:
            self.wrong_guesses += 1
        self.guessed_letters.add(letter)
        self.guessed_word = self.build_guessed_word()
        # update the guessed word (wat?)
        # update GUI
        self.window[f"-letter-{letter}-"].update(disabled=True)  # کلمه ی انتخاب شده رو غیرفعال میکنه
        self.window["-DISPLAY-WORD-"].update(self.guessed_word)
        self.draw_hanged_man()

    def check_winner(self):
        if self.wrong_guesses < MAX_WRONG_GUESSES:
            answer = sg.PopupYesNo(
                "You've won! Congratulations!\n"
                "Another round?",
                title="Winner!",
            )
        else:
            answer = sg.PopupYesNo(
                f"You've lost! The word was '{self.target_word}'.\n"
                "Another round?",
                title="Sorry!",
            )
        self.quit = answer == "No"
        if not self.quit:
            self.new_game()

    def is_over(self):
        return any(  # any() func. works like 'or' statement
            [
                self.wrong_guesses == MAX_WRONG_GUESSES,
                set(self.target_word) <= self.guessed_letters
                # checks if the player has guessed the word right or not
            ]
        )

    def close_app(self):
        self.window.close()


if __name__ == '__main__':
    game = Hangman()

    while not game.quit:
        # Event loop
        while not game.is_over():
            event_id = game.read_event()
            if event_id in {sg.WIN_CLOSED, "-QUIT-"}:
                game.quit = True
                break
            game.process_event(event_id)

        if not game.quit:
            game.check_winner()

    game.close_app()
